---
title: Bot list
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Query the list of Bots.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/bots/list

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| offset   | string    | No       | Used for pagination; specifies the starting position in the Bot list. |  |
| count    | int       | No       | Number of items per page; default is 20, maximum is 50. |  |


### Request Example{#req_demo}
``` js
GET /jim/bots/list?count=50 HTTP/1.1
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
        "bot_id": "botid1",
        "nickname": "bot1",
        "avatar": "https://file.juggle.im/abcdfafsdaf.png"
      },
      {
        "user_id": "botid2",
        "nickname": "bot2",
        "avatar": "https://file.juggle.im/abcdfafsdaf.png"
      }
    ],
    "offset": "xxxx"
  }
}
```
