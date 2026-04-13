---
title: Search for groups to join
hide_title: true
sidebar_position: 6
---
### Function description{#intro}

Search for groups I have joined.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/mygroups/search

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| keyword  | string    | Yes      | Search keyword |  |
| offset   | string    | No       | Paging offset; leave blank for the first request |  |
| limit    | int       | No       | Number of items returned per request |  |


### Request Example{#req_demo}
``` js
POST /jim/groups/mygroups/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "keyword": "group",
  "limit": 100
}
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