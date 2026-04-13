---
title: SMS verification code
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Send an SMS verification code.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/sms/send

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description         |   |
|:----------|:----------|:---------|:--------------------|---|
| phone     | string    | yes      | Mobile phone number |   |


### Request Example{#req_demo}
``` js
POST /jim/sms/send HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone": "15212345678"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```