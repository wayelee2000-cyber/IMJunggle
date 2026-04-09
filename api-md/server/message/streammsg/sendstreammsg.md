---
title: 发送流式消息
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

发送流式消息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/messages/private/stream/send

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|msg_id|string|否|首次调用留空，后续调用，传首次调用返回的msg_id||
|sender_id|string|是|消息发送者id||
|target_id|string|是|消息接收者id||
|partial_content|string|是|消息分片，文本格式||
|is_finished|bool|否|标识流式消息是否结束，默认 false||

### 请求示例{#req_demo}
```js
POST /apigateway/messages/private/stream/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "msg_id":"xxxxxx",   // 首次可以留空， 后续调用传第一个分片发送的返回值里面的 msg_id
  "from_id":"userid1",
  "target_id":"userid2",
  "partial_content":"content 1",
  "seq":1,
  "is_finished":false
}
```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|msg_id|string|消息的唯一标识||

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "msg_id":"xxxx",
    "msg_time":1722212323123
  }
}
```

