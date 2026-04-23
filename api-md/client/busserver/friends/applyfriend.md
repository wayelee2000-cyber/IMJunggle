---
title: Apply to Add Friends
hide_title: true
sidebar_position: 1
---
### Function Description{#intro}

Submit a request to add a friend.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/apply

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter  | Data Type | Required | Description                              |   |
|:-----------|:----------|:---------|:---------------------------------------|---|
| friend_id  | string    | Yes      | The user ID of the person to add as a friend |   |


### Request Example{#req_demo}
``` js
POST /jim/friends/apply HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "friend_id": "userid1"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response Codes

| Response Code | Description                                                      |   |
|:--------------|:-----------------------------------------------------------------|---|
| 17101         | The other party does not accept friend requests from anyone.    |   |
| 17102         | Duplicate friend request, or the other party is already your friend. |

