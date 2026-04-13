---
title: add user label
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Add tags to users.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/usertags/add

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
POST /apigateway/usertags/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "user_tags":[
        {
            "user_id":"xxxxx",
            "tags":["aa","bb"]
        }
    ]
}
```

### Request parameters {#param}

| Parameters | Data type | Required | Parameter description           |
|:-----------|:----------|:---------|:-------------------------------|
| user_id    | string    | yes      | The user ID to which tags are added |
| tags       | string[]  | yes      | A list of tags to add           |

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