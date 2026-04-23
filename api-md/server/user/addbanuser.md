---
title: Ban user
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

Once a user is banned, they cannot establish a connection with the IM Server. The client connection will return the user [Banned](../status.md#connection) status code. If a user who is already connected is banned, the current connection will remain unaffected.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/banusers/ban

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter     | Data type | Required | Description                                                                                              |   |
|:--------------|:----------|:---------|:-----------------------------------------------------------------------------------------------------|---|
| user_ids     | array     | Yes      | A list of user IDs to be banned.                                                                       |   |
| end_time     | number    | No       | The timestamp (in milliseconds) when the ban ends. A value of 0 indicates a permanent ban.            |   |
| end_time_offset | number  | No       | Duration in milliseconds. If `end_time` is not specified, the server calculates `end_time` as the current time plus this offset. |   |
| scope_key    | string    | Yes      | The scope of the ban. Options include: `default` (ban the user), `platform` (ban specified platforms), `device` (ban specified devices), `ip` (ban specified IPs). |   |
| scope_value  | string    | No       | Used with `scope_key`. For example, if `scope_key` is `platform`, `scope_value` specifies the platforms to ban (multiple values separated by commas). |   |
| ext          | string    | No       | Additional information included with the ban, which can be used for custom ban messages. Limited to 100 bytes. |   |

### Request Example{#req_demo}
```js
POST /apigateway/users/banusers/ban HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "items":[
    {
      "user_id":"user1",
      "scope_key":"default",
      "scope_value":"xx",
      "ext":"aabbcc"
    },
    {
      "user_id":"user2",
      "end_time":1715846960362,
      "scope_key":"device",
      "scope_value":"xxxxxxxx,yyyyyyy",
      "ext":"aabbcc"
    },
    {
      "user_id":"user2",
      "end_time_offset":300000,
      "scope_key":"platform",
      "scope_value":"iOS,Android",
      "ext":"aabbcc"
    },
    {
      "user_id":"user4",
      "scope_key":"ip",
      "scope_value":"127.0.0.1,172.20.30.12",
      "ext":"aabbcc"
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
