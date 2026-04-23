---
title: friends list
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

My friends list, sorted alphabetically by default.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                          |   |
|:-----------|:----------|:---------|:-----------------------------------|---|
| page       | int       | No       | Used for pagination; starting page number, beginning at 1 |   |
| size       | int       | No       | Number of items per page; default is 20, maximum is 50   |   |
| order_tag  | string    | No       | Starting Pinyin letter to filter results                   |   |


### Request Example{#req_demo}
``` js
GET /jim/friends/list?size=50&page=1&order_tag=a HTTP/1.1
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
    "items": [
      {
        "user_id": "userid1",
        "nickname": "user1",
        "avatar": "https://file.juggle.im/abcdfafsdaf.png",
        "pinyin": "u",
        "friend_info": {
          "is_friend": true,
          "display_name": "displayname"
        }
      },
      {
        "user_id": "userid2",
        "nickname": "user2",
        "avatar": "https://file.juggle.im/abcdfafsdaf.png",
        "pinyin": "u",
        "friend_info": {
          "is_friend": true,
          "display_name": "displayname"
        }
      }
    ]
  }
}
```
