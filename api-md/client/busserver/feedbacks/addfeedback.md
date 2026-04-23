---
title: Report feedback
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Submit feedback information.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/feedbacks/add

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /jim/feedbacks/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "category": "Feedback Category",
  "text": "Feedback content",
  "images": ["https://xxxxx.jpg"],
  "videos": ["https://xxxxx.mp3"]
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

|Response code|Description||
|:--|:---|:--|
