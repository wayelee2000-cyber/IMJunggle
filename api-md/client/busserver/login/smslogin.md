---
title: Short verification login
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Log in using a mobile phone number and SMS verification code.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/sms/login

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Description               |   |
|:-----------|:----------|:---------|:--------------------------|---|
| phone      | string    | yes      | Mobile phone number       |   |
| code       | string    | yes      | Received SMS verification code |   |


### Request Example{#req_demo}
``` js
POST /jim/sms/login HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone": "15212345678",
  "code": "000000"
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
