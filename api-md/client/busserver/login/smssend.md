---
title: 短信验证码
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

发送短信验证码

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/sms/send

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|phone|string|是|手机号||


### 请求示例{#req_demo}
``` js
POST /jim/sms/send HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone":"15212345678"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```