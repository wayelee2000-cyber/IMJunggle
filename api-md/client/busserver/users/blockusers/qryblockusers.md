---
title: Query Blacklist User List
hide_title: true
sidebar_position: 3
---
### Function Description{#intro}

Retrieve the list of users in the blacklist.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/users/blockusers/list

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| count    | int       | No       | Pagination parameter specifying the number of items per page. Default is 20. |  |
| offset   | string    | No       | Pagination offset. |  |


### Request Example{#req_demo}
``` js
GET /jim/users/blockusers/list?count=20&offset=xxx HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "user_id": "userid1",
        "nickname": "user1",
        "avatar": "https://aaabbcc.png"
      },
      {
        "user_id": "userid2",
        "nickname": "user2",
        "avatar": "https://aaabbcc.png"
      }
    ],
    "offset": "xxx"
  }
}
```

### Response Codes

| Response Code | Description |  |
|:--------------|:------------|:--|