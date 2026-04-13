---
title: Set session label
hide_title: true
sidebar_position: 8
---

### Function description{#intro}

Set labels for conversations to enable conversation grouping.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/convers/tags/add

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter          | Data type | Required | Description                                  |   |
|:-------------------|:----------|:---------|:---------------------------------------------|---|
| user_id            | string    | yes      | The user ID for setting conversation labels |   |
| tag                | string    | yes      | Tag identifier                              |   |
| tag_name           | string    | no       | Tag nickname                               |   |
| convers            | array     | yes      | List of conversations to label             |   |
| convers.target_id   | string    | yes      | Session ID                                  |   |
| convers.channel_type| int       | yes      | Conversation type: 1 for single chat; 2 for group chat |   |

### Request Example{#req_demo}
```js
POST /apigateway/convers/tags/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "tag": "tag1",
  "tag_name": "tag1",
  "convers": [
    {
      "target_id": "userid2",
      "channel_type": 1
    },
    {
      "target_id": "groupid1",
      "channel_type": 2
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