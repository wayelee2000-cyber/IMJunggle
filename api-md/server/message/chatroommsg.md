---
title: 发送聊天室消息
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

开发者在服务端发送聊天室消息，支持发送普通`文本`、`图片`、`语音` 等消息类型。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/messages/chatroom/send

> **Content-Type**：`application/json`

### 请求参数{#param}
|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|sender_id|string|是|消息发送者id||
|target_ids|array|是|聊天室id列表||
|msg_type|string|是|消息类型标识||
|msg_content|string|是|消息内容，建议json格式||

### 请求示例{#req_demo}
```js
POST /apigateway/messages/chatroom/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id":"userid1",
  "target_ids":["chatroom1","chatroom2"],
  "msg_type":"text",
  "msg_content":"{\"content\":\"aabbcc\"}"
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
  "data":[
    {
      "target_id":"chatroom1",
      "msg_id":"aaaaaaa"
    },
    {
      "target_id":"chatroom2",
      "msg_id":"bbbbbbb"
    }
  ]
}
```
