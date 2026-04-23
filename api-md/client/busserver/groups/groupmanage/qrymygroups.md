---
title: Query the list of joined groups
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Retrieve the list of groups I have joined.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/mygroups

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| offset   | string    | No       | Paging offset; leave blank for the first request |  |
| count    | int       | No       | Number of items to return per request |  |


### Request Example{#req_demo}
``` js
GET /jim/groups/mygroups?count=100 HTTP/1.1
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
    "items": [{
      "group_id": "groupid1",
      "group_name": "group1",
      "group_portrait": "https://xxxxxx.png"
    }],
    "offset": "xxxx"
  }
}
```

### Response code

| Response code | Description |  |
|:--------------|:------------|:--|
