---
title: Change group owner
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Only the current group owner can change the group owner, and the new owner must be a member of the group.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/management/chgowner

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description               |  |
|:-----------|:----------|:---------|:--------------------------|:--|
| group_id   | string    | yes      | Group ID                  |   |
| owner_id   | string    | yes      | New group owner user ID   |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/management/chgowner HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "owner_id": "userid2"
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

| Response code | Description |  |
|:--------------|:------------|:--|
