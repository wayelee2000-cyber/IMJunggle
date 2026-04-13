---
title: Can new members view historical messages when joining the group?
hide_title: true
sidebar_position: 4
---
### Function description{#intro}

Can new members view historical messages when they join the group? By default, they cannot.

### Request description{#req}

> **Request Authentication**: This API requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/management/sethismsgvisible

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter             | Data type | Required | Description                      |   |
|:----------------------|:----------|:---------|:--------------------------------|---|
| group_id              | string    | Yes      | Group ID                       |   |
| group_his_msg_visible | int       | Yes      | 0: Not viewable; 1: Viewable; Default is 0 |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/management/sethismsgvisible HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "group_his_msg_visible": 1
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