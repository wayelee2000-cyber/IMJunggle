---
title: Smart Reply
hide_title: true
sidebar_position: 6
---
### Function Description{#intro}

Generate smart replies.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/assistants/answer

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter    | Data Type | Required | Description                              |   |
|:-------------|:----------|:---------|:---------------------------------------|---|
| conver_id    | string    | yes      | Session ID                             |   |
| channel_type | int       | yes      | Conversation type: 1 for single chat; 2 for group chat |   |
| prompt_id    | string    | no       | Prompt word ID                         |   |
| msgs         | array     | no       | The latest n messages in the session  |   |


### Request Example{#req_demo}
``` js
POST /jim/assistants/answer HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "conver_id": "xx",
  "channel_type": 1,
  "prompt_id": "xxx",
  "msgs": [
    {
      "sender_id": "xx",
      "content": "xxxxx",
      "msg_time": 1741234567893
    }
  ]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "answer": "xxxxxxxxx"
  }
}
```

### Response Codes

| Response Code | Description |   |
|:--------------|:------------|---|

