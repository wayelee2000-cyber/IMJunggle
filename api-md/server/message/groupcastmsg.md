---
title: 发送群发消息
hide_title: true
sidebar_position: 4
---
### 功能说明{#intro}

群发消息功能，一次性向多个会话发送消息内容，群发消息不影响发送方的会话列表排序，影响接收方的会话列表排序，对于消息发送者，会单独记录群发消息历史，按target_id 汇聚，单独形成会话，此会话只包含发送方的消息。根据 `target_convers`，分别以 `sender_id` 身份向每个会话发送消息，支持 `单聊` 和 `群聊`。

:::danger 特殊限频
`target_convers` 支持多个会话，每个会话间隔发送时间为 `50ms`，会话越多发送耗时越长，返回时间越长
:::

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/messages/groupcast/send

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|sender_id|string|是|消息发送者id||
|target_id|string|否|群发目标id，id相同的群发历史消息会汇聚在一起，这个参数为空时，将不为发送者生成此会话||
|msg_type|string|是|消息类型标识||
|msg_content|string|是|消息内容，建议json格式||
|target_convers|array|是|群发的目标会话，支持单聊和群聊||
  
### 请求示例{#req_demo}
```js
POST /apigateway/messages/groupcast/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id":"userid1",
  "target_id":"groupcastid1",
  "msg_type":"text",
  "msg_content":"{\"content\":\"aabbcc\"}",
  "target_convers":[
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