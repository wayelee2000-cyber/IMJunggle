---
title: Set ban on group members
hide_title: true
sidebar_position: 8
---
### Function description{#intro}

Banned group members will no longer be able to send messages within the group.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/management/setgrpmembersmute

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter   | Data type | Required | Description                     |   |
|:------------|:----------|:---------|:--------------------------------|---|
| group_id   | string    | Yes      | The ID of the group             |   |
| member_ids | array     | Yes      | List of group member IDs to ban |   |
| is_mute    | int       | Yes      | 0: Unmute; 1: Mute              |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/management/setgrpmembersmute HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "member_ids": ["userid1", "userid2"],
  "is_mute": 1
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