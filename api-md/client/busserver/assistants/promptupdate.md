---
title: Update Prompt Word
hide_title: true
sidebar_position: 2
---
### Function Description{#intro}

Update a prompt word.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/assistants/prompts/update

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description               |   |
|:----------|:----------|:---------|:--------------------------|---|
| id        | string    | yes      | Prompt word ID            |   |
| prompts   | string    | yes      | Prompt word content (prompt) |   |


### Request Example{#req_demo}
``` js
POST /jim/assistants/prompts/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "id": "xxx",
  "prompts": "xxxxxxxxxxxx"
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

| Response Code | Description    |   |
|:--------------|:---------------|---|
| 17300         | Update failed  |   |

