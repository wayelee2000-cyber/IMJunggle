---
title: 添加禁发群聊消息用户
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

设置用户禁止发送群聊消息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../../api#api)/apigateway/group/globalmutemembers/add

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_ids|array|是|禁发单聊消息用户id列表||


### 请求示例{#req_demo}
``` js
POST /apigateway/group/globalmutemembers/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_ids":["user1","user2"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```