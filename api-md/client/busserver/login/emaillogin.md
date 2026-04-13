---
title: Email login
hide_title: true
sidebar_position: 6
---
### Function description{#intro}

Log in using email and a verification code.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/email/login

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description                     |   |
|:----------|:----------|:---------|:-------------------------------|---|
| email    | string    | yes      | Email address                   |   |
| code     | string    | yes      | Verification code received via email |   |


### Request Example{#req_demo}
``` js
POST /jim/email/login HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "email":"xxxx@abc.com",
  "code":"000000"
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