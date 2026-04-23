---
title: Bind Mobile Phone Number
hide_title: true
sidebar_position: 8
---
### Function Description{#intro}

Bind a mobile phone number using an SMS verification code.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/bindphone

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description         |   |
|:----------|:----------|:---------|:--------------------|---|
| phone     | string    | yes      | Mobile phone number |   |
| code      | string    | yes      | Verification code   |   |


### Request Example{#req_demo}
``` js
POST /jim/users/bindphone HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone": "13812345678",
  "code": "123456"
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

| Response Code | Description |   |
|:--------------|:------------|---|

