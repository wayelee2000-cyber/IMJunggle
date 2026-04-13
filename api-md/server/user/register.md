---
title: registered user
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

User registration obtains a token for the client (Android, iOS, Web) to connect to the IM Server. By default, the token is permanently valid, but the application management can set a token validity period.  
Once the token is successfully obtained, it can be cached on the developer's business server and returned directly when the user logs in, reducing the number of network requests.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please see [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/users/register

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter      | Data type | Required | Description                                                                 |  |
|----------------|-----------|----------|-----------------------------------------------------------------------------|--|
| user_id        | string    | Yes      | User ID, no longer than 64 characters                                       |  |
| nickname       | string    | No       | User nickname. If empty, the client may display the nickname abnormally     |  |
| user_portrait  | string    | No       | User avatar URL. If empty, the client may display the avatar abnormally     |  |
| ext_fields     | map       | No       | Extended user information fields in key-value format                        |  |
| permit_convers | array     | No       | Permission control field that restricts the token to access specified sessions and limits the maximum number of historical messages retrievable per session |  |

### Request Example{#req_demo}

```js
POST /apigateway/users/register HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "user1",
  "nickname": "nickname",
  "user_portrait": "https://portrait.example.com/avatar.png",
  "ext_fields": {
    "k1": "v1",
    "k2": "v2"
  },
  "permit_convers": [
    {
      "target_id": "groupid1",
      "channel_type": 2,
      "max_his_msg_count": 100
    }
  ]
}
```

### Response parameters {#res_param}

| Parameter | Data type | Description                                                                 |  |
|-----------|-----------|-----------------------------------------------------------------------------|--|
| code      | int       | Status code. Please refer to [Status Code](../status.md) for details        |  |
| user_id   | string    | User ID                                                                     |  |
| token     | string    | Authentication token returned to the client for connection                  |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "user_id": "user1",
    "token": "tokenStr"
  }
}
```