---
title: 账号注册
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

注册接口，支持账号密码注册，手机号注册，邮箱注册

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/register

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|account|string|否|账号，建议字母+数字组合，长度5~20位, 注：account,phone,email 三选一即可||
|phone|string|否|手机号||
|email|string|否|邮箱地址||
|code|string|否|手机号和邮箱注册时必填，为收到的6位数字验证码||
|password|string|是|账号密码||


### 请求示例{#req_demo}
``` js
POST /jim/register HTTP/1.1
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
  "msg":"sucess"
}
```