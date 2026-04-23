---
title: delete friend
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

Delete a friend.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/friends/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                     |   |
|:------------|:----------|:---------|:-------------------------------|---|
| user_id    | string    | yes      | The user's ID                  |   |
| friend_ids | array     | yes      | A list of user IDs to unfriend |   |


### Request Example{#req_demo}
``` js
POST /apigateway/friends/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "friend_ids": ["userid2", "userid3"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
