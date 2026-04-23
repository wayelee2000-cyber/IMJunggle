---
title: Destroy public account
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

Destroying a public account will also terminate all subscription relationships associated with it.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/publicchannel/destroy

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description          |   |
|:------------|:----------|:---------|:---------------------|---|
| channel_id  | string    | yes      | Public account ID    |   |


### Request Example{#req_demo}
``` js
POST /apigateway/publicchannel/destroy HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "channel_id": "channel1"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
