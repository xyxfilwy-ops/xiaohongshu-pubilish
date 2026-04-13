#!/usr/bin/env python3
"""
技能反馈分析脚本
Learning Loop - Feedback Analyzer

功能：
1. 读取指定技能的反馈日志
2. 统计 OK/满意/不满意 分布
3. 识别重复失败模式
4. 生成改进建议

用法：
    python analyze_feedback.py --skill <技能名> [--period day|week|month]
"""

import os
import re
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter, defaultdict
from typing import List, Dict, Tuple

# 配置
LOGS_DIR = Path("./learning-loop/logs")
TEMPLATES_DIR = Path("./learning-loop/templates")


class FeedbackEntry:
    """单条反馈记录"""
    
    def __init__(self, timestamp: str, task_type: str, feedback: str, 
                 notes: str, duration: int = 0):
        self.timestamp = timestamp
        self.task_type = task_type
        self.feedback = feedback  # ok, success, fail
        self.notes = notes
        self.duration = duration
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            timestamp=data.get('timestamp', ''),
            task_type=data.get('task_type', ''),
            feedback=data.get('feedback', 'ok'),
            notes=data.get('notes', ''),
            duration=data.get('duration', 0)
        )
    
    def to_dict(self) -> dict:
        return {
            'timestamp': self.timestamp,
            'task_type': self.task_type,
            'feedback': self.feedback,
            'notes': self.notes,
            'duration': self.duration
        }


class FeedbackAnalyzer:
    """反馈分析器"""
    
    def __init__(self, skill_name: str):
        self.skill_name = skill_name
        self.log_dir = LOGS_DIR / skill_name
        self.entries: List[FeedbackEntry] = []
        self.stats = {
            'total': 0,
            'ok': 0,
            'success': 0,
            'fail': 0
        }
        self.patterns = defaultdict(list)
    
    def load_logs(self, period: str = 'week') -> int:
        """加载反馈日志"""
        if not self.log_dir.exists():
            print(f"⚠️  日志目录不存在: {self.log_dir}")
            return 0
        
        # 确定时间范围
        now = datetime.now()
        if period == 'day':
            start_date = now - timedelta(days=1)
        elif period == 'week':
            start_date = now - timedelta(weeks=1)
        elif period == 'month':
            start_date = now - timedelta(days=30)
        else:
            start_date = datetime(2000, 1, 1)
        
        # 扫描日志文件
        loaded = 0
        for log_file in sorted(self.log_dir.glob("feedback-*.md")):
            try:
                # 解析文件名中的日期
                date_str = log_file.stem.replace('feedback-', '')
                file_date = datetime.strptime(date_str, '%Y-%m-%d')
                
                if file_date >= start_date:
                    entries = self._parse_feedback_file(log_file)
                    self.entries.extend(entries)
                    loaded += len(entries)
            except Exception as e:
                print(f"⚠️  解析文件失败 {log_file}: {e}")
        
        return loaded
    
    def _parse_feedback_file(self, file_path: Path) -> List[FeedbackEntry]:
        """解析反馈日志文件"""
        entries = []
        content = file_path.read_text(encoding='utf-8')
        
        # 提取每个执行记录块
        pattern = r'### #\d+.*?(?=\n---|\n## |\Z)'
        blocks = re.findall(pattern, content, re.DOTALL)
        
        for block in blocks:
            try:
                # 解析反馈类型 - 更灵活的匹配
                feedback = None
                if '\[x\] OK' in block or '[x] OK' in block or '✓ OK' in block:
                    feedback = 'ok'
                elif '\[x\] 满意' in block or '[x] 满意' in block:
                    feedback = 'success'
                elif '\[x\] 不满意' in block or '[x] 不满意' in block:
                    feedback = 'fail'
                
                if feedback:
                    # 提取备注
                    notes_match = re.search(r'\*\*备注\*\*:\s*(.+?)(?:\n|$)', block)
                    time_match = re.search(r'### #\d+.*?-\s*(.+?)(?:\n|$)', block)
                    
                    notes = notes_match.group(1).strip() if notes_match else ''
                    timestamp = time_match.group(1).strip() if time_match else ''
                    
                    entries.append(FeedbackEntry(
                        timestamp=timestamp,
                        task_type='',
                        feedback=feedback,
                        notes=notes
                    ))
            except Exception:
                continue
        
        return entries
    
    def analyze(self) -> Dict:
        """执行分析"""
        if not self.entries:
            return {'error': 'No data to analyze'}
        
        # 统计
        self.stats['total'] = len(self.entries)
        for entry in self.entries:
            if entry.feedback == 'ok':
                self.stats['ok'] += 1
            elif entry.feedback in ('success', '满意'):
                self.stats['success'] += 1
            elif entry.feedback in ('fail', '不满意'):
                self.stats['fail'] += 1
        
        # 识别失败模式
        fail_entries = [e for e in self.entries if e.feedback in ('fail', '不满意')]
        self._identify_patterns(fail_entries)
        
        return self._generate_results()
    
    def _identify_patterns(self, fail_entries: List[FeedbackEntry]):
        """识别失败模式"""
        # 关键词模式
        fail_keywords = [
            '超时', 'timeout', '错误', 'error', '失败', 'fail',
            '无法', 'cannot', 'unexpected', '异常', '问题'
        ]
        
        for entry in fail_entries:
            notes_lower = entry.notes.lower()
            for keyword in fail_keywords:
                if keyword in notes_lower:
                    self.patterns[keyword].append(entry)
    
    def _generate_results(self) -> Dict:
        """生成分析结果"""
        total = self.stats['total']
        fail_rate = (self.stats['fail'] / total * 100) if total > 0 else 0
        success_rate = (self.stats['success'] / total * 100) if total > 0 else 0
        
        # 健康度评分
        health_score = max(0, 100 - fail_rate * 2)
        
        # 紧迫度
        if fail_rate > 30:
            urgency = '紧急'
        elif fail_rate > 15:
            urgency = '高'
        elif fail_rate > 5:
            urgency = '中'
        else:
            urgency = '低'
        
        return {
            'skill': self.skill_name,
            'period': self.period if hasattr(self, 'period') else 'week',
            'timestamp': datetime.now().isoformat(),
            'stats': {
                'total': total,
                'ok': self.stats['ok'],
                'success': self.stats['success'],
                'fail': self.stats['fail'],
                'ok_rate': round(self.stats['ok'] / total * 100, 1) if total > 0 else 0,
                'success_rate': round(success_rate, 1),
                'fail_rate': round(fail_rate, 1)
            },
            'patterns': {
                keyword: len(entries) 
                for keyword, entries in self.patterns.items()
            },
            'health_score': round(health_score, 1),
            'urgency': urgency,
            'recommendations': self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[Dict]:
        """生成改进建议"""
        recommendations = []
        
        # 基于失败率的建议
        fail_rate = self.stats['fail'] / self.stats['total'] * 100 if self.stats['total'] > 0 else 0
        
        if fail_rate > 30:
            recommendations.append({
                'priority': 'P0',
                'title': '失败率过高',
                'suggestion': '需要紧急排查和修复，建议停止使用该技能直到问题解决',
                'action': '立即分析失败日志'
            })
        elif fail_rate > 15:
            recommendations.append({
                'priority': 'P1',
                'title': '失败率偏高',
                'suggestion': '建议运行 improve 操作生成详细改进报告',
                'action': '/learning-loop --action improve --skill ' + self.skill_name
            })
        
        # 基于模式的建议
        for keyword, count in self.patterns.items():
            if count >= 3:
                recommendations.append({
                    'priority': 'P1',
                    'title': f'关键词"{keyword}"出现{count}次',
                    'suggestion': f'识别到{keyword}相关的重复失败，建议添加专门的处理规则',
                    'action': '在SKILL.md中添加错误处理规则'
                })
        
        return recommendations
    
    def print_report(self, results: Dict):
        """打印分析报告"""
        print("\n" + "="*60)
        print(f"📊 {self.skill_name} 反馈分析报告")
        print("="*60)
        
        if 'error' in results:
            print(f"\n❌ {results['error']}")
            return
        
        stats = results['stats']
        print(f"\n📈 统计数据 (共 {stats['total']} 条)")
        print("-"*40)
        print(f"  OK响应:     {stats['ok']:3d} ({stats['ok_rate']}%)")
        print(f"  满意:       {stats['success']:3d} ({stats['success_rate']}%)")
        print(f"  不满意:     {stats['fail']:3d} ({stats['fail_rate']}%)")
        
        print(f"\n🏥 健康度评分: {results['health_score']}/100")
        print(f"⚡ 改进紧迫度: {results['urgency']}")
        
        if results['patterns']:
            print(f"\n🔍 识别到的模式:")
            for keyword, count in sorted(results['patterns'].items(), key=lambda x: -x[1]):
                print(f"  - '{keyword}': {count}次")
        
        if results['recommendations']:
            print(f"\n💡 改进建议:")
            for i, rec in enumerate(results['recommendations'], 1):
                print(f"  [{rec['priority']}] {rec['title']}")
                print(f"      {rec['suggestion']}")
                if 'action' in rec:
                    print(f"      → {rec['action']}")
        
        print("\n" + "="*60)
    
    def save_json(self, results: Dict, output_path: str = None):
        """保存JSON结果"""
        if output_path is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
            output_path = f"./learning-loop/logs/{self.skill_name}/analysis-{date_str}.json"
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 分析结果已保存: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='技能反馈分析工具')
    parser.add_argument('--skill', required=True, help='技能名称')
    parser.add_argument('--period', choices=['day', 'week', 'month', 'all'], 
                        default='week', help='分析周期')
    parser.add_argument('--output', help='输出文件路径(JSON)')
    parser.add_argument('--json-only', action='store_true', help='仅输出JSON')
    
    args = parser.parse_args()
    
    analyzer = FeedbackAnalyzer(args.skill)
    analyzer.period = args.period
    
    print(f"🔍 正在分析 {args.skill} 的反馈数据...")
    loaded = analyzer.load_logs(args.period)
    
    if loaded == 0:
        print(f"\n❌ 未找到 {args.period} 内的反馈日志")
        print(f"   提示: 先使用 --action collect 收集反馈")
        return
    
    print(f"   已加载 {loaded} 条反馈记录")
    
    results = analyzer.analyze()
    
    if args.json_only:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        analyzer.print_report(results)
    
    if args.output or results.get('stats', {}).get('total', 0) > 0:
        analyzer.save_json(results, args.output)


if __name__ == '__main__':
    main()
