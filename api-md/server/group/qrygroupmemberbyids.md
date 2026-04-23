---
title: Query Information by Member ID
hide_title: true
sidebar_position: 12
---

### Function Description{#intro}

Query information for specified group members within a group, such as checking whether a group member is muted.

Request description{#req}

> <strong>Request Authentication</strong>: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/members/querybyids

> <strong>Content-Type</strong>: `application/json`

### Request Parameters {#param}

| Parameter   | Data Type | Required | Description               |   |
|:------------|:----------|:---------|:--------------------------|---|
| group_id    | string    | yes      | Group ID                  |   |
| member_ids  | array     | yes      | List of group member IDs  |   |

### Request Example{#req_demo}
```js
POST /apigateway/groups/members/querybyids HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["member1", "member2"]
}
```
### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "member_id": "member1",
        "is_mute": 0
      },
      {
        "member_id": "member2",
        "is_mute": 0
      }
    ]
  }
}
```



