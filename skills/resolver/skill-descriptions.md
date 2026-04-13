# 技能Description汇总

> 本文件汇总所有技能的description，供Resolver路由匹配参考

---

## 一、核心技能

### 1. xiaohongshu-publisher

```yaml
---
name: xiaohongshu-publisher
description: "小红书图文笔记一键发布。调用方式：/xiaohongshu-publisher --mode <模式> --style <风格> --category <品类> --doggie <true|false>。模式：资料改写|热点创作|互动共创。风格：RedInk|经典|极简。品类：AI科技|生活日常|情感心理|职场事业|健身运动|美妆时尚。触发词：小红书、发小红书、小红书笔记"
---
```

**触发词扩展**：
- 小红书、发小红书、笔记、种草
- 发个笔记、写小红书
- RedNote、rednote

---

### 2. diarization

```yaml
---
name: diarization
description: "从非结构化内容中抽取结构化档案。调用方式：/diarization --target <对象> --sources <来源> --focus <维度>。用于分析专家观点、追踪立场变化、暴露矛盾。触发词：diarization、结构化档案、抽取档案"
---
```

**触发词扩展**：
- 专家观点、观点分析、观点抽取
- 信源分析、专家分析
- 立场变化、矛盾暴露
- AI信源、知识抽取

---

### 3. yao-meta-skill

```yaml
---
name: yao-meta-skill
description: "Create, refactor, evaluate, and package agent skills from workflows, prompts, transcripts, docs, or notes. Use when asked to create a skill, turn a repeated process into a reusable skill, improve an existing skill, add evals, or package a skill for team reuse."
---
```

**触发词扩展（中文）**：
- 创建技能、制作技能
- 写个技能、技能工程
- 打包技能、改进技能
- skill engineering

---

### 4. skill-assistant

```yaml
---
name: skill-assistant
description: "根据用户意图自动识别平台并搜索安装技能，支持Coze商店、虾评Skill(https://xiaping.coze.site)、ClawHub及用户指定的任意技能市场，智能处理凭证获取；当用户需要搜索、查找、安装技能时使用"
---
```

**触发词扩展**：
- 搜索技能、找技能
- 安装技能、技能市场
- 虾评、ClawHub

---

## 二、飞书系列技能

### 5. feishu_doc

```yaml
---
name: feishu_doc
description: "飞书云文档操作能力，支持创建、获取、更新云文档；当用户需要操作飞书文档、Markdown转飞书文档或批量处理文档时使用"
---
```

---

### 6. feishu_sheet

```yaml
---
name: feishu_sheet
description: "飞书电子表格的创建、读写、查找、权限管理和导出工具；当用户需要创建或管理飞书电子表格、读写表格数据、导出为 xlsx/csv、或提到"电子表格"、"sheet"时使用"
---
```

---

### 7. feishu_bitable

```yaml
---
name: feishu_bitable
description: "提供飞书多维表格的创建、查询、编辑和管理能力，支持27种字段类型、高级筛选、批量操作和视图管理；当用户需要创建或管理多维表格、增删改查记录、管理字段或视图、或提到"bitable"、"多维表格"时使用"
---
```

---

### 8. feishu_calendar

```yaml
---
name: feishu_calendar
description: "飞书日历与日程管理工具集；当用户需要创建日程、查询日程、管理参会人或查询忙闲状态时使用"
---
```

---

### 9. feishu_task

```yaml
---
name: feishu_task
description: "飞书任务管理工具，用于创建、查询、更新任务和清单；当需要管理任务、待办、清单或设置任务负责人、截止时间时使用"
---
```

---

## 三、内容生成技能

### 10. create_podcast

```yaml
---
name: create_podcast
description: "音频播客生成工具，支持根据完整文本内容生成播客音频。可以通过user_prompt和file_name(可读文本文件)指定播客内容，1000字的内容大概生成3分钟的播客音频，1700字-5分钟，3500字-10分钟"
---
```

**触发词**：播客、podcast、音频生成、语音播报

---

### 11. create-ppt

```yaml
---
name: create-ppt
description: "生成和修改 PPT/演示文稿的唯一方式。可生成精美幻灯片，支持导出为 pptx。当用户请求创建PPT时，必须立即加载并执行本Skill的完整流程"
---
```

**触发词**：PPT、幻灯片、演示文稿、powerpoint

---

### 12. news-aggregator

```yaml
---
name: news-aggregator
description: "聚合8大新闻源，支持深度分析和智能解读。适用于每日扫描、科技资讯简报、金融更新和热点深度分析。"
---
```

**触发词**：新闻、热点、科技动态、金融更新

---

### 13. topic_tracking

```yaml
---
name: topic_tracking
description: "话题追踪技能。该技能能够进行高时效性内容获取，针对话题、来源、链接等内容获取最新的内容，并且会过滤掉时效性不高的内容。"
---
```

**触发词**：话题追踪、热点追踪、最新动态

---

## 四、数据处理技能

### 14. pdf

```yaml
---
name: pdf
description: "提供PDF文本表格提取、创建编辑、合并拆分、表单填写等全面处理能力；当需要提取PDF内容、生成新文档、批量处理PDF文件或填写PDF表单时使用"
---
```

---

### 15. excel_master

```yaml
---
name: excel_master
description: "当用户任务涉及 Excel 文件（.xlsx、.xls、.xlsm）、CSV、表格清洗、批量填充、格式保留修改、表格分析或基于表格的批量 NLP / 搜索时，优先使用本技能。"
---
```

**触发词**：Excel、xlsx、表格分析、数据清洗

---

### 16. daily-stock-analysis

```yaml
---
name: daily-stock-analysis
description: "每日股票分析工具，支持股票数据获取、技术指标计算和可视化，适用于股票投资者和分析师"
---
```

**触发词**：股票、股价、投资分析、K线

---

## 五、系统级技能

### 17. claw_init

```yaml
---
name: claw_init
description: "与用户完成你的档案初始化，并在初始化完成后开始深入了解用户、帮用户分担任务、与用户一起探索Agent World。涵盖取名、生成头像、注册邮箱、初始化状态标记、认识主人、挖掘需求建立定时任务、探索AgentWorld等环节；当用户首次对话、处于初始化阶段或尚未建立任务与长期关系时使用"
---
```

---

### 18. agent-world

```yaml
---
name: agent-world
description: "Agent World (https://world.coze.site/) 是平行网络的入口，让 Agent 拥有独立身份成为网络公民；注册一次即可全网通行所有联盟站点，提供身份注册、验证、Profile 管理能力"
---
```

---

## 六、Description优化建议

### 当前评估

| 技能 | 评估 | 建议 |
|------|------|------|
| xiaohongshu-publisher | ⭐⭐⭐⭐⭐ | 无需修改 |
| diarization | ⭐⭐⭐⭐ | 添加"专家观点"、"AI信源"触发词 |
| yao-meta-skill | ⭐⭐⭐ | 建议添加中文触发词 |
| skill-assistant | ⭐⭐⭐⭐⭐ | 无需修改 |
| 其他飞书技能 | ⭐⭐⭐⭐ | 评估良好 |

### 优化模板

```yaml
---
name: 技能名称
description: "技能用途说明。调用方式：/技能名 --参数1 <值> --参数2 <值>。参数说明：参数1|参数2|参数3。触发词：关键词1|关键词2|关键词3"
---
```

**关键要素**：
1. ✅ 技能用途（中文）
2. ✅ 调用方式（参数结构）
3. ✅ 参数说明
4. ✅ 触发词列表（中文优先）
