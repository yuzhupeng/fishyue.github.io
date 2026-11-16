---
layout: post
title: Elasticsearch 和 Kibana 学习
date: 2025-05-21 09:00:00
summary: Elasticsearch 的核心是一个强大的 JSON 文档数据库，它支持复杂查询、高性能全文搜索和聚合分析。
categories: Database
---

---

## 🧠 第一步：理解 Elasticsearch 是什么

**Elasticsearch** 是一个分布式、开源的搜索和分析引擎，适合处理大规模的结构化或半结构化数据。它常用于：

- 全文搜索
- 日志分析（如配合 Filebeat、Logstash 使用）
- 实时指标监控（如 APM）
- 数据可视化（通常配合 Kibana）

Elasticsearch 的核心是一个强大的 JSON 文档数据库，它支持复杂查询、高性能全文搜索和聚合分析。

---

## 🧱 第二步：核心概念详解

### 1. **文档（Document）**

- Elasticsearch 的基本数据单位。
- 一个文档是一个 JSON 对象。
- 类似于数据库中的“行”。

```json
{
  "name": "Audrey",
  "age": 28,
  "skills": ["Python", "Elasticsearch"]
}
```

### 2. **索引（Index）**

- 文档的集合，相当于数据库中的“表”。
- 每个索引都有自己的名称和配置。
- 文档必须属于某个索引。

创建索引示例：

```bash
PUT /my_index
```

### 3. **映射（Mapping）**

- 定义索引中字段的结构（类似 SQL 的 schema）。
- 包括字段的类型（如 `text`、`keyword`、`date`、`integer`）和属性（是否可被搜索、是否建立倒排索引等）。

示例：

```bash
PUT /my_index
{
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "age": { "type": "integer" },
      "join_date": { "type": "date" }
    }
  }
}
```

### 4. **类型（Type）**

- 老版本中一个索引可有多个“type”，但**新版本已废弃 type 概念**，每个索引只允许一个文档类型。

---

## 🔧 第三步：基本操作（使用 Kibana Console）

打开 Kibana Dev Tools，可以输入如下命令：

### 插入文档（Indexing）

```bash
POST /my_index/_doc
{
  "name": "Alice",
  "age": 30,
  "skills": ["Java", "Elasticsearch"]
}
```

### 查询文档（Search）

```bash
GET /my_index/_search
{
  "query": {
    "match": {
      "name": "Alice"
    }
  }
}
```

### 获取文档（Get）

```bash
GET /my_index/_doc/1
```

### 删除文档

```bash
DELETE /my_index/_doc/1
```

---

## 📊 第四步：学习 Kibana 可视化

Kibana 是 Elasticsearch 的可视化界面，主要功能包括：

- 数据可视化（创建图表、仪表盘）
- Dev Tools（发送 API 请求）
- Discover（浏览数据）
- 管理索引模式（Index Pattern）

### 第一次使用建议：

1. 在 Kibana 中创建 Index Pattern，如 `my_index*`
2. 使用 Discover 浏览你插入的数据
3. 尝试创建一个可视化图表，如柱状图或折线图

---

## 📚 第五步：进阶建议

等你掌握了基本操作后，建议继续学习以下内容：

- **布尔查询、过滤器查询**
- **聚合分析（Aggregations）**
- **全文检索 vs 精确匹配（`text` vs `keyword`）**
- **分析器（Analyzer）和分词（Tokenizer）**
- **索引生命周期管理（ILM）**
- **使用 Logstash/Beats 输入数据**

---

## 🗂 示例练习项目（建议动手）

- 创建一个包含“用户简历信息”的索引，字段如 `name`、`age`、`skills`、`experience_years`。
- 插入几条文档数据。
- 用 match 查询技能为“Python”的用户。
- 创建一个柱状图展示技能分布。

---

要查询 `lili_goods` 索引查询 `lili_goods` 索引的数据，你可以通过 Kibana 的 **Dev Tools** 或直接使用 Elasticsearch 的 API。下面是几种常见的查询方式。

### 1. **查询所有文档**

如果你想查询 `lili_goods` 索引中的所有文档，可以使用如下的简单查询：

```bash
GET /lili_goods/_search
```

这会返回 `lili_goods` 索引中的所有文档，默认只返回前 10 条数据。

### 2. **查询特定字段**

如果你只想查询某个字段，或者用特定的关键词来查找数据，例如查找商品名称包含某个关键词的文档：

```bash
GET /lili_goods/_search
{
  "query": {
    "match": {
      "product_name": "some_keyword"
    }
  }
}
```

这里 `product_name` 是假设的字段名，`some_keyword` 是你要匹配的关键词。你可以根据实际的字段名和关键词进行修改。

### 3. **分页查询（获取更多文档）**

如果 `lili_goods` 索引有很多文档，默认返回 10 条，你可以使用 `size` 和 `from` 来控制分页查询。例如，获取第 2 页的 10 条记录：

```bash
GET /lili_goods/_search
{
  "size": 10,
  "from": 10
}
```

这会跳过前 10 条记录，返回第 11 到第 20 条记录。

### 4. **查询特定条件的文档（例如价格范围）**

假设你想根据商品价格查询，以下是一个查询示例，查找价格在 50 到 100 之间的商品：

```bash
GET /lili_goods/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 50,
        "lte": 100
      }
    }
  }
}
```

这里 `price` 是字段名，`gte` 和 `lte` 表示价格的范围。

### 5. **查询所有文档并返回特定字段**

如果你只关心某些字段，而不需要返回整个文档，可以使用 `_source` 来指定返回的字段：

```bash
GET /lili_goods/_search
{
  "_source": ["product_name", "price", "stock"],
  "query": {
    "match_all": {}
  }
}
```

这会返回所有文档，但只包含 `product_name`、`price` 和 `stock` 字段。

### 6. **查看索引的映射（Mapping）**

如果你不知道 `lili_goods` 索引的字段结构，可以先查看它的映射，了解字段类型和配置：

```bash
GET /lili_goods/_mapping
```

这会返回索引的映射信息，告诉你各字段的数据类型及是否支持搜索。

---

### 小结

通过这些查询，你可以灵活地查询 `lili_goods` 索引中的数据。如果你需要根据特定条件过滤、分页或指定字段等，使用 Elasticsearch 强大的查询语法进行操作。

你可以先试试这些查询，如果有其他问题或更复杂的查询需求，随时告诉我！
