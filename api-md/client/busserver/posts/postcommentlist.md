---
title: Comment list
hide_title: true
sidebar_position: 14
---
### Function description{#intro}

Retrieve the list of comments for a post.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/posts/comments/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter         | Data type | Required | Description                                      |   |
|:------------------|:----------|:---------|:------------------------------------------------|---|
| post_id           | string    | Yes      | The ID of the post                              |   |
| start             | int       | No       | Start timestamp for incremental query, in milliseconds (13 digits) |   |
| limit             | int       | No       | Number of items per page, default is 20, maximum is 50 |   |
| order             | int       | No       | Query order: 0 for reverse order; 1 for forward order |   |


### Request Example{#req_demo}
``` js
GET /jim/posts/comments/list?limit=20&start=1723456789123 HTTP/1.1
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
        "post_id": "postid1",
        "parent_comment_id": "xxx",
        "parent_user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx",
          "user_type": 0
        },
        "text": "xxxxxxxx",
        "user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx",
          "user_type": 0
        },
        "created_time": 1732123456789,
        "updated_time": 1732123456789
      }
    ],
    "is_finished": true
  }
}
```