---
title: 应用列表
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

查询工作台中应用的列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/applications/list

> **Content-Type**：`application/json`


### 请求参数{#param}


### 请求示例{#req_demo}
``` js
GET /jim/applications/list?page=1&size=20&order=0 HTTP/1.1
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
        "app_id":"xxx",
        "app_name":"xxx",
        "app_icon":"xxxx",
        "app_desc":"xxxx",
        "app_url":"https://abc.aab.com",
        "app_order":1,
        "created_time":1721234567890,
        "updated_time":1721234567890
      }
    ],
    "page":1,
    "size":20
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|