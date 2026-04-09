---
title: 封禁用户
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

封禁用户后用户无法与 IM Server 建立连接，客户端连接会返回用户 [已封禁](../../status/#connection) 状态码，如果已经连接成功的用户被封禁，当次连接不受影响。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/banusers/ban

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_ids|array|是|需要封禁的用户id列表||
|end_time|number|否|封禁结束的时间戳(ms)，为0时，表示永久封禁||
|end_time_offset|number|否|单位：毫秒。当不指定end_time时，服务端使用end_time_offset+当前时间来计算end_time||
|scope_key|string|是|封禁的范围，default:该用户封禁；platform:该用户指定的平台类型封禁；device:该用户指定的设备封禁;ip:该用户指定的ip封禁；||
|scope_value|string|否|与scope_key配合使用，如按平台封禁，scope_key=platform，则scope_value用来指定平台列表(多个间用逗号隔开)||
|ext|string|否|封禁时携带的扩展信息，可用于被封禁时的自定义提示，限制100字节内||


### 请求示例{#req_demo}
```js
POST /apigateway/users/banusers/ban HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "items":[
    {
      "user_id":"user1",
      "scope_key":"default",
      "scope_value":"xx",
      "ext":"aabbcc"
    },
    {
      "user_id":"user2",
      "end_time":1715846960362,
      "scope_key":"device",
      "scope_value":"xxxxxxxx,yyyyyyy",
      "ext":"aabbcc"
    },
    {
      "user_id":"user2",
      "end_time_offset":300000,
      "scope_key":"platform",
      "scope_value":"iOS,Android",
      "ext":"aabbcc"
    },
    {
      "user_id":"user4",
      "scope_key":"ip",
      "scope_value":"127.0.0.1,172.20.30.12",
      "ext":"aabbcc"
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