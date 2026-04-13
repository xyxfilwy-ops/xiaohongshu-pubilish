# 学习循环系统使用指南

## 快速开始

### 1. 收集反馈

每次技能执行后，收集用户反馈：

```bash
# 正面反馈
python ./learning-loop/scripts/collect_feedback.py \
  --skill xiaohongshu-publisher \
  --feedback ok \
  --notes "封面图效果不错"

# 失败反馈
python ./learning-loop/scripts/collect_feedback.py \
  --skill xiaohongshu-publisher \
  --feedback fail \
  --notes "图片生成超时，提示request timeout"
```

### 2. 分析反馈

定期分析收集到的反馈：

```bash
# 分析最近一周
python ./learning-loop/scripts/analyze_feedback.py \
  --skill xiaohongshu-publisher \
  --period week

# 分析最近一个月
python ./learning-loop/scripts/analyze_feedback.py \
  --skill xiaohongshu-publisher \
  --period month
```

### 3. 生成改进建议

基于分析结果生成改进建议：

```bash
python ./learning-loop/scripts/generate_improvement.py \
  --skill xiaohongshu-publisher \
  --days 7
```

### 4. 更新 SKILL.md

将生成的改进建议复制到技能的 SKILL.md 文件中。

---

## 集成到工作流

### 手动模式

```
用户执行技能 → 询问反馈 → collect_feedback → 定期 analyze → improve → 更新SKILL.md
```

### 自动模式（定时任务）

```bash
# 每周日凌晨2点运行分析
0 2 * * 0 cd /app/data && python ./learning-loop/scripts/analyze_feedback.py --skill xiaohongshu-publisher --period week
```

---

## 日志文件位置

```
./learning-loop/
└── logs/
    └── {skill-name}/
        ├── feedback-2026-04-15.md    # 每日反馈
        ├── stats.json                 # 累计统计
        ├── analysis-2026-04-15.json   # 分析结果
        ├── improvement-2026-04-15.md  # 改进报告
        └── rules-2026-04-15.json      # 规则JSON
```

---

## 反馈类型说明

| 类型 | 命令参数 | 含义 |
|------|----------|------|
| OK | `--feedback ok` | 任务成功，可接受 |
| 满意 | `--feedback success` | 完全符合预期 |
| 不满意 | `--feedback fail` | 未达到预期 |

---

## 常见问题

### Q: 日志目录不存在？
A: 首次运行 `collect_feedback.py` 会自动创建目录。

### Q: 如何查看累计统计？
A: 查看 `logs/{skill}/stats.json` 文件。

### Q: 改进建议太多怎么办？
A: 使用 `--days 3` 只分析最近3天的数据。

### Q: 如何撤销改进？
A: 查看 `SKILL.md` 的版本历史，使用 git 回退或手动删除新增规则。

---

## 示例场景

### 场景1: 小红书发布技能优化

```bash
# 1. 用户反馈封面图文字渲染有问题
python ./learning-loop/scripts/collect_feedback.py \
  --skill xiaohongshu-publisher \
  --feedback fail \
  --notes "封面图文字变成'#1A1A2E'，颜色代码被渲染"

# 2. 分析一周数据
python ./learning-loop/scripts/analyze_feedback.py \
  --skill xiaohongshu-publisher \
  --period week

# 3. 生成改进建议
python ./learning-loop/scripts/generate_improvement.py \
  --skill xiaohongshu-publisher

# 4. 建议输出：
# - 建议在Prompt中禁止颜色代码
# - 建议分层生成（背景+文字）
# - 建议使用Canva添加文字
```

### 场景2: 飞书文档技能优化

```bash
# 1. 收集反馈
python ./learning-loop/scripts/collect_feedback.py \
  --skill feishu_doc \
  --feedback ok \
  --notes "文档创建成功，但权限设置有问题"

# 2. 分析问题
python ./learning-loop/scripts/analyze_feedback.py \
  --skill feishu_doc \
  --period week

# 3. 生成改进
python ./learning-loop/scripts/generate_improvement.py \
  --skill feishu_doc
```
