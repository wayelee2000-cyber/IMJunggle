---
title: 绑定手机号
hide_title: true
sidebar_position: 8
---
### 功能说明{#intro}

使用短信验证码，绑定手机号

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/bindphone

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|phone|string|是|手机号||
|code|string|是|验证码||


### 请求示例{#req_demo}
``` js
POST /jim/users/bindphone HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "phone":"13812345678",
  "code":"123456"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|