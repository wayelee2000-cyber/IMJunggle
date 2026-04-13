---
title: Administrator withdraws message
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Allows a group administrator to withdraw messages sent by other group members.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/messages/recall

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter    | Data type | Required | Description                                                                 |
|:-------------|:----------|:---------|:----------------------------------------------------------------------------|
| from_id     | string    | yes      | The sender ID of the message to be withdrawn.                              |
| target_id   | string    | yes      | The recipient of the message; for groups, this is the group ID.            |
| channel_type| int       | yes      | Session type: 1 for single chat; 2 for group chat.                         |
| msg_id      | string    | yes      | The ID of the message to be withdrawn.                                    |
| msg_time    | int       | yes      | The sending time of the message to be recalled (timestamp).                |
| exts        | map       | no       | Extended information (optional).                                           |


### Request Example{#req_demo}
``` js
POST /jim/messages/recall HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "from_id": "userid1",
  "target_id": "group1",
  "channel_type": 2,
  "msg_id": "xxxxxxxxxx",
  "msg_time": 1731234567823,
  "exts": {
    "k1": "v1",
    "k2": "v2"
  }
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response code

| Response code | Description |
|:--------------|:------------|