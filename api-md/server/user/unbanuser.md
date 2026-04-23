---
title: Unban user
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

Users can be reconnected after being unbanned. Users can be unbanned by `platform`, `device`, or `user` dimensions, allowing developers to flexibly control user permission verification.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/banusers/unban

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters | Data type | Required | Parameter description |  |
|:-----------|:----------|:---------|:----------------------|:--|
| user_id   | string    | Yes      | The user ID to be unbanned |  |
| scope_key | string    | No       | Specifies the scope of the unban. If omitted, all scopes are unbanned. Possible values: <br> - `default`: unban the user globally <br> - `platform`: unban the user on a specified platform <br> - `device`: unban the user on a specified device <br> - `ip`: unban the user on a specified IP address |  |


### Request Example{#req_demo}

```js
POST /apigateway/users/banusers/unban HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "items":[
    {
      "user_id":"user1",
      "scope_key":"default"
    },
    {
      "user_id":"user2"
    }
  ]
}
```
### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
