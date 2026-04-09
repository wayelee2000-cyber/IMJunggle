---
title: 设置群成员属性
hide_title: true
sidebar_position: 13
---

### 功能说明{#intro}

为群成员设置在本群内的属性，例如群昵称，群徽章等。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/members/update

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组 Id||
|member_id|string|是|群成员 Id||
|grp_display_name|string|否|该成员在本群的备注昵称||
|ext_fields|map|否|该成员在本群的扩展字段||


### 请求示例{#req_demo}
```js
POST /apigateway/groups/members/update HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "member_id":"member1",
  "grp_display_name":"群昵称",
  "ext_fields":{
    "k1":"v1",
    "k2":"v2"
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