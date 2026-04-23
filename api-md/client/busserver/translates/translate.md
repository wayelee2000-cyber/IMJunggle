---
title: translation
hide_title: true
sidebar_position: 1
---
### Function description{#intro}

Translation interface

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/translate

> **Content-Type**: `application/json`


### Request parameters {#param}


### Request Example{#req_demo}
``` js
POST /jim/translate HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "items":[
    {
      "key":"xxx",
      "content":"original text"
    }
  ],
  "source_lang":"zh",
  "target_lang":"en"
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
        "key": "xxx",
        "content": "Translated content"
      }
    ],
    "source_lang": "zh",
    "target_lang": "en"
  }
}
```

### Response code

| Response code | Description |  |
|:-------------:|:-----------:|:-:|
