---
title: Destroy chat room
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

Destroys a chat room.  
:::danger
Once the chat room is destroyed, all members and attributes associated with the chat room will be permanently removed.
:::

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/chatrooms/destroy

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description          |   |
|:----------|:----------|:---------|:---------------------|---|
| chat_id   | string    | Yes      | The ID of the chat room |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/destroy HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id": "chatroom1"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```