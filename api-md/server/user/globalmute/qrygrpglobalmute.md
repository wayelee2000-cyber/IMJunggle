---
title: 查询禁发群聊消息用户
hide_title: true
sidebar_position: 6
---

### 功能说明{#intro}

查询禁发群聊消息用户列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/group/globalmutemembers/query

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|offset|string|否|用于分页查询的偏移量，每次查询列表时会返回下次的offset，初次可传空||
|limit|int|否|查询数量，默认100，最大1000||


### 请求示例{#req_demo}
``` js
POST /apigateway/group/globalmutemembers/query?offset=xx&limit=100 HTTP/1.1
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
            "user_id":"xxx",
            "created_time":172987634564
        }
    ],
    "offset":"xxxx"
  }
}
```