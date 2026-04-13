---
title: Chat message subscription
hide_title: true
sidebar_position: 2
---

### Request description{#req}

> **Push Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header) for details.

> **Push Result**: Upon receiving the push, the business party must ensure the response status code is 200 to confirm successful receipt.

> **Mechanism description**: The message CC will attempt to push up to 3 times, with a 100ms interval between attempts. If all 3 attempts fail, the push is considered unsuccessful. The push mechanism uses Google's adaptive circuit breaker. If too many failures occur within a sliding time window, the circuit breaker will activate, temporarily suspending pushes from CCs to the business.

### Request parameters {#param}

| Parameters                 | Data type | Required | Description                                                                                  |   |
|:---------------------------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| sender                    | string    | yes      | Message sender ID                                                                            |   |
| receiver                  | string    | yes      | Message receiver ID                                                                          |   |
| msg_type                  | string    | yes      | Message type identifier                                                                     |   |
| msg_content               | string    | yes      | Message content; JSON format is recommended                                                 |   |
| mention_info.mention_type | string    | no       | @Message type: `mention_all` for @everyone; `mention_someone` for @someone; `mention_all_someone` for @everyone and some people |   |
| mention_info.target_user_ids | array  | no       | When mentioning specific people, specify the user IDs of those to be mentioned              |   |

### Request Example{#req_demo}

```js
POST /message/notification HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "event_type": "message", // Event type: message, online, offline
  "timestamp": 1713456000000, // Millisecond timestamp
  "payload": [
    {
      "platform": "iOS", // iOS/Android/Web/PC/Server
      "sender": "userid1", // Sender user ID
      "receiver": "userid2", // Receiver user ID
      "conver_type": 1, // 1: private, 2: group, 3: chatroom
      "msg_type": "text",
      "msg_content": "Hello, world!",
      "mention_info": {
        "mention_type": "mention_all",
        "target_user_ids": ["userid1", "userid2"]
      },
      "msg_id": "123",
      "msg_time": 1718980832156
    }
  ]
}
```