---
title: Bind email
hide_title: true
sidebar_position: 10
---
### Function description{#intro}

Bind an email address using a verification code.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/bindemail

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description       |   |
|:----------|:----------|:---------|:------------------|---|
| email     | string    | yes      | Email address     |   |
| code      | string    | yes      | Verification code |   |


### Request Example{#req_demo}
``` js
POST /jim/users/bindemail HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "email": "test@abc.com",
  "code": "123456"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response code

| Response code | Description |   |
|:--------------|:------------|---|