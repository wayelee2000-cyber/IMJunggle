---
title: Update post
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Update a post.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/posts/update

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /jim/posts/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "post_id": "xxxxxxx",
  "content": {
    "text": "Moments text",
    "images": [
      {
        "url": "image url"
      }
    ],
    "video": {
      "url": "video url"
    }
  }
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

| Response code | Description |  |
|:-------------:|:-----------:|:--|