---
title: 发送单聊消息
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

开发者在服务端模拟某个用户发送单聊私信消息，例如添加好友时，开发者服务端验证好友通过后，以某个用户的身份发送 `某某添加你为好友`

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/messages/private/send

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|sender_id|string|是|消息发送者id||
|target_ids|array|是|消息接收者id列表||
|msg_type|string|是|消息类型标识||
|msg_content|string|是|消息内容，建议json格式||
|push_data.push_text|string|否|指定推送的内容||
|push_data.push_extra|string|否|指定推送的自定义扩展，建议json字符串||
|is_storage|bool|否|设置该消息是否存储到历史消息里面，默认 true||
|is_count|bool|否|设置该消息是否记录未读数，默认true，记入未读数||
|is_notify_sender|bool|否|设置该消息是否通知消息的发送者，默认 true||
|is_state|bool|否|状态消息，该消息有极高的发送性能，但不保证可靠||
|life_time|int|否|消息的存活时间，单位到毫秒，0标识永久存活||
|life_time_after_read|int|否|消息阅读后的存活周期，单位到毫秒||

### 请求示例{#req_demo}
```js
POST /apigateway/messages/private/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id":"userid1",
  "target_ids":["userid2","userid3"],
  "msg_type":"jg:text",
  "msg_content":"{\"content\":\"aabbcc\"}",
  "push_data":{
    "push_text":"push content",
    "push_extra":"extra"
  },
  "is_storage":true,
  "is_notify_sender":true,
  "is_state":false
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
      "target_id":"userid2",
      "msg_id":"aaaaaaa"
    },
    {
      "target_id":"userid3",
      "msg_id":"bbbbbbb"
    }
  ]
}
```

