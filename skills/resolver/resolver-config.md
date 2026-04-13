# Resolver路由配置

> 根据 Garry Tan 的"Thin Harness, Fat Skills"理念设计的技能路由机制
> 解析器是上下文的路由表，当任务类型X出现时，首先加载文档Y

---

## 一、关键词 → 技能映射

### 1.1 核心技能路由表

| 关键词 | 技能 | 优先级 | 触发条件 |
|--------|------|--------|----------|
| 小红书、发小红书、笔记、种草 | xiaohongshu-publisher | 高 | 用户提到发布小红书/笔记 |
| 结构化档案、抽取档案、观点抽取 | diarization | 高 | 需要从非结构化内容提取结构 |
| 专家分析、信源分析、观点追踪 | diarization | 高 | 分析专家观点、立场变化 |
| 创建技能、制作技能、写技能 | yao-meta-skill | 高 | 用户要求创建/打包技能 |
| 搜索技能、找技能、安装技能 | skill-assistant | 高 | 用户要求搜索或安装技能 |
| 飞书文档、云文档 | feishu_doc | 中 | 操作飞书文档 |
| 飞书表格、电子表格、sheet | feishu_sheet | 中 | 操作飞书电子表格 |
| 飞书多维表格、bitable | feishu_bitable | 中 | 操作飞书多维表格 |
| 日历、日程、calendar | feishu_calendar | 中 | 管理日历和日程 |
| 飞书任务、todo、待办 | feishu_task | 中 | 管理飞书任务 |
| 播客、podcast、音频 | create_podcast | 中 | 生成播客音频 |
| PDF、pdf、文档解析 | pdf | 中 | 处理PDF文件 |
| Excel、xlsx、表格分析 | excel_master | 中 | 处理Excel文件 |
| 新闻、热点、科技动态 | news-aggregator | 中 | 聚合新闻资讯 |
| 股票、股价、投资分析 | daily-stock-analysis | 中 | 股票数据分析 |
| PPT、幻灯片、演示文稿 | create-ppt | 中 | 生成PPT文件 |

### 1.2 触发词扩展库

```yaml
xiaohongshu-publisher:
  - 小红书
  - 发小红书
  - 发个笔记
  - 写小红书
  - 种草
  - 笔记发布
  - RedNote
  - rednote

diarization:
  - 结构化档案
  - 抽取档案
  - 观点分析
  - 专家观点
  - 立场变化
  - 矛盾暴露
  - 信源分析
  - diarization

yao-meta-skill:
  - 创建技能
  - 制作技能
  - 写个技能
  - 技能工程
  - skill engineering
  - 打包技能
  - 改进技能

skill-assistant:
  - 搜索技能
  - 找技能
  - 安装技能
  - 技能市场
  - 虾评
  - ClawHub
```

---

## 二、场景 → 上下文加载

### 2.1 技能执行阶段上下文

| 执行阶段 | 加载文件 | 说明 |
|----------|----------|------|
| 技能识别 | ./resolver/skill-descriptions.md | 解析技能description |
| 技能加载前 | 技能的 SKILL.md | 主流程文件 |
| 参数解析 | 技能的 references/*.md | 参数说明文档 |
| 执行失败 | ./resolver/error-handling.md | 失败处理指南 |
| 用户不满意 | ./resolver/improvement-workflow.md | 改进流程 |

### 2.2 条件上下文加载

```yaml
# 当以下情况发生时，加载对应上下文
context_triggers:
  failure_count > 3:
    - ./resolver/error-handling.md
    - ./进化引擎/self_evolution.py
  
  user_negative_feedback:
    - ./resolver/improvement-workflow.md
  
  new_domain_detected:
    - ./resolver/domain-expansion.md
    - skill-assistant
  
  skill_not_found:
    - skill-assistant  # 自动搜索匹配技能
```

---

## 三、组合技能规则

### 3.1 常见技能组合

| 场景 | 技能组合 | 说明 |
|------|----------|------|
| AI专家信源分析 | diarization + topic_tracking | 抽取观点 + 追踪最新 |
| 小红书热点创作 | xiaohongshu-publisher + news-aggregator | 热点获取 + 内容生成 |
| 播客生成 | create_podcast + news-aggregator | 资讯聚合 + 音频生成 |
| 技能创建与发布 | yao-meta-skill + feishu_doc | 创建技能 + 文档记录 |

### 3.2 组合触发条件

```yaml
combo_rules:
  ai_expert_analysis:
    triggers: ["AI专家", "专家分析", "信源追踪"]
    skills: [diarization, topic_tracking]
    order: [topic_tracking, diarization]  # 先追踪后分析
  
  hot_content_creation:
    triggers: ["热点创作", "爆款", "热点小红书"]
    skills: [news-aggregator, xiaohongshu-publisher]
    order: [news-aggregator, xiaohongshu-publisher]
```

---

## 四、技能Description优化标准

### 4.1 优秀Description的标准

```
✓ 包含技能名称（中文）
✓ 包含调用方式（参数结构）
✓ 包含触发词列表
✓ 包含使用场景说明
✓ 使用中文描述（面向中国用户）
```

### 4.2 当前技能Description评估

| 技能 | 当前Description质量 | 建议优化 |
|------|---------------------|----------|
| xiaohongshu-publisher | ⭐⭐⭐⭐⭐ | 已达标，无需修改 |
| diarization | ⭐⭐⭐⭐ | 可增加"专家观点"、"AI信源"等触发词 |
| skill-assistant | ⭐⭐⭐⭐⭐ | 已达标 |
| yao-meta-skill | ⭐⭐⭐ | 建议添加中文触发词 |

---

## 五、路由执行流程

```
用户输入
    ↓
[1. 关键词匹配]
    ↓
匹配到: xiaohongshu-publisher
    ↓
[2. 技能加载]
    ↓
加载 ./xiaohongshu-publisher/SKILL.md
    ↓
[3. 参数解析]
    ↓
识别模式: --mode 热点创作
    ↓
[4. 上下文补充]
    ↓
加载 references/cover-prompt-v4.md
    ↓
[5. 执行]
    ↓
返回结果
    ↓
[6. 评估]
    ↓
失败? → 加载 error-handling.md
不满意? → 加载 improvement-workflow.md
```

---

## 六、配置更新日志

| 日期 | 版本 | 更新内容 |
|------|------|----------|
| 2026-04-13 | v1.0 | 初始版本，包含核心路由规则 |
