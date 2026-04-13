---
title: Bind Email - Send Email
hide_title: true
sidebar_position: 9
---
### Function Description{#intro}

Before binding an email, trigger the email verification code.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/bindemail/send

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| email    | string    | yes      | Email address |  |


### Request Example{#req_demo}
``` js
POST /jim/users/bindemail/send HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "email": "test@abc.com"
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

| Response Code | Description |  |
|:--------------|:------------|:--|