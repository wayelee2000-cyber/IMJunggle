---
title: 解禁用户
hide_title: true
sidebar_position: 3
---

### 功能说明{#intro}

解禁用户后可重新连接，支持按 `平台`、`设备`、`用户` 维度解禁用户，便于开发者灵活控制用户的权限校验。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/banusers/unban

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|需要解禁的用户id||
|scope_key|string|否|按封禁范围解禁，不传时解禁所有范围。取值范围：default:该用户封禁；platform:该用户指定的平台类型封禁；device:该用户指定的设备封禁;ip:该用户指定的ip封禁；||


### 请求示例{#req_demo}

```js
POST /apigateway/users/banusers/unban HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "items":[
    {
      "user_id":"user1",
      "scope_key":"default"
    },
    {
      "user_id":"user2"
    }
  ]
}
```
### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```
