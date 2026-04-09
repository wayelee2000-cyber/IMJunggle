---
title: 查询用户信息
hide_title: true
sidebar_position: 10
---

### 功能说明{#intro}

查询单个用户信息，用作和开发者服务端用户信息对比，以开发者服务端用户信息为准，开发者服务端用户信息变更后需及时同步至 IM 服务端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/info

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|查询单聊禁言的用户||

### 请求示例{#req_demo}
```js
GET /apigateway/users/info?user_id=user1 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|user_id|string|是| 用户 Id||
|nickname|string|否|用户昵称||
|user_portrait|string|否|用户头像||
|ext_fields|map|否|扩展字段列表||

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "user_id":"user1",
    "nickname":"user1",
    "user_portrait":"xxxxx",
    "ext_fields":{
      "field1":"aaa",
      "field2":"bbb"
    }
  }
}
```

