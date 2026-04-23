---
title: Destroy chatroom
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

Destroys a chatroom.  
<div style="margin: 1rem 0; padding: 1rem 1.25rem; border-left: 4px solid #e5484d; background: #fff1f2; border-radius: 0 16px 16px 0;">
<p style="margin: 0 0 0.75rem; font-size: 1rem; font-weight: 700; color: #b42318;">Warning</p>
<p style="margin: 0; color: #344054;">Once the chatroom is destroyed, all members and attributes associated with the chatroom will be permanently deleted.</p>
</div>
Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/chatrooms/destroy

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter | Data type | Required | Description          |   |
|:----------|:----------|:---------|:---------------------|---|
| chat_id   | string    | Yes      | The ID of the chatroom |   |


### Request Example{#req_demo}
``` js
POST /apigateway/chatrooms/destroy HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id": "chatroom1"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```

