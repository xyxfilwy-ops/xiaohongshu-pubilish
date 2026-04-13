#!/usr/bin/env python3
"""
技能反馈收集脚本
Learning Loop - Feedback Collector

功能：
1. 收集技能执行后的用户反馈
2. 保存到日志文件
3. 更新统计信息

用法：
    python collect_feedback.py --skill <技能名> --feedback <ok|success|fail> --notes <备注>
"""

import os
import argparse
from datetime import datetime
from pathlib import Path

# 配置
LOGS_DIR = Path("./learning-loop/logs")
TEMPLATES_DIR = Path("./learning-loop/templates")


class FeedbackCollector:
    """反馈收集器"""
    
    def __init__(self, skill_name: str):
        self.skill_name = skill_name
        self.log_dir = LOGS_DIR / skill_name
        self.log_dir.mkdir(parents=True, exist_ok=True)
    
    def collect(self, feedback: str, notes: str = '', task_type: str = '', duration: int = 0) -> dict:
        """收集反馈"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 反馈映射
        feedback_map = {
            'ok': 'OK',
            'success': '满意',
            'fail': '不满意',
            'o': 'OK',
            's': '满意',
            'f': '不满意'
        }
        feedback_display = feedback_map.get(feedback.lower(), feedback)
        
        # 获取序号
        log_file = self.log_dir / f"feedback-{date_str}.md"
        record_num = self._get_next_record_num(log_file)
        
        # 创建记录
        record = {
            'num': record_num,
            'timestamp': timestamp,
            'task_type': task_type,
            'feedback': feedback_display,
            'feedback_key': feedback.lower(),
            'notes': notes,
            'duration': duration,
            'needs_improvement': feedback.lower() in ('fail', 'f')
        }
        
        # 保存到日志文件
        self._append_to_log(log_file, record)
        
        # 更新统计
        self._update_stats(record)
        
        return record
    
    def _get_next_record_num(self, log_file: Path) -> int:
        """获取下一个记录序号"""
        if not log_file.exists():
            return 1
        
        content = log_file.read_text(encoding='utf-8')
        nums = [int(n) for n in _findall(r'### #(\d+)', content)]
        return max(nums) + 1 if nums else 1
    
    def _append_to_log(self, log_file: Path, record: dict):
        """追加到日志文件"""
        # 检查文件是否存在，不存在则创建
        if not log_file.exists():
            header = self._generate_log_header()
            log_file.write_text(header, encoding='utf-8')
        
        # 构建记录块
        record_block = self._format_record(record)
        
        # 追加到文件
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(record_block)
        
        print(f"✅ 反馈已记录: #{record['num']}")
    
    def _generate_log_header(self) -> str:
        """生成日志文件头"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        return f"""# {self.skill_name} 反馈日志

> 学习循环反馈收集记录 - {date_str}

## 基本信息

| 字段 | 值 |
|------|-----|
| 技能名 | {self.skill_name} |
| 创建日期 | {date_str} |

---

## 执行记录

"""
    
    def _format_record(self, record: dict) -> str:
        """格式化单条记录"""
        check_ok = '[x]' if record['feedback_key'] == 'ok' else '[ ]'
        check_success = '[x]' if record['feedback_key'] in ('success', 's') else '[ ]'
        check_fail = '[x]' if record['feedback_key'] in ('fail', 'f') else '[ ]'
        
        notes = record['notes'] if record['notes'] else '(无备注)'
        
        return f"""### #{record['num']} - {record['timestamp']}

**任务类型**: {record['task_type'] or '(未指定)'}
**备注**: {notes}
**执行时长**: {record['duration']}s

**反馈类型**: 
- {check_ok} OK
- {check_success} 满意
- {check_fail} 不满意

**需要改进**: {'是' if record['needs_improvement'] else '否'}

---

"""
    
    def _update_stats(self, record: dict):
        """更新统计文件"""
        stats_file = self.log_dir / "stats.json"
        
        import json
        stats = {'ok': 0, 'success': 0, 'fail': 0}
        
        if stats_file.exists():
            try:
                stats = json.loads(stats_file.read_text(encoding='utf-8'))
            except:
                pass
        
        # 更新计数
        key = record['feedback_key']
        if key in ('ok', 'o'):
            stats['ok'] = stats.get('ok', 0) + 1
        elif key in ('success', 's'):
            stats['success'] = stats.get('success', 0) + 1
        elif key in ('fail', 'f'):
            stats['fail'] = stats.get('fail', 0) + 1
        
        # 重新计算总计
        total = stats['ok'] + stats['success'] + stats['fail']
        stats['total'] = total
        stats['last_updated'] = datetime.now().isoformat()
        
        # 计算比率
        if total > 0:
            stats['ok_rate'] = round(stats['ok'] / total * 100, 1)
            stats['success_rate'] = round(stats['success'] / total * 100, 1)
            stats['fail_rate'] = round(stats['fail'] / total * 100, 1)
        
        stats_file.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding='utf-8')
        
        print(f"📊 累计统计: OK={stats.get('ok', 0)}, 满意={stats.get('success', 0)}, 不满意={stats.get('fail', 0)}")


def _findall(pattern: str, text: str):
    """简单的正则匹配"""
    import re
    return re.findall(pattern, text)


def main():
    parser = argparse.ArgumentParser(description='收集技能反馈')
    parser.add_argument('--skill', required=True, help='技能名称')
    parser.add_argument('--feedback', required=True, 
                       choices=['ok', 'success', 'fail', 'o', 's', 'f'],
                       help='反馈类型 (ok/success/fail)')
    parser.add_argument('--notes', default='', help='备注说明')
    parser.add_argument('--task', default='', help='任务类型')
    parser.add_argument('--duration', type=int, default=0, help='执行时长(秒)')
    
    args = parser.parse_args()
    
    collector = FeedbackCollector(args.skill)
    result = collector.collect(
        feedback=args.feedback,
        notes=args.notes,
        task_type=args.task,
        duration=args.duration
    )
    
    # 打印结果
    print(f"\n{'='*50}")
    print(f"技能: {args.skill}")
    print(f"反馈: {result['feedback']}")
    print(f"需要改进: {'是 ⚠️' if result['needs_improvement'] else '否'}")
    print(f"{'='*50}")
    
    if result['needs_improvement']:
        print(f"\n建议运行分析: python scripts/analyze_feedback.py --skill {args.skill}")


if __name__ == '__main__':
    main()
