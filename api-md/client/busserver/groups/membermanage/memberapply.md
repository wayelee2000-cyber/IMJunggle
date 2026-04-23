---
title: Apply to Join a Group
hide_title: true
sidebar_position: 5
---
### Function Description{#intro}

User applies to join a group.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/apply

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter  | Data Type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| group_id  | string    | yes      | Group ID    |  |


### Request Example{#req_demo}
``` js
POST /jim/groups/apply HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response Codes

| Response Code | Description |  |
|:--------------|:------------|:--|

