---
title: Login QR code
hide_title: true
sidebar_position: 7
---
### Function description{#intro}

Retrieve the QR code for login.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/login/qrcode

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description                      |   |
|:----------|:----------|:---------|:--------------------------------|---|
| email    | string    | yes      | Email address                   |   |
| code     | string    | yes      | Verification code received via email |   |


### Request Example{#req_demo}
``` js
GET /jim/login/qrcode HTTP/1.1
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
    "id": "QR code unique identifier",
    "qr_code": "base64 data of QR code image"
  }
}
```