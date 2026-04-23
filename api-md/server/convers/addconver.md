---
title: add conversation
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

Adds a conversation to indicate that the user has inserted a conversation. For example, when searching for friends, a friend may be selected without sending a message. In this case, the conversation list should display the searched conversations at the latest position. The added conversation will be automatically synchronized across multiple devices.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/convers/add

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                      |   |
|:-------------|:----------|:---------|:--------------------------------|---|
| user_id      | string    | yes      | The user ID to add the conversation  |   |
| target_id    | string    | yes      | The ID of the other party to add the conversation |   |
| channel_type | int       | yes      | The type of conversation             |   |

### Request Example{#req_demo}
```js
POST /apigateway/convers/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "target_id": "userid2",
  "channel_type": 1
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

