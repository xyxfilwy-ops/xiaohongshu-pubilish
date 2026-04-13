# Skills 技能索引

本仓库管理所有AI Agent技能，每个技能独立目录存放。

---

## 技能列表

| 技能名称 | 版本 | 用途 | 目录 |
|----------|------|------|------|
| xiaohongshu-publisher | v5.0 | 小红书图文笔记一键发布 | [skills/xiaohongshu-publisher](skills/xiaohongshu-publisher) |
| diarization | v1.0 | 从非结构化内容抽取结构化档案 | [skills/diarization](skills/diarization) |

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

\`\`\`
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
    └── diarization/             # 结构化档案抽取
        ├── SKILL.md
        ├── templates/
        └── references/
\`\`\`

---

*最后更新：2026-04-13*
