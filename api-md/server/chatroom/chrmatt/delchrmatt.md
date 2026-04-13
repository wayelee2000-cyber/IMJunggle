---
title: Delete chat room attributes
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

Removes custom attributes from the specified chat room.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request rate limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/atts/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter       | Data type | Required | Description                          |   |
|:----------------|:----------|:---------|:-----------------------------------|---|
| from_id         | string    | Yes      | The user ID of the attribute initiator |   |
| chat_id         | string    | Yes      | The ID of the chat room             |   |
| atts            | array     | Yes      | A list of attributes to delete     |   |
| atts[0].key     | string    | Yes      | The key of the attribute            |   |
| atts[0].is_force| bool      | No       | Whether to force deletion; defaults to false |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/atts/del HTTP/1.1
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