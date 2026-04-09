---
title: 设置单聊禁言
hide_title: true
sidebar_position: 6
---

### 功能说明{#intro}

单聊禁言后用户将无法发送私信消息，发送群组消息、聊天室消息不受影响，例如开发者平台发现某些用户经常在平台私信导流或做违法操作，此时开发者可将当前用户的发私信能力禁用。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/blockusers/block

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|设置单聊禁言的用户||
|block_user_ids|array|是|禁言的用户列表||

### 请求示例{#req_demo}
```js
POST /apigateway/users/blockusers/block HTTP/1.1
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
