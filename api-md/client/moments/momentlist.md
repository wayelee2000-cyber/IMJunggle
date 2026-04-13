---
title: Moments list
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Retrieve the list of moments from the circle of friends.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/momentgateway/moments/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                                      |   |
|:-----------|:----------|:---------|:------------------------------------------------|---|
| start      | int       | No       | Start timestamp for incremental query, in milliseconds (13 digits) |
| limit      | int       | No       | Number of items per page, default is 20, maximum is 50 |
| order      | int       | No       | Query order: 0 for reverse order; 1 for forward order |
| user_id    | string    | No       | Retrieve moments posted by the specified user  |


### Request Example{#req_demo}
``` js
GET /momentgateway/moments/list?limit=20&start=1723456789123 HTTP/1.1
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
        "moment_id": "momentid1",
        "content": {
          "text": "xxxxxx",
          "medias": [
            {
              "type": "image",
              "url": "xxx",
              "snapshot_url": "xxxx",
              "height": 100,
              "width": 100
            },
            {
              "type": "video",
              "url": "xxxx",
              "snapshot_url": "xxxx",
              "duration": 10,
              "height": 100,
              "width": 100
            }
          ]
        },
        "user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx"
        },
        "reactions": [
          {
            "value": "val1",
            "timestamp": 17312345678,
            "user_info": {
              "user_id": "xxx",
              "nickname": "xxxxx",
              "avatar": "xxxx"
            }
          }
        ],
        "top_comments": [
          {
            "comment_id": "xxxx",
            "moment_id": "xxx",
            "parent_comment_id": "xxxx",
            "content": {
              "text": "xxxxx"
            },
            "parent_user_info": {
              "nickname": "xxxxx",
              "avatar": "xxxx",
              "user_type": 1
            },
            "user_info": {
              "nickname": "xxxxx",
              "avatar": "xxxx",
              "user_type": 1
            },
            "comment_time": 1732123456789
          }
        ],
        "moment_time": 1732123456789
      }
    ],
    "is_finished": true
  }
}
```