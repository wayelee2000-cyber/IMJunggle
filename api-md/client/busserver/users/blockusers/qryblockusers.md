---
title: 查询黑名单用户列表
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

查询黑名单用户列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/blockusers/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|count|int|否|分页参数，一页数据数量,默认20||
|offset|string|否|分页偏移量||


### 请求示例{#req_demo}
``` js
GET /jim/users/blockusers/list?count=20&offset=xxx HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
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
        "user_id":"userid1",
        "nickname":"user1",
        "avatar":"https://aaabbcc.png"
      },{
        "user_id":"userid2",
        "nickname":"user2",
        "avatar":"https://aaabbcc.png"
      }
    ],
    "offset":"xxx"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|