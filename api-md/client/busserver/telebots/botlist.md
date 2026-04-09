---
title: Bot列表
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

查询Bot列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/telegrambots/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|offset|string|否|用于分页，查询Bot列表的起始位置||
|count|int|否|单页数量，默认20，最大不超过50||


### 请求示例{#req_demo}
``` js
GET /jim/telegrambots/list?count=50 HTTP/1.1
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
            "bot_id":"botid1",
            "bot_name":"bot1",
            "bot_token":"xxxxxxxx",
            "created_time":1732123456789
        },{
            "user_id":"botid2",
            "bot_name":"bot2",
            "bot_token":"xxxxxxxx",
            "created_time":1751234567876
        }
    ],
    "offset":"xxxx"
  }
}
```