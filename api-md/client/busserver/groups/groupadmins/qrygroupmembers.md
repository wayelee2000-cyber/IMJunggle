---
title: 查询群管理员列表
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

查询群管理员列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/management/administrators/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||


### 请求示例{#req_demo}
``` js
GET /jim/groups/management/administrators/list?group_id=groupid1 HTTP/1.1
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
    "items":[
      {
        "user_id":"userid1",
        "nickname":"user1",
        "avatar":"https://aaabbcc.png",
        "member_type":0,// 0:普通用户；1：机器人；
        "role":2  //0:群成员；1：群主；2：群管理员
      },{
        "user_id":"userid2",
        "nickname":"user2",
        "avatar":"https://aaabbcc.png",
        "member_type":0,// 0:普通用户；1：机器人；
        "role":2  //0:群成员；1：群主；2：群管理员
      }
    ],
    "offset":"xxx"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|