---
title: 添加会话
hide_title: true
sidebar_position: 4
---

### 功能说明{#intro}

添加会话指定用户插入一个会话，例如在搜索好友时选中好友但没有发送消息，此时会话列表要将搜索过的会话显示到最新的位置，添加会话多端自动同步。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/convers/add

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|string|是|添加会话的用户id||
|target_id|string|是|添加会话的对方id||
|channel_type|int|是|会话的类型||


### 请求示例{#req_demo}
```js
POST /apigateway/convers/add HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id":"userid1",
  "target_id":"userid2",
  "channel_type":1
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```