---
title: Check online status
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Query a user's online status.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/onlinestatus

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description       |   |
|:----------|:----------|:---------|:------------------|---|
| user_ids  | array     | yes      | List of user IDs  |   |


### Request Example{#req_demo}
``` js
POST /jim/users/onlinestatus HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_ids": ["userid1", "userid2", "userid3"]
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "user_id": "userid1",
        "is_online": true
      },
      {
        "user_id": "userid2",
        "is_online": false
      },
      {
        "user_id": "userid3",
        "is_online": false
      }
    ]
  }
}
```

### Response code

| Response code | Description |   |
|:--------------|:------------|---|
