---
title: Delete Moments
hide_title: true
sidebar_position: 3
---
### Function Description{#intro}

Delete Moments.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/momentgateway/moments/del

> **Content-Type**: `application/json`


### Request Parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"userid1",   // Moments belonging to this user
  "moment_ids":["xxxxxxxx","xxxxxx"]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response Codes

| Response Code | Description |  |
|:-------------:|:-----------:|:-:|

