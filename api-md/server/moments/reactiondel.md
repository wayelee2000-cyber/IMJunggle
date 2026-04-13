---
title: Remove likes
hide_title: true
sidebar_position: 22
---
### Function description{#intro}

Remove likes from a moment.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/momentgateway/moments/reactions/del

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/reactions/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"userid1",   // The user performing the action
  "moment_id":"momentid1",
  "reaction":{
    "key":"k1"
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