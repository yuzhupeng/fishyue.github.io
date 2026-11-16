# 改造记录：从 Gridea 到 Jekyll（Tw93 主题）

记录 2026-11-16 这次改造做了什么、为什么这么做。

## 起点

- **旧站**：`https://yuzhupeng.top/myblogs/`，Gridea 生成的纯静态 HTML 产物（35 篇文章）。
- **问题**：仓库里只有渲染后的 HTML，没有任何 Markdown 源文，本机也没装 Gridea 客户端。
  写新文章必须回到装有 Gridea 的机器，且外观无法改造。
- **目标**：换成 Tw93 的 Jekyll 主题，能直接写 `.md` 发布。

## 关键决策

| 决策点 | 结论 | 理由 |
|---|---|---|
| 迁移方式 | fork Tw93 仓库，删内容留模板 | 主题是 7 layout + 14 include + 7 Ruby 插件的组合体，重写不划算 |
| 承载仓库 | `yuzhupeng/fishyue.github.io` | 已存在的 fork，直接改 |
| 域名 | `blog.yuzhupeng.top`（子域名） | 根路径 `yuzhupeng.top` 被一个 Vue SPA 占据；`/myblogs` 由旧仓库提供，路径无法迁移 |
| 部署 | GitHub Actions | 仓库只存源文，push 后自动构建 |
| 本地构建 | 不装 Ruby | 本机无 Ruby/winget/choco，先靠 Actions |

## 已做的改动

### 1. 清理 Tw93 内容

删除：`_posts/`（101 篇）、`_posts_en/`（98 篇）、`en/`、`projects/`、`files/`（180MB）、
`images/`（200MB）、`api/`、`llms*.txt`、`openapi.json`、`vercel.json`、`github.html`、
`pricing.md`、`privacy.md`、IndexNow 密钥文件。

仓库从 **737MB 降到约 30MB**（.git 350MB 是历史包袱，未清理）。

### 2. 替换站点标识

- `_config.yml`：title/description/url/author/menu/analytics 全部换成 fishyue
- `_includes/head.html`：SEO 标题、JSON-LD、logo/og 图、清掉 Tw93 的 YouTube/知乎/V2EX 外链
- `_includes/footer.html`：ASCII art、自我介绍、作品链接（Mole/Yado/Pake/MiaoYan/Kaku）全部替换
- `_includes/giscus.html`：评论默认关闭（`page.comments == true` 才加载），避免加载不存在的仓库
- `package.json` / `package-lock.json` / `robots.txt` / `_plugins/*.rb` 里的 `tw93` 硬编码

### 3. 修构建链

- `.github/workflows/jekyll.yml:12`：`branches: ["master"]` → `["main"]`
  （否则默认分支是 main，push 永不触发构建）
- `.github/workflows/jekyll.yml:39`：Ruby `3.1` → `3.3`（与 `.ruby-version` 对齐）
- 删除 tw93 专属的 `indexnow` job（向 `api.indexnow.org` 提交 tw93.fun 的 URL）
- 新增 `python3 scripts/image_sizes.py` 步骤（否则图片无 width/height，构建打 warn）

### 4. URL 规则

`_config.yml` 两处 permalink 从 `/:year-:month-:day/:title.html` 改为 `/post/:title/`。

最终网址：`https://blog.yuzhupeng.top/post/<slug>/`

### 5. 文章迁移

用 `scripts/html2md.py` 把 35 篇旧 HTML 反解成 Markdown：

- 定位 `<div class="post-content" v-pre>` 区段取正文
- 42 张 base64 内嵌图抽成实体文件（`images/posts/git-ji-chu-shi-yong/`）
- 剥离 hljs 高亮 span，还原 `<pre><code>`，补回 `language-xxx` 围栏标识
- 剥掉 Gridea 把 Hugo YAML 头误渲染成的 `<h2>` 脏数据
- 清理浏览器抓图产生的垃圾 alt 文本
- 按关键词自动分到 6 个分类，再人工修正 7 篇误判

结果：`post/git-ji-chu-shi-yong/index.html` 从 **7.2MB 缩到 14KB** 的 Markdown。

## 已知未完成事项

| 项 | 状态 | 说明 |
|---|---|---|
| DNS 配置 | **待你操作** | Cloudflare 加 CNAME `blog` → `yuzhupeng.github.io` |
| GitHub Pages 启用 | 待在仓库 Settings → Pages 选 "GitHub Actions" |
| 评论（giscus） | 已写好但关闭 | 需在 giscus.app 用本仓库配置后，替换 `_includes/giscus.html` 里的 `REPLACE_ME_*` |
| 短记（Notes） | 数据为空 | `_data/notes.json` 是 `[]`，菜单入口保留 |
| `.git` 历史 | 350MB | 含 Tw93 全部历史，如需瘦身要 `git filter-repo`（有破坏性，未做） |
| 旧站下线 | 未做 | `myblogs` 仓库仍在提供 `/myblogs` 服务 |
| 外链图片 | 159 张仍是外链 | 旧文章里的 cnblogs/zhimg 图片未转存，对方删图会裂 |

## 回滚方式

```bash
# 查看原始状态
git show tw93-original-20261116:_config.yml

# 整体回滚（会丢弃当前所有改动）
git checkout tw93-original-20261116
```

## 相关文档

- [写作手册](writing.md)
- [README](../README.md)
