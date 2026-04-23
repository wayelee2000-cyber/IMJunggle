---
title: Add Users Prohibited from Sending Group Chat Messages
hide_title: true
sidebar_position: 4
---

### Function Description{#intro}

Set users who are prohibited from sending group chat messages.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/apigateway/group/globalmutemembers/add

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter  | Data Type | Required | Description                                      |   |
|:-----------|:----------|:---------|:------------------------------------------------|---|
| user_ids  | array     | yes      | List of user IDs to be prohibited from sending group chat messages |   |


### Request Example{#req_demo}
``` js
POST /apigateway/group/globalmutemembers/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_ids": ["user1", "user2"]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

