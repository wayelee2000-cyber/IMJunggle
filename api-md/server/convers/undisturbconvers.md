---
title: 设置免打扰
hide_title: true
sidebar_position: 1
---

### 功能说明{#intro}

会话设置免打扰后，当前会话不会接受离线消息推送，调用此接口后 IM 服务端会将 `undisturb_type` 自动同步到指定用户的各端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/convers/undisturb

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|设置免打扰的用户id||
|target_id|string|是| 免打扰会话id ||
|channel_type|int|是|免打扰会话的类型||
|undisturb_type|int|是|免打扰类型：0:取消免打扰；1:普通会话免打扰；||

### 请求示例{#req_demo}
```js
POST /apigateway/convers/undisturb HTTP/1.1
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
      "undisturb_type":1
    },
    {
      "target_id":"groupid1",
      "channel_type":2,
      "undisturb_type":1
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