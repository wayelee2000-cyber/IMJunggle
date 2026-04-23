---
title: Create a public account
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Create a public account channel.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/publicchannel/create

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter       | Data type | Required | Description             |  |
|:----------------|:----------|:---------|:------------------------|--|
| channel_id      | string    | Yes      | Public account ID       |  |
| channel_name    | string    | No       | Public account nickname |  |
| channel_portrait| string    | No       | Public account avatar   |  |
| creator_id      | string    | No       | Creator user ID         |  |


### Request Example{#req_demo}
``` js
POST /apigateway/publicchannel/create HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "channel_id": "channel1",
  "channel_name": "publicchannel",
  "channel_portrait": "https://xxxxxx.jpg",
  "creator_id": "userid1"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
