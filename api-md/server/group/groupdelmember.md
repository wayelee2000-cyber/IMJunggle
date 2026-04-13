---
title: Remove group members
hide_title: true
sidebar_position: 8
---

### Function description{#intro}

When members are removed from a developer server group, the changes will be synchronized to the IM server.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/members/del

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter   | Data type | Required | Description           |   |
|:------------|:----------|:---------|:----------------------|---|
| group_id    | string    | yes      | Group ID              |   |
| member_ids  | array     | yes      | List of user IDs to remove |   |

### Request Example{#req_demo}
```js
POST /apigateway/groups/members/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["userid1", "userid2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```