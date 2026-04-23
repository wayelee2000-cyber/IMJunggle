---
title: Set group nickname
hide_title: true
sidebar_position: 7
---
### Function description{#intro}

Set a group nickname.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/setdisplayname

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter       | Data type | Required | Description       |   |
|:----------------|:----------|:---------|:------------------|---|
| group_id        | string    | yes      | Group ID          |   |
| grp_display_name | string    | yes      | Group nickname    |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/setdisplayname HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "group1",
  "grp_display_name": "xxxxxxxx"
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
