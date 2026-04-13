---
title: Remove group members
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Remove members from a group.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request rate limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/members/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                          |   |
|:------------|:----------|:---------|:-----------------------------------|---|
| group_id    | string    | yes      | The ID of the group                |   |
| member_ids  | array     | yes      | List of user IDs to be removed from the group |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/members/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["userid1", "userid2"]
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