---
title: 好友列表
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

我的好友列表，默认按字母序排序

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/friends/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|page|int|否|用于分页，起始页数，从1开始||
|size|int|否|单页数量，默认20，最大不超过50||
|order_tag|string|否|起始的拼音字母||


### 请求示例{#req_demo}
``` js
GET /jim/friends/list?size=50&page=1&order_tag=a HTTP/1.1
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
    "items":[
        {
            "user_id":"userid1",
            "nickname":"user1",
            "avatar":"https://file.juggle.im/abcdfafsdaf.png",
            "pinyin":"u",
            "friend_info":{
              "is_friend":true,
              "display_name":"displayname"
            }
        },{
            "user_id":"userid2",
            "nickname":"user2",
            "avatar":"https://file.juggle.im/abcdfafsdaf.png",
            "pinyin":"u",
            "friend_info":{
              "is_friend":true,
              "display_name":"displayname"
            }
        }
    ]
  }
}
```