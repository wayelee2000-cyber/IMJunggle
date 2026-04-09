---
title: 查询提示词
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

查询提示词列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/assistants/prompts/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|offset |string|否|分页参数||
|count|int|否|一页数量，默认20||


### 请求示例{#req_demo}
``` js
GET /jim/assistants/prompts/list HTTP/1.1
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
        "id":"xx",
        "prompts":"xxxxxxxx",
        "created_time":1722345674321
      }
    ],
    "offset":"xxx"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|
|17300|失败||