---
title: Query friends list
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

Retrieve the list of friends.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/friends/query

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                                  |   |
|:-----------|:----------|:---------|:---------------------------------------------|---|
| user_id   | string    | Yes      | User’s ID                                   |   |
| order     | int       | No       | Sorting order of the friend list: 0 for descending; 1 for ascending |   |
| limit     | int       | No       | Number of friends to retrieve per request, default is 100 |   |
| offset    | string    | No       | Pagination offset                            |   |


### Request Example{#req_demo}
``` js
GET /apigateway/friends/query?user_id=userid1&limit=100 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "friend_id": "userid2",
        "display_name": "xxx"
      }
    ],
    "offset": "xxxx"
  }
}
```