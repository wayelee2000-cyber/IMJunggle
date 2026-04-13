---
title: Import historical messages
hide_title: true
sidebar_position: 6
---

### Function description{#intro}

Import historical messages. Sessions will be created synchronously as messages are imported. Please ensure that messages are imported in chronological order, from oldest to newest.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request rate limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/hismsgs/import

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                                                                                  |   |
|:-------------|:----------|:---------|:--------------------------------------------------------------------------------------------|---|
| from_id     | string    | No       | In a single chat session, the ID of the user in the conversation                            |   |
| target_id   | string    | Yes      | In a single chat session, the ID of the other user; in a group chat session, the group ID  |   |
| channel_type| int       | Yes      | Conversation type: 1 for single chat; 2 for group chat                                     |   |
| msg_time    | int       | Yes      | Timestamp of the message, in milliseconds                                                  |   |
| msg_type    | string    | Yes      | Message type                                                                               |   |
| msg_content | string    | Yes      | Message content; a JSON structure is recommended                                           |   |

### Request Example{#req_demo}
```js
POST /apigateway/hismsgs/import HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id": "xxx",
  "target_id": "xxx",
  "channel_type": 1,
  "msg_time": 1723245643456,
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