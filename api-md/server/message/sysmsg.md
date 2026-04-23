---
title: Send system message
hide_title: true
sidebar_position: 3
---

### Function description{#intro}

Developers can send notifications through the server system, which is suitable for features such as `official account` or `system notification` types.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/messages/system/send

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters  | Data type | Required | Description                                                                 |  |
|:------------|:----------|:---------|:----------------------------------------------------------------------------|:--|
| sender_id   | string    | Yes      | ID of the message sender                                                    |  |
| target_ids  | array     | Yes      | List of message receiver IDs                                                |  |
| msg_type   | string    | Yes      | Message type identifier                                                     |  |
| msg_content | string    | Yes      | Message content; JSON format is recommended                                |  |
| is_storage  | bool      | No       | Whether to store the message in history; default is true                   |  |
| is_count   | bool      | No       | Whether to track unread counts; default is true, and unreads will be recorded |  |
| is_state   | bool      | No       | Status message flag; this message type offers very high sending performance but does not guarantee reliability |  |

### Request Example{#req_demo}
```js
POST /apigateway/messages/system/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id": "sys1",
  "target_ids": ["userid1", "userid2"],
  "msg_type": "text",
  "msg_content": "{\"content\":\"aabbcc\"}",
  "is_storage": true,
  "is_state": false
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description                      |  |
|:-----------|:----------|:--------------------------------|:--|
| msg_id    | string    | Unique identifier of the message |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "target_id": "userid1",
      "msg_id": "aaaaaaa"
    },
    {
      "target_id": "userid2",
      "msg_id": "bbbbbbb"
    }
  ]
}
```

