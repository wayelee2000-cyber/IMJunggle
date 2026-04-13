---
title: Bind Mobile Phone Number - Send SMS
hide_title: true
sidebar_position: 7
---
### Function Description{#intro}

Trigger the SMS verification code before binding the mobile phone number.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/bindphone/send

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description        |   |
|:----------|:----------|:---------|:-------------------|---|
| phone     | string    | yes      | Mobile phone number |   |


### Request Example{#req_demo}
``` js
POST /jim/users/bindphone/send HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone": "13812345678"
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