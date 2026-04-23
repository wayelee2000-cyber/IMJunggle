---
title: Check if Group Member
hide_title: true
sidebar_position: 7
---
### Function Description{#intro}

Check whether a user is a member of a group.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/members/check

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter   | Data Type | Required | Description          |   |
|:------------|:----------|:---------|:---------------------|---|
| group_id   | string    | yes      | Group ID             |   |
| member_ids | array     | yes      | List of user IDs     |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/members/check HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["userid1", "userid2"]
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "group_id": "groupid1",
    "group_member_map": {
      "userid1": true,
      "userid2": false
    }
  }
}
```

### Response Codes

| Response Code | Description |   |
|:--------------|:------------|---|

