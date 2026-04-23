---
title: Set Group Member Whitelist
hide_title: true
sidebar_position: 11
---

### Function Description{#intro}

After enabling a group ban, if you want to allow certain users to send messages, you can add those users to the group whitelist.

<div style="margin: 1rem 0; padding: 1rem 1.25rem; border-left: 4px solid #e5484d; background: #fff1f2; border-radius: 0 16px 16px 0;">
<p style="margin: 0 0 0.75rem; font-size: 1rem; font-weight: 700; color: #b42318;">priority</p>
<p style="margin: 0; color: #344054;">If the developer calls `Group ban`, `Group member ban`, and `Group whitelist` simultaneously, the group whitelist takes the highest priority, allowing users on the whitelist to continue sending messages.</p>
</div>
Request description{#req}

> <strong>Request Authentication</strong>: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/groupmemberallow/set

> <strong>Content-Type</strong>: `application/json`

### Request Parameters {#param}

| Parameter   | Data Type | Required | Description                  |   |
|:------------|:----------|:---------|:----------------------------|---|
| group_id    | string    | Yes      | The group ID                |   |
| member_ids  | array     | Yes      | A list of group member IDs |   |
| is_allow    | int       | Yes      | 0: Non-whitelist user; 1: Whitelist user |   |

### Request Example{#req_demo}
```js
POST /apigateway/groups/groupmemberallow/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["member1", "member2"],
  "is_allow": 1
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```



