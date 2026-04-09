---
title: 查询聊天室指定属性
hide_title: true
sidebar_position: 3
---

### 功能说明{#intro}

查询聊天室中部分自定义属性。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/chatrooms/atts/qry

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|chat_id|string|是|聊天室的id||
|att_keys|array|是|要查询属性的key列表||


### 请求示例{#req_demo}
``` js
POST /apigateway/chatrooms/atts/qry HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "chat_id":"chatroom1",
  "att_keys":["k1","k2"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "chat_id":"chatroom1",
    "atts":[
        {
            "key":"k1",
            "value":"v1",
            "user_id":"userid1",
            "att_time":1732123445223
        }
    ]
  }
}
```