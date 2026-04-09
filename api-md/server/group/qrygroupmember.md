---
title: 查询群成员
hide_title: true
sidebar_position: 9
---

### 功能说明{#intro}

查询单个群成员信息，用作和开发者服务端用群成员息对比，以开发者服务端群成员信息为准，开发者服务端群成员信息变更后需及时同步至 IM 服务端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/members/query

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组 Id||
|limit|int|否|分页参数||
|offset|string|否|分页偏移量||


### 请求示例{#req_demo}
```js
GET /apigateway/groups/members/query?group_id=group1&limit=50&offset=aabb HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

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
        "is_mute":0,
        "is_allow":0,
        "grp_display_name":"群昵称",
        "ext_fields":{
          "k1":"v1",
          "k2":"v2"
        }
      },
      {
        "member_id":"member2",
        "is_mute":0,
        "is_allow":0
      }
    ],
    "offset":"aabbcc"
  }
}
```