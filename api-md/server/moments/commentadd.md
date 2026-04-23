---
title: Post a comment
hide_title: true
sidebar_position: 11
---
### Function description{#intro}

Post a comment on Moments.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/momentgateway/moments/comments/add

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/comments/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id": "userid1",   // Post as this user
  "moment_id": "moment circle id",
  "parent_comment_id": "ID of parent comment",
  "content": {
    "text": "Comment content"
  }
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "comment_id": "xxx",
    "comment_time": 17212345678,
    "user_info": {
      "user_id": "xxx",
      "nickname": "xxxxx",
      "avatar": "xxxx"
    }
  }
}
```

### Response code

| Response code | Description |  |
|:-------------:|:-----------:|:-:|
