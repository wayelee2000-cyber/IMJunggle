---
title: Remove user blacklist
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Remove users from the blacklist.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api#api)/jim/users/blockusers/del

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter       | Data type | Required | Description                 |   |
|:----------------|:----------|:---------|:----------------------------|---|
| block_user_ids  | array     | yes      | A list of user IDs to remove from the blacklist |   |


### Request Example{#req_demo}
``` js
POST /jim/users/blockusers/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "block_user_ids": ["userid1", "userid2"]
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