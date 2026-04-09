---
title: 检查扫码状态
hide_title: true
sidebar_position: 8
---
### 功能说明{#intro}

检查二维码是否已被扫码

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/qrcode/check

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|id|string|是|要检查的二维码id， 建议每3秒检查一次，扫码成功即可返回登录信息||


### 请求示例{#req_demo}
``` js
POST /jim/qrcode/check HTTP/1.1
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
### 响应码

|响应码|说明||
|:--|:---|:--|
|17006|还未被扫码，继续检查||
|17007|二维码已过期||
