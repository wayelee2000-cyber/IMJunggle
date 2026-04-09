---
title: 更新公众号
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

更新公众号信息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/publicchannel/update

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|channel_id|string|是|公众号id||
|channel_name|string|否|公众号昵称||
|channel_portrait|string|否|公众号头像||
|creator_id|string|否|创建者用户id||


### 请求示例{#req_demo}
``` js
POST /apigateway/publicchannel/update HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "channel_id":"channel1",
  "channel_name":"publicchannel",
  "channel_portrait":"https://xxxxxx.jpg",
  "creator_id":"userid1"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```