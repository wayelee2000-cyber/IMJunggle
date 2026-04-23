---
title: Query all attributes of chatroom
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

Retrieve all attributes of a chatroom.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/apigateway/chatrooms/atts/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description          |   |
|:----------|:----------|:---------|:---------------------|---|
| chat_id   | string    | Yes      | The ID of the chatroom |   |


### Request Example{#req_demo}
``` js
GET /apigateway/chatrooms/atts/list HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response example{#res_demo}

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
