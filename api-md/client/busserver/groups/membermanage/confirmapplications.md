---
title: Approval of Application for Invitation to Join the Group
hide_title: true
sidebar_position: 9
---
### Function Description{#intro}

The administrator approves an application to join the group.

### Request Description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/grpapplications/confirm

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter      | Data Type | Required | Description          |   |
|:---------------|:----------|:---------|:---------------------|---|
| application_id | string    | Yes      | Application ID       |   |
| is_agree       | bool      | Yes      | Approval status      |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/grpapplications/confirm HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "application_id": "xxxxxx",
  "is_agree": true
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