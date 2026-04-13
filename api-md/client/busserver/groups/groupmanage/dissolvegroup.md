---
title: Disband Group
hide_title: true
sidebar_position: 3
---
### Function Description{#intro}

Update group information by disbanding the group.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/dissolve

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter  | Data Type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| group_id   | string    | yes      | The ID of the group to be disbanded | |


### Request Example{#req_demo}
``` js
POST /jim/groups/dissolve HTTP/1.1
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