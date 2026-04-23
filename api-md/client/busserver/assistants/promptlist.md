---
title: query prompt word
hide_title: true
sidebar_position: 5
---
### Function Description{#intro}

Retrieve a list of query prompt words.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/assistants/prompts/list

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description          |   |
|:----------|:----------|:---------|:---------------------|---|
| offset   | string    | No       | Pagination parameter |   |
| count    | int       | No       | Number of items to return, default is 20 |   |


### Request Example{#req_demo}
``` js
GET /jim/assistants/prompts/list HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "xx",
        "prompts": "xxxxxxxx",
        "created_time": 1722345674321
      }
    ],
    "offset": "xxx"
  }
}
```

### Response Codes

| Response Code | Description |   |
|:--------------|:------------|---|
| 17300         | Failed      |   |

