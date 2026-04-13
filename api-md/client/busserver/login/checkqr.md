---
title: Check scan code status
hide_title: true
sidebar_position: 8
---
### Function description{#intro}

Check whether the QR code has been scanned.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/qrcode/check

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Parameter description |  |
|:-----------|:----------|:---------|:----------------------|:--|
| id         | string    | yes      | The QR code ID to be checked. It is recommended to check every 3 seconds. If the code is successfully scanned, the login information will be returned. | |


### Request Example{#req_demo}
``` js
POST /jim/qrcode/check HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "id":"xxxxxxx"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "user_id": "userid1",
    "authorization": "xxxxxxxxx",
    "nickname": "user1",
    "avatar": "xxxxxxxx",
    "status": 0,
    "im_token": "xxxxxxxxx"
  }
}
```
### Response code

| Response code | Description                          |  |
|:--------------|:-----------------------------------|:--|
| 17006         | The code has not been scanned yet; continue checking. | |
| 17007         | The QR code has expired.            | |