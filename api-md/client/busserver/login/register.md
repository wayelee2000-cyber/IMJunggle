---
title: Account registration
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Registration interface supporting account and password registration, mobile phone number registration, and email registration.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/register

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| account   | string    | No       | Account name. It is recommended to use a combination of letters and numbers, 5 to 20 characters in length. Note: choose one of account, phone, or email. |  |
| phone     | string    | No       | Mobile phone number. |  |
| email     | string    | No       | Email address. |  |
| code      | string    | No       | Required when registering with a mobile phone number or email address. The 6-digit verification code received. |  |
| password  | string    | Yes      | Account password. |  |


### Request Example{#req_demo}
``` js
POST /jim/register HTTP/1.1
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
  "msg": "success"
}
```
