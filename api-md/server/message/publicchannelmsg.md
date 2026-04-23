---
title: Send official account message
hide_title: true
sidebar_position: 8
---

### Function description{#intro}

Send a message from an official account.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/messages/publicchannel/send

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters              | Data type | Required | Description                                               |  |
|:------------------------|:----------|:---------|:----------------------------------------------------------|--|
| sender_id               | string    | Yes      | ID of the message sender                                  |  |
| target_ids              | array     | Yes      | List of official account IDs                              |  |
| msg_type                | string    | Yes      | Message type identifier                                   |  |
| msg_content             | string    | Yes      | Message content; JSON format is recommended               |  |
| push_data.push_text     | string    | No       | Content to be pushed                                      |  |
| push_data.push_extra    | string    | No       | Custom push extension; JSON string is recommended         |  |
| push_data.push_level    | number    | No       | Push priority: 0 (Default), 1 (Ignore push speed control), 2 (Ignore Do Not Disturb) |  |
| is_storage              | bool      | No       | Whether to store the message in history; default is true |  |
| is_count                | bool      | No       | Whether to record unread counts; default is true         |  |

### Request Example{#req_demo}
```js
POST /apigateway/messages/publicchannel/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id": "userid1",
  "target_ids": ["channel1"],
  "msg_type": "text",
  "msg_content": "{\"content\":\"aabbcc\"}"
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description                      |  |
|:-----------|:----------|:--------------------------------|--|
| msg_id     | string    | Unique identifier of the message |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "target_id": "channel1",
      "msg_id": "aaaaaaa"
    }
  ]
}
```

