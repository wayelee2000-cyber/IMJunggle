---
title: Like list
hide_title: true
sidebar_position: 23
---
### Function description{#intro}

Retrieve the list of likes for a post.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/momentgateway/moments/reactions/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                  |   |
|:-----------|:----------|:---------|:----------------------------|---|
| moment_id  | string    | yes      | The ID of the post          |   |


### Request Example{#req_demo}
``` js
GET /momentgateway/moments/reactions/list?moment_id=xxx HTTP/1.1
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
        "key": "k1",
        "value": "v1",
        "timestamp": 1732123456789,
        "user_info": {
          "user_id": "xxx",
          "nickname": "xxxxx",
          "avatar": "xxxx",
          "user_type": 0
        }
      }
    ]
  }
}
```