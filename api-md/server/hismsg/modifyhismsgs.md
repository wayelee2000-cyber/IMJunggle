---
title: 消息修改
hide_title: true
sidebar_position: 5
---

### 功能说明{#intro}

对已有的消息进行修改，可以修改消息类型和消息体，多设备同步

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/hismsgs/modify

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|否|单聊会话时，会话一方用户的 Id||
|target_id|string|是|单聊会话时，会话另一方用户的 Id；群聊会话时，群 Id||
|channel_type|int|是|会话类型，1:单聊；2:群聊||
|msg_id|string|是|被修改消息的id||
|msg_type|string|是|消息类型||
|msg_content|string|是|消息内容，建议json结构||


### 请求示例{#req_demo}
```js
POST /apigateway/hismsgs/modify HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "from_id":"xxx",
  "target_id":"xxx",
  "channel_type":1,
  "msg_id":"xxxxxx",
  "msg_type":"text",
  "msg_content":"{\"content\":\"aabbcc\"}"
}

```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```
