---
title: delete message
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Deleting messages by message ID supports both single-item and two-way deletion. The deletion operation is **automatically synchronized** across all devices of the current user.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/hismsgs/del

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters   | Data type | Required | Description                                                                                                         |   |
|:-------------|:----------|:---------|:--------------------------------------------------------------------------------------------------------------------|---|
| from_id      | string    | No       | In a single chat session, the ID of the user in the conversation.                                                  |   |
| target_id    | string    | Yes      | In a single chat session, the ID of the other user; in a group chat session, the group ID.                         |   |
| channel_type | int       | Yes      | Conversation type: 1 for single chat; 2 for group chat.                                                             |   |
| del_scope    | int       | No       | The scope of message deletion: 0 means deleting messages only from the perspective of `from_id`; 1 means deleting messages for all participants (both parties in a single chat or all members in a group) so that no one can view them. |   |
| msgs         | array     | Yes      | A list of message IDs to be deleted.                                                                                |   |

### Request Example{#req_demo}
```js
POST /apigateway/hismsgs/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id": "xxx",
  "target_id": "xxx",
  "channel_type": 1,
  "del_scope": 0,
  "msgs": [
    {
      "msg_id": "xxxxx"
    }
  ]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```