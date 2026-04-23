---
title: Set Group Ban
hide_title: true
sidebar_position: 5
---

### Function Description{#intro}

After enabling a group ban, all members of the specified group will be prevented from sending messages to the group. <strong>Messages sent via the Server API are not affected by the group ban</strong>.

Request description{#req}

> <strong>Request Authentication</strong>: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/groupmute/set

> <strong>Content-Type</strong>: `application/json`

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



