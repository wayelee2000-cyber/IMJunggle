---
title: 查询在线状态
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

批量查询用户的在线状态，当前功能用于首次展示用户状态，若想实时感知用户在线离线状态，请使用用户 [上下线订阅](../../subscription/onlineofflinesub) 功能实现

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/onlinestatus/query

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_ids|array|是|需要查询在线状态的用户id列表||

### 请求示例{#req_demo}

```js
POST /apigateway/users/onlinestatus/query HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_ids":["userid1","userid2"]
}
```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|user_id|string|用户的 Id ||
|is_online|bool|用户是否在线||

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
      {
        "user_id":"user1",
        "is_online":true
      },
      {
        "user_id":"user2",
        "is_online":false
      }
    ]
  }
}
```