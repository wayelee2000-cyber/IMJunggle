---
title: 点赞列表
hide_title: true
sidebar_position: 23
---
### 功能说明{#intro}

查询帖子的点赞列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/posts/reactions/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|post_id"|string|是|帖子的id||


### 请求示例{#req_demo}
``` js
GET /jim/posts/reactions/list?post_id=xxx HTTP/1.1
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
            "post_id":"postid1",
            "key":"k1",
            "value":"v1",
            "timestamp":1732123456789,
            "user_info":{
              "user_id":"xxx",
              "nickname":"xxxxx",
              "avatar":"xxxx",
              "user_type":0
            }
        }
    ]
  }
}
```