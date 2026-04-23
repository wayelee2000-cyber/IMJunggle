---
title: Delete Moments
hide_title: true
sidebar_position: 3
---
### Function Description{#intro}

Deletes Moments.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/momentgateway/moments/del

> **Content-Type**: `application/json`


### Request Parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "moment_ids": ["xxxxxxxx", "xxxxxx"]
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

| Response Code | Description |
|:-------------:|:------------|

