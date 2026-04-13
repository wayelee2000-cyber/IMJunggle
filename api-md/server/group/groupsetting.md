---
title: Update group settings
hide_title: true
sidebar_position: 6
---

### Function description{#intro}

Groups support various parameter settings, such as whether new members can access previous historical messages.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/settings/set

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description                                               |   |
|:-------------|:----------|:---------|:----------------------------------------------------------|---|
| group_id    | string    | Yes      | The ID of the group                                       |   |
| hide_grp_msg | int       | No       | Controls whether to hide historical messages before joining the group; 0: Do not hide; 1: Hide |   |

### Request Example{#req_demo}
```js
POST /apigateway/groups/settings/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1",
  "settings": {
    "hide_grp_msg": "1"
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