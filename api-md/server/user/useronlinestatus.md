---
title: Check online status
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Query the online status of users in batches. This function is intended for the initial display of user status. To monitor users' online and offline status in real time, please use the [online and offline subscription](../subscription/onlineofflinesub.md) feature.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/onlinestatus/query

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters | Data type | Required | Description                              |
|:-----------|:----------|:---------|:---------------------------------------|
| user_ids  | array     | yes      | A list of user IDs whose online status you want to query |

### Request Example{#req_demo}

```js
POST /apigateway/users/onlinestatus/query HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_ids": ["userid1", "userid2"]
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description          |
|:-----------|:----------|:---------------------|
| user_id   | string    | User ID              |
| is_online | bool      | Indicates if the user is online |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "user_id": "user1",
        "is_online": true
      },
      {
        "user_id": "user2",
        "is_online": false
      }
    ]
  }
}
```
