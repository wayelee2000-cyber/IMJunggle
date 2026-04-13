---
title: Add Chat Room Member Whitelist
hide_title: true
sidebar_position: 1
---

### Function Description{#intro}

Set chat room members to a whitelist. When the chat room is globally banned, whitelist members can still send messages.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/allowmembers/add

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter    | Data Type | Required | Description                                                                 |  |
|:-------------|:----------|:---------|:----------------------------------------------------------------------------|--|
| chat_id      | string    | Yes      | The ID of the chat room                                                     |  |
| member_ids   | array     | Yes      | List of member IDs to be added to the chat room whitelist                   |  |
| end_time     | number    | No       | Ban end time in milliseconds. A value of 0 indicates a permanent ban       |  |
| end_time_offset | number | No       | Time offset in milliseconds. When `end_time` is not specified, the server calculates `end_time` as current time plus this offset |  |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/allowmembers/add HTTP/1.1
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