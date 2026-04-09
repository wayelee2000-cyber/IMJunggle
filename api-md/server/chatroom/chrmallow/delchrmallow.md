---
title: 移除聊天室成员白名单
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

将聊天室成员从白名单中移除。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/chatrooms/allowmembers/del

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|chat_id|string|是|聊天室的id||
|member_ids|array|是|聊天室白名单成员id列表||


### 请求示例{#req_demo}
``` js
POST /apigateway/chatrooms/allowmembers/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id":"chatroom1",
  "member_ids":["member1","member2"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```