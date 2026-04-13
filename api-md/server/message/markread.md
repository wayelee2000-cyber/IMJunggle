---
title: Mark message as read
hide_title: true
sidebar_position: 9
---

### Function description{#intro}

Mark a message as read.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/messages/markread

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters   | Data type | Required | Description                                                                                   |  |
|:-------------|:----------|:---------|:----------------------------------------------------------------------------------------------|--|
| user_id      | string    | Yes      | The user ID of the user marking the message as read                                          |  |
| target_id    | string    | Yes      | The session ID of the message. This is the sender's user ID for one-on-one chats, or the group ID for group chats |  |
| channel_type | int       | Yes      | Conversation type: 1 for single chat; 2 for group chat                                       |  |
| msg_ids      | array     | Yes      | A list of message IDs to be marked as read                                                   |  |

### Request Example{#req_demo}
```js
POST /apigateway/messages/markread HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "target_id": "userid2",
  "channel_type": 1,
  "msg_ids": ["xxxxxxx", "yyyyyyy"]
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description |  |
|:-----------|:----------|:------------|--|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```