---
title: upload token
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Retrieve a file upload token.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/file_cred

> **Content-Type**: `application/json`


### Request parameters {#param}
| Field name | Type | Description |
| --:|:----:|:------|
| file_type | int | 0: default; 1: picture; 2: voice; 3: video; 4: file; 5: log |
| ext | string | File extension |

### Request Example{#req_demo}
``` js
POST /jim/file_cred HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "file_type": 0,
  "ext": "jpg"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "oss_type": 0,
    "qiniu_resp": {
      "domain": "xxxxx",
      "token": "xxxxxxx"
    },
    "pre_sign_resp": {
      "url": "xxxxxx",
      "obj_key": "xxx",
      "policy": "policy",
      "sign_version": "xxx",
      "credential": "xxxx",
      "date": "xxx",
      "signature": "xxxx"
    }
  }
}
```

### Response parameters
| Field name | Type | Description |
| --:|:----:|:------|
| oss_type | int | 0: default; 1: qiniu; 2: aws s3; 3: minio; 4: oss |

### Response code

| Response code | Description | |
|:--|:---|:--|