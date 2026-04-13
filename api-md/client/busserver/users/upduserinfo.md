---
title: Update user information
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Update a user's basic information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/update

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| user_id   | string    | yes      | User ID     |  |
| nickname  | string    | no       | Nickname   |  |
| avatar    | string    | no       | Avatar URL |  |


### Request Example{#req_demo}
``` js
POST /jim/users/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id": "userid1",
  "nickname": "user1",
  "avatar": "xxxxxx"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response code

| Response code | Description |  |
|:--------------|:------------|:--|