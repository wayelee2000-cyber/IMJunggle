---
title: Set Group Ban
hide_title: true
sidebar_position: 5
---

### Function Description{#intro}

After enabling a group ban, all members of the specified group will be prevented from sending messages to the group. **Messages sent via the Server API are not affected by the group ban**.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/groupmute/set

> **Content-Type**: `application/json`

### Request Parameters {#param}

| Parameter  | Data Type | Required | Description                  |   |
|:-----------|:----------|:---------|:----------------------------|---|
| group_id  | string    | yes      | The ID of the group         |   |
| is_mute   | int       | yes      | 0: unmuted; 1: muted        |   |

### Request Example{#req_demo}
```js
POST /apigateway/groups/groupmute/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
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