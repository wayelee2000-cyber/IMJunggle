---
title: Add group members
hide_title: true
sidebar_position: 7
---

### Function description{#intro}

When the members of a developer server group are updated, the new members will be synchronized with the IM server.

Request description{#req}

> <strong>Request Authentication</strong>: This API requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/members/add

> <strong>Content-Type</strong>: `application/json`

### Request parameters {#param}

| Parameters  | Data type | Required | Description                  |   |
|:------------|:----------|:---------|:----------------------------|---|
| group_id    | string    | yes      | Group ID                    |   |
| group_name  | string    | no       | Group nickname              |   |
| member_ids  | array     | yes      | List of user IDs to add to the group |   |

### Request Example{#req_demo}

```json
POST /apigateway/groups/members/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "group_name": "group1",
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



