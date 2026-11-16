---
layout: post
title: MySQL 索引核心要点摘要（结构化）
date: 2025-08-18 09:00:00
summary: ALTER TABLE t ADD COLUMN revname VARCHAR(255) AS (REVERSE(name)) STORED;
categories: Database
---

**MySQL 索引核心要点摘要（结构化）**

---

## 1. 模糊匹配（LIKE）与索引

| 匹配方式 | 能否使用索引 | 解决方案 |
| --- | --- | --- |
| `LIKE 'prefix%'`（前缀匹配） | ✅ 能使用普通 B‑Tree 索引 | 直接建普通索引 |
| `LIKE '%suffix'`（后缀匹配） | ❌ 索引失效（全表扫描） | ① 生成 **反转列** `REVERSE(col)` 并建索引； ② MySQL 8.0+ 可用 **函数索引**（生成列） |
| `LIKE '%mid%'`（左右模糊） | ❌ 索引失效 | 同上，使用 N‑gram、全文索引或 Elasticsearch 等外部检索方案 |

---

## 2. 函数/表达式索引（Generated Column）

- MySQL 8.0 起支持 **函数索引**：把表达式结果存入隐藏/显式生成列，再对该列建索引。

```sql
ALTER TABLE t ADD COLUMN rev_name VARCHAR(255) AS (REVERSE(name)) STORED;
CREATE INDEX idx_rev_name ON t (rev_name);
```

- 仅在 **WHERE / ON** 条件中使用该函数时才能走索引；在 SELECT、ORDER BY、GROUP BY 等仅做展示的地方不影响索引使用。

---

## 3. 数据类型转换与索引

- **列是数值型**，查询条件写成字符串（如 `'123'`）仍会走索引，因为 MySQL 会把字符串转为数值后比较。
- **列是字符串型**，查询条件写成数值（如 `WHERE name = 123`）会导致 **隐式转为数值**，索引失效，回到全表扫描。  
  **建议**：

- 数值列不加引号；
- 字符串列加单/双引号。

---

## 4. 联合索引（复合索引）与最左前缀原则

- 索引列的顺序决定查询能否使用该索引。
- **最左匹配**：只有从索引最左边开始连续的等值列才会被使用。

**可用示例**（索引 `(a,b,c)`）

| 查询条件 | 是否走索引 |
| --- | --- |
| `WHERE a=1` | ✅ |
| `WHERE a=1 AND b=2` | ✅ |
| `WHERE a=1 AND b=2 AND c=3` | ✅ |
| `WHERE b=2` | ❌ |
| `WHERE c=3` | ❌ |
| `WHERE b=2 AND c=3` | ❌ |
| `WHERE a=1 AND c=0` | ✅（仅使用 `a`） |

- **范围条件**（`>、>=、<、BETWEEN、LIKE 'p%'`）一旦出现，就会 **阻断**后续列的索引使用。

---

## 5. WHERE 条件的书写顺序

- MySQL 优化器会 **重新排列** WHERE 子句以获得最佳执行计划，顺序本身不决定是否走索引。
- 但 **把最左索引列的等值条件写在前面**，有助于阅读和调试，也避免因错误的提示误以为顺序有影响。

---

## 6. OR / IN / NOT 系列

| 场景 | 索引使用情况 | 备注 |
| --- | --- | --- |
| `WHERE col1 = 'a' OR col1 = 'b'` | ✅ (同一列的 OR) | 可走索引的 **合并**（union） |
| `WHERE indexed_col = 1 OR non_indexed_col = 2` | ❌ 触发全表扫描 | 任意一个条件不走索引，整体失效 |
| `WHERE col IN (1,2,3,…)` | ✅ 在大多数情况下走索引 | **IN 元素 ≤ 1000** 且匹配度 <≈30% 时更佳 |
| `WHERE col NOT IN (…)`、`col != …`、`NOT LIKE` | ❌ 通常不能走索引 | 只在 **极端低基数**、**小表** 时可能走索引 |
| **例外** | 当优化器评估**全表扫描成本更低**（如返回 >30% 行）时，即使写 `IN` 也会放弃索引 | 需通过 `FORCE INDEX` 或统计信息调优纠正 |

---

## 7. 范围查询对复合索引的影响

```sql
-- 索引 (shop_id, created_at, order_status)
SELECT * FROM _order
WHERE shop_id = 1               -- 等值，可用
  AND created_at > '2021-01-01' -- 范围，阻断后续列
  AND order_status = 10;       -- **不走索引**（因为已被范围查询阻断）
```

- 若范围条件在最左列，则后续列全部失效。
- 若需要同时过滤 `order_status`，考虑 **拆分索引** 或使用 **覆盖索引**（包括 `order_status`）与 `WHERE` 重排。

---

## 8. 覆盖索引（Covering Index）

- 当查询的 **所有列**（包括 SELECT、WHERE、ORDER BY、GROUP BY）都包含在同一个二级索引的叶子节点时，**不需要回表**，直接返回结果。
- 常见做法：在联合索引中把 **需要返回的列**（非主键列）也加入索引。

```sql
CREATE INDEX idx_user_name_addr ON user (name, address);
SELECT name, address FROM user WHERE name='seven';
-- 直接从索引返回，无回表
```

---

## 9. ASC / DESC 混合排序与索引

- MySQL 8.0+ 支持 **显式指定排序方向**的二级索引（如 `(a ASC, b DESC)`），但 **老版本只能使用 ASC**。
- 当 `ORDER BY` 的列顺序或方向与索引定义不一致时，索引会失效，导致 **文件排序**（filesort）。

```sql
-- 索引 (customer_id ASC, order_date ASC)
SELECT * FROM orders ORDER BY customer_id DESC, order_date; -- 索引失效
```

- 解决办法：
  - 创建匹配的 `(customer_id DESC, order_date ASC)` 索引（MySQL 8.0+）。
  - 或者只使用 **单列索引** + 二次排序。

---

## 10. 更新索引列的代价

- **INSERT / UPDATE / DELETE** 涉及索引列时，需要 **维护 B‑Tree**（分裂、合并、重新平衡）。
- 对高并发写入、频繁更新的列（如状态位）**不建议建索引**，或使用 **延迟写、分表** 等方案。

---

## 11. 必须建立索引的关键字段

| 场景 | 推荐索引类型 |
| --- | --- |
| `UPDATE` / `DELETE` 的 `WHERE` 条件 | 单列或复合索引 |
| `SELECT … ORDER BY`、`GROUP BY`、`DISTINCT` | 包含排序/分组列的索引 |
| 多表 `JOIN`（ON 条件） | 连接列的索引 |
| 高频过滤的业务字段（如 `status`、`type`） | 视基数决定，必要时使用 **位图索引**（MySQL 不直接支持） |

---

## 12. 子查询 vs. JOIN

- **JOIN** 更易被优化器利用 **索引合并、哈希/嵌套循环** 等高级执行计划。
- **子查询**（尤其是相关子查询）往往导致 **多次扫描**，性能劣于等价的 JOIN。
- 推荐：把可改写为 **等价的内连接** 的子查询改写为 JOIN。

---

## 13. ORDER BY 与 LIMIT 的深分页优化

### 13.1 LIMIT 的成本

| 语句 | 执行过程 | 性能影响 |
| --- | --- | --- |
| `SELECT * FROM t ORDER BY id LIMIT 0, 10` | 直接取前 10 条索引行 | 快 |
| `SELECT * FROM t ORDER BY id LIMIT 500000, 10` | 读取 500010 条索引行 → 丢弃前 500000 条 | 较慢（I/O、CPU） |

### 13.2 优化方案

1. **Keyset Pagination（基于索引的分页）**
```sql
SELECT * FROM t WHERE id > :last_id ORDER BY id LIMIT 10;
```

2. **子查询获取起始点**（仅返回主键列）
```sql
SELECT * FROM t
WHERE id >= (SELECT id FROM t ORDER BY id LIMIT 500000, 1)
ORDER BY id LIMIT 10;
```

3. **使用覆盖索引**：只查询主键列，减少回表数据量。
4. **使用更高效的存储引擎/缓存**（如 **InnoDB** 的自适应哈希）或 **物化视图**。

---

## 14. 大表（千万级+）性能提升手段

| 方法 | 适用场景 | 关键点 |
| --- | --- | --- |
| **合理建索引**（最左前缀、覆盖索引） | 常用过滤/排序列 | `EXPLAIN` 检查是否走索引 |
| **水平分区**（基于时间、业务维度） | 时间范围查询频繁 | 分区裁剪，避免扫描无关分区 |
| **读写分离** | 写入压力大、读请求多 | 主库写，多个从库读 |
| **分库分表**（垂直/水平） | 单库并发/容量到达上限 | 业务拆分、统一路由层 |
| **缓存**（Redis、Memcached） | 热点数据、计数、查询结果 | 缓存失效策略、缓存穿透防护 |
| **外部搜索**（Elasticsearch、OpenSearch） | 高级全文、模糊搜索 | 业务层同步、双写 |
| **冷热数据分离** | 老数据访问少 | 冷库归档、热库保留活跃数据 |
| **升级数据库引擎**（TiDB、OceanBase） | 需要分布式水平扩展 | 兼容 MySQL 协议，评估迁移成本 |
| **表结构优化**（列裁剪、压缩） | 大宽表 | 只保留必要列、使用 `ROW_FORMAT=COMPRESSED` |
| **统计信息维护** | 优化器判断失误 | `ANALYZE TABLE`、`UPDATE STATISTICS` |

---

## 15. 索引失效却提升性能的典型情形

| 场景 | 原因 | 建议 |
| --- | --- | --- |
| **小表（行数几千以下）** | 全表扫描顺序读硬盘，比随机读索引更快 | 可不建索引，或使用 `FORCE INDEX` 让优化器走索引 |
| **查询返回大量行（>30%）** | 索引查找 + 回表成本 > 顺序全表扫描 | 考虑 **覆盖索引**，或拆分查询 |
| **低基数列（布尔、枚举）** | 索引选择性低，查找大量相同值 | 不为此类列单独建索引；合并到复合索引中提升过滤 |
| **写入频繁且更新索引列** | 索引维护开销大 | 减少索引列、延迟写、使用 **延迟更新**（如异步批量） |
| \*\*优化器误估 | 统计信息过时、数据分布不均\*\* | 手动 `ANALYZE TABLE`、使用 `FORCE INDEX` 或 `USE INDEX` 调整计划 |

---

## 16. 常用调优小技巧

- **使用 `EXPLAIN` 检查执行计划**：关注 `type`、`possible_keys`、`key`、`rows`、`Extra` 中的 “Using where”, “Using index”, “Using filesort”, “Using temporary”。
- **利用 `INFORMATION_SCHEMA.STATISTICS` 与 `ANALYZE`** 更新统计信息。
- **避免函数/表达式在 WHERE 左侧**（除非已建函数索引）。
- **对经常 `GROUP BY` / `ORDER BY` 的列**，使用 **前缀索引** 或 **覆盖索引**。
- **开启 `innodb_buffer_pool_size`** 至机器物理内存的 70% 左右，提升缓存命中率。
- **监控慢查询日志**、`performance_schema`、`sys.schema_table_statistics`，定位热点。

---

> **核心结论**：
>
> - **最左前缀原则**是复合索引的根本，任何破坏该原则的查询（范围、% 开头的 LIKE、OR/NOT 等）都会导致索引失效。
> - **覆盖索引**、**函数索引**、**键值分页**是提升查询效率的关键手段。
> - **合理规划索引（列顺序、方向、基数）**、**维护统计信息**、**结合分区/缓存**，才能在大表、高并发场景下保持 MySQL 的高性能。
