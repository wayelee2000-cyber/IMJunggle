---
title: 设置好友备注名
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

为好友设置备注名

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/friends/setdisplayname

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|用户的id||
|friend_id|string|是|好友用户id||
|display_name|string|是|好友备注名||


### 请求示例{#req_demo}
``` js
POST /apigateway/friends/setdisplayname HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "friend_id":"userid2",
  "display_name":"u2"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```