---
title: Send chat room message
hide_title: true
sidebar_position: 6
---
### Function description{#intro}

Developers can send chat room messages on the server side, supporting various message types such as `text`, `picture`, `voice`, and others.

### Request description{#req}

> **Request Authentication**: This API requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/messages/chatroom/send

> **Content-Type**: `application/json`

### Request parameters {#param}
| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| sender_id  | string    | yes      | ID of the message sender |  |
| target_ids | array     | yes      | List of chat room IDs |  |
| msg_type   | string    | yes      | Message type identifier |  |
| msg_content| string    | yes      | Message content; JSON format is recommended |  |

### Request Example{#req_demo}
```js
POST /apigateway/messages/chatroom/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id": "userid1",
  "target_ids": ["chatroom1", "chatroom2"],
  "msg_type": "text",
  "msg_content": "{\"content\":\"aabbcc\"}"
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description |  |
|:-----------|:----------|:------------|:--|
| msg_id     | string    | Unique identifier of the message |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "target_id": "chatroom1",
      "msg_id": "aaaaaaa"
    },
    {
      "target_id": "chatroom2",
      "msg_id": "bbbbbbb"
    }
  ]
}
```

