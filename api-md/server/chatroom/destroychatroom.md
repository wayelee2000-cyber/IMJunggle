---
title: 销毁聊天室
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

销毁一个聊天室。
:::danger 
聊天室销毁后，聊天室相关的成员，属性均会被清空
:::

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/chatrooms/destroy

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|chat_id|string|是|聊天室的id||


### 请求示例{#req_demo}
``` js
POST /apigateway/chatrooms/destroy HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id":"chatroom1"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```