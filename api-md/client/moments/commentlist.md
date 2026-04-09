---
title: 评论列表
hide_title: true
sidebar_position: 14
---
### 功能说明{#intro}

查询评论列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/momentgateway/moments/comments/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|moment_id"|string|是|朋友圈的id||
|start|int|否|增量查询帖子的起始时间戳，毫秒(13位)||
|limit|int|否|单页数量，默认20，最大不超过50||
|order|int|否|查询顺序，0:倒序；1:正序||


### 请求示例{#req_demo}
``` js
GET /momentgateway/moments/comments/list?moment_id=xxx&limit=20&start=1723456789123 HTTP/1.1
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
            "comment_id":"commentid1",
            "moment_id":"momentid1",
            "parent_comment_id":"xxx",
            "parent_user_info":{
              "user_id":"xxx",
              "nickname":"xxxxx",
              "avatar":"xxxx"
            },
            "content":{
              "text":"xxxxxxxx"
            },
            "user_info":{
              "user_id":"xxx",
              "nickname":"xxxxx",
              "avatar":"xxxx",
              "user_type":0
            },
            "comment_time":1732123456789
        }
    ],
    "is_finished":true
  }
}
```