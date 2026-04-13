---
title: Remove Chat Room Members from Whitelist
hide_title: true
sidebar_position: 2
---

### Function Description{#intro}

Removes members from the chat room whitelist.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/allowmembers/del

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter   | Data Type | Required | Description                      |   |
|:------------|:----------|:---------|:--------------------------------|:--|
| chat_id     | string    | Yes      | The ID of the chat room         |   |
| member_ids  | array     | Yes      | List of member IDs to remove from the chat room whitelist |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/allowmembers/del HTTP/1.1
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

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```