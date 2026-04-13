# Skills 技能索引

本仓库管理所有AI Agent技能，每个技能独立目录存放。

---

## 技能列表

| 技能名称 | 版本 | 用途 | 目录 |
|----------|------|------|------|
| xiaohongshu-publisher | v5.0 | 小红书图文笔记一键发布 | [skills/xiaohongshu-publisher](skills/xiaohongshu-publisher) |
| diarization | v1.0 | 从非结构化内容抽取结构化档案 | [skills/diarization](skills/diarization) |
| learning-loop | v1.0 | 技能自进化学习循环系统 | [skills/learning-loop](skills/learning-loop) |
| resolver | v1.0 | 技能路由与上下文解析机制 | [skills/resolver](skills/resolver) |

---

## 技能详情

### xiaohongshu-publisher v5.0

**用途**：小红书图文笔记一键发布

**调用方式**：
```bash
/xiaohongshu-publisher
  --mode <模式>        # 资料改写|热点创作|互动共创
  --style <风格>       # RedInk|经典|极简
  --category <品类>    # AI科技|生活日常|情感心理|...
  --doggie <布尔>      # true|false
```

**核心能力**：
- 三种创作模式
- 参数化配置（风格、品类、Doggie开关）
- RedInk风格简化prompt
- 参考图机制保持风格统一

**相关文档**：
- [SKILL.md](skills/xiaohongshu-publisher/SKILL.md)
- [封面图指南](skills/xiaohongshu-publisher/references/cover-prompt-v4.md)
- [内容图指南](skills/xiaohongshu-publisher/references/content-image-v4.md)

---

### diarization v1.0

**用途**：从非结构化内容中抽取结构化档案

**调用方式**：
```bash
/diarization
  --target <对象>        # 专家/主题/人物
  --sources <来源列表>   # 信源文件或URL
  --focus <关注维度>     # 观点|立场|预测|方法论|关系
```

**核心能力**：
- 观点矩阵抽取
- 矛盾分析（内部/外部）
- 时间线生成
- 缺口标注

**应用场景**：
- AI专家信源扫描
- 专家观点追踪
- 公司战略分析

**相关文档**：
- [SKILL.md](skills/diarization/SKILL.md)
- [专家档案模板](skills/diarization/templates/expert-profile.md)
- [使用示例](skills/diarization/references/examples.md)

---

### learning-loop v1.0

**用途**：技能自进化学习循环系统

**调用方式**：
```bash
python ./learning-loop/scripts/collect_feedback.py
  --skill <技能名>    # 目标技能
  --feedback <类型>   # success|fail|partial
  --notes <备注>      # 反馈详情

python ./learning-loop/scripts/analyze_feedback.py
  --skill <技能名>    # 目标技能
  --period <周期>     # day|week|month

python ./learning-loop/scripts/generate_improvement.py
  --skill <技能名>    # 目标技能
  --days <天数>       # 分析最近N天
```

**核心能力**：
- 反馈收集（collect）
- 模式分析（analyze）
- 改进建议生成（improve）
- SKILL.md自动更新

**工作流**：
```
执行技能 → collect_feedback → 日志记录 → analyze → 模式识别 → improve → SKILL.md更新
    ↑                                                                              ↓
    └──────────────────────────── 持续迭代 ◄───────────────────────────────────────┘
```

**相关文档**：
- [SKILL.md](skills/learning-loop/SKILL.md)
- [README.md](skills/learning-loop/README.md)
- [反馈日志模板](skills/learning-loop/templates/feedback-log.md)

---

### resolver v1.0

**用途**：技能路由与上下文解析机制

**核心功能**：
- **意图识别**：将用户需求映射到具体技能
- **上下文加载**：根据场景加载相关记忆和文档
- **错误处理**：技能执行失败时的降级策略
- **改进工作流**：持续优化路由规则

**路由规则示例**：
```yaml
intent_mapping:
  小红书:
    - xiaohongshu-publisher
  档案:
    - diarization
  反馈:
    - learning-loop
```

**应用场景**：
- 用户需求自动路由到合适的技能
- 技能执行前的上下文准备
- 执行失败后的降级处理

**相关文档**：
- [resolver-config.md](skills/resolver/resolver-config.md)
- [README.md](skills/resolver/README.md)
- [错误处理指南](skills/resolver/error-handling.md)
- [改进工作流](skills/resolver/improvement-workflow.md)

---

## 技能设计原则

基于 Garry Tan 的 "Thin Harness, Fat Skills" 理念：

1. **技能是方法调用，不是提示词**
   - 参数化、可复用、与上下文无关

2. **技能承载判断，不仅仅是步骤**
   - Process + Judgment + Context + Constraints

3. **Latent vs Deterministic边界清晰**
   - Latent（模型）：Judgment、Synthesis
   - Deterministic（代码）：API calls、File operations

4. **不做一次性工作**
   - 第一次手动做3-10个样本
   - 用户确认后固化成skill
   - 周期性任务挂cron

---

## 如何添加新技能

1. 在 \`skills/\` 下创建新目录
2. 创建 \`SKILL.md\` 主文件
3. 创建必要的子目录（prompts/、templates/、references/）
4. 更新本索引文件

---

## 目录结构

```
xiaohongshu-pubilish/
├── README.md
├── skills-index.md              # 本文件
└── skills/                      # 技能目录
    ├── xiaohongshu-publisher/   # 小红书发布
    │   ├── SKILL.md
    │   ├── SKILL-v3-backup.md
    │   ├── config.yaml
    │   ├── prompts/
    │   └── references/
    ├── diarization/             # 结构化档案抽取
    │   ├── SKILL.md
    │   ├── templates/
    │   └── references/
    ├── learning-loop/           # 学习循环系统
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── scripts/
    │   │   ├── collect_feedback.py
    │   │   ├── analyze_feedback.py
    │   │   └── generate_improvement.py
    │   ├── templates/
    │   └── logs/
    └── resolver/                # 技能路由机制
        ├── README.md
        ├── resolver-config.md
        ├── skill-descriptions.md
        ├── error-handling.md
        └── improvement-workflow.md
```

---

*最后更新：2026-04-13*
