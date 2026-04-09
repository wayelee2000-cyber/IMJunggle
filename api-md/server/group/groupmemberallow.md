---
title: 设置群成员白名单
hide_title: true
sidebar_position: 11
---

### 功能说明{#intro}

设置群组禁言后，如允许部分用户可以发送消息，可将指定用户加入群组白名单中。

:::danger 优先级
若开发者同时调用 `群组禁言`、`群成员禁言`、`群成白名单`，群成白名单优先级最高，白名单中的用户依然可以发送消息
:::

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/groupmemberallow/set

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组 Id||
|member_ids|array|是|群成员 Id 列表||
|is_allow|int|是|0:非白名单用户；1:白名单用户；||


### 请求示例{#req_demo}
```js
POST /apigateway/groups/groupmemberallow/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "member_ids":["member1","member2"]
  "is_allow":1
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```