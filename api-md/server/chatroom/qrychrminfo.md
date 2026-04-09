---
title: 查询聊天室信息
hide_title: true
sidebar_position: 3
---

### 功能说明{#intro}

查询聊天室的基本信息，包括聊天室的昵称，属性列表，成员数量和部分成员信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/chatrooms/info

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|chat_id|string|是|聊天室的id||
|order|int|否|聊天室成员的排序规则，0：倒序；1：正序||
|count|int|否|查询聊天室成员的数量，默认100||


### 请求示例{#req_demo}
``` js
GET /apigateway/chatrooms/info?chat_id=xxx&order=0&count=100 HTTP/1.1
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
    "chat_id":"xxx",
    "chat_name":"xxx",
    "is_mute":false,
    "member_count":10000,
    "members":[
        {
            "member_id":"xxx",
            "member_name":"xxx",
            "added_time":172987634564
        }
    ],
    "atts":[
        {
            "key":"k1",
            "value":"v1",
            "att_time":172345678345,
            "user_id":"userid1"
        }
    ]
  }
}
```