---
title: 创建群组
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

创建群组

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/create

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_name|string|是|群组昵称||
|group_portrait|string|否|群组头像||
|members.user_id|string|是|入群成员用户id||


### 请求示例{#req_demo}
``` js
POST /jim/groups/create HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_name":"group1",
  "group_portrait":"https://aaaa.png",
  "member_ids":["userid1","userid2"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "group_id":"groupid1",
    "group_name":"group1",
    "group_portrait":"https://aaaa.png"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|