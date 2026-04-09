---
title: 删除聊天室属性
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

在指定聊天室中删除自定义属性。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/chatrooms/atts/del

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|是|发起属性设置的用户id||
|chat_id|string|是|聊天室的id||
|atts|array|是|要设置的属性列表||
|atts[0].key|string|是|属性的key||
|atts[0].is_force|bool|否|是否强制删除，默认false||


### 请求示例{#req_demo}
``` js
POST /apigateway/chatrooms/atts/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id":"userid1",
  "chat_id":"chatroom1",
  "atts":[
    {
        "key":"k1",
        "is_force":false
    }
  ]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "atts":[
        {
            "key":"k1",
            "code":0,
            "att_time":1732123445223
        }
    ]
  }
}
```