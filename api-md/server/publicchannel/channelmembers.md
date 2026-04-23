---
title: Public Account Subscription List
hide_title: true
sidebar_position: 6
---

### Function Description{#intro}

Retrieve the list of users subscribed to a public account.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/publicchannel/members/list

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter   | Data Type | Required | Description          |   |
|:------------|:----------|:---------|:---------------------|---|
| channel_id  | string    | Yes      | Public account ID    |   |
| limit       | int       | No       | Pagination limit     |   |
| offset      | string    | No       | Pagination offset    |   |


### Request Example{#req_demo}
``` js
GET /apigateway/publicchannel/members/list?channel_id=xxx&limit=50&offset=xxx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "members": [
      {
        "member_id": "userid1",
        "created_time": 17312345678
      }
    ],
    "offset": "xxxx"
  }
}
```

