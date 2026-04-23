---
title: Set Ban on Single Chat
hide_title: true
sidebar_position: 6
---

### Function Description{#intro}

After banning individual chats, users will no longer be able to send private messages. However, sending group messages and chat room messages will remain unaffected. For example, if the developer platform detects that certain users frequently divert private messages or engage in illegal activities, the developer can disable those users' ability to send private messages.

### Request Description{#req}

> **Request Authentication**: This API requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/blockusers/block

> **Content-Type**: `application/json`

### Request Parameters {#param}

| Parameter       | Data Type | Required | Description                      |   |
|:----------------|:----------|:---------|:--------------------------------|---|
| user_id         | string    | Yes      | The user who sets the single chat ban |   |
| block_user_ids  | array     | Yes      | A list of users to be banned    |   |

### Request Example{#req_demo}
```js
POST /apigateway/users/blockusers/block HTTP/1.1
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

