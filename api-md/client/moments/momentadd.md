---
title: Post to Moments
hide_title: true
sidebar_position: 1
---
### Function Description{#intro}

Post a moment to your circle of friends, supporting images, text, and videos.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/momentgateway/moments/add

> **Content-Type**: `application/json`


### Request Parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "content": {
    "text": "Moments text",
    "medias": [
      {
        "type": "image",
        "url": "xxx",
        "snapshot_url": "xxxx",
        "height": 100,
        "width": 100
      },
      {
        "type": "video",
        "url": "xxxx",
        "snapshot_url": "xxxx",
        "duration": 10,
        "height": 100,
        "width": 100
      }
    ]
  }
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "moment_id": "xxx",
    "moment_time": 17212345678,
    "user_info": {
      "user_id": "xxx",
      "nickname": "xxxxx",
      "avatar": "xxxx"
    }
  }
}
```

### Response Codes

| Response Code | Description |  |
|:-------------:|:-----------:|:-:|