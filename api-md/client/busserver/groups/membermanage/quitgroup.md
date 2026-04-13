---
title: Exit group
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Exit a group.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/quit

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| group_id  | string    | yes      | The ID of the group to exit |  |


### Request Example{#req_demo}
``` js
POST /jim/groups/quit HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1"
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