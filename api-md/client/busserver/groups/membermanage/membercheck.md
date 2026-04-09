---
title: 检查是否群成员
hide_title: true
sidebar_position: 7
---
### 功能说明{#intro}

查询用户是否是群成员

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/members/check

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|member_ids|array |是| 用户id列表||



### 请求示例{#req_demo}
``` js
POST /jim/groups/members/check HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id":"groupid1",
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
    "member_exist_map":{
      "userid1":true,
      "userid2":false
    }
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|