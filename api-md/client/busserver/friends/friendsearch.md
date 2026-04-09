---
title: 好友搜索
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

搜索我的好友

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/friends/search

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|key|string |是| 关键词||
|offset|string|否|分页偏移量||
|limit|number|否|一页数据条数，默认100||

### 请求示例{#req_demo}
``` js
POST /jim/friends/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "key":"user"
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
            "nickname":"user1",
            "avatar":"https://file.juggle.im/abcdfafsdaf.png",
            "user_type":0
        },{
            "user_id":"userid2",
            "nickname":"user2",
            "avatar":"https://file.juggle.im/abcdfafsdaf.png",
            "user_type":0
        }
    ]
  }
}
```