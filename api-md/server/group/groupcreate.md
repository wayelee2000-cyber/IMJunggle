---
title: 创建群组
hide_title: true
sidebar_position: 1
---

### 功能说明{#intro}

将开发者服务端创建的群组同步至 IM 服务，用于消息发送、会话列表展示和消息推送等，群组支持扩展信息，例如自定义群等级。

:::danger 群组创建通知
群组创建成功后，IM 服务端 **不会** 发送创建群通知，开发者需要自定义通知消息发送至群里
:::

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/add

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|group_name|string|否|群组昵称||
|member_ids|array|是|入群的用户id列表||
|ext_fields|map|否|群组扩展信息，KV 格式||


### 请求示例{#req_demo}
``` js
POST /apigateway/groups/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "group_name":"group1",
  "member_ids":["userid1","userid2"],
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