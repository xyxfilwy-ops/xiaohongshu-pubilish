#!/usr/bin/env python3
"""
技能改进建议生成脚本
Learning Loop - Improvement Generator

功能：
1. 分析反馈日志
2. 识别失败模式
3. 生成可执行的改进建议
4. 输出可复制到SKILL.md的内容

用法：
    python generate_improvement.py --skill <技能名> [--output <文件>]
"""

import os
import re
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Tuple

# 配置
LOGS_DIR = Path("./learning-loop/logs")
OUTPUT_DIR = Path("./learning-loop/logs")


class ImprovementGenerator:
    """改进建议生成器"""
    
    def __init__(self, skill_name: str):
        self.skill_name = skill_name
        self.log_dir = LOGS_DIR / skill_name
        self.fail_entries = []
        self.patterns = {}
        self.stats = {}
    
    def load_data(self, days: int = 7) -> bool:
        """加载数据"""
        if not self.log_dir.exists():
            print(f"❌ 日志目录不存在: {self.log_dir}")
            return False
        
        # 加载反馈日志
        self._load_feedback_logs(days)
        
        # 加载统计
        self._load_stats()
        
        return True
    
    def _load_feedback_logs(self, days: int):
        """加载反馈日志"""
        start_date = datetime.now() - timedelta(days=days)
        
        for log_file in sorted(self.log_dir.glob("feedback-*.md")):
            try:
                date_str = log_file.stem.replace('feedback-', '')
                file_date = datetime.strptime(date_str, '%Y-%m-%d')
                
                if file_date >= start_date:
                    self._parse_feedback_file(log_file)
            except Exception as e:
                print(f"⚠️ 解析失败 {log_file}: {e}")
    
    def _parse_feedback_file(self, file_path: Path):
        """解析反馈文件"""
        content = file_path.read_text(encoding='utf-8')
        
        # 提取每个执行记录块
        pattern = r'### #\d+.*?(?=\n---|\n## |\Z)'
        blocks = re.findall(pattern, content, re.DOTALL)
        
        for block in blocks:
            # 检查是否是失败记录
            if '[x] 不满意' not in block:
                continue
            
            # 提取备注
            notes_match = re.search(r'\*\*备注\*\*:\s*(.+?)(?:\n|$)', block)
            time_match = re.search(r'### #\d+.*?-\s*(.+?)(?:\n|$)', block)
            
            entry = {
                'notes': notes_match.group(1).strip() if notes_match else '',
                'timestamp': time_match.group(1).strip() if time_match else ''
            }
            self.fail_entries.append(entry)
    
    def _load_stats(self):
        """加载统计文件"""
        stats_file = self.log_dir / "stats.json"
        if stats_file.exists():
            try:
                self.stats = json.loads(stats_file.read_text(encoding='utf-8'))
            except:
                self.stats = {}
    
    def analyze(self) -> List[Dict]:
        """分析并生成改进建议"""
        self._identify_patterns()
        return self._generate_suggestions()
    
    def _identify_patterns(self):
        """识别失败模式"""
        # 问题类型关键词
        problem_patterns = {
            '超时': ['超时', 'timeout', 'timed out', '60秒', '请求超时'],
            '参数错误': ['参数', 'param', 'missing', '必填', 'validation'],
            '网络问题': ['网络', 'network', '连接', 'connection', 'dns'],
            '权限问题': ['权限', 'permission', 'auth', '认证', 'token'],
            '格式错误': ['格式', 'format', 'json', '解析', 'parse'],
            '内容问题': ['内容', '生成', '质量', '效果', '渲染'],
            'API错误': ['api', '错误码', 'error_code', 'rate limit', '429'],
            '文件问题': ['文件', 'file', '路径', '不存在', '读写'],
        }
        
        # 统计每种模式的失败次数
        pattern_counts = {}
        for entry in self.fail_entries:
            notes = entry['notes'].lower()
            for pattern_name, keywords in problem_patterns.items():
                if any(kw.lower() in notes for kw in keywords):
                    if pattern_name not in pattern_counts:
                        pattern_counts[pattern_name] = {
                            'count': 0,
                            'entries': [],
                            'keywords': keywords
                        }
                    pattern_counts[pattern_name]['count'] += 1
                    pattern_counts[pattern_name]['entries'].append(entry)
        
        self.patterns = pattern_counts
    
    def _generate_suggestions(self) -> List[Dict]:
        """生成改进建议"""
        suggestions = []
        
        for pattern_name, data in self.patterns.items():
            count = data['count']
            entries = data['entries']
            
            if count >= 1:  # 至少出现一次就生成建议
                suggestion = self._create_suggestion(pattern_name, count, entries)
                suggestions.append(suggestion)
        
        # 按优先级排序
        priority_order = {'P0': 0, 'P1': 1, 'P2': 2}
        suggestions.sort(key=lambda x: (priority_order.get(x['priority'], 3), -x['count']))
        
        return suggestions
    
    def _create_suggestion(self, pattern_name: str, count: int, entries: List[Dict]) -> Dict:
        """创建单条建议"""
        # 根据模式确定优先级和具体建议
        pattern_configs = {
            '超时': {
                'priority': 'P0' if count >= 3 else 'P1',
                'solution': '添加超时重试机制，失败后自动重试1-2次',
                'rule_type': '错误处理'
            },
            '参数错误': {
                'priority': 'P1',
                'solution': '在执行前增加参数校验，提前抛出明确的错误提示',
                'rule_type': '输入验证'
            },
            '网络问题': {
                'priority': 'P1',
                'solution': '添加网络状态检查，失败时提示用户检查网络',
                'rule_type': '错误处理'
            },
            '权限问题': {
                'priority': 'P0',
                'solution': '检查API凭证有效性，添加权限验证步骤',
                'rule_type': '认证校验'
            },
            '格式错误': {
                'priority': 'P1',
                'solution': '添加响应格式校验，解析失败时提供详细日志',
                'rule_type': '错误处理'
            },
            '内容问题': {
                'priority': 'P2',
                'solution': '优化Prompt或调整生成参数',
                'rule_type': 'Prompt优化'
            },
            'API错误': {
                'priority': 'P0' if 'rate' in str(entries).lower() else 'P1',
                'solution': '添加API限流处理，429错误后等待合适时间重试',
                'rule_type': '错误处理'
            },
            '文件问题': {
                'priority': 'P1',
                'solution': '添加文件存在性检查，创建必要的目录结构',
                'rule_type': '输入验证'
            }
        }
        
        config = pattern_configs.get(pattern_name, {
            'priority': 'P2',
            'solution': '需要进一步分析具体问题',
            'rule_type': '其他'
        })
        
        # 示例
        examples = [e['notes'][:100] + '...' if len(e['notes']) > 100 else e['notes'] 
                   for e in entries[:2] if e['notes']]
        
        return {
            'pattern': pattern_name,
            'count': count,
            'priority': config['priority'],
            'rule_type': config['rule_type'],
            'problem': f"连续{count}次出现{pattern_name}相关问题",
            'solution': config['solution'],
            'examples': examples,
            'suggested_rule': self._generate_rule_snippet(pattern_name, config)
        }
    
    def _generate_rule_snippet(self, pattern_name: str, config: Dict) -> str:
        """生成规则代码片段"""
        rule_templates = {
            '超时': '''
```markdown
### 超时处理规则
- **触发条件**: API响应超时
- **处理方式**: 
  1. 首次失败等待2秒重试
  2. 第二次失败等待5秒重试
  3. 第三次失败返回明确错误信息
- **示例**:
  ```
  if "timeout" in str(error):
      retry_with_backoff(max_retries=2)
  ```
```''',
            '参数错误': '''
```markdown
### 参数校验规则
- **触发条件**: 必填参数缺失或格式错误
- **处理方式**:
  1. 定义明确的参数规范
  2. 执行前进行校验
  3. 缺失时返回具体哪个参数有问题
```''',
            'API错误': '''
```markdown
### API限流处理
- **触发条件**: 429错误或rate limit相关
- **处理方式**:
  1. 解析Retry-After头
  2. 等待指定时间后重试
  3. 记录连续触发次数
```'''
        }
        
        return rule_templates.get(pattern_name, f'''
```markdown
### {config['rule_type']}规则
- **问题**: {pattern_name}
- **建议**: {config['solution']}
```
''')
    
    def generate_report(self, suggestions: List[Dict]) -> str:
        """生成完整的改进报告"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        total_fails = len(self.fail_entries)
        
        report = f"""# {self.skill_name} 改进建议报告

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 概览

| 指标 | 数值 |
|------|------|
| 分析周期 | 近{days}天 |
| 失败记录数 | {total_fails} |
| 识别模式数 | {len(suggestions)} |

## 失败原因分布

```
"""
        
        # 饼图（文本版）
        if suggestions:
            max_count = max(s['count'] for s in suggestions)
            for s in suggestions:
                bar_len = int(s['count'] / max_count * 20)
                bar = '█' * bar_len
                report += f"{s['pattern']:8} {bar:20} {s['count']}次 [{s['priority']}]\n"
        
        report += f"""
## 改进建议

"""
        
        for i, s in enumerate(suggestions, 1):
            report += f"""### {i}. {s['pattern']} (优先级: {s['priority']})

**问题**: {s['problem']}
**建议方案**: {s['solution']}
**规则类型**: {s['rule_type']}

**示例案例**:
"""
            for ex in s['examples']:
                report += f"- {ex}\n"
            
            report += f"""
{s['suggested_rule']}
---
"""
        
        # 生成可复制的更新内容
        report += f"""
## SKILL.md 更新内容

请将以下内容追加到 {self.skill_name}/SKILL.md 的 "版本历史" 部分：

```markdown
## 版本历史

### v{self._suggest_version()} ({date_str})
- 改进: 修复了{', '.join(s['pattern'] for s in suggestions[:3])}问题
- 原因: 连续{total_fails}次失败反馈分析得出
- 日期: {date_str}
```
"""
        
        return report
    
    def _suggest_version(self) -> str:
        """建议版本号"""
        # 尝试读取当前版本
        skill_md = Path(f"./workspace/skills/{self.skill_name}/SKILL.md")
        if skill_md.exists():
            content = skill_md.read_text(encoding='utf-8')
            version_match = re.search(r'### v(\d+)\.(\d+)', content)
            if version_match:
                major, minor = int(version_match.group(1)), int(version_match.group(2))
                return f"{major}.{minor + 1}"
        
        return "1.1"  # 默认从1.1开始
    
    def save_report(self, report: str, output_path: str = None):
        """保存报告"""
        if output_path is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
            output_path = self.log_dir / f"improvement-{date_str}.md"
        
        Path(output_path).write_text(report, encoding='utf-8')
        print(f"💾 报告已保存: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='生成技能改进建议')
    parser.add_argument('--skill', required=True, help='技能名称')
    parser.add_argument('--days', type=int, default=7, help='分析天数')
    parser.add_argument('--output', help='输出文件路径')
    parser.add_argument('--copy-rules', action='store_true', help='仅输出规则片段')
    
    args = parser.parse_args()
    
    generator = ImprovementGenerator(args.skill)
    
    print(f"🔍 正在分析 {args.skill} 的失败模式...")
    if not generator.load_data(days=args.days):
        return
    
    if not generator.fail_entries:
        print("✅ 未发现失败记录，当前技能运行良好！")
        return
    
    suggestions = generator.analyze()
    
    print(f"📊 识别到 {len(suggestions)} 个可改进的模式\n")
    
    if args.copy_rules:
        # 仅输出规则片段
        for s in suggestions:
            print(f"\n{'='*50}")
            print(f"[{s['priority']}] {s['pattern']}")
            print(f"{'='*50}")
            print(s['suggested_rule'])
    else:
        report = generator.generate_report(suggestions)
        print(report)
        generator.save_report(report, args.output)
        
        # 同时保存JSON格式的规则
        rules_path = generator.log_dir / f"rules-{datetime.now().strftime('%Y-%m-%d')}.json"
        with open(rules_path, 'w', encoding='utf-8') as f:
            json.dump(suggestions, f, ensure_ascii=False, indent=2)
        print(f"\n💾 规则JSON已保存: {rules_path}")


if __name__ == '__main__':
    import sys
    if '--days' in sys.argv:
        # 处理 days 参数
        days_idx = sys.argv.index('--days')
        days = int(sys.argv[days_idx + 1])
        sys.argv[days_idx + 1] = str(days)
    
    main()
