# AI Agent Skills 仓库

管理所有AI Agent技能，每个技能独立目录存放。

---

## 技能列表

| 技能 | 版本 | 用途 |
|------|------|------|
| [xiaohongshu-publisher](skills/xiaohongshu-publisher) | v5.0 | 小红书图文笔记一键发布 |
| [diarization](skills/diarization) | v1.0 | 从非结构化内容抽取结构化档案 |

---

## 快速开始

### xiaohongshu-publisher

```bash
/xiaohongshu-publisher --mode 热点创作 --style RedInk --category AI科技 --doggie true
```

### diarization

```bash
/diarization --target "Ilya Sutskever" --sources "./AI专家信源/*.md" --focus 观点
```

---

## 目录结构

```
xiaohongshu-pubilish/
├── README.md                    # 本文件
├── skills-index.md              # 详细技能索引
└── skills/                      # 技能目录
    ├── xiaohongshu-publisher/   # 小红书发布
    └── diarization/             # 结构化档案抽取
```

---

## 技能设计原则

基于 Garry Tan 的 "Thin Harness, Fat Skills" 理念：

- **技能是方法调用**：参数化、可复用
- **承载判断**：Process + Judgment + Context + Constraints
- **不做一次性工作**：固化成skill，永久升级

详见 [skills-index.md](skills-index.md)

---

## License

MIT
