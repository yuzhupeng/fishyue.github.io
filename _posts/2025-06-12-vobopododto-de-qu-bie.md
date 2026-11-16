---
layout: post
title: VO，BO，PO，DO，DTO的区别
date: 2025-06-12 09:00:00
summary: 看完图估计大部分人就已经有了一个直观的感受了
categories: Note
---

看完图估计大部分人就已经有了一个直观的感受了

![](https://pic3.zhimg.com/v2-24e3ed681c02b6434681719753c53b40_1440w.jpg)

面对这个图，让我们先从承上启下的DTO开始入手

**DTO（Data Transfer Object）数据传输对象**

这个传输通常指的前后端之间的传输

DTO是一个比较特殊的对象，他有两种存在形式：

在后端，他的存在形式是java对象，也就是在controller里面定义的那个东东，通常在后端不需要关心怎么从json转成java对象的，这个都是由一些成熟的框架帮你完成啦，比如spring框架

在前端，他的存在形式通常是js里面的对象（也可以简单理解成json），也就是通过ajax请求的那个数据体

这也是为什么把他画成横跨两层的原因

这里可能会遇到个问题，现在微服务盛行，服务和服务之间调用的传输对象能叫DTO吗？  
我的理解是看情况  
DTO本身的一个隐含的意义是要能够完整的表达一个业务模块的输出  
如果服务和服务之间相对独立，那就可以叫DTO  
如果服务和服务之间不独立，每个都不是一个完整的业务模块，拆开可能仅仅是因为计算复杂度或者性能的问题，那这就不能够叫做DTO，只能是BO

**VO（Value Object）值对象**  
VO就是展示用的数据，不管展示方式是网页，还是客户端，还是APP，只要是这个东西是让人看到的，这就叫VO  
VO主要的存在形式就是js里面的对象（也可以简单理解成json）

**VO和DTO的区别**  
主要有两个区别  
一个是字段不一样，VO根据需要会删减一些字段  
另一个是值不一样，VO会根据需要对DTO中的值进行展示业务的解释  
举个简单的例子  
DTO可能是这样的

```js
{
    "gender":"男", 
    "age":35 
}
```

对于业务一来说只需要性别，而且因为是一个古风聊天室，也不能直接展示男，因此经过业务解释业务一的VO是

```js
{ 
    "gender":"公子" 
}
```

对于业务二来说只需要年龄，而且不需要精确的年龄，因此经过业务解释业务二的VO是

```js
{ 
    "age":"30~39" 
}
```

**PO（Persistant Object）持久对象**  
PO比较好理解  
简单说PO就是数据库中的记录，一个PO的数据结构对应着库中表的结构，表中的一条记录就是一个PO对象  
通常PO里面除了get，set之外没有别的方法  
对于PO来说，数量是相对固定的，一定不会超过数据库表的数量  
等同于Entity，这俩概念是一致的

**BO（Business Object）业务对象**  
BO就是PO的组合  
简单的例子比如说PO是一条交易记录，BO是一个人全部的交易记录集合对象  
复杂点儿的例子PO1是交易记录，PO2是登录记录，PO3是商品浏览记录，PO4是添加购物车记录，PO5是搜索记录，BO是个人网站行为对象  
BO是一个业务对象，一类业务就会对应一个BO，数量上没有限制，而且BO会有很多业务操作，也就是说除了get，set方法以外，BO会有很多针对自身数据进行计算的方法  
为什么BO也画成横跨两层呢？原因是现在很多持久层框架自身就提供了数据组合的功能，因此BO有可能是在业务层由业务来拼装PO而成，也有可能是在数据库访问层由框架直接生成  
很多情况下为了追求查询的效率，框架跳过PO直接生成BO的情况非常普遍，PO只是用来增删改使用

**BO和DTO的区别**  
这两个的区别主要是就是字段的删减  
BO对内，为了进行业务计算需要辅助数据，或者是一个业务有多个对外的接口，BO可能会含有很多接口对外所不需要的数据，因此DTO需要在BO的基础上，只要自己需要的数据，然后对外提供  
在这个关系上，通常不会有数据内容的变化，内容变化要么在BO内部业务计算的时候完成，要么在解释VO的时候完成

OK，到这里这些关系基本就理清楚了

**等等，DO是什么**  
DO呢，标题不是还有个DO么？  
上面这些概念基本上已经涵盖了全部的流程，DO只是跟其中一个概念相同  
但是跟哪个概念相同呢？  
现在主要有两个版本  
一个是阿里巴巴的开发手册中的定义  
DO（ Data Object）这个等同于上面的PO  
另一个是在[DDD](https://zhida.zhihu.com/search?content_id=110884076&content_type=Article&match_order=1&q=DDD&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDk4ODA5MzEsInEiOiJEREQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxMTA4ODQwNzYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.76X571SMiTJH3YFhJu2NYP2T_8MM3I1OYKdUdzsJLxY&zhida_source=entity)（Domain-Driven Design）领域驱动设计中  
DO（Domain Object）这个等同于上面的BO

**最后，让我们再说说实际应用**  
这几个概念很完整，我们在用的时候是必须按这个来做吗？  
当然不是的，系统和系统的复杂度不同，协作水平不同，完全没有必要教条主义，这些概念全上  
上哪些概念，省哪些，我给一些实际建议  
1，PO这个没法省，不管叫PO还是Entity，怎么着都得有  
2，一些工具类的系统和一些业务不是很复杂的系统DTO是可以和BO合并成一个，当业务扩展的时候注意拆分就行  
3，VO是可以第一个优化掉的，展示业务不复杂的可以压根儿不要，直接用DTO  
4，这也是最重要的一条，概念是给人用的，多人协作的时候一定要保证大家的概念一致，赶紧把这篇文章转发给跟你协作的人吧

# 什么是AO、BO、DO、DAO、DTO、Domain、Entity、Mapper、PO、POJO、QO、Query、Req、Resp、RPC、VO、WebSocket

## **1. AO（Application Object，应用对象）**

- **用途**：协调多个业务对象或服务，处理**跨业务域的复杂流程**（如订单支付、用户注册）。
- **特点**：位于应用层，负责流程编排，不直接处理业务逻辑。

## **2. BO（Business Object，业务对象）**

- **用途**：封装**核心业务逻辑**（如订单计算、库存扣减）。
- **特点**：包含业务规则和状态管理。

## **3. DO（Domain Object，领域对象）**

- **用途**：在领域驱动设计（DDD）中表示**业务领域核心概念**（如用户、订单）。
- **特点**：包含数据和业务行为，与持久化无关。

## **4. DAO（Data Access Object，数据访问对象）**

- **用途**：封装数据库操作（CRUD），隔离数据库细节。
- **特点**：直接操作 PO（持久化对象）。

## **5. DTO（Data Transfer Object，数据传输对象）**

- **用途**：在层间或服务间传输数据（如 Controller → Service）。
- **特点**：纯数据结构，无业务逻辑。

## **6. Domain（领域模型）**

- **用途**：DDD 中的核心模型，包含实体（Entity）、值对象（Value Object）、聚合根（Aggregate Root）等。
- **特点**：聚焦业务语义，与数据库无关。

## **7. Entity（实体）**

- **用途**：具有唯一标识（ID）的业务对象（如用户），常与数据库表映射。
- **特点**：通过 ID 区分实例，可能包含业务逻辑。

## **8. Mapper（映射器）**

- **用途**：在不同对象类型间转换数据。

## **9. PO（Persistent Object，持久化对象）**

- **用途**：直接映射数据库表结构（如 JPA/Hibernate 的 `@Entity`）。
- **特点**：字段与表列一一对应。

## **10. POJO（Plain Old Java Object，简单Java对象）**

- **用途**：泛指不依赖框架的普通 Java 对象。
- **特点**：无强制继承或注解，灵活通用。

## **11. QO（Query Object，查询对象）**

- **用途**：封装复杂查询条件（如分页、排序）。
- **特点**：解耦 DAO 层的查询参数。

## **12. Query（查询参数）**

- **用途**：同 QO，表示查询条件（如 `UserQuery`）。

## **13. Req/Resp（请求/响应对象）**

- **用途**：专用于 API 接口的输入（Req）和输出（Resp）。

## **14. RPC（Remote Procedure Call，远程过程调用）**

- **用途**：跨服务或跨进程通信的协议规范。

## **15. VO（Value Object / View Object）**

- **用途**：

  - **值对象**：不可变的业务概念（如 `Money`）。
  - **视图对象**：前端展示数据聚合。

## **16. WebSocket**

- **用途**：双向实时通信协议的消息对象（如聊天消息）。
- **特点**：定义消息格式（JSON/二进制）。

---

## **关键对比表**

| 类型 | 核心用途 | 典型场景 | 特点 |
| --- | --- | --- | --- |
| **DTO** | 跨层/跨服务数据传输 | API 请求/响应 | 无逻辑，纯数据容器 |
| **VO** | 前端展示 | 页面数据聚合 | 适配展示需求 |
| **BO** | 封装业务规则 | 订单计算、库存管理 | 包含业务逻辑 |
| **Entity** | 持久化+业务实体 | 数据库映射的领域对象 | 有唯一标识（ID） |
| **PO** | 直接映射数据库表 | JPA/Hibernate 实体 | 与表结构严格对应 |
| **RPC** | 跨进程通信协议 | 微服务间调用 | 定义请求/响应格式 |
| **WebSocket** | 实时双向通信 | 聊天室、实时通知 | 基于消息驱动 |

## 前言

最近有小伙伴问我：O、VO、BO、DTO、DAO、POJO有什么区别？

第一眼看到，你可能也会有点懵。

这些对象的概念很多，确实容易搞混。

今天这篇文章跟大家一起聊聊这6种对象的含义、职责、区别和常见的坑，希望对你会有所帮助。

## 一、6种对象的职责边界

**对象设计的本质是关注点分离**——每个对象只做一件事，且做好它！

### 1.1 PO

它的含义是Persistent Object，即持久化对象。

- **职责**：与数据库表严格1:1映射，**仅承载数据存储结构**
- **特征**：
  - 属性与表字段完全对应
  - 无业务逻辑方法（仅有getter/setter）
- **代码示例**：

  public class UserPO {  
  private Long id; // 对应表主键  
  private String name; // 对应name字段  
  }

### 1.2 DAO

它的含义是Data Access Object，即数据访问对象。

- **职责**：**封装所有数据库操作**（CRUD），隔离业务与存储细节
- **特征**：
  - 接口方法对应SQL操作
  - 返回PO或PO集合
- **代码示例**：

  public interface UserDao {  
  // 根据ID查询PO  
  UserPO findById(Long id);

  
```
  // 分页查询  
  List<UserPO> findPage(@Param("offset") int offset, @Param("limit") int limit);
```

  }

**底层原理**：DAO模式 = 接口 + 实现类 + PO

![image](https://img2024.cnblogs.com/blog/2238006/202508/2238006-20250814170755724-1671378180.png)

### 1.3 BO

它的含义是Business Object，即业务对象。

- **职责**：**封装核心业务逻辑**，聚合多个PO完成复杂操作
- **特征**：
  - 包含业务状态机、校验规则
  - 可持有多个PO引用
- **代码示例**：订单退款BO

  public class OrderBO {  
  // 主订单数据  
  private OrderPO orderPO;  
  // 子订单项  
  private List items;

  
```
 // 业务方法：执行退款  
 public RefundResult refund(String reason) {     
 if (!"PAID".equals(orderPO.getStatus())) {  
    throw new IllegalStateException("未支付订单不可退款"); 
 }  // 计算退款金额、调用支付网关等  }
```

  }

### 1.4 DTO

它的含义是Data Transfer Object，即数据传输对象。

- **职责**：**跨层/跨服务数据传输**，屏蔽敏感字段
- **特征**：
  - 属性集是PO的子集（如排除`password`字段）
  - 支持序列化（实现`Serializable`）
- **代码示例**：用户信息DTO

  public class UserDTO implements Serializable {  
  private Long id;  
  private String name;  
  }

### 1.5 VO

它的含义是View Object，即视图对象。

- **职责**：**适配前端展示**，包含渲染逻辑
- **特征**：
  - 属性可包含格式化数据（如日期转`yyyy-MM-dd`）
  - 聚合多表数据（如订单VO包含用户名字）
- **代码示例**：

  public class OrderVO {  
  private String orderNo;  
  private String createTime; // 格式化后的日期 private String userName; // 关联用户表字段

  
```
//状态码转文字描述  
public String getStatusText() {  
   return OrderStatus.of(this.status).getDesc();  
}
```

  }

### 1.6 POJO

它的含义是Plain Old Java Object，即普通Java对象。

- **职责**：**基础数据容器**，可扮演PO/DTO/VO角色
- **特征**：
  - 只有属性+getter/setter
  - 无框架依赖（如不继承Spring类）
- **典型实现**：Lombok简化代码

  // 自动生成getter/setter  
  @Data  
  public class UserPOJO {  
  private Long id;  
  private String name;  
  }

## 二、主流的对象流转模型

### 场景1

传统三层架构（DAO → DTO → VO）。

**适用系统**：后台管理系统、工具类应用

**核心流程**：

![image](https://img2024.cnblogs.com/blog/2238006/202508/2238006-20250814170814243-1458026113.png)

**代码示例**：用户查询服务

```
// Service层  
public UserDTO getUserById(Long id) {  
   UserPO userPO = userDao.findById(id); // 从DAO获取PO  
   UserDTO dto = new UserDTO();  
   dto.setId(userPO.getId());  
   dto.setName(userPO.getName()); // 过滤敏感字段  
   return dto; // 返回DTO  
}  

// Controller层  
public UserVO getUser(Long id) {  
   UserDTO dto = userService.getUserById(id);  
   UserVO vo = new UserVO();  
   vo.setUserId(dto.getId());  
   vo.setUserName(dto.getName());  
   vo.setRegisterTime(formatDate(dto.getCreateTime())); // 格式化日期  
   return vo;  
}
```

**优点**：简单直接，适合CRUD场景

**缺点**：业务逻辑易泄漏到Service层

### 场景2

DDD架构（PO → DO → DTO → VO）。

**适用系统**：电商、金融等复杂业务系统

**核心流程**：

![image](https://img2024.cnblogs.com/blog/2238006/202508/2238006-20250814170827171-2014308076.png)

**关键角色**：DO（Domain Object）替代BO

**代码示例**：订单支付域

```
// Domain层：订单领域对象  
public class OrderDO {  
   private OrderPO orderPO;  
   private PaymentPO paymentPO;  

   // 业务方法：支付校验  
   public void validatePayment() {  
     if (paymentPO.getAmount() < orderPO.getTotalAmount()) {  
        throw new PaymentException("支付金额不足");  
      } 
   }  
}  

// App层：协调领域对象  
public OrderPaymentDTO pay(OrderPayCmd cmd) {  
    OrderDO order = orderRepo.findById(cmd.getOrderId());  
    order.validatePayment(); // 调用领域方法  return OrderConverter.toDTO(order); // 转DTO  
}
```

**优点**：业务高内聚，适合复杂规则系统

**缺点**：转换层级多，开发成本高

## 三、高效转换工具

手动转换对象？效率低且易错！

苏三在这里推荐三大利器。

### 3.1 MapStruct：编译期代码生成

**原理**：APT注解处理器生成转换代码

**示例**：PO转DTO

```
@Mapper  
public interface UserConverter {  
   UserConverter INSTANCE = Mappers.getMapper(UserConverter.class);  

   @Mapping(source = "createTime", target = "registerDate")  
   UserDTO poToDto(UserPO po);  
}  

// 编译后生成UserConverterImpl.java  
public class UserConverterImpl {  
   public UserDTO poToDto(UserPO po) {  
      UserDTO dto = new UserDTO();  
      dto.setRegisterDate(po.getCreateTime()); // 自动赋值！  
      return dto;  
  }  
}
```

**优点**：零反射损耗，性能接近手写代码

**开源地址**：<https://github.com/mapstruct/mapstruct>

### 3.2 Dozer + Lombok：注解驱动转换

**组合方案**：

- **Lombok**：自动生成getter/setter
- **Dozer**：XML/注解配置字段映射

  // Lombok注解  
  @Data  
  public class UserVO {  
  private String userId;  
  private String userName;  
  }

  // 转换配置  
    
  userId  
  **id**

**适用场景**：字段名不一致的复杂转换

### 3.3 手动Builder模式：精细控制

**适用场景**：需要动态构造的VO

```
public class OrderVOBuilder {  
   public OrderVO build(OrderDTO dto) {  
     return OrderVO.builder()  
        .orderNo(dto.getOrderNo())  
        .amount(dto.getAmount() + "元") // 动态拼接  
        .statusText(convertStatus(dto.getStatus()))  
        .build();  
    }  
}
```

## 四、避坑指南

### 坑1：PO直接返回给前端

```
// 致命错误：暴露数据库敏感字段！  
public UserPO getUser(Long id) {  
  // 返回的PO包含password  
  return userDao.findById(id); 
}
```

**解决方案**：

- 使用DTO过滤字段
- 注解屏蔽：`@JsonIgnore`

### 坑2：DTO中嵌入业务逻辑

```
public class OrderDTO {
    // 错误！DTO不应有业务方法  
    public void validate() { 
       if (amount < 0) 
          throw new Exception();  
    }  
}
```

**本质错误**：混淆DTO与BO的职责

### 坑3：循环嵌套转换

```
// OrderVO中嵌套List<ProductVO>  
public class OrderVO {
   // 嵌套对象  
   private List<ProductVO> products; 
}  

// 转换时触发N+1查询  
orderVO.setProducts(order.getProducts()
       .stream()  
       .map(p -> convertToVO(p)) // 循环查询数据库  
       .collect(toList()));
```

**优化方案**：批量查询 + 并行转换

### 五、如何选择对象模型？

![image](https://img2024.cnblogs.com/blog/2238006/202508/2238006-20250814170846460-909071477.png)

## 总结

关于对象的4个核心原则：

1. **单一职责**：

   PO只存数据，BO只管业务，VO只负责展示——**绝不越界！**
2. **安全隔离**：
   - PO永不出DAO层（防数据库泄露）
   - VO永不出Controller（防前端逻辑污染服务）
3. **性能优先**：
   - 大对象转换用**MapStruct**（编译期生成代码）
   - 嵌套集合用**批量查询**（杜绝N+1）
4. **适度设计**：
   - 10张表以内的系统：可用POJO一撸到底
   - 百张表以上核心系统：**必须严格分层**

对象设计没有银弹，**理解业务比套用模式更重要**！

当你在为对象命名纠结时，不妨回到业务的起点问一句：“它此刻的核心职责是什么？”
