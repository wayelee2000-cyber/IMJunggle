---
title: Update group settings
hide_title: true
sidebar_position: 6
---

### Function description{#intro}

Groups support various parameter settings, such as whether new members can access previous historical messages.

Request description{#req}

> <strong>Request Authentication</strong>: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/settings/set

> <strong>Content-Type</strong>: `application/json`

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


