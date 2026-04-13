---
title: Query Information by Member ID
hide_title: true
sidebar_position: 12
---

### Function Description{#intro}

Query information for specified group members within a group, such as checking whether a group member is muted.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/members/querybyids

> **Content-Type**: `application/json`

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