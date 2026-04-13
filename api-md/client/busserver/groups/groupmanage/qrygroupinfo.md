---
title: Query group information
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Retrieve group information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/info

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| group_id  | string    | yes      | Group ID    |  |


### Request Example{#req_demo}
``` js
GET /jim/groups/info?group_id=groupid1 HTTP/1.1
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
    "group_id": "groupid1",
    "group_name": "group1",
    "group_portrait": "https://aaaa.png",
    "member_count": 10,
    "members": [
      {
        "user_id": "userid1",
        "nickname": "user1",
        "avatar": "https://aaabbcc.png",
        "member_type": 0, // 0: Ordinary user; 1: Robot
        "role": 0        // 0: Group member; 1: Group owner; 2: Group administrator
      },
      {
        "user_id": "userid2",
        "nickname": "user2",
        "avatar": "https://aaabbcc.png",
        "member_type": 0, // 0: Ordinary user; 1: Robot
        "role": 0        // 0: Group member; 1: Group owner; 2: Group administrator
      }
    ],
    "owner": {
      "user_id": "userid1",
      "nickname": "user1",
      "avatar": "https://aaabbcc.png"
    },
    "my_role": 0, // My role in this group: 0 - Ordinary member; 1 - Group owner; 2 - Group administrator
    "group_management": {
      "group_mute": 0,        // Whether group mute is enabled
      "max_admin_count": 10,  // Maximum number of group administrators
      "admin_count": 2,       // Current number of administrators
      "group_verify_type": 0  // 0: [Description missing]
    },
    "grp_display_name": "grp1" // My group nickname
  }
}
```

### Response code

| Response code | Description |  |
|:--------------|:------------|:--|