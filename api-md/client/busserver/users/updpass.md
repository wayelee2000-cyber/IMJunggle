---
title: 更新密码
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

更新登录密码

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/updpass

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|用户id||
|password|string|是|旧密码，注意进行散列操作||
|new_password|string|是|新密码，注意进行散列操作||


### 请求示例{#req_demo}
``` js
POST /jim/users/updpass HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"xxxxxxx",
  "password":"xxxxxx",
  "new_password":"xxxxx"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```
