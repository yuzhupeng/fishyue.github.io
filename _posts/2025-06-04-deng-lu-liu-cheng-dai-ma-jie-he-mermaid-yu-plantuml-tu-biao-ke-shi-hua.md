---
layout: post
title: 登录流程代码，结合 Mermaid 与 PlantUML 图表可视化
date: 2025-06-04 09:00:00
summary: 本文结合前后端实现代码，对一个集成了拼图验证码与AD域认证的账号密码登录流程进行可视化说明。我们分别使用 Mermaid 与 PlantUML 进行时序图与流程图的绘制，以便于开发团队理解整体业务流程
categories: Architecture
---

---

# 企业统一登录流程图文解析（含 Mermaid 与 PlantUML 可视化）

本文结合前后端实现代码，对一个集成了**拼图验证码**与**AD域认证**的账号密码登录流程进行可视化说明。我们分别使用 **Mermaid** 与 **PlantUML** 进行时序图与流程图的绘制，以便于开发团队理解整体业务流程。

---

## 🧩 登录流程概览

用户通过前端页面提交账号密码，系统先进行拼图验证，再根据是否为系统已有用户决定走本地校验或 AD 域认证，并最终完成 token 的生成与登录跳转。

---

## 📊 Mermaid 流程图（简洁结构）

```mermaid
flowchart TD
  A[用户点击登录按钮] --> B[handleSubmit 调用]
  B --> C[初始化拼图验证码 verifyInit]
  C --> D[用户验证通过]
  D --> E[调用 API: /userLogin]
  E --> F[后端接收参数: username, password, truthpassword, uuid]

  F --> G{系统中是否存在用户？}
  G -- 否 --> H[获取 accessToken]
  H --> I[调用 AD 域认证接口]
  I --> J{AD认证是否通过？}
  J -- 否 --> K[返回错误：AD认证失败]
  J -- 是 --> L[调用 AD 接口获取员工信息]
  L --> M{是否查到员工信息？}
  M -- 否 --> N[根据工号再次获取员工信息]
  N --> O[注册为新用户]
  M -- 是 --> O

  G -- 是 --> P[本地校验密码]
  P --> Q{密码验证是否通过？}
  Q -- 是 --> R[登录成功]
  Q -- 否 --> S[尝试 AD 认证]
  S --> T{AD认证是否通过？}
  T -- 否 --> U[返回错误：密码错误]
  T -- 是 --> V[更新本地密码]

  O --> R
  V --> R
  R --> W[创建 Token]
  W --> X[返回 Token 到前端]
  X --> Y[前端存储 Token 并跳转首页]
```

> ✅ 建议使用支持 Mermaid 的 Markdown 编辑器（如 Typora、Obsidian、VS Code 插件）进行渲染。  
> ![](https://yuzhupeng.top/myblogs//post-images/1749008217718.png)

---

## ⏱ PlantUML 时序图（完整调用关系）

```plantuml
@startuml
actor 用户
participant "前端 Login.vue" as Frontend
participant "后端 Controller" as Controller
participant "MemberService" as Service
participant "ADMemberSyncService" as ADService
participant "TokenService" as TokenService

用户 -> Frontend: 输入用户名/密码\n点击登录
Frontend -> Frontend: verify.init() 验证码校验
Frontend -> 用户: 展示拼图验证码
用户 -> Frontend: 验证通过
Frontend -> Controller: POST /userLogin\nusername + password + truthpassword + uuid

Controller -> Service: usernameLogin(username, password, truthpassword)

alt 用户不存在
  Service -> ADService: getAccessToken()
  Service -> ADService: adAuthenticate(username, truthpassword, accessToken)
  alt 认证失败
    ADService --> Service: false
    Service -> Controller: 返回错误
  else 认证成功
    Service -> ADService: getEmployeeInfo(username, accessToken)
    alt 未获取成功
      Service -> ADService: getEmployeeInfoByWorkNumber(username)
    end
    Service -> Service: 创建新用户(member)
  end
else 用户存在
  Service -> Service: 校验本地密码
  alt 密码正确
    Service -> TokenService: 创建 token
  else 密码错误
    Service -> ADService: getAccessToken()
    Service -> ADService: adAuthenticate(username, truthpassword, accessToken)
    alt AD认证失败
      Service -> Controller: 返回错误
    else AD认证成功
      Service -> Service: 更新本地密码
      Service -> TokenService: 创建 token
    end
  end
end

TokenService --> Service: 返回 token
Service --> Controller: 返回 accessToken/refreshToken
Controller --> Frontend: 登录成功
Frontend -> 用户: 跳转首页
@enduml
```

> ✅ 可通过 [PlantUML Live](https://www.plantuml.com/plantuml/) 或 VS Code 插件进行可视化。  
> ![](https://yuzhupeng.top/myblogs//post-images/1749008228294.png)  
> ![](https://yuzhupeng.top/myblogs//post-images/1749008234309.png)

---

## 🔎 总结

- 登录流程中使用了 **双重校验机制**：先本地密码校验，再补偿性调用 AD 域认证。
- 用户不存在时，也能通过 AD 信息自动建档，做到「无缝引导入系统」。
- 图表工具如 **Mermaid** 更适合概览类展示，**PlantUML** 则适合详细链路跟踪。

---
