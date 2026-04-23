---
title: Scan Code to Confirm
hide_title: true
sidebar_position: 9
---
### Function Description{#intro}

Scan the QR code with your mobile phone and confirm your authorization to log in.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/qrcode/confirm

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description                      |   |
|:----------|:----------|:---------|:--------------------------------|---|
| id        | string    | yes      | The QR code ID obtained from scanning the code |   |


### Request Example{#req_demo}
``` js
POST /jim/qrcode/confirm HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "id": "xxxxxxx"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

