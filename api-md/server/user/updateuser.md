---
title: 更新用户信息
hide_title: true
sidebar_position: 9
---
### 功能说明{#intro}

IM Server 存储用户信息，用于展示消息发送信息或会话信息，当用户信息变更，需将变更后的信息调用此接口同步给 IM 服务。

:::danger 用户信息同步时机
用户信息更新后 IM 服务 **不会主动通知** 至客户端，与当前用户有关的会话产生消息后会 IM 服务会自动将最新的用户信息同步至客户端
:::

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/update

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|需要更新的用户id||
|nickname|string|否|昵称||
|user_portrait|string|否|头像||
|ext_fields|map|否|扩展字段列表||

### 请求示例{#req_demo}

```js
POST /apigateway/users/update HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "nickname":"user1",
  "user_portrait":"xxxxx",
  "ext_fields":{
    "field1":"aaa",
    "field2":"bbb"
  }
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```