---
title: Clean up unread
hide_title: true
sidebar_position: 6
---

### Function description{#intro}

Clears unread sessions.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/convers/clearunread

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                  |   |
|:-------------|:----------|:---------|:----------------------------|---|
| user_id     | string    | yes      | The user ID for which to clear sessions |   |
| target_id   | string    | yes      | The session to be cleared    |   |
| channel_type| int       | yes      | The type of session          |   |

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