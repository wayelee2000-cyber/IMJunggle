---
title: 登录
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

登录接口，用于账号/手机号/邮箱+密码 登录

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/login

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|account|string|否|账号，建议字母+数字组合，长度5~20位, 注：account,phone,email 三选一即可||
|phone|string|否|手机号||
|email|string|否|邮箱地址||
|password|string|是|账号密码||


### 请求示例{#req_demo}
``` js
POST /jim/login HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "account":"username",
  "password":"xxxxxx"
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
````````````- [账户密码登录](./passlogin)
- [短验登录](./smslogin)
- [邮箱登录](./emaillogin)
- [登录二维码](./getloginqr)
- [检查扫码状态](./checkqr)
- [扫码确认](./confirmqr)
