---
title: Update comment
hide_title: true
sidebar_position: 12
---
### Function description{#intro}

Update a comment.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/momentgateway/moments/comments/update

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/comments/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "comment_id": "post id",
  "content": {
    "text": "Comment content"
  }
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response code

| Response code | Description |  |
|:-------------:|:-----------:|:-:|