---
title: Remove ban from chat room member
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

Unban a member from a chat room.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/banmembers/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                     |   |
|:------------|:----------|:---------|:-------------------------------|---|
| chat_id     | string    | Yes      | The ID of the chat room         |   |
| member_ids  | array     | Yes      | List of banned chat room member IDs |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/banmembers/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id": "chatroom1",
  "member_ids": ["member1", "member2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```