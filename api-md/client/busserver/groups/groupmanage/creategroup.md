---
title: Create group
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Create a group.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/create

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter          | Data type | Required | Description              |   |
|:-------------------|:----------|:---------|:-------------------------|---|
| group_name         | string    | yes      | Group nickname           |   |
| group_portrait     | string    | no       | Group avatar             |   |
| members.user_id    | string    | yes      | User ID of group member  |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/create HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_name": "group1",
  "group_portrait": "https://aaaa.png",
  "member_ids": ["userid1", "userid2"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "group_id": "groupid1",
    "group_name": "group1",
    "group_portrait": "https://aaaa.png"
  }
}
```

### Response code

| Response code | Description |   |
|:--------------|:------------|---|
