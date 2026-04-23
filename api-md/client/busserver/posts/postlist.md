---
title: Post list
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Query the list of posts.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/posts/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| start     | int       | No       | Start timestamp for incremental post queries, in milliseconds (13 digits) |  |
| limit     | int       | No       | Number of posts per page, default is 20, maximum is 50 |  |
| order     | int       | No       | Query order: 0 for reverse order; 1 for forward order |  |


### Request Example{#req_demo}
``` js
GET /jim/posts/list?limit=20&start=1723456789123 HTTP/1.1
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
    ],
    "is_finished": true
  }
}
```
