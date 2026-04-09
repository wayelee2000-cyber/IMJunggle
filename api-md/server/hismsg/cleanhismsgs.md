---
title: 清空历史消息
hide_title: true
sidebar_position: 3
---

### 功能说明{#intro}

按时间清空历史消息，支持清理指定用户自己一侧的消息和清空会话所有的消息，可通过 `clean_scope` 指定，清空消息指令会自动同步各端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/hismsgs/clean

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|否|单聊会话时，会话一方用户的 Id||
|target_id|string|是|单聊会话时，会话另一方用户的id；群聊会话时，群 Id||
|channel_type|int|是|会话类型，1:单聊；2:群聊||
|clean_time|int|是|单位：毫秒。要清理消息的起始时间戳，时间戳之前的消息都将被清理||
|clean_time_offset|int|否|单位：毫秒。当不指定 clean_time 时，服务端使用 当前时间 clean_time_offse 来计算清理时间||
|clean_scope|int|是|清理消息的范围，0: 代表只清理 fromid 视角的消息；1: 全视角清理，会话双方(或群里所有人)都将无法再查看消息；||
|sender_id|string|否| 如果指定sender_id，将只清理该会话中这个发送者，clean_time 之前的消息||


### 请求示例{#req_demo}
```js
POST /apigateway/hismsgs/clean HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id":"xxx",
  "target_id":"xxx",
  "channel_type":1,
  "clean_time":1569345643212,
  "clean_time_offset":0,
  "clean_scope":0,
  "sender_id":"user1"
}

```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```
