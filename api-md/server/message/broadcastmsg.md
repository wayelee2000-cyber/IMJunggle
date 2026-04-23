---
title: Send broadcast message
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Broadcast a message to all registered users within the application.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/messages/broadcast/send

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters  | Data type | Required | Description                          |  |
|:------------|:----------|:---------|:-----------------------------------|:--|
| sender_id   | string    | yes      | ID of the message sender            |   |
| msg_type    | string    | yes      | Identifier for the message type     |   |
| msg_content | string    | yes      | Message content in JSON string format |   |

### Request Example{#req_demo}
```js
POST /apigateway/messages/broadcast/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id": "userid1",
  "msg_type": "text",
  "msg_content": "{\"content\":\"aabbcc\"}"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

