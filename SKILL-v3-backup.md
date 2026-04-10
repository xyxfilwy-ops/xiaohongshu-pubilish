---
name: xiaohongshu-publisher
description: "小红书图文笔记一键发布。三种模式：(1)资料改写：链接/PDF/文字/图片→提取改写→封面图+内容图+标题+文案+话题 (2)热点创作：自动搜索小红书爆款→转化为自己的内容 (3)互动共创：通过对话问答共同打磨内容。触发词：小红书、发小红书、小红书笔记、图文笔记、一键发布小红书"
---

# 小红书图文笔记一键发布 v2.0

## 核心理念

**小红书的核心是图片，文字是配角**

| 维度 | 关键点 |
|------|--------|
| 封面图 | 0.8秒定生死，必须带文字（标题直接渲染在图上） |
| 内容图 | 每页都是完整的视觉作品，文字是图片的一部分 |
| 文案 | 图片下方的补充说明，SEO 关键词载体 |

---

## 内容一致性系统（关键！）

### 铁律：标题数字 = 内容数量

**执行流程**：

```
1. 分析素材 → 提取所有可用要点
2. 统计要点数量 → 确定实际数量 N
3. 生成标题 → 使用实际数量 N
4. 分页内容 → 确保每个要点都出现
```

### 数量匹配表

| 标题模式 | 示例 | 内容要求 |
|---------|------|---------|
| "N个技巧" | "7个技巧" | 必须有完整的7个技巧 |
| "N招搞定" | "5招搞定" | 必须有完整的5个方法 |
| "N步学会" | "3步学会" | 必须有完整的3个步骤 |
| 无数字 | "从根本上解决" | 不受数量约束 |

### 禁止行为

❌ 标题写"21个技巧"，内容只有6个
❌ 标题写"完整攻略"，内容缺失关键步骤
❌ 先定标题再凑内容（应该先统计内容再定标题）

### 修正机制

如果素材只能提取 N 个要点：
- 标题直接用 N（如"6个技巧"而不是"21个技巧"）
- 或者使用无数字标题（如"这些技巧真的有用"）

---

## 分层图片生成架构（核心创新）

### 设计原则

**一张图 = 一个 Prompt = 三层叠加**

```
┌─────────────────────────────────────┐
│  上层 (TEXT LAYER)                   │
│  • 标题文字                          │
│  • 正文内容                          │
│  • 页码指示                          │
├─────────────────────────────────────┤
│  中层 (ILLUSTRATION LAYER)           │
│  • 装饰插画                          │
│  • 图标符号                          │
│  • 视觉引导元素                       │
├─────────────────────────────────────┤
│  底层 (BACKGROUND LAYER)             │
│  • 背景色/渐变                        │
│  • 纹理质感                          │
│  • 氛围光效                          │
└─────────────────────────────────────┘
```

### 提示词模板（三层结构）

```
Generate a Xiaohongshu image (1080x1440px, 3:4 ratio).

===== LAYER 1: BACKGROUND (底层) =====
- Base color: {背景色}
- Gradient: subtle radial from center, {渐变方向}
- Texture: {纹理类型} at 5% opacity
- Mood: {氛围描述}

===== LAYER 2: ILLUSTRATION (中层) =====
- Style: {插画风格}
- Elements: {装饰元素列表}
- Position: {元素位置}
- Opacity: {透明度}
- Color palette: {配色}

===== LAYER 3: TEXT (上层) =====
【Title】{标题文字}
- Font: Bold Chinese (思源黑体/苹方 style)
- Size: {字号}px equivalent
- Color: {文字色}
- Position: {位置}
- Effect: {效果：阴影/描边}

【Body】{正文内容}
- Font: Regular Chinese
- Size: {字号}px
- Line height: 1.8x
- Color: {文字色}

【Accent Text】{强调文字}
- Style: {强调样式}
- Color: {强调色}

【Page Indicator】{页码} (bottom-center, 24px, 40% opacity)

===== COMPOSITION RULES =====
- Text must be FULLY READABLE, not obscured by illustrations
- Illustrations support the text, never compete with it
- Maintain visual hierarchy: Text > Illustration > Background
- All Chinese characters must be crisp and clear
```

---

## 三种模式

启动时根据用户输入自动识别模式：

| 模式 | 触发条件 | 输入 | 输出 |
|------|----------|------|------|
| **资料改写** | 用户提供素材（链接/PDF/文字/图片） | 具体素材 | 完整笔记 |
| **热点创作** | 用户说"热点"、"爆款"、"找选题" | 品类/方向 | 热点分析 + 完整笔记 |
| **互动共创** | 用户说"一起写"、"帮我想"、无明确素材 | 模糊想法 | 对话引导 → 完整笔记 |

---

## 模式一：资料改写

> 用户提供具体素材，提取改写为小红书笔记

### Phase 1：素材分析与内容规划

收到用户素材后：

```
## 素材分析

### 提取的核心要点（共 N 个）
1. {要点1} — {一句话说明}
2. {要点2} — {一句话说明}
...
N. {要点N} — {一句话说明}

### 标题建议（基于 N 个要点）
A. "{N}个{主题}的{结果}" — 数字冲击型
B. "{人群}必看 {主题}全攻略" — 身份认同型
C. "{现象}原来是这样" — 悬念好奇型（无数字）

### 内容分页预览
- 封面：标题 + 核心价值
- 第1-{X}页：每页 1-2 个要点
- 尾页：总结 + 行动引导

共 {Y} 页，确认后开始生成。
```

---

### Phase 2：封面图生成

使用 `codepilot_generate_image` 生成封面图：

```
Generate a Xiaohongshu COVER image (1080x1440px, 3:4 ratio).
This is a COVER that must grab attention in 0.8 seconds.

===== LAYER 1: BACKGROUND =====
- Base: {品类背景色} solid
- Gradient: radial from center, lighter at center
- Subtle decorative glow orbs at 15% opacity

===== LAYER 2: ILLUSTRATION =====
- Style: Modern flat illustration, clean and minimal
- Elements:
  • {与主题相关的图标/插画} at top-right, 60% opacity
  • Geometric accent shapes (circles, rounded rectangles)
  • **Doggie IP 角色（推荐使用）**：
    - 为什么用：品牌识别 + 情感连接 + 差异化（区别于其他 AI 生成的同质化内容）
    - 位置：右下角或左下角，占图片高度 20-25%
    - 设定：Q版拟人化柴犬，2.5头身，橘黄色毛发+白色面具花纹，圆脸三角立耳，黑豆眼小黑鼻，粉色腮红，蓬松卷尾
    - 服装：根据品类选择（daily=奶白卫衣，education=衬衫背心圆眼镜，career=西装领结，fitness=运动背心头带）
    - 姿态：与内容呼应（指引、兴奋、思考、疑惑等）
    - 详细设定见 prompts/doggie-character.md
- Keep illustrations SUBTLE, they should not compete with text

===== LAYER 3: TEXT (DOMINANT) =====
【Main Title】"{完整标题}"
- Font: Extra Bold Chinese (like 思源黑体 Heavy)
- Size: 100-120px equivalent, HUGE and impactful
- Color: {文字色} with subtle drop shadow
- Position: Center, occupying 50-60% of visual weight
- Line break at: {自然断句位置}

【Key Number/Word Highlight】"{数字或关键词}"
- Color: {强调色}
- Size: 130% of title size
- Make this the FIRST thing the eye sees

【Subtitle/Tag】"{副标题或标签}"
- Size: 32px
- Color: {文字色} at 70% opacity
- Position: Below main title

===== CRITICAL =====
- Title text must be INSTANTLY readable at thumbnail size
- NO more than 15 characters total in title
- Strong contrast between text and background
```

---

### Phase 3：内容图批量生成

为每一页生成内容图：

```
Generate a Xiaohongshu CONTENT PAGE image (1080x1440px, 3:4 ratio).
This is page {X} of {Y}. This is a READING page, readability is #1 priority.

===== LAYER 1: BACKGROUND =====
- Base: {品类背景色} (same as cover for consistency)
- Very subtle paper texture at 3% opacity
- Clean and minimal, optimized for reading

===== LAYER 2: ILLUSTRATION =====
- Style: Minimal line icons or small decorative elements
- Elements:
  • Small {主题相关图标} as bullet point markers
  • Thin decorative divider line (20% opacity)
  • **Doggie IP 角色（推荐使用）**：
    - 为什么用：品牌识别 + 情感连接 + 差异化
    - 位置：角落位置，占图片高度 15-20%（比封面稍小，不遮挡文字）
    - 设定：Q版拟人化柴犬，2.5头身，橘黄色毛发+白色面具花纹，圆脸三角立耳，黑豆眼小黑鼻，粉色腮红，蓬松卷尾
    - 服装：根据品类选择（与封面保持一致）
    - 姿态：根据页面内容调整（第1页疑惑、第2页思考、第3页指引、尾页挥手等）
- Keep illustrations EXTREMELY subtle
- They should ENHANCE readability, not distract

===== LAYER 3: TEXT (MAIN CONTENT) =====
【Hook Line — 钩子句】
"{钩子句}"
- Font: Bold Chinese
- Size: 44px
- Color: {强调色}
- Position: Top area
- Prefix: ▸ symbol

【Body Content — 正文】
"{正文内容，80-120字}"
- Font: Regular Chinese
- Size: 38px
- Line height: 1.8x
- Color: {文字色}
- Padding: 80px on all sides
- Key terms: highlighted with {强调色} background at 15% opacity

【Suspense Line — 悬念句】
"{悬念句}"
- Font: Italic style
- Size: 36px
- Color: {文字色} fading to 60% opacity
- Position: Bottom area
- Suffix: → or ↓ symbol

【Page Number】
"{X}/{Y}"
- Position: Bottom center
- Size: 24px
- Color: {文字色} at 40% opacity

===== VISUAL EMPHASIS =====
{根据内容标注具体强调位置}
- Numbers: enlarged and colored with {强调色}
- Key terms: subtle highlight background
- Lists: decorative bullet points

===== ANTI-PATTERNS =====
❌ Text smaller than 36px
❌ Line height less than 1.6x
❌ More than 120 characters
❌ Busy or distracting backgrounds
❌ Illustrations that overlap with text
```

---

### Phase 4：文案与话题

```
## 正文文案（图片下方显示）

{钩子段：50字以内，戳中痛点}

{核心价值：分点说明，用符号分割}

{行动引导：收藏/关注/评论}

---

### 话题标签（5-8个）
#核心话题 #细分话题 #场景话题 #人群话题 #情绪话题

### SEO关键词
- 主词：{xxx}
- 长尾：{xxx}、{xxx}
```

---

### Phase 5：质检与发布

```
## 质检清单

| 检查项 | 结果 |
|--------|------|
| 标题数字与内容数量匹配 | ✅/❌ |
| 每页文字清晰可读 | ✅/❌ |
| 图片风格统一 | ✅/❌ |
| 无 AI 味 | ✅/❌ |
| 话题精准 | ✅/❌ |

通过后调用 myaibo API 发布到草稿箱。
```

---

## 模式二：热点创作

> 自动搜索小红书爆款内容，转化为自己的原创笔记

### Phase H1：热点搜集

使用联网搜索获取当前热点：

```
## 热点搜索

搜索关键词：
- "小红书 {品类} 爆款"
- "小红书 {品类} 热门笔记"
- "{品类} 最近很火"

### 搜索结果分析（Top 10）

| 排名 | 标题 | 爆点分析 | 可复制元素 |
|------|------|----------|------------|
| 1 | {标题} | {为什么火} | {可借鉴的点} |
| 2 | ... | ... | ... |
...

### 选题建议（3个方向）

A. {选题1} — 结合热点 #{爆款标题关键词}
   角度：{切入角度}
   适合人群：{目标人群}

B. {选题2} — 蹭热度 #{热门话题}
   角度：{切入角度}
   适合人群：{目标人群}

C. {选题3} — 反向选题 #{争议点}
   角度：{切入角度}
   适合人群：{目标人群}

请选择方向（A/B/C），或告诉我你的想法。
```

---

### Phase H2：内容策划

用户选定方向后：

```
## 内容策划

### 选定方向
{用户选择的方向}

### 差异化策略
- 原爆款角度：{原来怎么写的}
- 我们的角度：{我们怎么写不一样}
- 独特价值：{我们能提供什么原创价值}

### 内容大纲

**标题**：{基于热点改造的标题}

**封面图方向**：
- 版式：{大字报/数字冲击/对比冲突/清单列表}
- 核心文案：{封面上要写什么}

**内容分页**：
- 第1页：{钩子 + 关联热点}
- 第2-N页：{核心内容}
- 尾页：{行动引导}

确认后开始生成图片。
```

---

### Phase H3-H5：图片生成与发布

> 同模式一的 Phase 2-5，生成封面图、内容图、文案、发布

---

## 模式三：互动共创

> 通过对话问答，一步步引导用户打磨内容

### Phase C1：需求挖掘

用户没有明确素材时，主动引导：

```
## 让我们一起创作！

先回答几个问题，帮我了解你的想法：

**1. 你想写什么品类？**
[ ] 美妆护肤   [ ] 穿搭时尚   [ ] 健身减脂
[ ] 学习成长   [ ] 生活日常   [ ] 情感关系
[ ] 职场干货   [ ] 旅行探店   [ ] 其他：___

**2. 你的目标读者是谁？**
例如：大学生、职场新人、宝妈、健身小白...

**3. 你有什么独特经历或专业知识？**
例如：我做过3年HR、我减肥成功20斤、我考研上岸...

**4. 你希望读者看完后？**
[ ] 学到方法/技巧
[ ] 产生共鸣/被理解
[ ] 行动（关注/收藏/购买）
[ ] 其他：___

随便聊聊就行，不用回答所有问题！
```

---

### Phase C2：选题共创

根据用户回答，给出选题建议：

```
## 选题共创

基于你分享的内容，我帮你想了几个方向：

### 选题方向 A：{经验分享型}
**标题**："{基于用户经历的标题}"
**角度**：{切入点}
**适合**：{为什么这个角度适合你}

### 选题方向 B：{干货总结型}
**标题**："{基于用户知识的标题}"
**角度**：{切入点}
**适合**：{为什么这个角度适合你}

### 选题方向 C：{情绪共鸣型}
**标题**："{情绪化标题}"
**角度**：{切入点}
**适合**：{为什么这个角度适合你}

---

你觉得哪个方向更适合你？
或者我们可以混搭，比如 A 的角度 + B 的标题风格。
```

---

### Phase C3：内容打磨

用户选定方向后，逐步打磨内容：

```
## 内容打磨

### 第一步：核心观点

你要表达的核心观点是什么？（一句话）

例如：
- "早起不是靠意志力，而是靠设计环境"
- "面试紧张不是因为你不行，是因为你太想要"

你的核心观点是：___

---

### 第二步：支撑内容

围绕核心观点，你能提供什么具体内容？

[ ] 亲身经历/故事
[ ] 方法/步骤
[ ] 数据/案例
[ ] 对比/反例
[ ] 工具/资源推荐

可以简单说说，我帮你整理成小红书的格式。

---

### 第三步：钩子设计

开头怎么抓住读者？选一个风格：

A. 扎心型："你是不是也...（痛点）"
B. 好奇型："原来...的秘密是..."
C. 反常识型："别再...了，其实..."
D. 数据型："90%的人都不知道..."

选哪个？或者你有其他想法？
```

---

### Phase C4：确认大纲

内容打磨完成后，确认完整大纲：

```
## 完整大纲确认

### 标题
{最终标题}

### 封面图
- 版式：{版式}
- 主视觉：{描述}
- 核心文案：{封面文字}

### 内容分页（共 {N} 页）

**第1页 — 钩子**
{钩子句}
{引出痛点/好奇点}

**第2页 — {小标题}**
{核心内容1}

**第3页 — {小标题}**
{核心内容2}

...

**第N页 — 行动引导**
{总结}
{引导互动}

### 文案
{底部文案预览}

### 话题
#{话题1} #{话题2} #{话题3} ...

---

确认无误后，我开始生成图片！
有任何想改的，随时告诉我。
```

---

### Phase C5-C7：图片生成与发布

> 同模式一的 Phase 2-5，生成封面图、内容图、文案、发布

---

## 去 AI 味铁律

### 必须做到
- 口语化："这玩意儿"、"说真的"、"挺有意思"
- 短句：每句不超过15字
- 用"你"称呼读者
- 有情绪温度

### 绝对禁止
- ❌ 首先/其次/最后/总之/综上所述
- ❌ 不是…而是…
- ❌ 想象一下…
- ❌ 破折号（全用逗号代替）
- ❌ 英文标点

---

## API 配置

### 图片生成

使用 Google AI Studio Gemini API：

```
Endpoint: https://aistudio.google
Model: gemini-3-pro-image-preview
API Key: {YOUR_GEMINI_API_KEY}
```

调用方式：`codepilot_generate_image`（自动使用上述配置）

### 发布接口

> 配色方案详见 [封面图生成指南](references/cover-prompt.md)

```bash
curl -X POST "https://www.myaibot.vip/api/rednote/publish" \
  -H "Authorization: Bearer {YOUR_MYAIBO_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "[标题]",
    "content": "[文案]",
    "images": ["[封面图URL]", "[内容图1URL]", ...],
    "topics": ["话题1", "话题2", ...],
    "save_draft": true
  }'
```

---

## 参考文档

- [封面图生成指南](references/cover-prompt.md) — 分层封面图 Prompt
- [内容图生成指南](references/content-image.md) — 分层内容图 Prompt
- [文案写作指南](references/copywriting.md) — 爆款标题与文案技巧
- [Doggie 角色设定](prompts/doggie-character.md) — 柴犬 IP 形象 Prompt
