---
title: 更新用户信息
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

更新用户的基本信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/update

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|用户id||
|nickname|string|否|昵称||
|avatar|string|否|头像||


### 请求示例{#req_demo}
``` js
POST /jim/users/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"userid1",
  "nickname":"user1",
  "avatar":"xxxxxx"
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