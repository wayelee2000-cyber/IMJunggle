---
title: Administrator deletes message
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

When a group administrator deletes messages sent by other group members, those messages will no longer be visible to any group members after deletion.

### Request description{#req}

> **Request Authentication**: This API requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/messages/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter       | Data type | Required | Description                                                                 |
|:----------------|:----------|:---------|:----------------------------------------------------------------------------|
| from_id         | string    | yes      | The sender ID of the message to be deleted                                  |
| target_id       | string    | yes      | The recipient of the message; for groups, this is the group ID             |
| channel_type    | int       | yes      | Session type: 1 for single chat; 2 for group chat                          |
| msgs.msg_id     | string    | yes      | The ID of the message to be deleted                                        |
| msgs.msg_time   | int       | yes      | The sending time of the message to be deleted                              |


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
  "msgs": [
    {
      "msg_id": "xxxx",
      "msg_time": 1731234567823
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

### Response code

| Response code | Description |
|:--------------|:------------|
