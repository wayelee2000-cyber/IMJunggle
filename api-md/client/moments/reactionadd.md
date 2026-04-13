---
title: add likes
hide_title: true
sidebar_position: 21
---
### Function description{#intro}

Like a post

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/momentgateway/moments/reactions/add

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/reactions/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "moment_id": "post id",
  "reaction": {
    "key": "k1",
    "value": "v1"
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
|:-------------|:------------|:--|