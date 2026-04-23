---
title: update password
hide_title: true
sidebar_position: 6
---
### Function description{#intro}

Update the login password.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/updpass

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter    | Data type | Required | Description                              |   |
|:-------------|:----------|:---------|:---------------------------------------|---|
| user_id     | string    | yes      | User ID                                |   |
| password   | string    | yes      | Old password (note: hashing is required) |   |
| new_password | string    | yes      | New password (note: hashing is required) |   |


### Request Example{#req_demo}
``` js
POST /jim/users/updpass HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id": "xxxxxxx",
  "password": "xxxxxx",
  "new_password": "xxxxx"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
