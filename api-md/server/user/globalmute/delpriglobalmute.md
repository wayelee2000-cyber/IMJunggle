---
title: Delete Users Banned from Sending Private Chat Messages
hide_title: true
sidebar_position: 2
---

### Function Description{#intro}

Deletes users who are banned from sending private chat messages and responds to the private chat function.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/private/globalmutemembers/del

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter  | Data Type | Required | Description                                      |
|:-----------|:----------|:---------|:------------------------------------------------|
| user_ids  | array     | Yes      | List of user IDs banned from sending private chat messages |


### Request Example{#req_demo}
``` js
POST /apigateway/private/globalmutemembers/del HTTP/1.1
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