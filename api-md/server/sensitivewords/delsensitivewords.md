---
title: 删除敏感词
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

添加的敏感词将用于单群聊文本消息的内容审核

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/sensitivewords/del

> **Content-Type**：`application/json`

### 请求示例{#req_demo}
```js
POST /apigateway/sensitivewords/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "words":["xxxxx","yyyyy"]
}
```


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|words|array|是|要删除的敏感词||

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|


### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```

