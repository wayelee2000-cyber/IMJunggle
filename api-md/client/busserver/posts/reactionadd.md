---
title: add likes
hide_title: true
sidebar_position: 21
---
### Function description{#intro}

Add a like to a post.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/posts/reactions/add

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /jim/posts/reactions/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "post_id": "post id",
  "key": "k1",
  "value": "v1"
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