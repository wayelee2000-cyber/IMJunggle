---
title: Send streaming message
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Send a streaming message.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/messages/private/stream/send

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameters     | Data type | Required | Description                                      |  |
|:---------------|:----------|:---------|:------------------------------------------------|--|
| msg_id         | string    | No       | Leave blank for the first call. For subsequent calls, provide the `msg_id` returned by the first call. |  |
| sender_id      | string    | Yes      | ID of the message sender.                        |  |
| target_id      | string    | Yes      | ID of the message recipient.                     |  |
| partial_content| string    | Yes      | Fragment of the message content, in text format.|  |
| is_finished    | bool      | No       | Indicates whether the streaming message is complete. Defaults to `false`. |  |

### Request Example{#req_demo}
```js
POST /apigateway/messages/private/stream/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "msg_id": "xxxxxx",   // Leave blank for the first call. For subsequent calls, use the msg_id returned from the first fragment.
  "from_id": "userid1",
  "target_id": "userid2",
  "partial_content": "content 1",
  "seq": 1,
  "is_finished": false
}
```

### Response parameters {#res_param}

| Parameters | Data type | Description                      |  |
|:-----------|:----------|:--------------------------------|--|
| msg_id     | string    | Unique identifier of the message|  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "msg_id": "xxxx",
    "msg_time": 1722212323123
  }
}
```