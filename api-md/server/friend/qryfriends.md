---
title: 查询好友列表
hide_title: true
sidebar_position: 3
---

### 功能说明{#intro}

查询好友列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/friends/query

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|用户的id||
|order|int|否|好友列表的排序规则，0：倒序；1：正序||
|limit|int|否|一次查询好友列表的数量，默认100||
|offset|string|否|分页偏移量||


### 请求示例{#req_demo}
``` js
GET /apigateway/friends/query?user_id=userid1&limit=100 HTTP/1.1
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
        "friend_id":"userid2",
        "display_name":"xxx"
      }
    ],
    "offset":"xxxx"
  }
}
```