---
title: Clear Historical Messages
hide_title: true
sidebar_position: 3
---

### Function Description{#intro}

Clearing historical messages by time supports deleting messages either on the specified user's side or for the entire session. This behavior can be controlled through the `clean_scope` parameter. The clear message command will automatically synchronize across all endpoints.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/hismsgs/clean

> **Content-Type**: `application/json`

### Request Parameters {#param}

| Parameter          | Data Type | Required | Description                                                                                                                      |   |
|:-------------------|:----------|:---------|:---------------------------------------------------------------------------------------------------------------------------------|---|
| from_id            | string    | No       | In a single chat session, the ID of the user initiating the conversation.                                                       |   |
| target_id          | string    | Yes      | In a single chat session, the ID of the other user; in a group chat session, the group ID.                                       |   |
| channel_type       | int       | Yes      | Conversation type: 1 for single chat; 2 for group chat.                                                                          |   |
| clean_time         | int       | Yes      | Timestamp in milliseconds indicating the starting point for clearing messages; messages before this timestamp will be deleted.  |   |
| clean_time_offset  | int       | No       | Offset in milliseconds used to calculate the cleanup time when `clean_time` is not specified; the server uses the current time. |   |
| clean_scope        | int       | Yes      | Scope of message clearing: 0 means only clearing messages from the `from_id` perspective; 1 means clearing messages for all parties in the conversation (or all group members), making the messages no longer visible to anyone. |   |
| sender_id          | string    | No       | If specified, only messages from this sender in the session before `clean_time` will be cleared.                                |   |

### Request Example{#req_demo}
```js
POST /apigateway/hismsgs/clean HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id": "xxx",
  "target_id": "xxx",
  "channel_type": 1,
  "clean_time": 1569345643212,
  "clean_time_offset": 0,
  "clean_scope": 0,
  "sender_id": "user1"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```