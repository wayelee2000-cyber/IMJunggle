---
title: Delete Prompt Word
hide_title: true
sidebar_position: 3
---
### Function Description{#intro}

Delete a prompt word.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/assistants/prompts/del

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description       |   |
|:----------|:----------|:---------|:------------------|---|
| id        | string    | yes      | Prompt word ID    |   |


### Request Example{#req_demo}
``` js
POST /jim/assistants/prompts/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "id": "xxx"
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