---
title: Set the group verification type
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Set the group verification method.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/management/setgrpverifytype

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                                                                 |  |
|:------------|:----------|:---------|:----------------------------------------------------------------------------|--|
| group_id   | string    | Yes      | The ID of the group.                                                        |  |
| verify_type | int       | Yes      | Verification type: 0 - No verification required; 1 - Administrator approval required; 2 - New members are denied entry. Default is 0. |  |


### Request Example{#req_demo}
``` js
POST /jim/groups/management/setgrpverifytype HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "verify_type": 1
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
|:--------------|:------------|--|
