# xiaohongshu-publisher

小红书图文笔记一键发布技能（RedInk风格简化版 v4.0）

## 核心理念

**简单就是好**：
- ❌ 不用复杂的英文分层prompt
- ❌ 不用颜色代码（#1A1A2E会显示在图上）
- ✅ 用简单中文描述
- ✅ 封面图作为参考图传给内容页，保持风格一致

## 三种模式

| 模式 | 触发条件 | 输入 | 输出 |
|------|----------|------|------|
| **资料改写** | 用户提供素材 | 链接/PDF/文字/图片 | 完整笔记 |
| **热点创作** | 用户说"热点"、"爆款" | 品类/方向 | 热点分析 + 笔记 |
| **互动共创** | 用户说"一起写" | 模糊想法 | 对话引导 → 笔记 |

## 文件结构

```
xiaohongshu-publisher/
├── SKILL.md                 # 主文件（v4.0 RedInk风格）
├── SKILL-v3-backup.md       # 旧版备份
├── config.yaml              # API配置
├── prompts/
│   └── doggie-character.md  # Doggie IP角色设定
└── references/
    ├── cover-prompt-v4.md   # 封面图生成指南（RedInk风格）
    ├── content-image-v4.md  # 内容图生成指南（RedInk风格）
    ├── cover-prompt.md      # 旧版封面指南
    ├── content-image.md     # 旧版内容图指南
    └── copywriting.md       # 文案写作指南
```

## RedInk方法核心

### 1. 简单中文Prompt

```
请生成一张小红书风格的封面图，尺寸1080x1440像素。

【标题内容】
SBTI刷屏了

【设计要求】
1. 整体风格：小红书爆款封面，清新精致有设计感
2. 背景色：深灰蓝渐变，科技感
3. 标题排版：标题要大、要醒目
```

### 2. 不用颜色代码

| ❌ 错误写法 | ✅ 正确写法 |
|------------|------------|
| \`Base color: #1A1A2E\` | \`背景色：深灰蓝渐变\` |
| 颜色代码会显示在图上 | 中文描述颜色 |

### 3. 参考图机制

\`\`\`python
# Step 1: 生成封面图
cover_image = generate_image(封面prompt)

# Step 2: 内容页传入封面图作为参考
content_image = generate_image(
    prompt=内容prompt,
    ref_images=[封面图路径]  # 关键！
)
\`\`\`

### 4. Doggie IP简化描述

\`\`\`
一只可爱的Q版柴犬卡通形象：
- 橘黄色毛发，白色脸蛋花纹
- 圆圆的脸，三角形的立耳朵
- 黑豆眼，小黑鼻，粉色腮红
- 穿着白衬衫和针织背心，戴着圆眼镜
- 大小：占图片高度15-20%
- 位置：右下角
\`\`\`

## 使用方法

1. 加载技能：调用 skill_load 工具
2. 选择模式：根据输入自动识别
3. 生成图片：使用RedInk风格的简化prompt
4. 发布：调用 myaibo API 发布到草稿箱

## 版本历史

- **v4.0** (2026-04-10): RedInk风格简化版，解决颜色代码显示、Doggie不一致等问题
- **v3.0**: 专家优化版，增加Doggie IP规范
- **v2.0**: 分层架构版
- **v1.0**: 初始版本

## License

MIT
