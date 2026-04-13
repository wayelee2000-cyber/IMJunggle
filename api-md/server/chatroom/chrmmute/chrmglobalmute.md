---
title: Set Global Ban on Chat Room
hide_title: true
sidebar_position: 4
---

### Function Description{#intro}

After enabling a global ban on a chat room, all members of that chat room will be prevented from sending messages, except for users on the whitelist. **Messages sent via the Server API are not affected by the ban**.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../../api#api)/apigateway/chatrooms/chrmmute/set

> **Content-Type**: `application/json`

### Request Parameters {#param}

| Parameter | Data Type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| chat_id   | string    | yes      | Chat room ID |  |
| is_mute   | int       | yes      | 0: unmuted; 1: muted |  |

### Request Example{#req_demo}
```js
POST /apigateway/chatrooms/chrmmute/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id": "chatroomid1",
  "is_mute": 1
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```