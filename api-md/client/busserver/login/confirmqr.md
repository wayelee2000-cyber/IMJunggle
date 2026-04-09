---
title: 扫码确认
hide_title: true
sidebar_position: 9
---
### 功能说明{#intro}

手机扫码，并确认允许登录

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/qrcode/confirm

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|id|string|是|扫码得到的二维码id||


### 请求示例{#req_demo}
``` js
POST /jim/qrcode/confirm HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "id":"xxxxxxx"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```
