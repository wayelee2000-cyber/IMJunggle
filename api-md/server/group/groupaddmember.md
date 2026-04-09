---
title: 添加群成员
hide_title: true
sidebar_position: 7
---

### 功能说明{#intro}

开发者服务端群成员变更后，将新成员同步至 IM 服务端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/members/add

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|group_name|string|否|群组昵称||
|member_ids|array|是|入群的用户id列表||

### 请求示例{#req_demo}

```json
POST /apigateway/groups/members/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "group_name":"group1",
  "member_ids":["userid1","userid2"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```