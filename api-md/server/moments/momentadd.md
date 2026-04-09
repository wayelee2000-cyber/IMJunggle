---
title: 发布朋友圈
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

发布一条朋友圈，可以支持图文和视频

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/momentgateway/moments/add

> **Content-Type**：`application/json`


### 请求参数{#param}


### 请求示例{#req_demo}
``` js
POST /momentgateway/moments/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"userid1",   // 以此用户身份
  "content":{
    "text":"朋友圈文本",
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
  }
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "moment_id":"xxx",
    "moment_time":17212345678,
    "user_info":{
      "user_id":"xxx",
      "nickname":"xxxxx",
      "avatar":"xxxx"
    }
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|