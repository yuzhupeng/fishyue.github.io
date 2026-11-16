# fishyue.github.io Agent Guide

## Project

本仓库是 https://blog.yuzhupeng.top 的源码，基于 Tw93 的 Jekyll 主题（MIT）改造。
原主题完整备份在 git tag `tw93-original-20261116`。

构建与部署：**GitHub Actions**。push 到 `main` 后由 `.github/workflows/jekyll.yml`
构建并发布到 GitHub Pages。没有 Vercel，没有本地构建依赖。

## 仓库地图

- `_posts/` - 中文文章，`YYYY-MM-DD-slug.md`
- `_layouts/` - 7 个页面骨架（post / page / home / notes / note / ppt / base）
- `_includes/` - 14 个片段（head / footer / giscus / search / pagination 等）
- `_sass/` + `css/` - SCSS 样式，经 `_plugins/inline_css.rb` 编译后内联进 head
- `_plugins/` - 7 个 Ruby 插件，改动需同步移除对应 Liquid 调用
- `images/posts/` - 文章配图
- `scripts/html2md.py` - 旧博客 HTML 到 Markdown 的转换脚本
- `docs/` - writing.md（写作手册）、migration.md（改造记录）

## 硬约束

1. **改 `_plugins/` 必须同步改模板**：删 `inline_css.rb` 要同时删 head.html 的
   `{% inline_css %}`；删 `cdn_image_filter.rb` 要同时删 post.html/page.html 的
   `| cdn_image_filter`，否则构建直接失败。
2. **front matter 值含冒号、井号、方括号时必须用双引号包起来**，否则 YAML 解析失败、
   整站构建失败。
3. **图片不要内嵌 base64**，放 `images/posts/<slug>/` 并用绝对路径引用。
4. **permalink 是 `/post/:title/`**，slug 必须是英文；改它会让所有旧链接失效。
5. **workflow 监听 `main` 分支**，不要改回 `master`。

## 已验证

- 35 篇文章的 front matter 全部通过 YAML 解析
- 所有 `/images/posts/` 引用都有对应文件
- Liquid `for`/`if` 标签在全部模板中平衡

## 未验证

本地无 Ruby 环境，Jekyll 构建本身未在本地跑过，首次 push 后需检查 Actions 结果。
