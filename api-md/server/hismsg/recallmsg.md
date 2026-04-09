---
title: 消息撤回
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

服务端消息撤回功能无撤回时间限制，开发者服务端可通过此接口在任意时间以任意人的身份撤回消息，撤回操作的指令自动同步至各端，同时支持在撤回指令中增加扩展信息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/hismsgs/recall

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|否|单聊会话时，会话一方用户的id||
|target_id|string|是|单聊会话时，会话另一方用户的id；群聊会话时，群id||
|channel_type|int|是|会话类型，1:单聊；2:群聊||
|msg_id|string|是|要撤回消息的id||
|msg_time|int|是| 要撤回消息的时间戳||
|exts|map|否|可携带扩展数据，用于端上定制化展示||


### 请求示例{#req_demo}
```js
POST /apigateway/hismsgs/recall HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id":"xxx",
  "target_id":"xxx",
  "channel_type":1,
  "msg_id":"xxxx",
  "msg_time":1569345643212,
  "exts":{
    "k1":"v1"
  }
}

```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```
