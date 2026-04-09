---
title: 好友申请列表
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

我的好友申请列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/friends/applications

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|start|int|否|查询列表的开始时间戳，倒序查询时，默认从当前时间开始；正序查询时，默认从0开始||
|count|int|否|单页数量，默认20，最大不超过50||
|order|int|否|查询顺序。0：倒序；1：正序；默认0||


### 请求示例{#req_demo}
``` js
GET /jim/friends/applications?start=1734407505753&count=50 HTTP/1.1
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
            "target_user":{ //申请发起方用户信息
                "user_id":"userid1",
                "nickname":"user1",
                "avatar":"https://file.juggle.im/abcdfafsdaf.png"
            },
            "is_sponsor":true, //是否发起者
            "status":1,    // 0：申请中；1：已同意；2：已拒绝；3：申请已过期
            "apply_time":1734407505000   //申请发起时间
        }
    ]
  }
}
```