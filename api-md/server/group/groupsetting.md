---
title: 更新群设置
hide_title: true
sidebar_position: 6
---

### 功能说明{#intro}

群组支持多种参数设置，例如新进入群组成员是否可以获取之前的历史消息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/settings/set

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|hide_grp_msg|int|否|控制是否隐藏入群前的历史消息；0:不隐藏；1:隐藏；||

### 请求示例{#req_demo}
```js
POST /apigateway/groups/settings/set HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "settings":{
    "hide_grp_msg":"1"
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