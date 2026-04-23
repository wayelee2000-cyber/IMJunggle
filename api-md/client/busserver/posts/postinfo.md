---
title: post information
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Retrieve post information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/posts/info

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| post_id   | string    | yes      | Post ID     |   |


### Request Example{#req_demo}
``` js
GET /jim/posts/info?post_id=xxxxxxx HTTP/1.1
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
    "post_id": "postid1",
    "content": {
      "text": "xxxxxx",
      "images": [
        {
          "url": "xxxx"
        }
      ],
      "video": {
        "url": "xxxxx"
      }
    },
    "user_info": {
      "user_id": "xxx",
      "nickname": "xxxxx",
      "avatar": "xxxx",
      "user_type": 1
    },
    "reactions": {
      "key1": [
        {
          "value": "val1",
          "user_info": {
            "user_id": "xxx",
            "nickname": "xxxxx",
            "avatar": "xxxx",
            "user_type": 1
          }
        }
      ]
    },
    "top_comments": [
      {
        "comment_id": "xxxx",
        "post_id": "xxx",
        "parent_comment_id": "xxxx",
        "text": "xxxx",
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
        "created_time": 1732123456789,
        "updated_time": 1732123456789
      }
    ],
    "created_time": 1732123456789,
    "updated_time": 1732123456789
  }
}
```
