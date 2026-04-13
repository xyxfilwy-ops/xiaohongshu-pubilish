# Resolver - 上下文按需加载机制

## 概述

Resolver是Garry Tan"Thin Harness, Fat Skills"理念的具体实现：
- **解析器** = 上下文的路由表
- **路由表** = 关键词到技能的映射
- **按需加载** = 只在需要时加载对应上下文

## 核心文件

```
resolver/
├── resolver-config.md    # 路由配置（关键词→技能映射）
├── README.md            # 本文件
├── skill-descriptions.md # 所有技能的description汇总
├── error-handling.md     # 失败处理指南
└── improvement-workflow.md # 改进流程
```

## 快速使用

### 1. 识别技能（自动）

当用户输入包含以下关键词时，系统自动识别技能：

| 用户输入 | 自动加载技能 |
|----------|--------------|
| "帮我发个小红书" | xiaohongshu-publisher |
| "分析这个专家的观点" | diarization |
| "创建一个技能" | yao-meta-skill |

### 2. 手动指定技能

用户也可以显式指定技能：
```
@xiaohongshu-publisher
@skill-assistant
```

### 3. 组合技能使用

复杂任务可以组合多个技能：
```
AI专家信源分析 → topic_tracking + diarization
小红书热点创作 → news-aggregator + xiaohongshu-publisher
```

## 路由规则

### 优先级规则

1. **显式指定** > **关键词匹配** > **模糊推断**
2. **高优先级技能** > **中优先级技能**
3. **精确匹配** > **部分匹配**

### 上下文加载时机

```
┌─────────────────────────────────────────────────────────────┐
│                     Resolver执行流程                         │
├─────────────────────────────────────────────────────────────┤
│  1. 接收用户输入                                              │
│  2. 提取关键词                                                │
│  3. 查询 resolver-config.md 中的路由表                        │
│  4. 加载匹配技能的 SKILL.md                                   │
│  5. 执行技能                                                 │
│  6. 评估结果：                                               │
│     ├─ 成功 → 返回结果                                       │
│     ├─ 失败(≤3次) → 重试 + 加载error-handling.md              │
│     └─ 失败(>3次) → 触发自进化 + 通知用户                      │
└─────────────────────────────────────────────────────────────┘
```

## 添加新技能到路由表

### 步骤1：更新SKILL.md的description

确保description包含：
```yaml
---
name: 技能名称
description: "技能用途说明。触发词：关键词1|关键词2|关键词3"
---
```

### 步骤2：更新resolver-config.md

在"关键词 → 技能映射"表中添加一行：
```markdown
| 新关键词 | 新技能名 | 优先级 | 触发条件 |
```

### 步骤3：更新skill-descriptions.md

添加技能的完整description供参考。

## 常见问题

### Q: 技能没有正确匹配怎么办？
A: 检查该技能的description是否包含当前用户输入的触发词，在resolver-config.md中添加对应映射。

### Q: 如何处理组合技能场景？
A: 在resolver-config.md的"组合技能规则"部分添加新场景，指定技能组合和执行顺序。

### Q: 技能执行失败后如何处理？
A: Resolver会自动加载error-handling.md，包含重试策略和自进化触发条件。

## 相关文件

- [resolver-config.md](resolver-config.md) - 路由配置文件
- [skill-descriptions.md](skill-descriptions.md) - 技能description汇总
- [error-handling.md](error-handling.md) - 失败处理指南
- [improvement-workflow.md](improvement-workflow.md) - 改进工作流
