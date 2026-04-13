---
title: Send group message
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

The group messaging function allows sending message content to multiple sessions simultaneously. Mass messaging does not affect the sender's session list order but does impact the receiver's session list sorting. For the sender, group messaging history is recorded separately, aggregated by `target_id`, and displayed as a distinct session. This session contains only the sender's messages. According to `target_convers`, messages are sent to each conversation as `sender_id` respectively, supporting both `single chat` and `group chat`.

:::danger special frequency limit
`target_convers` supports multiple sessions, with a sending interval of `50ms` per session. The more sessions included, the longer the sending and response times.
:::

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/messages/groupcast/send

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters     | Data type | Required | Description                                                                                  |   |
|:---------------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| sender_id      | string    | yes      | Message sender ID                                                                            |   |
| target_id      | string    | no       | Group target ID. Group message history with the same ID will be aggregated together. If empty, no conversation will be created for the sender. |   |
| msg_type       | string    | yes      | Message type identifier                                                                     |   |
| msg_content    | string    | yes      | Message content; JSON format is recommended                                                 |   |
| target_convers | array     | yes      | Target conversations for group sending, supporting both single chat and group chat          |   |
  
### Request Example{#req_demo}
```js
POST /apigateway/messages/groupcast/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id":"userid1",
  "target_id":"groupcastid1",
  "msg_type":"text",
  "msg_content":"{\"content\":\"aabbcc\"}",
  "target_convers":[
    {
      "target_id":"userid2",
      "channel_type":1
    },
    {
      "target_id":"groupid1",
      "channel_type":2
    }
  ]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```