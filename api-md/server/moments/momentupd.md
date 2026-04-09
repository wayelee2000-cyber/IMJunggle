---
title: 更新朋友圈
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

更新朋友圈

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/momentgateway/moments/update

> **Content-Type**：`application/json`


### 请求参数{#param}


### 请求示例{#req_demo}
``` js
POST /momentgateway/moments/update HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "user_id":"userid1",   // 以此用户身份
  "moment_id":"xxxxxxx",
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
  "msg":"sucess"
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|