---
title: Create group
hide_title: true
sidebar_position: 1
---

### Function description{#intro}

Synchronize groups created by the developer server with the IM service for message sending, conversation list display, message push, and more. The group supports extended information, such as custom group levels.

:::danger group creation notification
After a group is successfully created, the IM server will **not** send a group creation notification. Developers need to implement custom notification messages to be sent to the group.
:::

### Request description{#req}

> **Request Authentication**: This API requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/add

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                          |   |
|:------------|:----------|:---------|:-----------------------------------|---|
| group_id    | string    | Yes      | Group ID                           |   |
| group_name  | string    | No       | Group nickname                    |   |
| member_ids  | array     | Yes      | List of user IDs joining the group |   |
| ext_fields  | map       | No       | Group extension information in key-value format |   |


### Request Example{#req_demo}
``` js
POST /apigateway/groups/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "group_name": "group1",
  "member_ids": ["userid1", "userid2"],
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