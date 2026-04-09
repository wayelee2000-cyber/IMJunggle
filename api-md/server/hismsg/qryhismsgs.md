---
title: 查询历史消息
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

查询历史消息与客户端获取历史消息功能一致，用于开发者服务端查询指定人指定会话的历史消息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/hismsgs/query

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|否|单聊会话时，会话一方用户的id||
|target_id|string|是|单聊会话时，会话另一方用户的id；群聊会话时，群id||
|channel_type|int|是|会话类型，1:单聊；2:群聊||
|start|int|是|查询历史消息时的开始时间戳||
|count|int|否|分页查询，一页条数，默认20，最大不超过50||
|order|int|否|查询历史消息时的顺序，0:按时间倒序(默认)；1:按时间正序||


### 请求示例{#req_demo}
```js
GET /apigateway/hismsgs/query?from_id=xxx&target_id=xxx&channel_type=1&start=xxxx&count=xx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "msgs":[
      {
        "sender_id":"xxx",
        "receiver_id":"xxx",
        "channel_type":1,
        "msg_id":"xxxxx",
        "msg_time":1321122121223,
        "msg_type":"xxx",
        "msg_content":"xxxxxx"
      }
    ],
    "is_finished":false
  }
}
```