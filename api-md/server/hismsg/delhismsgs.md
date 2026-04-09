---
title: 删除消息
hide_title: true
sidebar_position: 1
---

### 功能说明{#intro}

根据消息 Id 删除消息，支持删除单项和双向，删除消息操作 **自动同步** 至当前用户各端。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/hismsgs/del

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|否|单聊会话时，会话一方用户的 Id||
|target_id|string|是|单聊会话时，会话另一方用户的 Id；群聊会话时，群 Id||
|channel_type|int|是|会话类型，1:单聊；2:群聊||
|del_scope|int|否|删除消息的范围，0: 代表只删除 fromid 视角的消息；1: 全视角消息删除，会话双方(或群里所有人)都将无法再查看消息；||
|msgs|array|是|要删除的消息的 Id 列表||

### 请求示例{#req_demo}
```js
POST /apigateway/hismsgs/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id":"xxx",
  "target_id":"xxx",
  "channel_type":1,
  "del_scope":0,
  "msgs":[
    {
      "msg_id":"xxxxx"
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
