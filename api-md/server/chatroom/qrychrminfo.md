---
title: Query chat room information
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

Retrieve the basic information of a chat room, including the chat room's nickname, attribute list, number of members, and some member details.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/chatrooms/info

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| chat_id    | string    | Yes      | The ID of the chat room |  |
| order      | int       | No       | Sorting order of chat room members: 0 for descending order; 1 for ascending order |  |
| count      | int       | No       | Number of chat room members to query; default is 100 |  |


### Request Example{#req_demo}
``` js
GET /apigateway/chatrooms/info?chat_id=xxx&order=0&count=100 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "chat_id": "xxx",
    "chat_name": "xxx",
    "is_mute": false,
    "member_count": 10000,
    "members": [
      {
        "member_id": "xxx",
        "member_name": "xxx",
        "added_time": 172987634564
      }
    ],
    "atts": [
      {
        "key": "k1",
        "value": "v1",
        "att_time": 172345678345,
        "user_id": "userid1"
      }
    ]
  }
}
```