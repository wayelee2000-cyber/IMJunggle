---
title: Set Group Member Whitelist
hide_title: true
sidebar_position: 11
---

### Function Description{#intro}

After enabling a group ban, if you want to allow certain users to send messages, you can add those users to the group whitelist.

:::danger priority
If the developer calls `Group ban`, `Group member ban`, and `Group whitelist` simultaneously, the group whitelist takes the highest priority, allowing users on the whitelist to continue sending messages.
:::

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/groupmemberallow/set

> **Content-Type**: `application/json`

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