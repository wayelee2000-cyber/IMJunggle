---
title: Query ban list
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

Retrieve the list of banned users with support for paginated queries.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request rate limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/users/banusers/query

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter | Data type | Required | Description           |   |
|:----------|:----------|:---------|:----------------------|---|
| limit    | int       | No       | Pagination parameter specifying the number of items per page |   |
| offset   | string    | No       | Offset value used for pagination |   |

### Request Example{#req_demo}

```js
GET /apigateway/users/banusers/query?limit=20&offset="" HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response parameters {#res_param}

| Parameter    | Data type | Description                              |   |
|:-------------|:----------|:---------------------------------------|---|
| user_id     | string    | ID of the banned user                   |   |
| created_time| number    | Timestamp when the ban was added        |   |
| end_time   | number    | Timestamp when the ban ends (in ms). A value of 0 indicates a permanent ban |   |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "user_id": "user1",
        "created_time": 1672233498000
      },
      {
        "user_id": "user2",
        "created_time": 1672233498000,
        "end_time": 1723455443563
      }
    ],
    "offset": "aabbcc"
  }
}
```