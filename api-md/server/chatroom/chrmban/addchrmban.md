---
title: Add chat room member ban
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Set chat room members to banned status. Banned members will be removed from the chat room and prevented from re-entering.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/banmembers/add

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter     | Data type | Required | Description                                                                 |  |
|:--------------|:----------|:---------|:----------------------------------------------------------------------------|--|
| chat_id       | string    | Yes      | The ID of the chat room                                                     |  |
| member_ids    | array     | Yes      | List of chat room member IDs to be banned                                  |  |
| end_time      | number    | No       | Ban expiration time in milliseconds. A value of 0 indicates a permanent ban |  |
| end_time_offset | number  | No       | Duration in milliseconds. If `end_time` is not specified, the server calculates `end_time` as current time plus `end_time_offset` |  |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/banmembers/add HTTP/1.1
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