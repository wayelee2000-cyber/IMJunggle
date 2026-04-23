---
title: Remove Bot
hide_title: true
sidebar_position: 3
---
### Function Description{#intro}

Remove a Telegram Bot.

### Request Description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/telegrambots/batchdel

> **Content-Type**: `application/json`


### Request Parameters {#param}


### Request Example{#req_demo}
``` js
POST /jim/telegrambots/batchdel HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "bot_ids": ["id1", "id2"]
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

