---
title: Remove administrator
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Remove a group administrator.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/management/administrators/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description           |   |
|:-----------|:----------|:---------|:----------------------|---|
| group_id   | string    | yes      | Group ID              |   |
| admin_ids  | array     | yes      | List of admin user IDs |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/management/administrators/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "group1",
  "admin_ids": ["userid1", "userid2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response code

| Response code | Description |   |
|:--------------|:------------|---|