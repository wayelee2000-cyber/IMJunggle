---
title: Invite to the group
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Update group information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/invite

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                          |   |
|:------------|:----------|:---------|:-----------------------------------|---|
| group_id    | string    | yes      | The ID of the group                 |   |
| member_ids  | array     | yes      | List of user IDs to be invited to the group |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/invite HTTP/1.1
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
|:--------------|:------------|:--|
