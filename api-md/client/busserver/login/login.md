---
title: login
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Login interface for authentication using account, mobile phone number, or email combined with a password.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/login

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| account   | string    | No       | Account identifier. It is recommended to use a combination of letters and numbers, 5 to 20 characters in length. Note: provide one of account, phone, or email. |  |
| phone     | string    | No       | Mobile phone number. |  |
| email     | string    | No       | Email address. |  |
| password  | string    | Yes      | Account password. |  |


### Request Example{#req_demo}
``` js
POST /jim/login HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "account": "username",
  "password": "xxxxxx"
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

- [Account password login](./passlogin.md)
- [SMS verification login](./smslogin.md)
- [Email login](./emaillogin.md)
- [Login QR code](./getloginqr.md)
- [Check scan status](./checkqr.md)
- [Confirm QR scan](./confirmqr.md)