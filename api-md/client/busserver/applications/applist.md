---
title: application list
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Retrieve the list of applications available in the workbench.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/applications/list

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
GET /jim/applications/list?page=1&size=20&order=0 HTTP/1.1
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
        "app_id": "xxx",
        "app_name": "xxx",
        "app_icon": "xxxx",
        "app_desc": "xxxx",
        "app_url": "https://abc.aab.com",
        "app_order": 1,
        "created_time": 1721234567890,
        "updated_time": 1721234567890
      }
    ],
    "page": 1,
    "size": 20
  }
}
```

### Response code

| Response code | Description |  |
|:-------------:|:-----------:|:--|

