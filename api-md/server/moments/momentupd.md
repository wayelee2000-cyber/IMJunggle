---
title: Update Moments
hide_title: true
sidebar_position: 2
---
### Function Description{#intro}

Update Moments.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/momentgateway/moments/update

> **Content-Type**: `application/json`


### Request Parameters {#param}


### Request Example{#req_demo}
``` js
POST /momentgateway/moments/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"userid1",   // The user performing the update
  "moment_id":"xxxxxxx",
  "content":{
    "text":"Moments text",
    "medias":[
      {
        "type":"image",
        "url":"xxx",
        "snapshot_url":"xxxx",
        "height":100,
        "width":100
      },{
        "type":"video",
        "url":"xxxx",
        "snapshot_url":"xxxx",
        "duration":10,
        "height":100,
        "width":100
      }
    ]
  }
}
```

### Response Example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

### Response Codes

| Response Code | Description |
|:-------------:|:-----------:|