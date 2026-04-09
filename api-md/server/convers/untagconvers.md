---
title: 移除会话标签
hide_title: true
sidebar_position: 9
---

### 功能说明{#intro}

移除会话的标签

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/convers/tags/del

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|设置会话表情的用户id||
|tag|string|是|标签标识||
|convers|array|是|设置标签的会话列表||
|convers.target_id|string|是|会话id||
|convers.channel_type|int|是|会话类型，1:单聊；2:群聊||

### 请求示例{#req_demo}
```js
POST /apigateway/convers/tags/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "tag":"tag1",
  "convers":[
    {
      "target_id":"userid2",
      "channel_type":1
    },
    {
      "target_id":"groupid1",
      "channel_type":2
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