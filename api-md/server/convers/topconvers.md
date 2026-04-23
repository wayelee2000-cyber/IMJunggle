---
title: Set top status
hide_title: true
sidebar_position: 7
---

### Function description{#intro}

Set pin state of a conversation.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/convers/top

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                  |   |
|:-------------|:----------|:---------|:----------------------------|---|
| user_id      | string    | Yes      | The user ID of the pinned conversation |   |
| target_id    | string    | Yes      | The conversation ID to pin        |   |
| channel_type | int       | Yes      | The type of conversation          |   |
| is_top      | bool      | Yes      | Whether the conversation is pinned to top |   |

### Request Example{#req_demo}
```js
POST /apigateway/convers/top HTTP/1.1
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
      "channel_type": 1,
      "is_top": true
    },
    {
      "target_id": "groupid1",
      "channel_type": 2,
      "is_top": false
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



