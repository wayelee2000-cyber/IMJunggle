---
title: Clean up unread
hide_title: true
sidebar_position: 6
---

### Function description{#intro}

Clears unread conversations.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/convers/clearunread

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                  |   |
|:-------------|:----------|:---------|:----------------------------|---|
| user_id     | string    | yes      | The user ID for which to clear conversations |   |
| target_id   | string    | yes      | The conversation to be cleared    |   |
| channel_type| int       | yes      | The type of conversation          |   |

### Request Example{#req_demo}
```js
POST /apigateway/convers/clearunread HTTP/1.1
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


