---
title: Query user information
hide_title: true
sidebar_position: 10
---

### Function description{#intro}

Retrieve information for a single user to compare with the user data on the developer server. The developer server's user information takes precedence. After any changes to the developer server's user information, it must be synchronized promptly with the IM server.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/info

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters | Data type | Required | Description                          |  |
|:-----------|:----------|:---------|:-----------------------------------|:--|
| user_id    | string    | yes      | The user ID to query for single chat ban status |  |

### Request Example{#req_demo}
```js
GET /apigateway/users/info?user_id=user1 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response parameters {#res_param}

| Parameters   | Data type | Description          |  |
|:-------------|:----------|:---------------------|:--|
| user_id      | string    | User ID              |  |
| nickname     | string    | User nickname        |  |
| user_portrait| string    | User avatar URL      |  |
| ext_fields   | map       | Extended fields list |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "user_id": "user1",
    "nickname": "user1",
    "user_portrait": "xxxxx",
    "ext_fields": {
      "field1": "aaa",
      "field2": "bbb"
    }
  }
}
```
