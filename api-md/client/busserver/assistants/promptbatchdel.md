---
title: Batch Delete Prompt Words
hide_title: true
sidebar_position: 4
---
### Function Description{#intro}

Batch delete prompt words.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/assistants/prompts/batchdel

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description           |   |
|:----------|:----------|:---------|:----------------------|---|
| ids       | array     | yes      | List of prompt word IDs |   |


### Request Example{#req_demo}
``` js
POST /jim/assistants/prompts/batchdel HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "ids": ["xxx", "yyy"]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response Codes

| Response Code | Description      |   |
|:--------------|:-----------------|---|
| 17300         | Deletion failed  |   |

