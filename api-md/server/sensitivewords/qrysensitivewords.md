---
title: Query sensitive words
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

The added sensitive words are used for content review of text messages in individual group chats.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/sensitivewords/list

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
GET /apigateway/sensitivewords/list?limit=20&offset=xx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| offset     | string    | Yes      | The starting ID for querying sensitive words. Each sensitive word entry has a unique ID. Leave blank for the initial query. |  |
| limit      | int       | No       | Number of items per page for pagination. Default is 50. |  |

### Response parameters {#res_param}

| Parameters | Data type | Description |  |
|:-----------|:----------|:------------|:--|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "xx",
        "word": "xx",
        "word_type": 1
      }
    ],
    "is_finished": false
  }
}
```