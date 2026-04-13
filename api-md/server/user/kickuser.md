---
title: Kick user offline
hide_title: true
sidebar_position: 11
---

### Function description{#intro}

Kick users offline who are currently connected to the IM service. Kicking users offline can be done by `Platform`, `Device`, or `User` dimensions. This interface only affects the current connection and does not impact the user's future connections. For example, if a user is logged in on multiple devices, the device that logs in later will kick the other devices offline.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/users/kick

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters  | Data type | Required | Description                                                                                      |   |
|:------------|:----------|:---------|:------------------------------------------------------------------------------------------------|---|
| user_id     | string    | Yes      | The ID of the user to be kicked offline                                                         |   |
| platforms   | array     | No       | Kick users based on the specified device types. This field is optional. If omitted, all devices will be kicked offline by default. |   |
| device_ids  | array     | No       | The unique identifiers of the devices to be kicked offline                                       |   |
| ext         | string    | No       | Extension field. This value will be returned to the business layer by the SDK when the user receives the kick notification and can be used for custom reminders or other purposes. |   |

### Request Example{#req_demo}
```js
GET /apigateway/users/kick HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "platforms": ["iOS", "Android"],
  "device_ids": ["xxxxx", "yyyyy"]
}
```

### Response example{#res_demo}
```json
{
  "code": 0,
  "message": "success"
}
```