---
title: 标记消息已读
hide_title: true
sidebar_position: 9
---

### 功能说明{#intro}

标记消息的已读状态。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/messages/markread

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|消息的已读用户id||
|target_id|string|是|该消息的会话id，单聊时为消息发送者id，群聊时为群id||
|channel_type|int|是|会话类型：1：单聊；2：群聊||
|msg_ids|array|是|要标记已读的消息id列表||

### 请求示例{#req_demo}
```js
POST /apigateway/messages/markread HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "target_id":"userid2",
  "channel_type":1,
  "msg_ids":["xxxxxxx","yyyyyyy"]
}
```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```