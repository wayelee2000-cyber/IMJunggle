---
title: Add New Prompt Word
hide_title: true
sidebar_position: 1
---
### Function Description{#intro}

Add prompt words to the AI assistant.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/assistants/prompts/add

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description               |   |
|:----------|:----------|:---------|:--------------------------|---|
| prompts  | string    | yes      | Content of the prompt word |   |


### Request Example{#req_demo}
``` js
POST /jim/assistants/prompts/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
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

| Response Code | Description  |   |
|:--------------|:-------------|---|
| 17300         | Add failed   |   |