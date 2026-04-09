---
title: 删除会话
hide_title: true
sidebar_position: 3
---

### 功能说明{#intro}

会话删除后，IM 服务端会将删除操作自动同步至当前用户各端，删除会话 **不会删除** 会话中的消息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/convers/del

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|删除会话的用户id||
|target_id|string|是|要删除的会话||
|channel_type|int|是|会话的类型||


### 请求示例{#req_demo}
```js
POST /apigateway/convers/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "items":[
    {
      "target_id":"userid2",
      "channel_type":1
    },
    {
      "target_id":"groupid1",
      "channel_type":2
    }
  ]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```