---
title: 解除单聊禁言
hide_title: true
sidebar_position: 7
---

### 功能说明{#intro}

解除封禁用户发送私信消息的能力。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/blockusers/unblock

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|设置单聊禁言的用户||
|block_user_ids|array|是|禁言的用户列表||


### 请求示例{#req_demo}

```js
POST /apigateway/users/blockusers/unblock HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"user1",
  "block_user_ids":["user2","user3"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```