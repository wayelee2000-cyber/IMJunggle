---
title: Single Chat Ban List
hide_title: true
sidebar_position: 8
---

### Function Description{#intro}

Query the list of users who are banned from single chat and private messages within the current application. Supports paginated queries.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/blockusers/query

> **Content-Type**: `application/json`

### Request Parameters {#param}

| Parameter   | Data Type | Required | Description                                  |
|:------------|:----------|:---------|:---------------------------------------------|
| user_id    | string    | Yes      | The user whose single chat ban list is queried |
| limit      | int       | No       | Pagination parameter specifying the number of items per page |
| offset     | string    | No       | Offset used for pagination                    |

### Request Example{#req_demo}
```js
GET /apigateway/users/blockusers/query?user_id=user1&limit=20&offset="" HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response Parameters {#res_param}

| Parameter      | Data Type | Description                  |
|:---------------|:----------|:-----------------------------|
| block_user_id  | array     | List of banned user IDs      |
| created_time   | number    | Timestamp when the ban was added |
| offset        | string    | Offset used for pagination    |

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "user_id": "user1",
    "items": [
      {
        "block_user_id": "user2",
        "created_time": 1672233498000 
      },
      {
        "block_user_id": "user3",
        "created_time": 1672233498000
      }
    ],
    "offset": "aaddcxx"
  }
}
```

