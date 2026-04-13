---
title: Set Do Not Disturb
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

After setting a session to Do Not Disturb, the current session will not receive offline message notifications. Once this interface is called, the IM server will automatically synchronize the `undisturb_type` status to all endpoints of the specified user.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/convers/undisturb

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters     | Data type | Required | Description                      |   |
|:---------------|:----------|:---------|:--------------------------------|---|
| user_id        | string    | Yes      | The user ID for whom to set Do Not Disturb |   |
| target_id      | string    | Yes      | The ID of the session to apply DND to       |   |
| channel_type   | int       | Yes      | The type of the DND session                  |   |
| undisturb_type | int       | Yes      | DND type: 0 = Cancel DND; 1 = Enable DND for normal conversation |   |

### Request Example{#req_demo}
```js
POST /apigateway/convers/undisturb HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "items": [
    {
      "target_id": "userid2",
      "channel_type": 1,
      "undisturb_type": 1
    },
    {
      "target_id": "groupid1",
      "channel_type": 2,
      "undisturb_type": 1
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