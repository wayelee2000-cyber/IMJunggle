---
title: 邮箱登录
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

使用邮箱和验证码登录

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/email/login

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|email|string|是|邮箱||
|code|string|是|邮箱收到的验证码||


### 请求示例{#req_demo}
``` js
POST /jim/email/login HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "email":"xxxx@abc.com",
  "code":"000000"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "user_id":"userid1",
    "authorization":"xxxxxxxxx",
    "nickname":"user1",
    "avatar":"xxxxxxxx",
    "status":0,
    "im_token":"xxxxxxxxx"
  }
}
```