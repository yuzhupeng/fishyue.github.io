# fishyue 博客（blog.yuzhupeng.top）

基于 [Tw93](https://tw93.fun) 的 Jekyll 主题（MIT 协议）改造的个人技术博客。
原主题完整备份在 git tag `tw93-original-20261116`。

- 线上地址：https://blog.yuzhupeng.top
- 文章源文：`_posts/*.md`
- 构建：GitHub Actions（`.github/workflows/jekyll.yml`）

## 快速开始

```bash
# 本机没有 Ruby 时，只能靠 push 触发 Actions 构建
git add -A && git commit -m "更新文章" && git push

# 若已装 Ruby 3.3+
bundle install
bundle exec jekyll serve      # 本地预览 http://127.0.0.1:4000
```

## 目录速查

| 路径 | 作用 |
|---|---|
| `_posts/` | 文章源文，`YYYY-MM-DD-slug.md` |
| `_layouts/` | 页面骨架：post 文章页、page 独立页、home 首页、notes 短记 |
| `_includes/` | 头尾、搜索、评论、分页等片段 |
| `_sass/` + `css/` | 样式，SCSS 编译后内联进 head |
| `_plugins/` | 7 个 Ruby 插件（内联 CSS、图片尺寸、notes 生成等） |
| `images/posts/` | 文章配图，从旧博客抽出的 42 张 |
| `scripts/html2md.py` | 旧博客 HTML 转 Markdown 的脚本 |

## 写一篇新文章

1. 在 `_posts/` 新建 `YYYY-MM-DD-英文slug.md`
2. 写 front matter（见 docs/writing.md）
3. 正文用 Markdown
4. 图片放 `images/posts/<slug>/`，正文用 `/images/posts/<slug>/xxx.png` 引用
5. commit + push，等 Actions 约 1-2 分钟

## 相关文档

- 写作手册：docs/writing.md
- 改造记录：docs/migration.md
