---
title: Get user information
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Retrieve user information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/info

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| user_id   | string    | yes      | User ID     |    |


### Request Example{#req_demo}
``` js
GET /jim/users/info?user_id=xxx HTTP/1.1
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
    "user_id": "userid1",
    "nickname": "user1",
    "avatar": "https://file.juggle.im/abcdfafsdaf.png",
    "phone": "xxxx",
    "status": 1,
    "is_friend": false,
    "settings": {
        "language": "zh_CN",
        "friend_verify_type": 1, // 0: No verification required; 1: Verification required; 2: Refuse friend requests;
        "grp_verify_type": 1,    // 0: No verification required; 2: Verification required; 3: Refuse group invitations;
        "undisturb": "{\"switch\":true,\"timezone\":\"shanghai\",\"rules\":[]}"
    }
  }
}
```