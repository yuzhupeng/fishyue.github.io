---
layout: post
title: 使用 source-map-explorer 分析前端打包结果进行包体积优化
date: 2025-06-03 09:00:00
summary: 对于前端打包构建生产环境的产出内容，特别是在采用了 Vue.js、React 或 Angular 等主流框架的时候，其体积达数 M 是很常见的现象。
categories: Note
---

# 使用 source-map-explorer 分析前端打包结果进行包体积优化

目录

[[隐藏](javascript:content_index_toggleToc())]

- [1 使用 source-map-explorer](https://lzw.me/a/source-map-explorer.html#1%20%E4%BD%BF%E7%94%A8%20source-map-explorer "1 使用 source-map-explorer")

  - [1.1 构建输出项目](https://lzw.me/a/source-map-explorer.html#1.1%20%E6%9E%84%E5%BB%BA%E8%BE%93%E5%87%BA%E9%A1%B9%E7%9B%AE "1.1 构建输出项目")
  - [1.2 使用 source-map-explorer 分析示例](https://lzw.me/a/source-map-explorer.html#1.2%20%E4%BD%BF%E7%94%A8%20source-map-explorer%20%E5%88%86%E6%9E%90%E7%A4%BA%E4%BE%8B "1.2 使用 source-map-explorer 分析示例")
- [2 source-map-explorer 功能参数](https://lzw.me/a/source-map-explorer.html#2%20source-map-explorer%20%E5%8A%9F%E8%83%BD%E5%8F%82%E6%95%B0 "2 source-map-explorer 功能参数")
- [3 更多参考](https://lzw.me/a/source-map-explorer.html#3%20%E6%9B%B4%E5%A4%9A%E5%8F%82%E8%80%83 "3 更多参考")

对于前端打包构建生产环境的产出内容，特别是在采用了 Vue.js、React 或 Angular 等主流框架的时候，其体积达数 M 是很常见的现象。

当希望对包体积进行优化分析时，或许你知道可以选择使用 `webpack-bundle-analyzer`， 其实 `source-map-explorer` 也是个不错的选择。当打包输出结果生成了 sourceMap，`source-map-explorer` 就可以据此分析出每个模块所占用的体积。而且它不仅限于 JavaScript，对于 Css 预处理器 LESS 和 Sass 来说同样适用。

## 1 使用 `source-map-explorer`

### 1.1 构建输出项目

首先对前端项目构建输出用于生产环境的内容，注意开启 sourceMap 的输出。

### 1.2 使用 `source-map-explorer` 分析示例

`source-map-explorer` 的用法相当简单。首先全局安装 `source-map-explorer`：

|  |  |
| --- | --- |
| 1 | ``` npm i -g ``source``-map-explorer ``` |

然后进入打包输出内容目录，执行如下命令（示例中的 为具体产出结果的 hash 值占位符）：

|  |  |
| --- | --- |
| 1 | ``` source``-map-explorer main.<``hash``>.js main.<``hash``>.js.map ``` |

你也可以不全局安装它，直接使用 npx 执行：

|  |  |
| --- | --- |
| 1 | ``` npx ``source``-map-explorer main.<``hash``>.js main.<``hash``>.js.map ``` |

如一切正常，该命令会在临时目录生成 html 文件分析结果，并自动打开浏览器进行显示。示例：

[![](https://lzw.me/wp-content/uploads/2020/04/source-map-explorer.png)](https://lzw.me/wp-content/uploads/2020/04/source-map-explorer.png)

以上为单文件分析的简单示例。也可以使用通配符方式，如：

|  |  |
| --- | --- |
| 1 | ``` npx ``source``-map-explorer dist``/prod/``*.js ``` |

我们可以将该命令配置到 `package.json` 的 `scripts` 脚本中：

|  |  |
| --- | --- |
| 12345 | ``` {``  ``"scripts"``: {``     ``"analyze"``: ``"npx source-map-explorer dist/prod/*.js"``,``  ``}``} ``` |

在完打包完成之后，执行 `npm run analyze` 即可得到分析结果。

## 2 `source-map-explorer` 功能参数

|  |  |
| --- | --- |
| 123456789101112131415161718192021222324252627282930 | ``` Analyze and debug space usage through ``source ``` ``` maps.``Usage:``source``-map-explorer script.js [script.js.map] [--json [result.json] | --html [result.html] | --tsv [result.csv]] [-m | --only-mapped] [--exclude-``source``-map] [--no-bor                                                                                                         der-checks] [--``gzip``] [--``sort``] [--replace=BEFORE_1 BEFORE_2 --with=AFTER_1 AFTER_2] [--no-root] [--coverage coverage.json] [--version] [--help | -h] ``` ``` Output:``  ``--json  If filename specified save output as JSON to specified ``file ``` ``` otherwise output to stdout.  [string]``  ``--tsv   If filename specified save output as TSV to specified ``file ``` ``` otherwise output to stdout.  [string]``  ``--html  If filename specified save output as HTML to specified ``file ``` `otherwise output to stdout rather than opening a browser.  [string]` ``` Replace:``  ``--replace  Apply a simple ``find``/replace ``` ``` on ``source ``` `file` ``` names. This can be used to fix some oddities with paths that appear ``in ``` ``` the ``source ``` ``` map generation process. Acce                                                                                                         pts regular expressions.  [array]``  ``--with     See --replace.  [array] ``` ``` Options:``  ``--version             Show version number  [boolean]``  ``--only-mapped, -m     Exclude ``"unmapped" ``` ``` bytes from the output. This will result ``in ``` ``` total counts ``less ``` ``` than the ``file ``` ``` size  [boolean]``  ``--exclude-``source``-map  Exclude ``source ``` ``` map comment size from output  [boolean]``  ``--no-root             To simplify the visualization, ``source``-map-explorer will remove any prefix shared by all sources. If you wish to disable this behavior, ``set ``` ``` --n                                                                                                         o-root.  [boolean]``  ``--no-border-checks    Disable invalid mapping column``/line ``` ``` checks.  [boolean]``  ``--coverage            If the path to a valid a chrome code coverage JSON ``export ``` ``` is supplied, the tree map will be colorized according to ``which ``` ``` percentage of the mod                                                                                                         ules code was executed  [string]``  ``--``gzip ```                ``` Calculate ``gzip ``` ``` size. It also sets onlyMapped flag  [boolean]``  ``--``sort ```                ``` Sort filenames  [boolean]``  ``-h, --help            Show help  [boolean] ``` ``` Examples:``  ``source``-map-explorer script.js script.js.map       Explore bundle``  ``source``-map-explorer script.js                     Explore bundle with inline ``source ``` ``` map``  ``source``-map-explorer dist``/js/``*.*                   Explore all bundles inside dist``/js ``` ``` folder``  ``source``-map-explorer script.js --tsv               Explore and output result as TSV to stdout``  ``source``-map-explorer script.js --json result.json  Explore and save result as JSON to the ``file ``` |

## 3 更多参考

- https://www.npmjs.com/package/source-map-explorer
- https://www.npmjs.com/package/webpack-bundle-analyzer

###
