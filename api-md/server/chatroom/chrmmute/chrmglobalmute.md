---
title: 设置聊天室全局禁言
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

设置聊天室全局禁言后，当前聊天室所有成员将无法向发送消息，白名单用户除外。**Server API 发送消息不受禁言影响**。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/chatrooms/chrmmute/set

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|chat_id|string|是|聊天室id||
|is_mute|int|是|0:未禁言；1:禁言；||

### 请求示例{#req_demo}
```js
POST /apigateway/chatrooms/chrmmute/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id":"chatroomid1",
  "is_mute":1
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```