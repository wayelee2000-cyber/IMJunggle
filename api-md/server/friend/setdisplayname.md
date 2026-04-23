---
title: Set the Friend's Note Name
hide_title: true
sidebar_position: 4
---

### Function Description{#intro}

Set a custom display name (note) for a friend.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/friends/setdisplayname

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter    | Data Type | Required | Description           |  |
|:-------------|:----------|:---------|:----------------------|--|
| user_id     | string    | yes      | User's ID             |  |
| friend_id   | string    | yes      | Friend's user ID      |  |
| display_name| string    | yes      | Friend's custom note name |  |


### Request Example{#req_demo}
``` js
POST /apigateway/friends/setdisplayname HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "friend_id": "userid2",
  "display_name": "u2"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

