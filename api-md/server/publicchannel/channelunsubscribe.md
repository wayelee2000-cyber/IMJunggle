---
title: 取消订阅公众号
hide_title: true
sidebar_position: 5
---

### 功能说明{#intro}

用户取消订阅公众号

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/publicchannel/unsubscribe

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|channel_id|string|是|公众号id||
|member_ids|array|是|订阅者用户id列表||


### 请求示例{#req_demo}
``` js
POST /apigateway/publicchannel/unsubscribe HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "channel_id":"channel1",
  "member_ids":["userid1","userid2"]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```