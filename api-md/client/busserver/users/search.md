---
title: 搜索用户
hide_title: true
sidebar_position: 4
---
### 功能说明{#intro}

根据手机号搜索用户

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/search

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|keyword|string|是|对方手机号，邮箱或账号||


### 请求示例{#req_demo}
``` js
POST /jim/users/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "keyword":"13812345678"
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
            "user_id":"userid1",
            "nickname":"user1",
            "avatar":"xxxxxxx",
            "is_friend":false
        }
    ]
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|