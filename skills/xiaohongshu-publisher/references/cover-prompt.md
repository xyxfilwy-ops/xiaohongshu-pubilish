# 封面图生成指南 v3.0

## 核心原则

**分层架构：一张图 = 一个 Prompt = 三层叠加**

所有图片生成都使用三层结构，让 AI 一次性生成完整的带文字图片：

| 层级 | 内容 | 优先级 |
|------|------|--------|
| **上层 TEXT** | 标题、副标题、标签 | **最高（绝对可读，主导视觉）** |
| **中层 ILLUSTRATION** | 装饰插画、Doggie 角色 | 辅助（点缀而非抢戏） |
| **底层 BACKGROUND** | 背景色、渐变、纹理 | 基础（不干扰） |

---

## 🔑 0.8秒法则（封面核心）

封面决定 **80% 点击率**，必须在 **0.8秒内** 传递核心价值：

| 要素 | 要求 |
|------|------|
| **主标题** | 3-7字，字号 ≥ 80px（实际建议100-120px） |
| **总字数** | ≤ 15字（越少越好） |
| **视觉占比** | 文字占据页面至少 **50-60%** 视觉空间 |
| **对比度** | 文字vs背景 ≥ **4.5:1** |
| **一眼识别** | 100px 缩略图下仍可读 |

### 三大要素（满足其一即可爆款）
1. **清晰主题文字** - 直击痛点/痒点
2. **吸引配色** - 暖色大地系 / 莫兰迪色系
3. **数字/对比** - 制造好奇，触发"等等，这怎么可能？"

### 四大爆款标题公式
| 公式 | 示例 |
|------|------|
| **情绪反差法** | "以为在省钱，其实一年多花2万" |
| **具体量化收益** | "3个动作，效率翻10倍" |
| **情绪宣泄共鸣** | "你是不是也这样？学了一堆但用不出来" |
| **"救命"系列** | "救命！终于有人讲清楚这个了" |

---

## Doggie IP 集成

### ⚠️ 关键原则：Doggie 是配角，不能喧宾夺主

| 场景 | Doggie 规格 | 位置 |
|------|-------------|------|
| **封面图** | 高度 15-20%（小而精致） | 角落，右下/左下 |
| **内容图** | 高度 15-25%（更活泼） | 配合内容动作 |
| **绝对禁止** | 占据画面中心、与文字重叠 | - |

### 封面图 Doggie Prompt

```
[OPTIONAL MASCOT - COVER]
Include Doggie mascot in bottom corner (15-20% of image height):
- A cute Q-style anthropomorphic Shiba Inu,
- 2.5 head-to-body ratio chibi proportions,
- orange-yellow fur with white face mask pattern,
- round face with triangle standing ears, small black dot eyes,
- pink circular blush on both cheeks, fluffy curled tail,
- {品类服装} — see prompts/doggie-character.md
- Small gesture related to the title theme (looking curious/thumbs up/pointing)
- Position: bottom-right or bottom-left corner
- Style: Subtle, semi-transparent at 85% opacity, NOT competing with text
```

### 品类服装映射

| 品类 | Doggie 服装 | 表情建议 |
|------|-------------|----------|
| beauty | 白色蕾丝围裙 + 蝴蝶结发箍 | 惊喜/兴奋 |
| fashion | 条纹T恤 + 背带裤 + 墨镜 | 自信/耍酷 |
| fitness | 运动背心 + 头带 | 加油/战斗 |
| education | 白衬衫 + 针织背心 + 圆眼镜 | 认真/可爱 |
| daily | 奶白色卫衣 | 温暖/治愈 |
| relationship | 粉色毛衣 + 围巾 | 温柔/害羞 |
| career | 小西装 + 领结 | 专业/认真 |
| travel | 渔夫帽 + 夏威夷衬衫 | 兴奋/探索 |

---

## 配色方案

### 配色趋势（选一）

| 风格 | 配色方案 |
|------|----------|
| **暖色大地系**（高信任感） | 背景: 温暖米色 #F5F0E8 / 文字: 深棕色 #4A3F35 / 强调: 焦糖色 #D4956A |
| **莫兰迪色系**（高级感） | 背景: 奶白色 #F8F6F3 / 文字: 雾霾蓝 #6B7B8C / 强调: 浅灰粉 #C4A5A5 |
| **科技风** | 背景: 深灰 #1A1A2E / 文字: 纯白 #FFFFFF / 强调: 科技蓝 #00D4FF |
| **清新自然** | 背景: 浅绿米 #EEF5E8 / 文字: 森林绿 #3D5A3D / 强调: 暖黄 #E8B86D |

### 色彩应用规则

```
强调色应用场景：
- 标题中的关键词/数字
- 高亮词
- 数字冲击版式的hero number
- 图标、装饰元素

文字色应用场景：
- 主标题（与背景高对比）
- 副标题
- 正文内容

背景色应用场景：
- 底层LAYER 1
- 渐变中心/边缘
```

---

## 封面图规格

| 参数 | 值 | 说明 |
|------|-----|------|
| 尺寸 | 1080 × 1440px | 3:4 竖版，小红书标准 |
| 主标题字号 | 100-120px | 确保100px缩略图可读 |
| 副标题字号 | 28-32px | 可选，增强信息 |
| 文字量 | 3-7字主标题 + 可选副标题 | 越少越有力 |
| 目的 | 0.8秒抓眼球，CTR是唯一指标 | - |

---

## 四大版式模板

### 1. 大字报版式（默认，CTR 最高）

**适用**：痛点扎心、极端结论、悬念好奇

```
Generate a Xiaohongshu COVER image (1080x1440px, 3:4 ratio).
This is a HEADLINE BOMB design - the text must dominate within 0.8 seconds.

===== LAYER 1: BACKGROUND (底层) =====
Base color: {背景色} solid
Gradient: Subtle radial from center, lighter at center (+10% brightness)
Texture: None or very subtle noise at 3%
Mood: Clean, modern, inviting, instantly readable

===== LAYER 2: ILLUSTRATION (中层) =====
Style: Abstract geometric shapes, EXTREMELY subtle
Elements:
  • Two soft glowing orbs (one {强调色}, one {辅助色}) at 8-12% opacity
  • Positioned at top-right and bottom-left corners
  • Blurred edges (50px Gaussian equivalent)
  • Optional: thin decorative lines at 5% opacity
  • DO NOT overlap with text area

[MASCOT - OPTIONAL]
Include Doggie mascot:
- Position: bottom-right corner, 15-18% of image height
- Gesture: looking curious or making a subtle supportive gesture
- Style: Semi-transparent at 80%, NOT competing with title
- See prompts/doggie-character.md for costume details

⚠️ CRITICAL: Illustrations are BACKGROUND SUPPORTS, never compete with text

===== LAYER 3: TEXT (上层 - DOMINANT) =====

【Main Title - 主导视觉，占50-60%画面】
Content: "{标题}"
Font: Extra Bold Chinese (思源黑体 Heavy / 苹方 Bold style)
Size: 100-120px equivalent
Color: {文字色}
Effects:
  • Subtle drop shadow (2px offset, 15% opacity, 8px blur)
  • Optional: thin white outline (1px) for extra pop on colored backgrounds
Position: Center-dominant, vertically centered or slightly above center
Line break: At natural pause point after {断句字数} characters

【Highlight Word/Number - 第一眼焦点】
Content: "{高亮词}" (数字或情绪关键词)
Color: {强调色}
Size: 130% of main title size
Position: Within main title, same line or highlighted
Purpose: This word/number is the FIRST thing the eye sees

【Subtitle/Tag】(optional)
Content: "{副标题}"
Font: Medium weight Chinese
Size: 28-32px
Color: {文字色} at 70% opacity
Position: 20px below main title

===== COMPOSITION RULES =====
✅ Title dominates - occupies 50-60% of visual weight
✅ Text readable at 100px thumbnail width
✅ Strong contrast: text vs background > 4.5:1
✅ Single clear focal point (the title)
✅ 0.8 seconds = user decides click or skip

===== ANTI-PATTERNS =====
❌ Text smaller than 80px
❌ More than 15 characters in title
❌ Illustrations that overlap or compete with text
❌ Busy or distracting backgrounds
❌ Multiple focal points
❌ Low contrast text
```

---

### 2. 数字冲击版式

**适用**：有具体数字的标题（3天瘦5斤、效率翻10倍）

```
Generate a Xiaohongshu COVER image (1080x1440px, 3:4 ratio).
This is a NUMBER IMPACT design - the number triggers "Wait, that's impressive!"

===== LAYER 1: BACKGROUND =====
Base: {背景色} solid
Gradient: Subtle radial from center, creating spotlight effect on number
Optional: Very subtle starburst pattern at 5% opacity radiating from number

===== LAYER 2: ILLUSTRATION =====
Style: Minimal accent elements, all supporting the number
Elements:
  • Circular badge or pill shape behind the hero number (12% opacity, {强调色})
  • Small decorative sparkles ✦ around number at 15% opacity
  • Optional: thin connecting lines suggesting "achievement"

[MASCOT - OPTIONAL]
Include Doggie mascot:
- Position: bottom-left corner, 15% of image height
- Gesture: surprised/amazed expression, supporting the "wow" moment
- Style: Subtle, 80% opacity

===== LAYER 3: TEXT =====

【Hero Number - 视觉焦点，占40%画面高度】
Content: "{数字}"
Font: Extra Bold / Black weight
Size: MASSIVE - 150-200px equivalent (largest element on page)
Color: {强调色}
Position: Center, occupying 40% of image height
Effects: Bold weight + subtle glow (same color, 20% opacity, 30px blur)

【Context Text - Above】
Content: "{上文}" (如："坚持了"、"只用")
Font: Regular weight
Size: 36-42px
Color: {文字色}
Position: Centered above hero number

【Context Text - Below】
Content: "{下文}" (如："天"、"招")
Font: Regular weight
Size: 36-42px
Color: {文字色}
Position: Centered below hero number

【Result/Benefit】
Content: "{结果说明}" (如："我的变化惊人")
Font: Regular weight
Size: 28-32px
Color: {文字色} at 80% opacity
Position: Bottom area

===== LAYOUT EXAMPLE =====
        坚持了          (36px, regular)
          30            (180px, BOLD, {强调色})
          天            (36px, regular)

    我的变化惊人        (28px, 80% opacity)

===== PSYCHOLOGY =====
The number triggers: "Wait, that's impressive/surprising/achievable"
0.8 seconds to make user think: "How is that possible?"
```

---

### 3. 对比冲突版式

**适用**：A vs B、以为X其实Y、错误做法vs正确做法

```
Generate a Xiaohongshu COVER image (1080x1440px, 3:4 ratio).
This is a CONTRAST SPLIT design - visual contrast makes the point instantly.

===== LAYER 1: BACKGROUND =====
Split design:
  • Left/Top side: Muted, desaturated ({背景色} darkened 20%)
  • Right/Bottom side: Vibrant ({背景色} normal)
  • Diagonal or vertical split line

===== LAYER 2: ILLUSTRATION =====

【Wrong Side Elements】
  • ❌ icon or crossed-out symbol
  • Desaturated, faded treatment
  • Optional: subtle "X" pattern overlay at 5% opacity

【Right Side Elements】
  • ✅ icon or glowing checkmark
  • Vibrant, emphasized treatment
  • Optional: subtle glow/highlight

【Divider】
  • Diagonal line, "VS" badge, or contrasting split
  • VS badge: {强调色} circle with white "VS" text
  • Position: Center of the divide

[MASCOT - OPTIONAL]
Include Doggie mascot:
- Position: bottom-right corner (right/good side), 15% height
- Gesture: thumbs up or pointing to the "correct" side
- Style: Celebrating the right choice

===== LAYER 3: TEXT =====

【Wrong Way Text】
Content: "{错误做法}"
Font: Regular weight, strikethrough optional
Size: 48-56px
Color: Gray (#888) or muted red
Position: Left/Top side
Style: Faded, deemphasized

【Right Way Text】
Content: "{正确做法}"
Font: Bold weight
Size: 56-64px (slightly larger)
Color: {强调色}
Position: Right/Bottom side
Style: Emphasized, confident

【Optional Header】
Content: "{主题}" (如："学习方法")
Size: 36px
Position: Top center
Color: {文字色}

===== CONTRAST MUST BE DRAMATIC =====
❌ Wrong side: faded, crossed out, gray
✅ Right side: vibrant, glowing, colored
Visual contrast should be INSTANT and OBVIOUS within 0.8 seconds
```

---

### 4. 清单列表版式

**适用**：N个方法、N个技巧、完整攻略

```
Generate a Xiaohongshu COVER image (1080x1440px, 3:4 ratio).
This is a CHECKLIST PREVIEW design - shows value promise at a glance.

===== LAYER 1: BACKGROUND =====
Base: {背景色} solid, clean
Texture: Optional paper-like texture at 5% opacity
Mood: Organized, structured, "this is useful"

===== LAYER 2: ILLUSTRATION =====
Style: Minimal list-style decorations
Elements:
  • Numbered circles (❶ ❷ ❸ ❹ ❺) or checkbox icons (☐ ✓)
  • Numbers in {强调色}, circles in lighter tint
  • Thin horizontal lines between items at 10% opacity

[MASCOT - OPTIONAL]
Include Doggie mascot:
- Position: bottom-right corner, 15% height
- Gesture: checking off items / excited about the list
- Style: Subtle support role

===== LAYER 3: TEXT =====

【Header Title】
Content: "{主标题}" (如："高效学习的5个方法")
Font: Bold
Size: 56-64px
Color: {文字色}
Position: Top area (top 20%)

【List Preview】
Content: 3-5 preview items, each 2-4 characters
Format:
  ❶ {要点1缩写}
  ❷ {要点2缩写}
  ❸ {要点3缩写}
  ❹ {要点4缩写} ← partial visibility (faded)
  ❺ ... ← dots to imply more

Font: Regular
Size: 36-42px
Color: {文字色}
Position: Middle 60% of image
Style: List items slightly faded toward bottom (100%→80%→60%)

【CTA Hint】(optional)
Content: "点击查看完整版 →"
Size: 24px
Color: {强调色}
Position: Bottom area
```

---

## Prompt 变量速查表

| 变量 | 说明 | 示例 |
|------|------|------|
| `{背景色}` | 背景主色 | #F5F0E8, #F8F6F3 |
| `{文字色}` | 主标题/正文色 | #4A3F35, #6B7B8C |
| `{强调色}` | 高亮/数字/图标 | #D4956A, #00D4FF |
| `{辅助色}` | 装饰元素 | #E8B86D, #C4A5A5 |
| `{标题}` | 主标题，3-7字 | "救命！终于有人讲清楚了" |
| `{高亮词}` | 标题中要突出的词 | "救命"、"3天" |
| `{副标题}` | 补充说明 | "亲测有效" |
| `{品类}` | 内容品类 | beauty, fitness, education |

---

## 快速生成 Checklist

在生成封面图前，确认以下要素：

```
□ 主标题 3-7 字？
□ 总字数 ≤ 15 字？
□ 字号 ≥ 80px（建议100-120px）？
□ 文字占据 50-60% 视觉空间？
□ 对比度 ≥ 4.5:1？
□ Doggie 位于角落，高度 15-20%？
□ 选择了合适的配色方案？
□ 满足四大爆款公式之一？
□ 0.8秒内能传递核心价值？
```
