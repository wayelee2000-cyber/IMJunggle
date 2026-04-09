---
title: 公众号订阅列表
hide_title: true
sidebar_position: 6
---

### 功能说明{#intro}

查询订阅公众号的用户列表

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/publicchannel/members/list

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|channel_id|string|是|公众号id||
|limit|int|否|分页参数||
|offset|string|否|分页偏移量||


### 请求示例{#req_demo}
``` js
GET /apigateway/publicchannel/members/list?channel_id=xxx&limit=50&offset=xxx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"success",
  "data":{
    "members":[
      {
        "member_id":"userid1",
        "created_time":17312345678
      }
    ],
    "offset":"xxxx"
  }
}
```