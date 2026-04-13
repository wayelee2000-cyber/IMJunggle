---
title: Add ban to chat room members
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Set chat room members to muted status. Muted members will be unable to send messages to the chat room.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/mutemembers/add

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters   | Data type | Required | Description                                      |  |
|:-------------|:----------|:---------|:------------------------------------------------|--|
| chat_id      | string    | Yes      | The ID of the chat room                          |  |
| member_ids   | array     | Yes      | List of chat room member IDs to be muted        |  |
| end_time     | number    | No       | Ban end time in milliseconds; 0 indicates a permanent ban |  |
| end_time_offset | number | No       | Unit: milliseconds. If `end_time` is not specified, the server calculates `end_time` as current time plus `end_time_offset` |  |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/mutemembers/add HTTP/1.1
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