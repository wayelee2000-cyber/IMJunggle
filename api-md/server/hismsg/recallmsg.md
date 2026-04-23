---
title: Message withdrawal
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

The server-side message withdrawal function has no time limit for withdrawal. Developers can withdraw messages at any time and on behalf of any user through this interface. Withdrawal operation instructions are automatically synchronized to all clients. The interface also supports adding extended information to the withdrawal instructions.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/hismsgs/recall

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                                                                                  |   |
|:-------------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| from_id     | string    | No       | In a single chat conversation, the ID of the user in the conversation                            |   |
| target_id   | string    | Yes      | In a single chat conversation, the ID of the other user; in a group chat conversation, the group ID   |   |
| channel_type| int       | Yes      | Conversation type: 1 for single chat; 2 for group chat                                      |   |
| msg_id      | string    | Yes      | The ID of the message to be withdrawn                                                      |   |
| msg_time    | int       | Yes      | The timestamp of the message to be withdrawn                                               |   |
| exts        | map       | No       | Extended data for customized display on the client side                                    |   |

### Request Example{#req_demo}
```js
POST /apigateway/hismsgs/recall HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id": "xxx",
  "target_id": "xxx",
  "channel_type": 1,
  "msg_id": "xxxx",
  "msg_time": 1569345643212,
  "exts": {
    "k1": "v1"
  }
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

