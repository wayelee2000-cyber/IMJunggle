---
title: 单聊禁言列表
hide_title: true
sidebar_position: 8
---

### 功能说明{#intro}

查询当前应用下被禁止单聊私信的用户列表，支持分页查询。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/blockusers/query

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|查询单聊禁言的用户||
|limit|int|否|分页参数，一页的数量||
|offset|string|否|偏移量，用于分页||

### 请求示例{#req_demo}
```js
GET /apigateway/users/blockusers/query?user_id=user1&limit=20&offset="" HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|block_user_id|array|禁言的用户id列表||
|created_time|number|添加封禁的时间||
|offset|string|用于分页的偏移量||

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "user_id":"user1",
    "items":[
      {
        "block_user_id":"user2",
        "created_time":1672233498000 
      },
      {
        "block_user_id":"user3",
        "created_time":1672233498000
      }
    ],
    "offset":"aaddcxx"
  }
}
```

