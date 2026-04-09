---
title: 获取用户信息
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

获取用户信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/info

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|用户id||


### 请求示例{#req_demo}
``` js
GET /jim/users/info?user_id=xxx HTTP/1.1
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
    "user_id":"userid1",
    "nickname":"user1",
    "avatar":"https://file.juggle.im/abcdfafsdaf.png",
    "phone":"xxxx",
    "status":1,
    "is_friend":false,
    "settings":{
        "language":"zh_CN",
        "friend_verify_type":1,//0:不需要验证；1：需要验证；2：拒绝被加好友；
        "grp_verify_type":1,//0：不需要吧严重；2：需要验证；3：拒绝被拉入群；
        "undisturb":"{\"switch\":true,\"timezone\":\"shanghai\",\"rules\":[]}"
    }
  }
}
```