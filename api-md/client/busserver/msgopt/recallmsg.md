---
title: 管理员撤回消息
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

群管理员撤回其他群成员的消息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim//messages/recall

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|是|要撤回消息的发送者id||
|target_id|string|是|消息的接收者，群组时为群id||
|channel_type|int|是|会话类型，1：单聊；2：群聊；||
|msg_id|string|是|撤回消息的id||
|msg_time|int|是|撤回消息的发送时间||
|exts|map|否|扩展信息||


### 请求示例{#req_demo}
``` js
POST /jim/messages/recall HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "from_id":"userid1",
  "target_id":"group1",
  "channel_type":2,
  "msg_id":"xxxxxxxxxx",
  "msg_time":1731234567823,
  "exts":{
    "k1":"v1",
    "k2":"v2"
  }
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|