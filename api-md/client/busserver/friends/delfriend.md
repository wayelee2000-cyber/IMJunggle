---
title: remove friend
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

Remove a friend.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                     |   |
|:------------|:----------|:---------|:-------------------------------|---|
| friend_ids  | array     | yes      | A list of user IDs to remove as friends |   |


### Request Example{#req_demo}
``` js
POST /jim/friends/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "friend_ids": ["userid1", "userid2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```