---
title: Add Bot
hide_title: true
sidebar_position: 2
---
### Function Description{#intro}

Add a Telegram Bot.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/telegrambots/add

> **Content-Type**: `application/json`


### Request Parameters {#param}


### Request Example{#req_demo}
``` js
POST /jim/telegrambots/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "bot_name":"xxxxxxxxxxxx",
  "bot_token":"xxxx"
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

| Response Code | Description  |  |
|:-------------:|:------------|:--|
| 17300         | Add failed  |  |

