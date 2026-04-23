---
title: Subscribe to the public account
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

Allows users to subscribe to public accounts.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/publicchannel/subscribe

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description               |   |
|:------------|:----------|:---------|:--------------------------|---|
| channel_id  | string    | yes      | Public account ID         |   |
| member_ids  | array     | yes      | List of subscriber user IDs |   |


### Request Example{#req_demo}
``` js
POST /apigateway/publicchannel/subscribe HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "channel_id": "channel1",
  "member_ids": ["userid1", "userid2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

