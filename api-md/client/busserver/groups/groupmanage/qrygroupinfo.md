---
title: 查询群信息
hide_title: true
sidebar_position: 4
---
### 功能说明{#intro}

查询群信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/info

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||


### 请求示例{#req_demo}
``` js
GET /jim/groups/info?group_id=groupid1 HTTP/1.1
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
    "group_id":"groupid1",
    "group_name":"group1",
    "group_portrait":"https://aaaa.png",
    "member_count":10,
    "members":[
      {
        "user_id":"userid1",
        "nickname":"user1",
        "avatar":"https://aaabbcc.png",
        "member_type":0,// 0:普通用户；1：机器人；
        "role":0  //0:群成员；1：群主；2：群管理员
      },{
        "user_id":"userid2",
        "nickname":"user2",
        "avatar":"https://aaabbcc.png",
        "member_type":0,// 0:普通用户；1：机器人；
        "role":0  //0:群成员；1：群主；2：群管理员
      }
    ],
    "owner":{
      "user_id":"userid1",
      "nickname":"user1",
      "avatar":"https://aaabbcc.png"
    },
    "my_role":0, //我在本群的角色。0：普通群成员；1：群主；2：群管理员；
    "group_management":{
      "group_mute":0,//群禁言是否开启；
      "max_admin_count":10,//群管理员最大数量；
      "admin_count":2,//当前管理员数量；
      "group_verify_type":0,//0：
    },
    "grp_display_name":"grp1"// 我的群昵称
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|