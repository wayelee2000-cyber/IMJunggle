---
title: add friend
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Add friends.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/friends/add

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters           | Data type | Required | Description           |   |
|:---------------------|:----------|:---------|:----------------------|---|
| user_id              | string    | yes      | User’s ID             |   |
| friends.friend_id    | string    | yes      | Friend’s user ID      |   |
| friends.display_name | string    | no       | Friend’s display name |   |


### Request Example{#req_demo}
``` js
POST /apigateway/friends/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "friends": [
    {
      "friend_id": "userid2",
      "display_name": "u2"
    },
    {
      "friend_id": "userid3",
      "display_name": "u3"
    }
  ]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```