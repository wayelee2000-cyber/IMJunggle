---
title: Add users prohibited from sending single chat messages
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Set users to be prohibited from sending single chat messages.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/apigateway/private/globalmutemembers/add

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                                         |  |
|:-----------|:----------|:---------|:----------------------------------------------------|--|
| user_ids  | array     | yes      | List of user IDs to be prohibited from sending single chat messages |  |


### Request Example{#req_demo}
``` js
POST /apigateway/private/globalmutemembers/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_ids": ["user1", "user2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
