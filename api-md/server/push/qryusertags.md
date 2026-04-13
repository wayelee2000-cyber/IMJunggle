---
title: clear user label
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Delete user labels

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/usertags/query

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
GET /apigateway/usertags/query?user_ids=userid1,userid2 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| user_id    | array     | yes      | The user IDs to query user tags for. For multiple users, use: `user_id=userid1&user_id=userid2` |  |

### Response parameters {#res_param}

| Parameters | Data type | Description |  |
|:-----------|:----------|:------------|:--|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "user_tags": [
      {
        "user_id": "userid1",
        "tags": ["aa", "bb"]
      },
      {
        "user_id": "userid2",
        "tags": ["aa", "bb"]
      }
    ]
  }
}
```