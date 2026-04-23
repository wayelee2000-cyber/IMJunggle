---
title: Set group member attributes
hide_title: true
sidebar_position: 13
---

### Function description{#intro}

Set attributes for group members within a group, such as group nickname, group badge, and more.

Request description{#req}

> <strong>Request Authentication</strong>: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/members/update

> <strong>Content-Type</strong>: `application/json`

### Request parameters {#param}

| Parameters      | Data type | Required | Description                        |   |
|:----------------|:----------|:---------|:---------------------------------|---|
| group_id        | string    | Yes      | Group ID                         |   |
| member_id       | string    | Yes      | Group member ID                  |   |
| grp_display_name| string    | No       | Member鈥檚 nickname within the group |   |
| ext_fields      | map       | No       | Extended fields for the member within the group |   |

### Request Example{#req_demo}
```js
POST /apigateway/groups/members/update HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_id": "member1",
  "grp_display_name": "Group Nickname",
  "ext_fields": {
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


