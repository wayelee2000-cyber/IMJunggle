---
title: Unban Single Chat
hide_title: true
sidebar_position: 7
---

### Function Description{#intro}

Unblock users' ability to send private messages.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/blockusers/unblock

> **Content-Type**: `application/json`

### Request Parameters {#param}

| Parameters      | Data Type | Required | Description                        |   |
|:----------------|:----------|:---------|:---------------------------------|---|
| user_id         | string    | yes      | The user who set the single chat ban |   |
| block_user_ids  | array     | yes      | A list of users to be unblocked  |   |

### Request Example{#req_demo}

```js
POST /apigateway/users/blockusers/unblock HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "user1",
  "block_user_ids": ["user2", "user3"]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

