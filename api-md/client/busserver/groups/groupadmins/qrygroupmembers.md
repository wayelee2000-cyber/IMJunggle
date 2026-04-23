---
title: Query the list of group administrators
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Retrieve the list of group administrators.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/management/administrators/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| group_id  | string    | yes      | The group ID |  |


### Request Example{#req_demo}
``` js
GET /jim/groups/management/administrators/list?group_id=groupid1 HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "group_id": "group1",
    "items": [
      {
        "user_id": "userid1",
        "nickname": "user1",
        "avatar": "https://aaabbcc.png",
        "member_type": 0, // 0: Ordinary user; 1: Robot
        "role": 2         // 0: Group member; 1: Group owner; 2: Group administrator
      },
      {
        "user_id": "userid2",
        "nickname": "user2",
        "avatar": "https://aaabbcc.png",
        "member_type": 0, // 0: Ordinary user; 1: Robot
        "role": 2         // 0: Group member; 1: Group owner; 2: Group administrator
      }
    ],
    "offset": "xxx"
  }
}
```

### Response code

| Response code | Description |  |
|:--------------|:------------|:--|
