---
title: 帖子信息
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

查询帖子信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/posts/info

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|post_id|string|是|帖子id||


### 请求示例{#req_demo}
``` js
GET /jim/posts/info?post_id=xxxxxxx HTTP/1.1
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
            "post_id":"postid1",
            "content":{
              "text":"xxxxxx",
              "images":[
                {
                  "url":"xxxx"
                }
              ],
              "video":{
                "url":"xxxxx"
              }
            },
            "user_info":{
              "user_id":"xxx",
              "nickname":"xxxxx",
              "avatar":"xxxx",
              "user_type":1
            },
            "reactions":{
              "key1":[
                {
                  "value":"val1",
                  "user_info":{
                    "user_id":"xxx",
                    "nickname":"xxxxx",
                    "avatar":"xxxx",
                    "user_type":1
                  }
                }
              ]
            },
            "top_comments":[
              {
                "comment_id":"xxxx",
                "post_id":"xxx",
                "parent_comment_id":"xxxx",
                "text":"xxxx",
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
                "created_time":1732123456789,
                "updated_time":1732123456789
              }
            ],
            "created_time":1732123456789,
            "updated_time":1732123456789
  }
}
```