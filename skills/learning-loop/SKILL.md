# 技能学习循环系统 (Skill Learning Loop)

> 基于 Garry Tan "Thin Harness, Fat Skills" 方法论构建的技能自我改进系统

## 核心循环

```
执行技能 → 收集反馈 → 分析模式 → 改进规则 → 迭代升级
    ↑                                              ↓
    └──────────────── 持续迭代 ◄────────────────────┘
```

### 四阶段循环

| 阶段 | 操作 | 说明 |
|------|------|------|
| **Collect** | 收集执行结果和反馈 | 记录每次技能执行的输出和用户反应 |
| **Analyze** | 识别成功/失败模式 | 统计"OK"/满意/不满意的分布 |
| **Improve** | 生成改进建议 | 将分析结论转化为可执行的新规则 |
| **Update** | 写回SKILL.md | 追加新规则，更新版本号 |

---

## 使用方法

### 基本命令格式

```bash
/learning-loop --action <collect|analyze|improve|report> --skill <技能名> [参数]
```

### 1. 收集反馈 (collect)

```bash
/learning-loop --action collect \
  --skill xiaohongshu-publisher \
  --feedback OK \
  --notes "封面图Prompt效果不错，但内容页文字渲染有问题"
```

### 2. 分析反馈 (analyze)

```bash
/learning-loop --action analyze --skill xiaohongshu-publisher
```

### 3. 生成改进 (improve)

```bash
/learning-loop --action improve --skill xiaohongshu-publisher
```

### 4. 生成报告 (report)

```bash
/learning-loop --action report --skill xiaohongshu-publisher --period week
```

---

## 反馈类型定义

| 类型 | 标识 | 说明 |
|------|------|------|
| **OK** | `ok` | 任务成功，输出质量可接受 |
| **满意** | `success` | 完全符合预期，超出预期 |
| **不满意** | `fail` | 未达到预期，需要改进 |

---

## 日志文件结构

```
./learning-loop/
├── logs/
│   └── {skill-name}/
│       ├── feedback-{date}.md      # 每日反馈日志
│       ├── execution-{date}.log    # 执行轨迹
│       └── improvement-{date}.md   # 改进建议
├── templates/
│   ├── feedback-log.md             # 反馈日志模板
│   └── improvement-report.md       # 改进报告模板
└── SKILL.md
```

---

## 分析维度

### 成功率指标

- **OK Rate**: "OK"响应的比例
- **Success Rate**: "满意"响应的比例
- **Fail Rate**: "不满意"响应的比例

### 模式识别

1. **重复失败模式**: 同一错误出现3次以上
2. **上下文敏感**: 特定输入类型导致失败
3. **边界条件**: 极端值或异常输入的处理

### 改进优先级

| 优先级 | 条件 | 行动 |
|--------|------|------|
| P0 | Fail Rate > 30% | 必须立即改进 |
| P1 | 特定模式连续失败 | 针对模式修复 |
| P2 | 优化建议 | 锦上添花的改进 |

---

## 版本管理

### 版本号规则

```
v{major}.{minor}
- major: 重大重构或范式改变
- minor: 增量改进（每次improve +0.1）
```

### 版本历史记录

在 SKILL.md 末尾追加：

```markdown
## 版本历史

### v1.2 (2026-04-15)
- 改进: 添加了"图片生成超时处理"规则
- 原因: 连续3次因超时导致任务失败
```

---

## 反馈日志格式

```markdown
# {技能名} 反馈日志

## {YYYY-MM-DD}

### 执行记录 #001
- **时间**: 2026-04-15 14:30
- **输入**: [简要描述任务输入]
- **输出**: [执行结果摘要]
- **反馈**: OK / 满意 / 不满意
- **备注**: 详细说明

### 执行记录 #002
...
```

---

## 改进报告格式

```markdown
# {技能名} 改进报告

## 基本信息
- **技能**: {技能名}
- **分析周期**: {start} ~ {end}
- **生成时间**: {timestamp}

## 统计概览
- 总执行次数: {count}
- OK: {ok_count} ({ok_rate}%)
- 满意: {success_count} ({success_rate}%)
- 不满意: {fail_count} ({fail_rate}%)

## 模式分析

### 成功模式
- {pattern 1}
- {pattern 2}

### 失败模式
- {pattern 1}
- {pattern 2}

## 改进建议

### 规则 #1
- **问题**: {描述}
- **建议**: {改进方案}
- **优先级**: P0/P1/P2

### 规则 #2
...
```

---

## 与自进化能力的区别

| 维度 | 自进化能力 | 学习循环 |
|------|-----------|---------|
| **触发条件** | 失败率>30% | 任意反馈 |
| **粒度** | 大规模测试 | 逐次执行 |
| **自动化** | 半自动 | 完全手动触发 |
| **适用场景** | 技能开发阶段 | 生产环境持续优化 |

---

## 最佳实践

1. **及时反馈**: 每次执行后立即记录，不要依赖记忆
2. **具体描述**: "不满意"时必须说明具体原因
3. **版本同步**: improve后立即更新SKILL.md
4. **定期复盘**: 每周运行一次 analyze + report
5. **保留证据**: 日志要详细，便于后续分析

---

## 示例流程

```
用户: /learning-loop --action collect --skill my-skill --feedback OK --notes "执行时间从10s优化到3s"

系统:
1. 记录反馈到 logs/my-skill/feedback-2026-04-15.md
2. 更新累计统计
3. 标记无需立即改进

用户: /learning-loop --action collect --skill my-skill --feedback 不满意 --notes "图片生成失败，颜色代码被当作文字渲染"

系统:
1. 记录失败案例
2. 标记需要分析
3. 建议运行 analyze

用户: /learning-loop --action analyze --skill my-skill

系统:
1. 读取所有日志
2. 识别模式（颜色代码问题）
3. 生成分析摘要

用户: /learning-loop --action improve --skill my-skill

系统:
1. 生成改进建议
2. 创建 improvement-{date}.md
3. 提示需要手动更新的规则

用户手动更新 SKILL.md，追加新规则
```
