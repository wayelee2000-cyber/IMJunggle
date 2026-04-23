---
title: Set ban on group members
hide_title: true
sidebar_position: 10
---

### Function description{#intro}

This function prohibits group members from sending messages within the group. For example, a group administrator can mute a member, preventing them from sending messages. Once muted, the member cannot send group messages but will still receive messages from the group.

Request description{#req}

> <strong>Request Authentication</strong>: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/groupmembermute/set

> <strong>Content-Type</strong>: `application/json`

### Request parameters {#param}

| Parameters  | Data type | Required | Description                                                                 |  |
|:------------|:----------|:---------|:----------------------------------------------------------------------------|--|
| group_id    | string    | Yes      | The ID of the group                                                        |  |
| member_ids  | array     | Yes      | A list of group member IDs to be muted                                     |  |
| is_mute     | int       | Yes      | 0: not muted; 1: muted                                                     |  |
| mute_minute | int       | No       | Duration of the mute in minutes. The mute will be automatically lifted after this period. Passing 0 indicates a permanent mute. |  |

### Request Example{#req_demo}
```js
POST /apigateway/groups/groupmembermute/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["member1", "member2"],
  "is_mute": 1,
  "mute_minute": 10
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```


