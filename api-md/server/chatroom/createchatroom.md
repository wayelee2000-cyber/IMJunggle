---
title: Create a chatroom
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Create a chatroom.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/chatrooms/create

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| chat_id    | string    | Yes      | The ID of the chatroom |  |
| chat_name  | string    | No       | Chatroom nickname |  |
| is_mute   | int       | No       | Whether to mute globally: 0 = no; 1 = yes; default is 0 |  |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/create HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id": "chatroom1",
  "chat_name": "chatroom1",
  "is_mute": 0
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
