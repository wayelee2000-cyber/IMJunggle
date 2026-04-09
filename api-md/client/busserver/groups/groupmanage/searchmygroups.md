---
title: 搜索加入的群
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

搜索我加入过的群

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/mygroups/search

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|keyword|string|是| 搜索关键词||
|offset|string|否|分页偏移量，初次可以不填||
|limit|int|否|一次返回数据条数||


### 请求示例{#req_demo}
``` js
POST /jim/groups/mygroups/search HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "keyword":"group",
  "limit":100
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[{
      "group_id":"groupid1",
      "group_name":"group1",
      "group_portrait":"https://xxxxxx.png"
    }],
    "offset":"xxxx"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|