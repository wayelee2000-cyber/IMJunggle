---
title: 查询群信息
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

查询单个群组信息，用作和开发者服务端用群组信息对比，以开发者服务端群组信息为准，开发者服务端群组信息变更后需及时同步至 IM 服务端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/info

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||


### 请求示例{#req_demo}
```js
GET /apigateway/groups/info?group_id=group1 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|group_id|string|群组id||
|group_name|string|群组的昵称||
|is_mute|int|0:未禁言；1:禁言；||
|ext_fields|map|群扩展字段||

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "group_id":"group1",
    "group_name":"group1",
    "is_mute":0,
    "ext_fields":{
      "field1":"aaa",
      "field2":"bbb"
    }
  }
}
```