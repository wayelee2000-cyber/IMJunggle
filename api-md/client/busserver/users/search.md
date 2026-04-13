---
title: Search user
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Search for users based on their mobile phone number.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/search

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description                                      |   |
|:----------|:----------|:---------|:------------------------------------------------|---|
| keyword   | string    | yes      | The other party’s mobile phone number, email address, or account number |   |


### Request Example{#req_demo}
``` js
POST /jim/users/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "keyword": "13812345678"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "user_id": "userid1",
        "nickname": "user1",
        "avatar": "xxxxxxx",
        "is_friend": false
      }
    ]
  }
}
```

### Response code

| Response code | Description |   |
|:--------------|:------------|---|