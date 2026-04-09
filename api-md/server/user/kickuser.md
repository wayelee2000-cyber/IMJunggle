---
title: 踢用户下线
hide_title: true
sidebar_position: 11
---

### 功能说明{#intro}

将已经连接至 IM 服务的用户踢下线，支持按 `平台`、`设备`、`用户` 维度踢用户下线，当前接口仅对当次连接有效，不影响用户后续连接，例如某个用户多个设备登录，在后登录的设备将其他设备踢掉线。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/kick

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|要踢下线的用户 Id||
|platforms|array|否|按指定设备类型来踢，这个字段非必填，不传时默认踢所有端||
|device_ids|array|否|需要踢下线的设备唯一标识||
|ext|string|否|扩展字段，该字段会在用户收到被踢通知时，由 SDK 返给业务层，可用于定制化提醒等||

### 请求示例{#req_demo}
```js
GET /apigateway/users/kick HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "platforms":["iOS","Android"],
  "device_ids":["xxxxx","yyyyy"]
}

```

### 响应示例{#res_demo}
```json
{
  "code":0,
  "message":"success"
}
```

