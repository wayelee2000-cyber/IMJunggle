---
title: Send chat room broadcast message
hide_title: true
sidebar_position: 7
---
### Function description{#intro}

Chat room broadcast messages allow you to send messages to all chat rooms currently active on the platform.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/messages/chatroom/broadcast

> **Content-Type**: `application/json`

### Request parameters {#param}
| Parameter   | Data type | Required | Description                     |
|:------------|:----------|:---------|:-------------------------------|
| sender_id   | string    | yes      | ID of the message sender       |
| msg_type    | string    | yes      | Message type identifier        |
| msg_content | string    | yes      | Message content; JSON format is recommended |

### Request Example{#req_demo}
```js
POST /apigateway/messages/chatroom/broadcast HTTP/1.1
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

### Response parameters {#res_param}

| Parameter | Data type | Description |
|:----------|:----------|:------------|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

