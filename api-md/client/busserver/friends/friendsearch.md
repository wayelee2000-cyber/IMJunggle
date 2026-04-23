---
title: Friend Search
hide_title: true
sidebar_position: 6
---
### Function Description{#intro}

Search my friends.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/search

> **Content-Type**: `application/json`


### Request Parameters {#param}

| Parameter | Data Type | Required | Description |  |
|:----------|:----------|:---------|:------------|:--|
| key       | string    | yes      | Keyword     |  |
| offset    | string    | no       | Paging offset |  |
| limit     | number    | no       | Number of items per page, default is 100 |  |

### Request Example{#req_demo}
``` js
POST /jim/friends/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "key": "user"
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "user_id": "userid1",
        "nickname": "user1",
        "avatar": "https://file.juggle.im/abcdfafsdaf.png",
        "user_type": 0
      },
      {
        "user_id": "userid2",
        "nickname": "user2",
        "avatar": "https://file.juggle.im/abcdfafsdaf.png",
        "user_type": 0
      }
    ]
  }
}
```

