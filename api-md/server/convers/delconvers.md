---
title: Delete conversation
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

After a conversation is deleted, the IM server will automatically synchronize the deletion across all devices of the current user. Deleting the conversation **does not delete** the messages within the conversation.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/convers/del

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters   | Data type | Required | Description               |   |
|:-------------|:----------|:---------|:--------------------------|---|
| user_id      | string    | yes      | The user ID whose conversation is to be deleted |   |
| target_id    | string    | yes      | The conversation to be deleted |   |
| channel_type | int       | yes      | The type of conversation       |   |

### Request Example{#req_demo}
```js
POST /apigateway/convers/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "items": [
    {
      "target_id": "userid2",
      "channel_type": 1
    },
    {
      "target_id": "groupid1",
      "channel_type": 2
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

