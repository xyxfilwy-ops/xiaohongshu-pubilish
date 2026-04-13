# 内容图生成指南 v3.0

## 核心原则

**分层架构：一张图 = 一个 Prompt = 三层叠加**

内容图的核心目的是**承载阅读**，文字必须清晰可读。

| 层级 | 封面图 | 内容图（本文档）|
|------|--------|----------------|
| 上层 TEXT | 大标题为主 | **正文内容为主（80-120字）** |
| 中层 ILLUSTRATION | 极简装饰 | **极简装饰 + Doggie（更活泼）** |
| 底层 BACKGROUND | 高对比 | **柔和护眼** |

---

## 🔑 信息密度法则

| 参数 | 值 | 说明 |
|------|-----|------|
| **每页字数** | 80-120字 | 超过太挤，阅读疲劳 |
| **总页数** | 6-9页 | 太少没内容，太多没耐心 |
| **字号** | 36-42px | 确保可读性 |
| **行高** | 1.8x | 阅读舒适 |
| **留白** | 段落间留白 | 提升呼吸感 |

### 三段式呼吸排版

```
┌─────────────────────────────────────┐
│  ▸ 钩子句（开头）                    │  ← 抓注意力，强调色
│                                     │
│    正文内容                          │  ← 核心价值，关键词高亮
│    （60-100字）                      │
│                                     │
│    悬念句（结尾）→                   │  ← 驱动翻页，渐隐效果
│                                     │
│             X/Y                     │  ← 页码指示
└─────────────────────────────────────┘
```

### 关键词晶体化

- 核心词嵌入首段并视觉强化
- 使用高亮/下划线等效果
- 数字/关键数据放大处理

---

## Doggie IP 集成

### ⚠️ 关键原则：Doggie 是配角，配合内容做动作

| 场景 | Doggie 规格 | 说明 |
|------|-------------|------|
| **封面图** | 高度 15-20% | 小而精致，位于角落 |
| **内容图** | 高度 15-25% | **更活泼，配合内容做动作** |
| **绝对禁止** | 占据画面中心、与文字重叠 | - |

### 动作 × 内容类型映射

| 内容阶段 | Doggie 动作 | 位置 | 表情 |
|----------|-------------|------|------|
| **痛点揭示** | 双手捧脸，惊讶表情 | 左下角 | 震惊 |
| **问题分析** | 挠头思考状 | 右下角 | 困惑 |
| **方法步骤** | 竖起食指，认真表情 | 右下角 | 认真 |
| **经验分享** | 单手挥手打招呼 | 底部中央 | 热情 |
| **对比展示** | 双手比✗ vs 双手比✓ | 中间两侧 | 嫌弃/开心 |
| **结论总结** | 双手比心，开心表情 | 右下角 | 满足 |
| **行动号召** | 双手握拳加油姿势 | 底部中央 | 加油 |

### 内容图 Doggie Prompt

```
[MASCOT - CONTENT PAGE]
Include Doggie mascot matching the content type:
- Size: 15-25% of image height (slightly larger than cover for more expression)
- Position: {根据内容类型选择，见上方映射表}
- Gesture: {对应的动作描述}
- Expression: {对应的表情}
- Costume: {品类服装} — see prompts/doggie-character.md
- Style: Semi-transparent at 85%, cute and approachable
- Do NOT overlap with text areas (keep 40px minimum distance)
```

### 品类服装映射

| 品类 | Doggie 服装 | 适用场景 |
|------|-------------|----------|
| beauty | 白色蕾丝围裙 + 蝴蝶结发箍 | 美妆教程、好物推荐 |
| fashion | 条纹T恤 + 背带裤 + 墨镜 | 穿搭分享、时尚种草 |
| fitness | 运动背心 + 头带 | 健身教程、减脂分享 |
| education | 白衬衫 + 针织背心 + 圆眼镜 | 学习方法、知识分享 |
| daily | 奶白色卫衣 | 日常vlog、生活记录 |
| relationship | 粉色毛衣 + 围巾 | 情感故事、人际交往 |
| career | 小西装 + 领结 | 职场干货、职业发展 |
| travel | 渔夫帽 + 夏威夷衬衫 | 旅行攻略、打卡分享 |

---

## 内容图规格

| 参数 | 值 | 说明 |
|------|-----|------|
| 尺寸 | 1080 × 1440px | 3:4 竖版 |
| 正文字数 | 80-120字/页 | 超过会太挤 |
| 总页数 | 6-9页 | 太少没内容，太多没耐心 |
| 字号 | 36-42px | 确保可读性 |
| 行高 | 1.8x | 阅读舒适 |
| 内边距 | 80px | 文字不贴边 |

---

## 钩子系统（6大类型）

### 1. 极端台词型（推荐第1页）
> 用一句扎心的话开场，制造"说的就是我"的共鸣

- "三天了，你没和真人好好说过一句话。"
- "你以为你在学习，其实你在表演努力。"
- "收藏了500个教程，一个都没看完。"

### 2. 极端画面型
> 描述一个具体的崩溃场景，让用户代入

- "凌晨两点，你又在刷手机，明天还有早会。"
- "打开收藏夹，满满当当，但你什么都没记住。"

### 3. 痛点扎心型（推荐第2页）
> 用亲身经历拉近距离，增加信任

- "说真的，这个坑我踩了整整两年。"
- "你是不是也这样，学了一堆但用不出来？"

### 4. 反常识型
> 打破常规认知，制造认知冲突

- "你一直在用的方法，可能从根上就是错的。"
- "越努力越学不会，这不是鸡汤是真的。"

### 5. 数据冲击型
> 用具体数字制造震撼

- "测了一下，这个方法效果好了10倍。"
- "坚持了30天，变化大到我自己都不信。"

### 6. 代价感型
> 强调不改变的后果，制造紧迫感

- "再不改，你会一直卡在这个阶段。"
- "每拖一天，差距就大一点。"

---

## 悬念系统（5大类型）

### 1. 断裂型（最强翻页驱动力）
> "但最关键的一步，我还没说……"

- "但最关键的一步，我还没说……"
- "真正改变我的，是后面这件事……"

### 2. 转折型
> 暗示事情没那么简单

- "但转折来了。"
- "事情没那么简单。"

### 3. 代价型
> 强调不知道某信息的代价

- "不知道这个，前面全白做了。"
- "少了这一步，效果直接打折。"

### 4. 递进型
> 暗示后面还有更精华的内容

- "以上都是铺垫，精华在后面。"
- "这只是基础，进阶玩法更绝。"

### 5. 引导型（推荐倒数第2页）
> 直接引导翻页

- "具体怎么操作？下一页拆解↓"
- "干货预警，下一页全是重点↓"

---

## 分层 Prompt 模板

### 通用内容图模板

```
Generate a Xiaohongshu CONTENT PAGE image (1080x1440px, 3:4 ratio).
This is page {X} of {Y}. This is a READING page - text readability is #1 priority.

===== LAYER 1: BACKGROUND (底层) =====
Base color: {背景色} (same as cover for consistency)
Texture: Very subtle paper/noise texture at 3-5% opacity
Gradient: None or extremely subtle
Mood: Clean, calm, reading-optimized, easy on the eyes

⚠️ CRITICAL: Background must be CALM and UNOBTRUSIVE
No busy patterns, no illustrations, no distractions

===== LAYER 2: ILLUSTRATION (中层) =====
Style: Minimal, nearly invisible
Elements:
  • Small themed icon ({主题图标}) as bullet/section marker, {强调色}, 24px
  • Thin horizontal divider line between sections, {文字色} at 10% opacity
  • Optional: tiny decorative dots at corners, {强调色} at 15% opacity

[MASCOT - CONTENT PAGE]
Include Doggie mascot matching this content type:
- Position: {根据内容类型选择位置}
- Gesture: {对应的动作描述}
- Expression: {对应的表情}
- Size: 18-22% of image height (larger than cover for more expression)
- Style: Cute, semi-transparent at 85%
- Do NOT overlap with text areas

⚠️ CRITICAL: Illustrations must be EXTREMELY subtle
They ENHANCE readability, never distract from it
Keep total illustration area under 5% of image

===== LAYER 3: TEXT (上层 - MAIN CONTENT) =====

【Hook Line — 钩子句】
Content: "{钩子句}"
Font: Bold Chinese (思源黑体 Bold)
Size: 42-44px
Color: {强调色}
Position: Top area, after 80px padding
Prefix: ▸ symbol in {强调色}
Effect: Slightly larger than body text, stands out

【Body Content — 正文】
Content:
"{正文内容，80-120字}"

Font: Regular Chinese (思源黑体 Regular / 苹方 Regular)
Size: 36-40px
Line height: 1.8x (comfortable reading)
Color: {文字色}
Padding: 80px on all sides
Alignment: Left-aligned

【Visual Emphasis within Body】
- Key terms: {强调色} background at 12% opacity (highlight effect)
- Numbers: {强调色} color + slightly larger (42px)
- Important phrase: thin wavy underline in {强调色} at 60% opacity

【Suspense Line — 悬念句】
Content: "{悬念句}"
Font: Regular Chinese, italic-style if possible
Size: 36px
Color: {文字色} fading from 100% to 50% opacity
Position: Bottom area, before page indicator
Suffix: → or ↓ symbol
Effect: Visual fade-out suggests continuation

【Page Indicator】
Content: "{X}/{Y}"
Font: Light weight
Size: 24px
Color: {文字色} at 35% opacity
Position: Bottom center, 40px from bottom edge

===== TEXT EMPHASIS SYSTEM =====
Apply these ONLY where marked in content:

Type A - Keyword Highlight:
  Background: {强调色} at 12% opacity
  Padding: 4px horizontal
  Use for: Core concepts, key terms

Type B - Number Emphasis:
  Color: {强调色}
  Size: 110% of body size
  Optional: circular badge background
  Use for: Statistics, quantities

Type C - Quote/Golden Line:
  Underline: Wavy line in {强调色} at 50%
  Optional: ✦ decoration
  Use for: Most powerful sentence

Type D - List Marker:
  Style: ❶❷❸ or ◆ in {强调色}
  Use for: Numbered steps or points

===== TYPOGRAPHY RULES =====
✅ Every line must be readable at a glance
✅ Generous whitespace - content should "breathe" (留白呼吸)
✅ Clear visual hierarchy: Hook > Body > Suspense
✅ Consistent margins and padding (80px minimum)

===== ANTI-PATTERNS =====
❌ Text smaller than 36px
❌ Line height less than 1.6x
❌ More than 120 characters on a page
❌ Busy or colorful backgrounds
❌ Illustrations that overlap with text
❌ Cover-style layouts (big title, minimal text)
❌ Text touching edges (need 80px padding minimum)
❌ Doggie overlapping text or dominating the page
```

---

## 特殊页面模板

### 第1页（开场页）

> 目的：3秒内让用户决定继续还是划走

```
===== LAYER 3: TEXT - OPENING PAGE =====

【Big Hook — 极端台词钩子】
Content: "{极端台词钩子}"
Font: Bold
Size: 48px (larger than normal hook)
Color: {强调色}
Position: Top 30%
Style: Dramatic, like a movie opening line
Prefix: ▸ symbol

【Supporting Context】
Content: "{背景说明，50字以内}"
Font: Regular
Size: 38px
Color: {文字色}
Position: Middle

【Teaser】
Content: "{整篇笔记的价值预告}"
Font: Regular
Size: 36px
Color: {文字色} at 80%
Position: Lower area

【Suspense】
Content: "往下看，你会发现……"
Style: Fading, with ↓ arrow
Size: 32px

[MASCOT - OPENING PAGE]
Include Doggie:
- Position: bottom-right corner, 20% height
- Gesture: pointing downward with curiosity (引导翻页)
- Expression: excited and curious
```

### 第2页（痛点深化）

> 目的：让用户产生"这不就是我吗"的共鸣

```
===== LAYER 3: TEXT - PAIN POINT PAGE =====

【Pain Point Hook】
Content: "{痛点描述}"
Font: Bold
Size: 44px
Color: {强调色}
Position: Top

【Personal Experience】
Content: "{亲身经历，80字左右}"
Font: Regular
Size: 38px
Color: {文字色}
Line height: 1.8x

【Impact Statement】
Content: "{影响说明}"
Font: Regular
Size: 36px
Color: {文字色} at 80%

[MASCOT - PAIN POINT PAGE]
Include Doggie:
- Position: bottom-left corner, 18% height
- Gesture: hands on cheeks, shocked/surprised face
- Expression: relatable pain/discomfort
```

### 中间页（方法/步骤页）

> 目的：提供干货价值，让用户愿意收藏

```
===== LAYER 3: TEXT - METHOD PAGE =====

【Step Marker】
Content: "❶ / ❷ / ❸"
Font: Bold
Size: 32px
Color: {强调色}
Position: Top-left

【Step Title】
Content: "{步骤标题}"
Font: Bold
Size: 42px
Color: {文字色}
Position: Below marker

【Step Content】
Content: "{步骤详解，80-100字}"
Font: Regular
Size: 38px
Color: {文字色}
Line height: 1.8x

【Key Point Highlight】
Content: "{核心要点}"
Style: {强调色} background at 12% opacity
Size: 38px

【Transition】
Content: "{过渡句，引导下一页}"
Font: Regular, italic
Size: 32px
Color: {文字色} at 60%

[MASCOT - METHOD PAGE]
Include Doggie:
- Position: bottom-right corner, 18% height
- Gesture: raising index finger (认真讲解)
- Expression: serious but adorable
```

### 倒数第2页（引导翻页）

> 目的：驱动用户翻到最后一页

```
===== LAYER 3: TEXT - PREVIEW PAGE =====

【Preview Hook】
Content: "最后这步，才是精髓"
Font: Bold
Size: 44px
Color: {强调色}
Position: Top

【Hint Content】
Content: "{关键提示，60字}"
Font: Regular
Size: 38px
Color: {文字色}

【Page Turn Cue】
Content: "翻下一页 ↓"
Font: Bold
Size: 36px
Color: {强调色}
Position: Bottom center
Style: Pulsing animation effect if possible

[MASCOT - PREVIEW PAGE]
Include Doggie:
- Position: bottom-left corner, 20% height
- Gesture: pointing to next page (引导翻页)
- Expression: mysterious/surprised
```

### 最后一页（收尾页）

> 目的：总结价值 + 行动号召

```
===== LAYER 3: TEXT - CLOSING PAGE =====

【Summary Header】
Content: "总结一下"
Font: Bold
Size: 44px
Color: {强调色}
Position: Top

【Key Takeaways】
Content: 3-5 bullet points summarizing the entire post
Format:
  ✓ {要点1}
  ✓ {要点2}
  ✓ {要点3}
Font: Regular
Size: 38px
Bullets: {强调色} checkmarks
Line height: 1.8x

【Call to Action】
Content: "觉得有用的话，收藏起来以后用！"
Font: Regular
Size: 36px
Color: {文字色}
Position: Bottom area

【Final Engagement】
Content: "评论区聊聊你的经历"
Font: Regular
Size: 32px
Color: {文字色} at 70%

[MASCOT - CLOSING PAGE]
Include Doggie:
- Position: bottom-right corner, 22% height
- Gesture: hands making heart shape / thumbs up
- Expression: happy, satisfied, grateful
```

---

## 五图四律

### 构图律
- 三分法：重要元素放在交叉点
- 对角线：引导视线流动
- 黄金比例：视觉最舒适的分布

### 光影律
- 文字区域保持足够亮度
- Doggie 可适当添加柔和阴影增加立体感
- 避免大面积暗色区域影响阅读

### 焦点律
- 每页只有一个视觉焦点（钩子句）
- 正文作为支撑，不抢焦点
- Doggie 作为次级焦点，引导阅读

### 色彩律
- 背景色：柔和、不刺眼
- 强调色：用于钩子和关键词
- 文字色：与背景高对比，易读

---

## Prompt 变量速查表

| 变量 | 说明 | 示例 |
|------|------|------|
| `{背景色}` | 背景主色 | #F5F0E8, #F8F6F3 |
| `{文字色}` | 主标题/正文色 | #4A3F35, #6B7B8C |
| `{强调色}` | 高亮/数字/图标 | #D4956A, #00D4FF |
| `{主题图标}` | 内容相关小图标 | 📚, 💪, ✨ |
| `{钩子句}` | 抓注意力的开头 | "你以为在学习..." |
| `{正文内容}` | 核心价值文字 | 80-120字 |
| `{悬念句}` | 驱动翻页的结尾 | "但最关键..." |
| `{品类}` | 内容品类 | beauty, fitness |
| `{X}/{Y}` | 当前页/总页数 | 3/6 |

---

## 快速生成 Checklist

在生成内容图前，确认以下要素：

```
□ 每页字数 80-120 字？
□ 字号 36-42px？
□ 行高 1.8x？
□ 内边距 80px？
□ 有清晰的钩子句（强调色）？
□ 有驱动翻页的悬念句？
□ Doggie 位置正确、不遮挡文字？
□ Doggie 动作与内容类型匹配？
□ 关键词有视觉强化（高亮/下划线）？
□ 留白充足，内容"呼吸"？
□ 与封面配色保持一致？
```
