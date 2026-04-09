---
title: 查询群公告
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

查询群公告

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/getgrpannouncement

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||


### 请求示例{#req_demo}
``` js
GET /jim/groups/getgrpannouncement HTTP/1.1
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
    "group_id":"group1",
    "content":"xxxxxxxx"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|