---
title: 登录二维码
hide_title: true
sidebar_position: 7
---
### 功能说明{#intro}

获取用于登录的二维码

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/login/qrcode

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|email|string|是|邮箱||
|code|string|是|邮箱收到的验证码||


### 请求示例{#req_demo}
``` js
GET /jim/login/qrcode HTTP/1.1
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
    "id":"二维码唯一标识",
    "qr_code":"二维码图片的base64数据"
  }
}
```