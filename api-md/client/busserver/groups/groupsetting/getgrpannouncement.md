---
title: Query group announcement
hide_title: true
sidebar_position: 6
---
### Function description{#intro}

Query the group announcement.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/getgrpannouncement

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| group_id  | string    | yes      | Group ID    |  |


### Request Example{#req_demo}
``` js
GET /jim/groups/getgrpannouncement HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "group_id": "group1",
    "content": "xxxxxxxx"
  }
}
```

### Response code

| Response code | Description |  |
|:--------------|:------------|:--|