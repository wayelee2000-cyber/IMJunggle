---
title: 短验登录
hide_title: true
sidebar_position: 4
---
### 功能说明{#intro}

使用手机号和短信验证码登录

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/sms/login

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|phone|string|是|手机号||
|code|string|是|收到的短信验证码||


### 请求示例{#req_demo}
``` js
POST /jim/sms/login HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone":"15212345678",
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