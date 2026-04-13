---
title: Email Verification Code
hide_title: true
sidebar_position: 5
---
### Function Description{#intro}

Send an email verification code.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/email/send

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description          |   |
|:----------|:----------|:---------|:---------------------|---|
| email     | string    | yes      | Email address        |   |


### Request Example{#req_demo}
``` js
POST /jim/email/send HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "email": "xxxxx@abc.com"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```