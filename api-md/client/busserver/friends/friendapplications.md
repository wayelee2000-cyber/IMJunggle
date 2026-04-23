---
title: Friend application list
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

List of friend applications

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/applications

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| start     | int       | No       | The start timestamp for the query list. When querying in reverse order, the default is the current time; when querying in forward order, the default is 0. |  |
| count     | int       | No       | Number of items per page. Default is 20, maximum is 50. |  |
| order     | int       | No       | Query order. 0: reverse order; 1: forward order; default is 0. |  |


### Request Example{#req_demo}
``` js
GET /jim/friends/applications?start=1734407505753&count=50 HTTP/1.1
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
    "items": [
      {
        "target_user": { // Application initiator user information
          "user_id": "userid1",
          "nickname": "user1",
          "avatar": "https://file.juggle.im/abcdfafsdaf.png"
        },
        "is_sponsor": true, // Is the initiator
        "status": 1,        // 0: Applying; 1: Approved; 2: Rejected; 3: Application expired
        "apply_time": 1734407505000 // Application initiation time
      }
    ]
  }
}
```
