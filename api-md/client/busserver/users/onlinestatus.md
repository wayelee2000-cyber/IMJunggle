---
title: 查询在线状态
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

查询用户的在线状态

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/onlinestatus

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_ids|array|是|用户id列表||


### 请求示例{#req_demo}
``` js
POST /jim/users/onlinestatus HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_ids":["userid1","userid2","userid3"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
        {
            "user_id":"userid1",
            "is_online":true
        },{
            "user_id":"userid2",
            "is_online":false
        },{
            "user_id":"userid3",
            "is_online":false
        }
    ]
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|