---
title: Message modification
hide_title: true
sidebar_position: 5
---

### Function description{#intro}

Modify existing messages by updating the message type and content, with support for synchronizing across multiple devices.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/hismsgs/modify

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                                                                                  |   |
|:-------------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| from_id     | string    | No       | In a single chat conversation, the ID of the user in the conversation                            |   |
| target_id   | string    | Yes      | In a single chat conversation, the ID of the other user; in a group chat conversation, the group ID   |   |
| channel_type| int       | Yes      | Conversation type: 1 for single chat; 2 for group chat                                     |   |
| msg_id      | string    | Yes      | The ID of the message to be modified                                                       |   |
| msg_type    | string    | Yes      | The type of the message                                                                    |   |
| msg_content | string    | Yes      | The message content; JSON structure is recommended                                         |   |

### Request Example{#req_demo}
```js
POST /apigateway/hismsgs/modify HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id": "xxx",
  "target_id": "xxx",
  "channel_type": 1,
  "msg_id": "xxxxxx",
  "msg_type": "text",
  "msg_content": "{\"content\":\"aabbcc\"}"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```



