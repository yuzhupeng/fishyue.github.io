---
layout: post
title: "java spring rules &amp;开发规范"
date: 2025-06-20 09:00:00
summary: "globs: [\"/controller//.java\", \"/api//.java\"]"
categories: Backend
---


globs: ["**/controller/**/*.java", "**/api/**/*.java"]  
alwaysApply: true  
description: |  
RESTful API设计规范

# URL设计规范

- 使用名词复数形式表示资源集合：`/users`, `/orders`
- 使用资源ID标识特定资源：`/users/{id}`, `/orders/{id}`
- 使用子资源表示资源关系：`/users/{id}/orders`
- 使用查询参数进行筛选、排序和分页：`/users?role=admin&sort=name&page=1&size=10`
- 避免在URL中使用动词，将动词映射到HTTP方法

# HTTP方法使用规范

- GET：获取资源（幂等）
- POST：创建资源
- PUT：全量更新资源（幂等）
- PATCH：部分更新资源
- DELETE：删除资源（幂等）

# 状态码使用规范

- 2xx：成功
  - 200 OK：请求成功
  - 201 Created：资源创建成功
  - 204 No Content：请求成功但无返回内容（如删除操作）
- 4xx：客户端错误
  - 400 Bad Request：请求参数错误
  - 401 Unauthorized：未认证
  - 403 Forbidden：权限不足
  - 404 Not Found：资源不存在
  - 409 Conflict：资源冲突
- 5xx：服务器错误
  - 500 Internal Server Error：服务器内部错误

# 响应体规范

## 成功响应格式

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    // 具体数据
  },
  "timestamp": 1642406400000
}
```

## 错误响应格式

```json
{
  "code": 400,
  "message": "参数错误",
  "errors": [
    {
      "field": "username",
      "message": "用户名不能为空"
    }
  ],
  "timestamp": 1642406400000
}
```

# API版本管理

- 使用URL路径版本：`/v1/users`, `/v2/orders`
- 或使用请求头版本：`Accept: application/vnd.company.v1+json`

# 安全规范

- 使用HTTPS保护通信
- 实施请求速率限制
- 验证所有输入参数
- 使用JWT或OAuth2进行身份验证
- 避免在URL中包含敏感信息

# 文档规范

- 使用Swagger/OpenAPI记录API
- 明确记录请求参数、响应格式和可能的错误码
- 提供示例请求和响应
- 记录API变更历史

globs:  
[  
"**/mapper/**/*.java",  
"**/repository/**/*.java",  
"**/dao/**/\*.java",  
"\*\*/\*Mapper.xml",  
]  
alwaysApply: true  
description: |  
数据库操作规范

# 数据库命名规范

## 表命名

- 使用小写字母和下划线分隔单词（snake_case）
- 使用复数形式表示实体集合：`users`, `orders`
- 使用前缀区分功能模块：`tb_user`, `tb_order`
- 中间表命名：`user_role`, `order_item`

## 字段命名

- 使用小写字母和下划线分隔单词（snake_case）
- 主键统一命名为`id`
- 创建时间统一命名为`create_time`
- 更新时间统一命名为`update_time`
- 外键命名格式：`表名_id`，如`user_id`, `order_id`
- 状态字段统一命名为`status`
- 逻辑删除字段统一命名为`is_deleted`

# 数据库设计规范

- 必须包含主键，优先使用自增ID或雪花ID
- 每个表必须包含创建时间和更新时间
- 考虑使用逻辑删除而非物理删除
- 对常用查询字段添加索引
- 所有表必须设定字符集为utf8mb4
- 所有表和字段必须添加注释

# MyBatis/MyBatis-Plus使用规范

## Mapper接口

- 继承BaseMapper以获取基础CRUD方法
- 自定义方法使用@Param注解标注参数
- 使用注解或XML管理SQL语句（推荐XML方式）

## XML映射文件

- XML文件应与Mapper接口同名
- 使用resultMap映射复杂对象关系
- 大型复杂查询SQL应放在XML中而非注解中
- 灵活使用动态SQL（if, choose, where, foreach等）

# SQL编写规范

- 关键字使用大写：SELECT, INSERT, UPDATE, DELETE
- 表名、字段名使用小写
- 复杂查询应当拆分为多行，提高可读性
- 避免使用SELECT \*，明确指定查询字段
- 使用参数化查询，避免SQL注入
- 大数据量查询应分页处理
- JOIN查询应谨慎使用，避免性能问题
- 使用COUNT(\*)而非COUNT(1)或COUNT(字段名)

# 事务管理

- 合理使用@Transactional注解
- 明确指定隔离级别和传播行为
- 避免长事务
- 避免嵌套事务可能导致的问题
- 合理配置事务超时时间

# 数据安全

- 敏感数据应加密存储
- 重要操作应记录审计日志
- 禁止直接拼接SQL语句
- 生产环境禁止使用高权限数据库账号
- 数据库访问密码应加密存储

globs: "\*\*/\*.java"  
alwaysApply: true  
description: |  
Java项目Git规范

# 提交规范

## 提交信息格式

- 标准格式：`<类型>(<范围>): <主题>`
- 类型：feat(新功能), fix(修复), docs(文档), style(格式), refactor(重构), test(测试), chore(其他)
- 范围：可选，表示影响的模块或功能
- 主题：简洁明了地描述本次提交的内容

## 提交示例

- `feat(user): 添加用户登录功能`
- `fix(order): 修复订单计算价格错误`
- `docs: 更新API文档`
- `style: 格式化代码`
- `refactor(payment): 重构支付模块`

# 分支管理

## 分支命名

- master/main：主分支，用于生产环境
- develop：开发分支，用于开发环境
- feature/\*：功能分支，用于开发新功能
- bugfix/\*：错误修复分支，用于修复问题
- release/\*：发布分支，用于版本发布
- hotfix/\*：热修复分支，用于紧急修复生产环境问题

## 分支示例

- `feature/user-login`
- `bugfix/order-calculation`
- `release/v1.2.0`
- `hotfix/critical-security-issue`

# Git工作流

## 基本流程

1. 从develop分支创建功能分支
2. 提交功能开发内容
3. 完成功能开发后，向develop分支提交合并请求
4. 经过代码审查后合并到develop分支
5. 发布时，从develop分支创建release分支
6. 经过测试后，将release分支合并到master和develop分支

# Java项目特殊规范

- 不要提交编译生成的文件（target/目录）
- 不要提交IDE配置文件（.idea/，.vscode/等，除非是团队共享配置）
- 不要提交敏感信息（密码，API密钥等）
- 对于大文件或二进制文件，考虑使用Git LFS

globs:  
alwaysApply: true  
description: |  
Java Spring Boot项目规范

# 开发规范

- 遵循Java代码风格和命名约定
- 始终使用Spring Boot最佳实践
- 保持代码简洁、模块化和可测试
- 正确处理异常并提供有意义的错误消息

# 代码规范

## 命名规范

- 类名：使用PascalCase（例如UserController, OrderService）
- 方法和变量：使用camelCase（例如findUserById, isOrderValid）
- 常量：使用ALL_CAPS（例如MAX_RETRY_ATTEMPTS, DEFAULT_PAGE_SIZE）
- 接口名称：使用PascalCase并可以以I作为前缀（例如IUserService）
- 抽象类名称：使用Abstract作为前缀（例如AbstractUserService）

## 包结构

- controller：存放控制器类
- service：存放服务接口
- serviceimpl：存放服务实现类
- mapper：存放MyBatis映射接口
- entity/vo/dto：存放数据模型
- config：存放配置类
- util：存放工具类

## Spring Boot最佳实践

- 使用构造函数注入而不是字段注入
- 合理使用Spring的注解（@RestController, @Service等）
- 使用统一的异常处理（@ControllerAdvice, @ExceptionHandler）
- API设计遵循RESTful原则
- 将配置参数外部化到application.properties/application.yml

## 数据库访问

- 使用MyBatis-Plus进行数据库操作
- 编写清晰的SQL或使用ORM映射
- 适当使用事务管理（@Transactional）
- 避免N+1查询问题

## 安全最佳实践

- 使用Spring Security进行身份验证和授权
- 实施适当的输入验证
- 对敏感数据进行加密
- 使用JWT进行无状态身份验证

## 代码质量

- 添加适当的日志记录（使用SLF4J）
- 编写单元测试（JUnit）和集成测试
- 遵循SOLID原则
- 使用代码格式化工具和静态分析工具

## 性能考虑

- 合理使用缓存（Redis）
- 优化数据库查询
- 使用异步处理（@Async）处理长时间运行的任务
- 监控应用程序性能
