---
title: Send group chat message
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Developers can send group messages on the server, supporting message types such as `@ messages`, standard `text`, `images`, and `voice`.

### Request description{#req}

> **Request Authentication**: This API requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/messages/group/send

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters               | Data type | Required | Description                                                                                  |   |
|:-------------------------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| sender_id                | string    | Yes      | ID of the message sender                                                                    |   |
| target_ids               | array     | Yes      | List of group IDs                                                                           |   |
| msg_type                 | string    | Yes      | Message type identifier                                                                     |   |
| msg_content              | string    | Yes      | Message content; JSON format is recommended                                                |   |
| to_user_ids              | array     | No       | Directed message; only sent to specified members within the group                           |   |
| push_data.push_text      | string    | No       | Content to be used for push notifications                                                  |   |
| push_data.push_extra     | string    | No       | Custom extension for push notifications; JSON string is recommended                         |   |
| push_data.push_level     | number    | No       | Push priority; 0: Default; 1: Ignore push speed control; 2: Ignore Do Not Disturb           |   |
| is_storage               | bool      | No       | Whether the message is stored in history; default is true                                  |   |
| is_count                 | bool      | No       | Whether the message counts as unread; default is true                                      |   |
| is_notify_sender         | bool      | No       | Whether the sender receives a notification for the message; default is true                |   |
| is_state                 | bool      | No       | Status message; this type has extremely high sending performance                            |   |
| mention_info.mention_type| string    | No       | @ message type: `mention_all` (@everyone); `mention_someone` (@someone); `mention_all_someone` (@everyone and some people) |   |
| mention_info.target_user_ids | array | No       | When mentioning specific users, specify their user IDs here                               |   |
| refer_msg                | object    | No       | Referenced message                                                                         |   |
| life_time                | int       | No       | Message lifespan in milliseconds; 0 indicates permanent                                   |   |
| life_time_after_read     | int       | No       | Lifespan after the message is read, in milliseconds                                       |   |

### Request Example{#req_demo}
```js
POST /apigateway/messages/group/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id": "userid1",
  "target_ids": ["groupid1", "groupid2"],
  "msg_type": "text",
  "msg_content": "{\"content\":\"aabbcc\"}",
  "to_user_ids": ["userid1"],
  "push_data": {
    "push_text": "push content",
    "push_extra": "extra",
    "push_level": 0
  },
  "is_storage": true,
  "is_notify_sender": true,
  "is_state": false,
  "mention_info": {
    "mention_type": "mention_all",
    "target_user_ids": ["userid1", "userid2"]
  },
  "refer_msg": {
    "msg_id": "xxx",
    "sender_id": "xxx",
    "target_id": "xxx",
    "channel_type": 1,
    "msg_type": "xxx",
    "msg_content": "xxxxx"
  }
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description                      |   |
|:-----------|:----------|:--------------------------------|---|
| msg_id     | string    | Unique identifier of the message |   |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "target_id": "groupid1",
      "msg_id": "aaaaaaa"
    },
    {
      "target_id": "groupid2",
      "msg_id": "bbbbbbb"
    }
  ]
}
```

