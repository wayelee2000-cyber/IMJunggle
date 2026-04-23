---
title: Query historical messages
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

The function for querying historical messages aligns with the client's capability to retrieve past messages. It is used by the developer's server to fetch historical messages from the conversation specified by the given user.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/hismsgs/query

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters   | Data type | Required | Description                                                                                  |   |
|:-------------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| from_id      | string    | No       | In a single chat conversation, the ID of the user in the conversation                            |   |
| target_id    | string    | Yes      | In a single chat conversation, the ID of the other user; in a group chat conversation, the group ID   |   |
| channel_type | int       | Yes      | Conversation type: 1 for single chat; 2 for group chat                                     |   |
| start        | int       | Yes      | The start timestamp for querying historical messages                                       |   |
| count        | int       | No       | Number of items per page for pagination; default is 20, maximum is 50                       |   |
| order        | int       | No       | Order of messages: 0 for reverse chronological (default); 1 for chronological              |   |

### Request Example{#req_demo}
```js
GET /apigateway/hismsgs/query?from_id=xxx&target_id=xxx&channel_type=1&start=xxxx&count=xx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "msgs": [
      {
        "sender_id": "xxx",
        "receiver_id": "xxx",
        "channel_type": 1,
        "msg_id": "xxxxx",
        "msg_time": 1321122121223,
        "msg_type": "xxx",
        "msg_content": "xxxxxx"
      }
    ],
    "is_finished": false
  }
}
```

