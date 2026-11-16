# 写作操作手册

这份手册只回答一件事：**怎么在这个博客里写一篇文章并发布**。

---

## 一、最小流程（3 步）

### 1. 新建文件

在 `_posts/` 目录下新建一个 `.md` 文件，文件名格式固定：

```
YYYY-MM-DD-slug.md
```

- `YYYY-MM-DD` 是发布日期，**必须是这个格式**，Jekyll 靠它排序。
- `slug` 是文章 URL 的最后一段，建议用**英文小写 + 连字符**，例如 `mysql-index-notes`。
  最终网址是 `https://blog.yuzhupeng.top/post/mysql-index-notes/`。
- 注意：`slug` 里**不要用中文**，Jekyll 会把中文转成一串编码，链接很难看。

示例：`_posts/2026-11-16-redis-cache-patterns.md`

### 2. 写 front matter

文件开头必须是三横线包围的 YAML：

```yaml
---
layout: post
title: Redis 缓存模式整理
date: 2026-11-16 10:00:00
summary: 一句话说清这篇讲什么，会显示在列表页和搜索结果里。
categories: Database
---
```

字段说明：

| 字段 | 必填 | 说明 |
|---|---|---|
| `layout` | 是 | 固定写 `post`（文章页）或 `page`（独立页，如关于） |
| `title` | 是 | 文章标题，中文可以 |
| `date` | 是 | `YYYY-MM-DD HH:MM:SS`，与文件名日期一致 |
| `summary` | 建议 | 摘要，显示在列表与搜索；不写会留空 |
| `categories` | 建议 | 只能是这 6 个之一：`Database` / `Architecture` / `Backend` / `Frontend` / `AI` / `Note` |
| `poem` | 否 | 文首那句诗，可不写 |
| `comments` | 否 | 写 `true` 才显示评论区（需先在 giscus.app 配好） |
| `hidden` | 否 | 写 `true` 则不出现在列表里，但仍可访问 |

### 3. 写正文并发布

front matter 的三横线之后，就是普通 Markdown。

写完执行：

```bash
git add -A
git commit -m "post: 新增 Redis 缓存模式整理"
git push
```

push 后 GitHub Actions 会自动构建，约 1-2 分钟后访问线上地址即可看到。

---

## 二、正文写法速查

### 标题层级

```markdown
# 一级标题（文章内很少用，会被页面自带的标题挤占）
## 二级标题，最常用
### 三级标题
```

### 代码块

**必须标注语言**，否则不会有语法高亮：

````markdown
```java
public class Demo {
    public static void main(String[] args) {
        System.out.println("hello");
    }
}
```
````

支持的语言名：`java`、`csharp`、`bash`、`sql`、`vue`、`svelte`、`json`、`javascript`、`xml`、`properties`、`yaml`、`python`、`mermaid`。

### 图片

三种方式，按场景选：

**方式 1：存本地（推荐）**

1. 把图片放进 `images/posts/<文章slug>/`，例如 `images/posts/redis-cache-patterns/flow.png`
2. 正文里写：

```markdown
![流程图](/images/posts/redis-cache-patterns/flow.png)
```

**方式 2：直接引用外链**

```markdown
![截图](https://example.com/pic.png)
```

缺点：对方删图你的文章就裂了。旧博客里 159 张图都是外链，属于历史遗留。

**方式 3：图床（如果有）**

```markdown
![图](https://cdn.example.com/xxx.jpg)
```

### 表格

```markdown
| 字段 | 类型 | 说明 |
|---|---|---|
| id | bigint | 主键 |
| name | varchar(64) | 名称 |
```

### 引用块

```markdown
> 这是一段引用。主题会渲染成左侧竖线 + 灰色文字。
```

### 有序 / 无序列表

```markdown
- 无序项
- 无序项
  - 嵌套项（前面留 2 个空格）

1. 有序项
2. 有序项
```

### 行内代码

```markdown
用 `SELECT * FROM t` 查询。
```

---

## 三、常见问题

### Q：本地没有 Ruby，怎么预览？

**没有预览，直接 push 看线上。** 这是当前配置的取舍——Actions 构建约 1-2 分钟。

如果想本地预览，需要装 Ruby 3.3+：

```bash
# 下载 RubyInstaller（带 DevKit）
# https://rubyinstaller.org/downloads/
bundle install
bundle exec jekyll serve
# 打开 http://127.0.0.1:4000
```

### Q：文章提交后线上没变化？

按顺序排查：

1. 打开 https://github.com/yuzhupeng/fishyue.github.io/actions 看最近一次构建是否变红
2. 红色则点进去看报错，常见原因：front matter YAML 格式错（冒号后要空格、字符串含冒号要加引号）
3. 绿色但没变化：清浏览器缓存，或等 2 分钟 CDN 刷新

### Q：YAML 里写了中文就会报错吗？

不会。但如果 `title` 或 `summary` 里包含 `:` `#` 或开头是 `-`，要用引号包起来：

```yaml
title: "Docker: 从入门到部署"
summary: "注意：冒号后面要加空格"
```

### Q：怎么把文章设为草稿？

在 front matter 加：

```yaml
hidden: true
```

它不会出现在首页和列表，但仍可通过完整 URL 访问，适合写完还没准备好发布的情况。

### Q：怎么删除一篇文章？

直接删掉 `_posts/` 下对应的 `.md` 文件，commit + push。它对应的 `images/posts/<slug>/` 也可以一起删。

### Q：短记（Notes）怎么写？

短记不是 `.md` 文件，而是 `_data/notes.json` 里的一个 JSON 数组。目前是空数组：

```json
[]
```

要加一条短记，往数组里加对象：

```json
[
  {
    "id": "唯一标识",
    "url": "来源链接（可空）",
    "date": "2026-11-16T10:00:00Z",
    "kind": "post",
    "lang": "zh",
    "category": "life",
    "text": "正文内容",
    "media": [],
    "metrics": {"like": 0, "reply": 0, "repost": 0, "quote": 0, "bookmark": 0, "view": 0},
    "long": false,
    "thin": false
  }
]
```

> 注意：这套结构原本服务于 Tw93 从 X（Twitter）同步推文的脚本（`scripts/notes/`）。
> 如果你不需要短记，也可以把菜单里的「短记」入口去掉（`_config.yml` 的 `menu` 段）。

### Q：分类可以自己加吗？

可以，但需要改两处：

1. `_config.yml` 不需要改
2. `posts/index.html` 第 8 行的 `categories` 变量，格式是 `"Key:显示名,Key:显示名"`

```liquid
{% assign categories = "Database:数据库,Architecture:架构,Backend:后端,Frontend:前端,AI:AI,Note:随笔" | split: "," %}
```

文章里的 `categories: Key` 必须与这里的 Key 对上，否则不会出现在对应分组里。

---

## 四、发布前自查清单

- [ ] 文件名是 `YYYY-MM-DD-slug.md`，slug 纯英文
- [ ] front matter 三横线闭合，`title`/`date`/`layout` 都有
- [ ] `categories` 用的是 6 个合法值之一
- [ ] 代码块标了语言
- [ ] 本地图片路径以 `/images/posts/<slug>/` 开头，且文件确实存在
- [ ] `git push` 后 Actions 变绿
- [ ] 线上打开文章，代码块高亮正常、图片能显示

---

## 相关文档

- [README](../README.md)
- [改造记录](migration.md)
