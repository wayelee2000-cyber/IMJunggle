---
title: clear user label
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Delete user labels.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/usertags/clear

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
POST /apigateway/usertags/clear HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "user_ids": ["userid1", "userid2"]
}
```


### Request parameters {#param}

| Parameters | Data type | Required | Parameter description               |
|:-----------|:----------|:---------|:----------------------------------|
| user_ids  | array     | yes      | List of user IDs for which tags will be cleared |


### Response parameters {#res_param}

| Parameters | Data type | Parameter description |
|:-----------|:----------|:----------------------|


### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```