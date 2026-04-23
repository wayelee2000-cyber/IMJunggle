---
title: Like list
hide_title: true
sidebar_position: 23
---
### Function description{#intro}

Retrieve the list of likes for a post.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/posts/reactions/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description          |   |
|:----------|:----------|:---------|:---------------------|---|
| post_id  | string    | Yes      | The ID of the post.  |   |


### Request Example{#req_demo}
``` js
GET /jim/posts/reactions/list?post_id=xxx HTTP/1.1
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
        "key": "k1",
        "value": "v1",
        "timestamp": 1732123456789,
        "user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx",
          "user_type": 0
        }
      }
    ]
  }
}
```
