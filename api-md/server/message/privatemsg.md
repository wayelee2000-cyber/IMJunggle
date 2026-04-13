---
title: Send private message
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

This function allows the developer to simulate a user on the server to send a private message in a one-on-one chat. For example, when adding a friend, after the developer server verifies the friend request, it sends a message as the user: `So-and-so adds you as a friend`.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/messages/private/send

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter           | Data type | Required | Description                                                                                  |  |
|:--------------------|:----------|:---------|:---------------------------------------------------------------------------------------------|--|
| sender_id           | string    | Yes      | ID of the message sender                                                                    |  |
| target_ids          | array     | Yes      | List of message recipient IDs                                                               |  |
| msg_type            | string    | Yes      | Message type identifier                                                                     |  |
| msg_content         | string    | Yes      | Message content; JSON format is recommended                                                 |  |
| push_data.push_text | string    | No       | Content to be displayed in the push notification                                            |  |
| push_data.push_extra| string    | No       | Custom extension data for push notifications; JSON string is recommended                     |  |
| is_storage          | bool      | No       | Whether to store the message in chat history; default is true                               |  |
| is_count            | bool      | No       | Whether to count the message as unread; default is true                                    |  |
| is_notify_sender    | bool      | No       | Whether to notify the sender of the message; default is true                               |  |
| is_state            | bool      | No       | Status message flag; this message type offers extremely high sending performance but no delivery guarantee |  |
| life_time           | int       | No       | Message lifespan in milliseconds; 0 means permanent                                        |  |
| life_time_after_read | int       | No       | Lifespan after the message is read, in milliseconds                                        |  |

### Request Example{#req_demo}
```js
POST /apigateway/messages/private/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id":"userid1",
  "target_ids":["userid2","userid3"],
  "msg_type":"jg:text",
  "msg_content":"{\"content\":\"aabbcc\"}",
  "push_data":{
    "push_text":"push content",
    "push_extra":"extra"
  },
  "is_storage":true,
  "is_notify_sender":true,
  "is_state":false
}
```

### Response parameters {#res_param}

| Parameter | Data type | Description                      |  |
|:----------|:----------|:--------------------------------|--|
| msg_id    | string    | Unique identifier of the message |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "target_id": "userid2",
      "msg_id": "aaaaaaa"
    },
    {
      "target_id": "userid3",
      "msg_id": "bbbbbbb"
    }
  ]
}
```