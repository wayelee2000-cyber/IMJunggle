---
title: Update group information
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Update group information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/update

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter          | Data type | Required | Description             |   |
|:-------------------|:----------|:---------|:------------------------|---|
| group_id           | string    | yes      | Group ID                |   |
| group_name         | string    | yes      | Group nickname          |   |
| group_portrait     | string    | no       | Group avatar URL        |   |
| members.user_id    | string    | yes      | Group member user ID    |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "group_name": "group1",
  "group_portrait": "https://aaaa.png"
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