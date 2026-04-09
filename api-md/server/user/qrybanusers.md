---
title: 查询封禁列表
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

查询已封禁用户列表，支持分页查询。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/banusers/query

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|limit|int|否|分页参数，每页的数量||
|offset|string|否|偏移量，用于分页||

### 请求示例{#req_demo}

```js
GET /apigateway/users/banusers/query?limit=20&offset="" HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|user_id|string|封禁用户id||
|created_time|number|添加封禁的时间||
|end_time|number|结束封禁的时间(ms)，为0时表示永久封禁||

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
      {
        "user_id":"user1",
        "created_time":1672233498000 
      },
      {
        "user_id":"user2",
        "created_time":1672233498000, 
        "end_time":1723455443563 
      }
    ],
    "offset":"aabbcc"
  }
}
```