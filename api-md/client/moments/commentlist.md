---
title: Comment list
hide_title: true
sidebar_position: 14
---
### Function description{#intro}

Retrieve a list of comments.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/momentgateway/moments/comments/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter       | Data type | Required | Description                                  |   |
|:----------------|:----------|:---------|:---------------------------------------------|---|
| moment_id       | string    | Yes      | The ID of the moment (circle of friends)    |   |
| start           | int       | No       | Start timestamp for incremental query, in milliseconds (13 digits) |   |
| limit           | int       | No       | Number of items per page, default is 20, maximum is 50 |   |
| order           | int       | No       | Query order: 0 for reverse order; 1 for forward order |   |


### Request Example{#req_demo}
``` js
GET /momentgateway/moments/comments/list?moment_id=xxx&limit=20&start=1723456789123 HTTP/1.1
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
        "comment_id": "commentid1",
        "moment_id": "momentid1",
        "parent_comment_id": "xxx",
        "parent_user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx"
        },
        "content": {
          "text": "xxxxxxxx"
        },
        "user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx",
          "user_type": 0
        },
        "comment_time": 1732123456789
      }
    ],
    "is_finished": true
  }
}
```
