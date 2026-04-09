---
title: 设置群成员禁言
hide_title: true
sidebar_position: 10
---

### 功能说明{#intro}

禁止群成员在群里发送消息，例如群管理员可将某个成员设置为禁止发言，禁言后不可以发送群消息，可以接收群消息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/groupmembermute/set

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组 Id||
|member_ids|array|是|群成员 Id 列表||
|is_mute|int|是|0:未禁言; 1:禁言||
|mute_minute|int|否|禁言的时长，到期后自动解封，单位：分钟，传0时表示永久禁言||


### 请求示例{#req_demo}
```js
POST /apigateway/groups/groupmembermute/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "member_ids":["member1","member2"]
  "is_mute":1,
  "mute_minute":10
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```