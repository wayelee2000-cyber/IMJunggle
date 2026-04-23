---
title: Add sensitive words
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

The added sensitive words will be used for content review of text messages in individual group chats.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/sensitivewords/add

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
POST /apigateway/sensitivewords/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "items":[
        {
            "word":"xxxxx",
            "word_type":1
        }
    ]
}
```

### Request parameters {#param}

| Parameter  | Data type | Required | Description                                      |
|:-----------|:----------|:---------|:------------------------------------------------|
| word       | string    | Yes      | The sensitive word to be added                   |
| word_type  | int       | Yes      | The sensitive word filtering type: 1 - Intercept sensitive words; 2 - Replace sensitive words |

### Response parameters {#res_param}

| Parameter | Data type | Description |
|:----------|:----------|:------------|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```
