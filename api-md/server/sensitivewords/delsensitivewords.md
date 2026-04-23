---
title: Delete sensitive words
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

The added sensitive words are used for content review of text messages in single group chats.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/sensitivewords/del

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
POST /apigateway/sensitivewords/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "words": ["xxxxx", "yyyyy"]
}
```

### Request parameters {#param}

| Parameters | Data type | Required | Parameter description |  |
|:-----------|:----------|:---------|:----------------------|:--|
| words      | array     | yes      | The sensitive words to be deleted |  |

### Response parameters {#res_param}

| Parameters | Data type | Parameter description |  |
|:-----------|:----------|:----------------------|:--|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
