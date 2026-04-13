---
title: Add friend notes
hide_title: true
sidebar_position: 6
---

### Function description{#intro}

Add notes for a friend.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/setdisplayname

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter            | Data type | Required | Description          |   |
|:---------------------|:----------|:---------|:---------------------|---|
| friend_id            | string    | Yes      | Friend’s user ID     |   |
| friend_display_name  | string    | Yes      | Friend's note or remark |   |


### Request Example{#req_demo}
``` js
POST /jim/friends/setdisplayname HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "friend_id": "friend1",
  "friend_display_name": "displayname"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```