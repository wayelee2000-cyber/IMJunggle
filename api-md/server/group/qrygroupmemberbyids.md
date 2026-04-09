---
title: 按成员 ID 查询信息
hide_title: true
sidebar_position: 12
---

### 功能说明{#intro}

查询群组中指定群成员的信息，例如查询某个群成员在群里禁言状态等。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/members/querybyids

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|member_ids|array|是|群成员id列表||


### 请求示例{#req_demo}
```js
POST /apigateway/groups/members/querybyids HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
  "member_ids":["member1","member2"]
}
```
### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
      {
        "member_id":"member1",
        "is_mute":0
      },
      {
        "member_id":"member2",
        "is_mute":0
      }
    ]
  }
}
```