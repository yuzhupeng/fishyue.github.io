---
layout: post
title: 前端项目框架 目录
date: 2025-07-28 09:00:00
summary: 前端项目框架包含了路由：svelte-spa-router 样式：less tailwind 国际化：svelte-i18n 接口请求：axios 环境变量配置:.env 组件库：melt-ui 图标
categories: Note
---

前端项目框架包含了路由：svelte-spa-router 样式：less tailwind 国际化：svelte-i18n 接口请求：axios 环境变量配置:.env 组件库：melt-ui 图标库：iconfont 轮播图：swiper node:20.18.1 npm 10.8.2

> **框架太“重”了**：通常一个小型项目只由少数几个简单页面构成，如果使用 Vue 或者 React 这些框架来研发的话，有点“大材小用”了。构建的产物中包含了不少框架运行时代码(虚拟 DOM、响应式、状态管理等)，这些代码对于小型项目而言是冗余的，它们影响了包体大小，进而影响页面的启动速度和执行性能。  
> **打包太慢了**：以 Vue CLI 为例，它的底层基于 Webpack，虽然 Webpack 具备更强大的功能和灵活性，但相比于 Vite、Esbuild 这些以速度为标杆的构建工具来说，它的速度确实慢了一些，影响了研发效率。

@

目录

- [一、 创建基本项目](#%E4%B8%80-%E5%88%9B%E5%BB%BA%E5%9F%BA%E6%9C%AC%E9%A1%B9%E7%9B%AE)

  - [1.1 全局安装 Vite](#11-%E5%85%A8%E5%B1%80%E5%AE%89%E8%A3%85-vite)
  - [1.2 创建 Svelte 项目](#12-%E5%88%9B%E5%BB%BA-svelte-%E9%A1%B9%E7%9B%AE)
- [二、目录结构](#%E4%BA%8C%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)
- [三、svelte路由配置](#%E4%B8%89svelte%E8%B7%AF%E7%94%B1%E9%85%8D%E7%BD%AE)

  - [3.1 npm安装](#31-npm%E5%AE%89%E8%A3%85)
  - [3.2 定义router](#32-%E5%AE%9A%E4%B9%89router)

    - [3.2.1 动态导入组件](#321-%E5%8A%A8%E6%80%81%E5%AF%BC%E5%85%A5%E7%BB%84%E4%BB%B6)
    - [3.2.2 在页面之间导航](#322-%E5%9C%A8%E9%A1%B5%E9%9D%A2%E4%B9%8B%E9%97%B4%E5%AF%BC%E8%88%AA)
  - [3.3 使用路由](#33-%E4%BD%BF%E7%94%A8%E8%B7%AF%E7%94%B1)
- [四、svelte CSS预处理器](#%E5%9B%9Bsvelte-css%E9%A2%84%E5%A4%84%E7%90%86%E5%99%A8)

  - [4.1 less的使用](#41-less%E7%9A%84%E4%BD%BF%E7%94%A8)
    - [4.1.1 npm安装](#411-npm%E5%AE%89%E8%A3%85)
  - [4.2 Tailwind CSS的使用](#42-tailwind-css%E7%9A%84%E4%BD%BF%E7%94%A8)
- [五、svelte环境变量配置](#%E4%BA%94svelte%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE)

  - [5.1 环境变量命名规则](#51-%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E5%91%BD%E5%90%8D%E8%A7%84%E5%88%99)
  - [5.2 .env文件的使用](#52-env%E6%96%87%E4%BB%B6%E7%9A%84%E4%BD%BF%E7%94%A8)
  - [5.3 在代码中使用环境变量](#53-%E5%9C%A8%E4%BB%A3%E7%A0%81%E4%B8%AD%E4%BD%BF%E7%94%A8%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
  - [5.4 配置运行与打包环境](#54-%E9%85%8D%E7%BD%AE%E8%BF%90%E8%A1%8C%E4%B8%8E%E6%89%93%E5%8C%85%E7%8E%AF%E5%A2%83)
- [六、svelte国际化](#%E5%85%ADsvelte%E5%9B%BD%E9%99%85%E5%8C%96)

  - [6.1 安装 `svelte-i18n`](#61-%E5%AE%89%E8%A3%85-svelte-i18n)
  - [6.2 初始化 `svelte-i18n`](#62-%E5%88%9D%E5%A7%8B%E5%8C%96-svelte-i18n)
  - [6.3 创建语言文件](#63-%E5%88%9B%E5%BB%BA%E8%AF%AD%E8%A8%80%E6%96%87%E4%BB%B6)
  - [6.4 在 Svelte 组件中使用 `svelte-i18n`](#64-%E5%9C%A8-svelte-%E7%BB%84%E4%BB%B6%E4%B8%AD%E4%BD%BF%E7%94%A8-svelte-i18n)
  - [6.5 切换语言](#65-%E5%88%87%E6%8D%A2%E8%AF%AD%E8%A8%80)
  - [6.6 在 `App.svelte` 中引入 `i18n.js`](#66-%E5%9C%A8-appsvelte-%E4%B8%AD%E5%BC%95%E5%85%A5-i18njs)
  - [6.7 运行项目](#67-%E8%BF%90%E8%A1%8C%E9%A1%B9%E7%9B%AE)
  - [6.8 构建项目](#68-%E6%9E%84%E5%BB%BA%E9%A1%B9%E7%9B%AE)
  - [6.9 预览项目](#69-%E9%A2%84%E8%A7%88%E9%A1%B9%E7%9B%AE)
  - [6.10 检查项目](#610-%E6%A3%80%E6%9F%A5%E9%A1%B9%E7%9B%AE)
- [七、svelte接口请求](#%E4%B8%83svelte%E6%8E%A5%E5%8F%A3%E8%AF%B7%E6%B1%82)

  - [7.1 安装 `axios`](#71-%E5%AE%89%E8%A3%85-axios)
  - [7.2 创建 `axios` 实例](#72-%E5%88%9B%E5%BB%BA-axios-%E5%AE%9E%E4%BE%8B)
  - [7.3 在 Svelte 组件中使用 `axios`](#73-%E5%9C%A8-svelte-%E7%BB%84%E4%BB%B6%E4%B8%AD%E4%BD%BF%E7%94%A8-axios)
  - [7.4 处理请求和响应拦截器](#74-%E5%A4%84%E7%90%86%E8%AF%B7%E6%B1%82%E5%92%8C%E5%93%8D%E5%BA%94%E6%8B%A6%E6%88%AA%E5%99%A8)
  - [7.5 在 `App.svelte` 中使用 `axios`](#75-%E5%9C%A8-appsvelte-%E4%B8%AD%E4%BD%BF%E7%94%A8-axios)
  - [7.6 处理错误](#76-%E5%A4%84%E7%90%86%E9%94%99%E8%AF%AF)
- [八、svelte组件库](#%E5%85%ABsvelte%E7%BB%84%E4%BB%B6%E5%BA%93)
- [九、svelte阿里图标库](#%E4%B9%9Dsvelte%E9%98%BF%E9%87%8C%E5%9B%BE%E6%A0%87%E5%BA%93)

  - [9.1 获取阿里图标](#91-%E8%8E%B7%E5%8F%96%E9%98%BF%E9%87%8C%E5%9B%BE%E6%A0%87)
  - [9.2 将图标文件放入项目](#92-%E5%B0%86%E5%9B%BE%E6%A0%87%E6%96%87%E4%BB%B6%E6%94%BE%E5%85%A5%E9%A1%B9%E7%9B%AE)
  - [9.3 引入图标文件](#93-%E5%BC%95%E5%85%A5%E5%9B%BE%E6%A0%87%E6%96%87%E4%BB%B6)
  - [9.4 使用图标](#94-%E4%BD%BF%E7%94%A8%E5%9B%BE%E6%A0%87)
  - [9.5 动态切换图标](#95-%E5%8A%A8%E6%80%81%E5%88%87%E6%8D%A2%E5%9B%BE%E6%A0%87)
  - [9.6 使用 Symbol 方式（可选）](#96-%E4%BD%BF%E7%94%A8-symbol-%E6%96%B9%E5%BC%8F%E5%8F%AF%E9%80%89)
  - [9.7 样式调整（可选）](#97-%E6%A0%B7%E5%BC%8F%E8%B0%83%E6%95%B4%E5%8F%AF%E9%80%89)
  - [9.8 示例代码](#98-%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81)
- [十、svelte轮播图](#%E5%8D%81svelte%E8%BD%AE%E6%92%AD%E5%9B%BE)
- [十一、store数据共享](#%E5%8D%81%E4%B8%80store%E6%95%B0%E6%8D%AE%E5%85%B1%E4%BA%AB)

  - [1. 创建 `store` 模块](#1-%E5%88%9B%E5%BB%BA-store-%E6%A8%A1%E5%9D%97)
  - [2. 创建全局 `store`](#2-%E5%88%9B%E5%BB%BA%E5%85%A8%E5%B1%80-store)
  - [3. 在组件中使用 `store`](#3-%E5%9C%A8%E7%BB%84%E4%BB%B6%E4%B8%AD%E4%BD%BF%E7%94%A8-store)
  - [4. 封装 `store` 的优势](#4-%E5%B0%81%E8%A3%85-store-%E7%9A%84%E4%BC%98%E5%8A%BF)
  - [5. 示例：`about.svelte` 中使用 `store`](#5-%E7%A4%BA%E4%BE%8Baboutsvelte-%E4%B8%AD%E4%BD%BF%E7%94%A8-store)
- [十二、扩展内容](#%E5%8D%81%E4%BA%8C%E6%89%A9%E5%B1%95%E5%86%85%E5%AE%B9)
- [十三、框架git地址](#%E5%8D%81%E4%B8%89%E6%A1%86%E6%9E%B6git%E5%9C%B0%E5%9D%80)

## 一、 创建基本项目

### 1.1 全局安装 Vite

通过 npm 全局安装 Vite

```mipsasm
npm install vite
```

### 1.2 创建 Svelte 项目

Vite 原生支持直接通过脚手架创建 Svelte 项目，执行以下命令

```sql
npm create vite@latest
```

输入命令后选择如下

```vhdl
✔ Project name: vite-svelte

? Select a framework: › - Use arrow-keys. Return to submit.
    Vanilla
    Vue
    React
    Preact
    Lit
❯   Svelte
    Solid
    Qwik
    Others

? Select a variant: › - Use arrow-keys. Return to submit.
    TypeScript
❯   JavaScript
    SvelteKit
```

**基本项目创建完成**

## 二、目录结构

根据上一步创建项目，项目的基本结构栓是完成了，但这样还是不够的，接下来介绍一下完整的项目目录  
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/faa1d82a4f50487caa9e5c9baa137743.png)

## 三、svelte路由配置

### 3.1 npm安装

项目中安装svelte-spa-router

```mipsasm
npm install svelte-spa-router
```

### 3.2 定义router

- 每条路由都是一个普通的Svelte组件，包含标记、脚本、绑定等。任何Svelte组件都可以是路由。
- 路由定义只是一个JavaScript字典（对象），其中键是一个带有路径（包括参数等）的字符串，值是路由对象。

```javascript
import Home from './routes/Home.svelte'
import Author from './routes/Author.svelte'
import Book from './routes/Book.svelte'
import NotFound from './routes/NotFound.svelte'

const routes = {
    // Exact path
    '/': Home,

    // Using named parameters, with last being optional
    '/author/:first/:last?': Author,

    // Wildcard parameter
    '/book/*': Book,

    // Catch-all
    // This is optional, but if present it must be the last
    '*': NotFound,
}
```

#### 3.2.1 动态导入组件

使用动态导入的优点是，如果您的打包器支持，您可以启用代码拆分并减小发送给用户的捆绑包的大小。这已经用包括Rollup和Webpack在内的捆绑器进行了测试

1. 要使用动态导入的组件，您需要利用包装方法（根据路线包装文档，该方法可用于各种操作）。首先，导入wrap方法：

```javascript
import {wrap} from 'svelte-spa-router/wrap'
```

2. 然后，在路由定义中，使用wrap方法包装路由，将一个函数传递给asyncComponent属性，该函数将动态导入的组件返回给asyncComponent：

```haskell
wrap({
    asyncComponent: () => import('./Foo.svelte')
})
```

案例：

```javascript
// Import the wrap method
import {wrap} from 'svelte-spa-router/wrap'

// Note that Author and Book are not imported here anymore, so they can be imported at runtime
import Home from './routes/Home.svelte'
import NotFound from './routes/NotFound.svelte'

const routes = {
    '/': Home,

    // Wrapping the Author component
    '/author/:first/:last?': wrap({
        asyncComponent: () => import('./routes/Author.svelte')
    }),

    // Wrapping the Book component
    '/book/*': wrap({
        asyncComponent: () => import('./routes/Book.svelte')
    }),

    // Catch-all route last
    '*': NotFound,
}
```

#### 3.2.2 在页面之间导航

1. 锚点导航

```xml
<a href="#/book/123">Thus Spoke Zarathustra</a>
```

2. use:link导航（可以使用use：link操作，而不必在每个链接前键入#）

```xml
<script>
import {link} from 'svelte-spa-router'
</script>
<a href="/book/321" use:link>The Little Prince</a>
```

### 3.3 使用路由

在app.svelte中全局调用

```javascript
import Router from 'svelte-spa-router'
```

然后，通过将组件放置在标记中，将路由器显示在您想要的任何位置

```xml
<body>
    <Router {routes}/>
</body>
```

## 四、svelte CSS预处理器

### 4.1 less的使用

#### 4.1.1 npm安装

安装less与svelte-preprocess-less依赖

```cmake
npm install --save-dev svelte-preprocess-less less
```

在vite.config.js进行配置

```javascript
import { less } from 'svelte-preprocess-less'
export default defineConfig({
    plugins: [svelte({
        preprocess: {
          style: less(),
        },
      })],
})
```

### 4.2 Tailwind CSS的使用

通过npx安装直接配置完 tailwindcss

```csharp
npx sv add tailwindcss
```

## 五、svelte环境变量配置

‌Vite中使用环境变量主要通过.env文件来配置，这些文件根据不同的环境（开发、测试、生产等）有不同的命名规则和使用方式。

### 5.1 环境变量命名规则

所有环境变量必须以VITE_为前缀

```ini
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My Vite App
```

### 5.2 .env文件的使用

1‌. **通用环境变量‌**：在项目的根目录下创建.env文件，用于定义所有环境通用的变量。  
2‌. **特定环境变量‌**：根据不同的环境需求，可以创建以下类型的.env文件：  
.env.devt：仅在开发环境中使用。  
.env.pro：仅在生产环境中使用。  
.env.local：通用的本地配置文件，通常不提交到版本控制系统中。  
.env.development.local：开发环境的本地配置文件。  
.env.production.local：生产环境的本地配置文件‌

### 5.3 在代码中使用环境变量

```cpp
console.log(import.meta.env.VITE_API_URL);
```

### 5.4 配置运行与打包环境

```json
  "scripts": {
    "dev": "vite --mode dev",//运行dev环境
    "dev-pro": "vite --mode pro",//运行pro环境
    "build": "vite build",
    "preview": "vite preview",
    "check": "svelte-check --tsconfig ./tsconfig.app.json && tsc -p tsconfig.node.json"
  },
```

## 六、svelte国际化

`svelte-i18n` 是一个用于 Svelte 应用的国际化（i18n）库，它可以帮助你轻松地管理和切换应用中的多语言内容。以下是如何在 Svelte 项目中使用 `svelte-i18n` 的基本步骤：

### 6.1 安装 `svelte-i18n`

首先，确保你已经安装了 `svelte-i18n`。根据你的 `package.json` 文件，它已经存在于 `dependencies` 中。

```bash
npm install svelte-i18n
```

### 6.2 初始化 `svelte-i18n`

在你的 Svelte 项目中，通常会在 `src` 目录下创建一个 `i18n.js` 或 `i18n.ts` 文件来初始化 `svelte-i18n`。

```javascript
// src/i18n.js
import { init, register, locale } from 'svelte-i18n';

// 注册默认语言
register('en', () => import('./locales/en.json'));
register('zh', () => import('./locales/zh.json'));

// 初始化并设置默认语言
init({
  fallbackLocale: 'en',
  initialLocale: 'en',
});
```

### 6.3 创建语言文件

在 `src/locales` 目录下创建语言文件，例如 `en.json` 和 `zh.json`。

```json
// src/locales/en.json
{
  "welcome": "Welcome to Svelte App",
  "greeting": "Hello, {name}!"
}
```

```json
// src/locales/zh.json
{
  "welcome": "欢迎使用 Svelte 应用",
  "greeting": "你好, {name}!"
}
```

### 6.4 在 Svelte 组件中使用 `svelte-i18n`

你可以在 Svelte 组件中使用 `$t` 函数来获取翻译内容。

```svelte
<script>
  import { t } from 'svelte-i18n';
</script>

<h1>{$t('welcome')}</h1>
<p>{$t('greeting', { name: 'John' })}</p>
```

### 6.5 切换语言

你可以通过 `locale.set` 方法来动态切换语言。

```svelte
<script>
  import { locale } from 'svelte-i18n';
</script>

<button on:click={() => locale.set('en')}>English</button>
<button on:click={() => locale.set('zh')}>中文</button>
```

### 6.6 在 `App.svelte` 中引入 `i18n.js`

1. 确保在 `App.svelte` 或你的主入口文件中引入 `i18n.js`。

```svelte
<script>
  import './i18n.js';
</script>
```

2. 确保加载完i18n后在加载页面

```App
<script>
  import { locale } from "svelte-i18n";
  import Router from "@/router/Router.svelte";
</script>
{#if $locale}
  <Layout>
    <Router />
  </Layout>
{/if}
```

### 6.7 运行项目

使用 `npm run dev` 运行你的项目，你应该能够看到国际化内容并根据按钮切换语言。

### 6.8 构建项目

当你准备好发布项目时，使用 `npm run build` 来构建项目。

```bash
npm run build
```

### 6.9 预览项目

使用 `npm run preview` 来预览构建后的项目。

```bash
npm run preview
```

### 6.10 检查项目

使用 `npm run check` 来检查 Svelte 和 TypeScript 的类型。

```bash
npm run check
```

通过以上步骤，你应该能够在 Svelte 项目中成功使用 `svelte-i18n` 来实现国际化功能。

## 七、svelte接口请求

在 Svelte 项目中使用 `axios` 进行 HTTP 请求是非常常见的操作。以下是如何在 Svelte 项目中集成和使用 `axios` 的步骤：

### 7.1 安装 `axios`

首先，确保你已经安装了 `axios`。根据你的 `package.json` 文件，它已经存在于 `dependencies` 中。

```bash
npm install axios
```

### 7.2 创建 `axios` 实例

为了更好的管理和配置 `axios`，通常会在 `src/utils` 目录下创建一个 `api.ts` 或 `api.js` 文件来创建 `axios` 实例。

```typescript
// src/utils/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com', // 你的 API 基础 URL
  timeout: 10000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
```

### 7.3 在 Svelte 组件中使用 `axios`

你可以在 Svelte 组件中导入并使用 `axios` 实例来发送 HTTP 请求。

```svelte
<script lang="ts">
  import api from '@/utils/api';
  import { onMount } from 'svelte';

  let data: any;

  onMount(async () => {
    try {
      const response = await api.get('/endpoint');
      data = response.data;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  });
</script>

{#if data}
  <div>
    <h1>{data.title}</h1>
    <p>{data.description}</p>
  </div>
{/if}
```

### 7.4 处理请求和响应拦截器

你可以在 `axios` 实例中添加请求和响应拦截器，以便在请求发送前或响应到达后进行一些处理。

```typescript
// src/utils/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 在请求发送之前做一些处理，例如添加 token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    // 对响应数据做一些处理
    return response;
  },
  (error) => {
    // 对响应错误做一些处理
    return Promise.reject(error);
  }
);

export default api;
```

### 7.5 在 `App.svelte` 中使用 `axios`

你可以在 `App.svelte` 中使用 `axios` 来获取数据或执行其他 HTTP 操作。

```svelte
<script lang="ts">
  import api from '@/utils/api';
  import { onMount } from 'svelte';

  let userData: any;

  onMount(async () => {
    try {
      const response = await api.get('/user');
      userData = response.data;
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  });
</script>

{#if userData}
  <div>
    <h1>Welcome, {userData.name}!</h1>
    <p>Email: {userData.email}</p>
  </div>
{/if}
```

### 7.6 处理错误

在使用 `axios` 时，确保你处理了可能的错误，例如网络错误或服务器错误。

```svelte
<script lang="ts">
  import api from '@/utils/api';
  import { onMount } from 'svelte';

  let userData: any;
  let errorMessage: string | null = null;

  onMount(async () => {
    try {
      const response = await api.get('/user');
      userData = response.data;
    } catch (error) {
      errorMessage = 'Failed to fetch user data. Please try again later.';
      console.error('Error fetching user data:', error);
    }
  });
</script>

{#if userData}
  <div>
    <h1>Welcome, {userData.name}!</h1>
    <p>Email: {userData.email}</p>
  </div>
{:else if errorMessage}
  <p style="color: red;">{errorMessage}</p>
{/if}
```

通过以上步骤，你应该能够在 Svelte 项目中成功使用 `axios` 来进行 HTTP 请求。

## 八、svelte组件库

这里用的是melt-ui，访问地址是：<https://www.melt-ui.com/docs/introduction>  
一键配置

```kotlin
npx @melt-ui/cli@latest init
```

## 九、svelte阿里图标库

在 Svelte 项目中使用阿里图标（如 [iconfont](https://www.iconfont.cn/)）可以通过以下步骤实现：

---

### 9.1 获取阿里图标

1. 访问 [iconfont](https://www.iconfont.cn/) 并登录。
2. 创建一个项目，将需要的图标添加到项目中。
3. 选择 `Font class` 或 `Symbol` 方式生成代码。
4. 点击 `下载至本地`，解压后得到图标文件。

---

### 9.2 将图标文件放入项目

将下载的图标文件（如 `iconfont.css` 和字体文件）放入项目的 `public` 或 `src/assets` 目录中。

例如：

```cpp
public/
  iconfont/
    iconfont.css
    iconfont.ttf
    iconfont.woff
    iconfont.woff2
```

---

### 9.3 引入图标文件

在 `App.svelte` 或 `main.ts` 中引入 `iconfont.css` 文件。

```svelte
<script lang="ts">
  import "./app.css";
  import Layout from "@/layout/Layout.svelte";
  import Router from "@/router/Router.svelte";
  import { locale } from "svelte-i18n";
  import Toast from "./components/Toast.svelte";
  import { toast } from "@/utils/toastService";

  // 引入阿里图标
  import '../public/iconfont/iconfont.css';
</script>
```

---

### 9.4 使用图标

在 Svelte 组件中使用阿里图标，直接通过 `class` 引用图标类名。

```svelte
<div>
  <i class="iconfont icon-home"></i> <!-- icon-home 是图标类名 -->
  <i class="iconfont icon-user"></i> <!-- icon-user 是图标类名 -->
</div>
```

---

### 9.5 动态切换图标

如果需要动态切换图标，可以将图标类名绑定到变量。

```svelte
<script lang="ts">
  let iconClass = 'icon-home';
</script>

<div>
  <i class={`iconfont ${iconClass}`}></i>
  <button on:click={() => iconClass = 'icon-user'}>切换图标</button>
</div>
```

---

### 9.6 使用 Symbol 方式（可选）

如果选择 `Symbol` 方式，需要引入 `iconfont.js` 文件，并使用 `<svg>` 标签。

```svelte
<script lang="ts">
  import '../public/iconfont/iconfont.js';
</script>

<svg class="icon" aria-hidden="true">
  <use xlink:href="#icon-home"></use> <!-- #icon-home 是图标 ID -->
</svg>
```

---

### 9.7 样式调整（可选）

如果需要调整图标大小或颜色，可以通过 CSS 设置。

```svelte
<style lang="less">
  .iconfont {
    font-size: 24px;
    color: #333;
  }
</style>
```

---

### 9.8 示例代码

以下是一个完整的示例：

```svelte
<script lang="ts">
  import "./app.css";
  import Layout from "@/layout/Layout.svelte";
  import Router from "@/router/Router.svelte";
  import { locale } from "svelte-i18n";
  import Toast from "./components/Toast.svelte";
  import { toast } from "@/utils/toastService";

  // 引入阿里图标
  import '../public/iconfont/iconfont.css';

  let iconClass = 'icon-home';
</script>

{#if $locale}
  <Layout>
    <Router />
  </Layout>
  {#if $toast.visible}
    <Toast message={$toast.message} />
  {/if}
{/if}

<div>
  <i class={`iconfont ${iconClass}`}></i>
  <button on:click={() => iconClass = 'icon-user'}>切换图标</button>
</div>

<style lang="less">
  .iconfont {
    font-size: 24px;
    color: #333;
  }
</style>
```

---

通过以上步骤，你可以在 Svelte 项目中成功使用阿里图标。如果需要更多定制化功能，可以参考 [iconfont 官方文档](https://www.iconfont.cn/help/detail?spm=a313x.7781069.1998910419.d8d11a391&helptype=code)。

## 十、svelte轮播图

这里用的是https://3.swiper.com.cn/  
下载引入相关css与js即可  
demo如下

```xml
<script>
    import { onMount } from 'svelte';
    import  '@/utils/swiper/swiper.min.js';
    import '@/utils/swiper/swiper.min.css';
    let swiperInstance;
    onMount(() => {
      // 初始化 Swiper
      swiperInstance = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        autoplay:2500,
        loop:true
      });
    });
  </script>
  
  <style>
   html, body {
        position: relative;
        height: 100%;
    }
    body {
        background: #eee;
        font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
        font-size: 14px;
        color:#000;
        margin: 0;
        padding: 0;
    }
    .swiper-container {
        width: 100%;
        height: 350px;
    }
    .swiper-slide {
        text-align: center;
        font-size: 18px;
        background: #fff;

        /* Center slide text vertically */
        display: -webkit-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        -webkit-justify-content: center;
        justify-content: center;
        -webkit-box-align: center;
        -ms-flex-align: center;
        -webkit-align-items: center;
        align-items: center;
    }
  </style>
  
 <!-- Swiper -->
 <div class="swiper-container">
  <div class="swiper-wrapper">
      <div class="swiper-slide">Slide 1</div>
      <div class="swiper-slide">Slide 2</div>
  </div>
  <!-- Add Pagination -->
  <div class="swiper-pagination"></div>
</div>
```

## 十一、store数据共享

在 Svelte 中，`store` 是一个核心概念，用于管理应用的状态。为了更好地组织代码，可以将 `store` 封装为模块，包括 `state`、`actions`、`getters` 和 `mutations`，类似于 Vuex 或 Redux 的设计模式。以下是如何封装 `store` 的示例：

---

### 1. 创建 `store` 模块

在 `src/store` 目录下创建一个模块，例如 `centerStore.ts`，用于管理特定模块的状态和逻辑。

```typescript
// src/store/centerStore.ts
import { writable, derived } from 'svelte/store';

// State
const state = writable({
  userData: null,
  loading: false,
  error: null,
});

// Actions
const actions = {
  async getUserData(params: { onlyMakeTheSame: boolean }) {
    try {
      state.update((s) => ({ ...s, loading: true, error: null }));
      // 模拟 API 调用
      const response = await fetch('/api/user', { method: 'GET' });
      const data = await response.json();
      state.update((s) => ({ ...s, userData: data, loading: false }));
    } catch (error) {
      state.update((s) => ({ ...s, error: error.message, loading: false }));
    }
  },
};

// Getters
const getters = {
  userData: derived(state, ($state) => $state.userData),
  isLoading: derived(state, ($state) => $state.loading),
  error: derived(state, ($state) => $state.error),
};

// Mutations (可选)
const mutations = {
  setUserData(userData: any) {
    state.update((s) => ({ ...s, userData }));
  },
};

// 导出模块
export const centerStore = {
  state,
  actions,
  getters,
  mutations,
};
```

---

### 2. 创建全局 `store`

在 `src/store/index.ts` 中整合所有模块，创建一个全局 `store`。

```typescript
// src/store/index.ts
import { centerStore } from './centerStore';

export const store = {
  center: centerStore,
};
```

---

### 3. 在组件中使用 `store`

在 Svelte 组件中导入并使用 `store`。

```svelte
<script lang="ts">
  import { store } from '@/store/index';
  import { onMount } from 'svelte';

  // 获取 state 和 getters
  const { state, getters } = store.center;

  // 调用 action
  function fetchData() {
    store.center.actions.getUserData({ onlyMakeTheSame: false });
  }

  onMount(() => {
    fetchData();
  });
</script>

{#if $getters.isLoading}
  <p>Loading...</p>
{:else if $getters.error}
  <p style="color: red;">Error: {$getters.error}</p>
{:else if $getters.userData}
  <div>
    <h1>User Data</h1>
    <pre>{JSON.stringify($getters.userData, null, 2)}</pre>
  </div>
{/if}

<button on:click={fetchData}>Refresh Data</button>
```

---

### 4. 封装 `store` 的优势

- **模块化**：将状态和逻辑按模块划分，便于维护和扩展。
- **复用性**：`actions` 和 `getters` 可以在多个组件中复用。
- **可测试性**：`actions` 和 `mutations` 可以单独测试。
- **清晰性**：`state`、`actions`、`getters` 和 `mutations` 分离，代码结构更清晰。

---

### 5. 示例：`about.svelte` 中使用 `store`

根据你的 `about.svelte` 文件，可以这样使用 `store`：

```svelte
<script lang="ts">
  import { t, locale } from "svelte-i18n";
  import { toast } from '@/utils/toastService';
  import { store } from '@/store/index';

  function getData() {
    store.center.actions.getUserData({ onlyMakeTheSame: false });
  }
</script>

<h1>{$t("welcome")}</h1>
<p>{$t("about")}</p>

<button on:click={getData}>获取接口数据</button>

{#if $store.center.getters.isLoading}
  <p>Loading...</p>
{:else if $store.center.getters.error}
  <p style="color: red;">Error: {$store.center.getters.error}</p>
{:else if $store.center.getters.userData}
  <div>
    <h1>User Data</h1>
    <pre>{JSON.stringify($store.center.getters.userData, null, 2)}</pre>
  </div>
{/if}
```

---

通过以上步骤，你可以在 Svelte 项目中封装 `store`，并实现 `state`、`actions`、`getters` 和 `mutations` 的分离，使代码更易于维护和扩展。

## 十二、扩展内容

这里由于使用的melt-ui没有toast提示于是做了一个全局组建toas.svelte

1. 组建创建

```xml
<script>
  import { fade } from "svelte/transition";
  export let message = "";
  export let duration = 3000; // 持续时间，单位毫秒

  let visible = false;

  const showToast = () => {
    visible = true;
    setTimeout(() => {
      visible = false;
    }, duration);
  };

  showToast(); // 显示Toast
</script>

{#if visible}
  <div class="toast" transition:fade>
    {message}
  </div>
{/if}

<style>
  .toast {
    position: fixed;
    top: 300px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px 20px;
    background-color: #333;
    color: white;
    border-radius: 5px;
    z-index: 1000;
  }
</style>
```

2. toastService封装

```javascript
import { writable } from 'svelte/store';
function createToast() {
  const { subscribe, set, update } = writable({ message: '', visible: false });
 
  function show(message, duration = 3000) {
    set({ message, visible: true });
    setTimeout(() => {
      update(current => ({ ...current, visible: false }));
    }, duration);
  }
 
  return {
    subscribe,
    show, // 公开show方法供外部调用
  };
}
 
export const toast = createToast(); // 创建并导出toast服务实例
```

3. 全局调用app.svelte

```xml
<script lang="ts">

  import Toast from "./components/Toast.svelte";
  import { toast } from "@/utils/toastService";
</script>
  {#if $toast.visible}
    <!-- 使用$来访问store的值 -->
    <Toast message={$toast.message} />
    <!-- 将消息传递给Toast组件 -->
  {/if}
```

4. 使用

```javascript
  import { toast } from '@/utils/toastService';
  toast.show('Hello, this is a toast!')
```

## 十三、框架git地址

<https://gitee.com/cyp926/svelte-vite>

[![](https://img2024.cnblogs.com/blog/35695/202506/35695-20250620221033642-784432140.webp)](https://www.doubao.com?channel=cnblogs&source=hw_db_cnblogs&type=lunt&theme=bianc)

**相关博文：**\

·  [10分钟了解MVVM，实现简易MVVM](https://www.cnblogs.com/ypSharing/p/17129546.html "10分钟了解MVVM，实现简易MVVM")

·  [微信小程序---快速上手云开发](https://www.cnblogs.com/ypSharing/p/15817954.html "微信小程序---快速上手云开发")

·  [Svelte](https://www.cnblogs.com/SRIGT/p/18406806 "Svelte")

·  [svelte使用总结](https://www.cnblogs.com/Dollom/p/17048043.html "svelte使用总结")

·  [SvelteKit 最新中文文档教程（1）—— 入门指南](https://www.cnblogs.com/yayujs/p/18768477 "SvelteKit 最新中文文档教程（1）—— 入门指南")

**阅读排行：**  
· [推荐 6 款基于 .NET 开源的串口调试工具，调试效率提升利器！](https://www.cnblogs.com/Can-daydayup/p/19006888)  
· [《HelloGitHub》第 112 期](https://www.cnblogs.com/xueweihan/p/19006999)  
· [大模型的JSON之殇：从脆弱的API调用到稳健的未来](https://www.cnblogs.com/sdcb/p/19005634/llm-json-hard)  
· [Abp vNext -动态 C# API 实现原理解析](https://www.cnblogs.com/yuxl01/p/18092437)  
· [千万级的大表如何新增字段？](https://www.cnblogs.com/12lisu/p/19008591)

- [react相关(11)](https://www.cnblogs.com/ypSharing/tag/react%E7%9B%B8%E5%85%B3/)
- [vue3.0(8)](https://www.cnblogs.com/ypSharing/tag/vue3.0/)
- [vue相关(6)](https://www.cnblogs.com/ypSharing/tag/vue%E7%9B%B8%E5%85%B3/)
- [前端问题处理与解释(6)](https://www.cnblogs.com/ypSharing/tag/%E5%89%8D%E7%AB%AF%E9%97%AE%E9%A2%98%E5%A4%84%E7%90%86%E4%B8%8E%E8%A7%A3%E9%87%8A/)
- [前端工程化(6)](https://www.cnblogs.com/ypSharing/tag/%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%8C%96/)
- [微信小程序(5)](https://www.cnblogs.com/ypSharing/tag/%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F/)
- [linux(4)](https://www.cnblogs.com/ypSharing/tag/linux/)
- [js相关(4)](https://www.cnblogs.com/ypSharing/tag/js%E7%9B%B8%E5%85%B3/)
- [案例(4)](https://www.cnblogs.com/ypSharing/tag/%E6%A1%88%E4%BE%8B/)
- [插件使用(3)](https://www.cnblogs.com/ypSharing/tag/%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8/)
- [更多](https://www.cnblogs.com/ypSharing/tag/)
- [1. vue.config.js中的webpack配置，优化及多页面应用开发(11360)](https://www.cnblogs.com/ypSharing/p/vue-webpack.html)
- [2. 8种Vue中数据更新了但页面没有更新的情况(10506)](https://www.cnblogs.com/ypSharing/p/updataHandler.html)
- [3. 九种实用的前端跨域处理方案(8257)](https://www.cnblogs.com/ypSharing/p/corsHanlder.html)
- [4. 前端-文件上传几种方式及其核心思想(5848)](https://www.cnblogs.com/ypSharing/p/16082614.html)
- [5. Vite详解(4508)](https://www.cnblogs.com/ypSharing/p/viteHandler.html)

### [推荐排行榜](https://www.cnblogs.com/ypSharing/most-liked)

- [1. 九种实用的前端跨域处理方案(6)](https://www.cnblogs.com/ypSharing/p/corsHanlder.html)
- [2. 23年用vuex进行状态管理out了，都开始用pinia啦！(5)](https://www.cnblogs.com/ypSharing/p/piniaShare.html)
- [3. 前端-文件上传几种方式及其核心思想(5)](https://www.cnblogs.com/ypSharing/p/16082614.html)
- [4. Vue3.x全家桶+vite+TS-搭建Vue3.x项目(4)](https://www.cnblogs.com/ypSharing/p/15304219.html)
- [5. vue.config.js中的webpack配置，优化及多页面应用开发(4)](https://www.cnblogs.com/ypSharing/p/vue-webpack.html)
