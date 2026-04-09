---
title: 查询敏感词
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

添加的敏感词将用于单群聊文本消息的内容审核

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/sensitivewords/list

> **Content-Type**：`application/json`

### 请求示例{#req_demo}
```js
GET /apigateway/sensitivewords/list?limit=20&offset=xx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|offset|string|是|查询敏感词的起始id，每条敏感词数据都会有一个唯一的id，初次查询可以留空||
|limit|int|否|分页一页的数据条数，默认50||

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|


### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
      {
        "id":"xx",
        "word":"xx",
        "word_type":1
      }
    ],
    "is_finished":false
  }
}
```

