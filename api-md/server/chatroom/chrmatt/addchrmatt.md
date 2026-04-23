---
title: Set chatroom attributes
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Set attributes for the specified chatroom.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/apigateway/chatrooms/atts/add

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter          | Data type | Required | Description                          |   |
|:-------------------|:----------|:---------|:-----------------------------------|---|
| from_id            | string    | Yes      | The user ID initiating the attribute setting |   |
| chat_id            | string    | Yes      | The ID of the chatroom             |   |
| atts               | array     | Yes      | A list of attributes to set         |   |
| atts[0].key        | string    | Yes      | The key of the attribute            |   |
| atts[0].value      | string    | Yes      | The value of the attribute          |   |
| atts[0].is_force   | bool      | No       | Whether to force override; default is false |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/atts/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id": "userid1",
  "chat_id": "chatroom1",
  "atts": [
    {
      "key": "k1",
      "value": "v1",
      "is_force": false
    }
  ]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "atts": [
      {
        "key": "k1",
        "code": 0,
        "att_time": 1732123445223
      }
    ]
  }
}
```
