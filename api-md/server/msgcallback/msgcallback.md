---
title: message callback
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Message callback allows the IM server to notify the customer's business server when it receives a message sending request. The business server then decides whether to continue distributing and sending the message. This feature is useful for scenarios such as message auditing and permission control.

### Request description{#req}

> **Push Authentication**: The interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Push result**: The business server should respond with HTTP status 200, and the response data must specify whether the message should continue to be sent. For details, see the parameter descriptions below.

> **Mechanism description**: Message callback provides the business server an opportunity to intervene before the message is actually distributed. The response time of the business server directly affects message processing delay. Note that messages sent through the Server API will not trigger callbacks.

### Request parameters {#param}

| Parameters                 | Data type | Required | Parameter description                                                                                  |   |
|:---------------------------|:----------|:---------|:-----------------------------------------------------------------------------------------------------|---|
| sender                    | string    | yes      | Message sender ID                                                                                      |   |
| receiver                  | string    | yes      | Message receiver ID                                                                                    |   |
| msg_type                  | string    | yes      | Message type identifier                                                                                |   |
| msg_content               | string    | yes      | Message content; JSON format is recommended                                                           |   |
| mention_info.mention_type | string    | no       | @Message type: mention_all for @everyone; mention_someone for @someone; mention_all_someone for @everyone and some people |   |
| mention_info.target_user_ids | array  | no       | When mentioning specific users, specify the user IDs to be mentioned here                             |   |

### Request Example{#req_demo}

```js
POST /message/callback HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "platform": "iOS", // iOS/Android/Web/PC/Server
    "sender": "userid1", // sender user ID
    "receiver": "userid2", // receiver user ID
    "channel_type": 1, // 1: private, 2: group, 3: chatroom
    "msg_type": "text",
    "msg_content": "Hello, world!",
    "mention_info": {
      "mention_type": "mention_all",
      "target_user_ids": ["userid1", "userid2"]
    }
}
```

### Response example{#resp_demo}

```js
{
    "result": "PASS", // REJECT, REPLACE, SILENT
    "msg_type": "jg:text",
    "msg_content": "{\"content\":\"hello world!\"}",
    "custom_code": 132
}
```

### Response parameters

| Parameters   | Data type | Required | Parameter description                                                                                                         |   |
|:-------------|:----------|:---------|:------------------------------------------------------------------------------------------------------------------------------|---|
| result       | string    | yes      | Message callback result. Possible values: PASS (continue distribution), REJECT (refuse delivery), REPLACE (replace content), SILENT (refuse delivery silently, sender unaware) |   |
| msg_type     | string    | no       | Valid when result is REPLACE; used to replace the original message type                                                        |   |
| msg_content  | string    | no       | Valid when result is REPLACE; used to replace the original message content                                                    |   |
| custom_code  | int       | no       | Valid when result is REJECT; custom error code returned to the sender. If set to 0, the default IM error code is used          |   |