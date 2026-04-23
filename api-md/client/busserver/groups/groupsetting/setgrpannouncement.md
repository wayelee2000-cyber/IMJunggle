---
title: Set up group announcement
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Configure group announcements.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/setgrpannouncement

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description               |   |
|:-----------|:----------|:---------|:--------------------------|---|
| group_id   | string    | yes      | Group ID                  |   |
| content    | string    | yes      | Group announcement content|   |


### Request Example{#req_demo}
``` js
POST /jim/groups/setgrpannouncement HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "group1",
  "content": "xxxxxxxx"
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
