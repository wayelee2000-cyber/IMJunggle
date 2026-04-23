---
title: Query the Specified Attributes of a Chatroom
hide_title: true
sidebar_position: 3
---

### Function Description{#intro}

Query specific attributes within a chatroom.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/apigateway/chatrooms/atts/qry

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description                  |   |
|:----------|:----------|:---------|:----------------------------|---|
| chat_id   | string    | Yes      | The ID of the chatroom     |   |
| att_keys  | array     | Yes      | List of attribute keys to query |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/atts/qry HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id": "chatroom1",
  "att_keys": ["k1", "k2"]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "chat_id": "chatroom1",
    "atts": [
      {
        "key": "k1",
        "value": "v1",
        "user_id": "userid1",
        "att_time": 1732123445223
      }
    ]
  }
}
```

