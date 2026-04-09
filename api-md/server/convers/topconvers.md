---
title: 设置置顶状态
hide_title: true
sidebar_position: 7
---

### 功能说明{#intro}

设置会话的指定状态

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/convers/top

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|置顶会话的用户id||
|target_id|string|是|要置顶的会话id||
|channel_type|int|是|会话的类型||
|is_top|bool|是|是否置顶||

### 请求示例{#req_demo}
```js
POST /apigateway/convers/top HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "items":[
    {
      "target_id":"userid2",
      "channel_type":1,
      "is_top":true
    },
    {
      "target_id":"groupid1",
      "channel_type":2,
      "is_top":false
    }
  ]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```