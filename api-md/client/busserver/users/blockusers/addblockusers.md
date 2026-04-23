---
title: Add User to Blacklist
hide_title: true
sidebar_position: 1
---
### Function Description{#intro}

Add users to the blacklist.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/users/blockusers/add

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter       | Data Type | Required | Description                 |   |
|:----------------|:----------|:---------|:----------------------------|---|
| block_user_ids  | array     | yes      | List of user IDs to blacklist |   |


### Request Example{#req_demo}
``` js
POST /jim/users/blockusers/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "block_user_ids": ["userid1", "userid2"]
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

| Response Code | Description |   |
|:--------------|:------------|---|

