---
title: 设置群禁言
hide_title: true
sidebar_position: 5
---

### 功能说明{#intro}

设置群组禁言后，当前群组所有成员将无法向群内发送消息，**Server API 发送消息不受群禁言影响**。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/groupmute/set

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|is_mute|int|是|0:未禁言；1:禁言；||

### 请求示例{#req_demo}
```js
POST /apigateway/groups/groupmute/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
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