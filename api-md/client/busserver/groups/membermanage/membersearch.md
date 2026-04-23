---
title: Search group members
hide_title: true
sidebar_position: 6
---
### Function description{#intro}

Search for group members.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/members/search

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                  |   |
|:-----------|:----------|:---------|:----------------------------|---|
| group_id  | string    | Yes      | Group ID                    |   |
| key       | string    | Yes      | Keyword                    |   |
| offset    | string    | No       | Paging offset               |   |
| limit     | number    | No       | Number of items per page, default is 100 |   |


### Request Example{#req_demo}
``` js
POST /jim/groups/members/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "key": "user"
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
        "nickname": "xxx",
        "avatar": "xxxxxxx",
        "member_type": 0
      }
    ],
    "offset": "xxxx"
  }
}
```

### Response code

| Response code | Description |   |
|:--------------|:------------|---|
