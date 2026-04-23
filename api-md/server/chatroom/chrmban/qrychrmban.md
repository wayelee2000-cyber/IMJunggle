---
title: Query banned chatroom members
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

Retrieve the list of banned members in a chatroom.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/apigateway/chatrooms/banmembers/query

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| chat_id   | string    | Yes      | The ID of the chatroom |  |
| offset    | string    | No       | Offset for pagination. The next offset is returned with each response. Pass empty for the initial request. |  |
| limit     | int       | No       | Number of records to query. Default is 100, maximum is 1000. |  |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/banmembers/query?chat_id=xxx&offset=xx&limit=100 HTTP/1.1
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
    "chat_id": "xxx",
    "members": [
      {
        "member_id": "xxx",
        "end_time": 172987634564
      }
    ],
    "offset": "xxxx"
  }
}
```

