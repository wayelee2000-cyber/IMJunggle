---
title: 解散群组
hide_title: true
sidebar_position: 2
---

### 功能说明{#intro}

开发者服务端解散群组后，将解散群组的信息同步至 IM 服务端，若发送解散通知消息，需要在调用此接口前 `优先发送通知消息`，再进行解散操作。

:::danger 群组解散通知
群组解散成功后，IM 服务端 **不会** 发送解散群通知，开发者需要自定义通知消息发送至群里
:::

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/groups/del

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||

### 请求示例{#req_demo}
```js
POST /apigateway/groups/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id":"groupid1",
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```