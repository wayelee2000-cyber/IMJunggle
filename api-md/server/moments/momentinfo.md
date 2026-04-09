---
title: 朋友圈信息
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

查询朋友圈信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/momentgateway/moments/info

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|moment_id|string|是|朋友圈id||


### 请求示例{#req_demo}
``` js
GET /momentgateway/moments/info?post_id=xxxxxxx HTTP/1.1
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
    "moment_id":"momentid1",
    "content":{
      "text":"xxxxxx",
      "medias":[
        {
          "type":"image",
          "url":"xxx",
          "snapshot_url":"xxxx",
          "height":100,
          "width":100
        },{
          "type":"video",
          "url":"xxxx",
          "snapshot_url":"xxxx",
          "duration":10,
          "height":100,
          "width":100
        }
      ]
    },
    "user_info":{
      "user_id":"xxx",
      "nickname":"xxxxx",
      "avatar":"xxxx"
    },
    "reactions":[
        {
          "value":"val1",
          "timestamp":17312345678,
          "user_info":{
            "user_id":"xxx",
            "nickname":"xxxxx",
            "avatar":"xxxx"
          }
        }
    ],
    "top_comments":[
      {
        "comment_id":"xxxx",
        "moment_id":"xxx",
        "parent_comment_id":"xxxx",
        "content":{
          "text":"xxxxx"
        },
        "parent_user_info":{
          "nickname":"xxxxx",
          "avatar":"xxxx",
          "user_type":1
        },
        "user_info":{
          "nickname":"xxxxx",
          "avatar":"xxxx",
          "user_type":1
        },
        "comment_time":1732123456789
      }
    ],
    "moment_time":1732123456789
  }
}
```