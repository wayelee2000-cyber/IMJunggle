---
title: 管理员删除消息
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

群管理员删除其他群成员的消息，删除后所有群成员均无法看到

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim//messages/del

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_id|string|是|要删除消息的发送者id||
|target_id|string|是|消息的接收者，群组时为群id||
|channel_type|int|是|会话类型，1：单聊；2：群聊；||
|msgs.msg_id|string|是|删除消息的id||
msgs.|msg_time|int|是|删除消息的发送时间||


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
  "msgs":[
    {
      "msg_id":"xxxx",
      "msg_time":1731234567823
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

### 响应码

|响应码|说明||
|:--|:---|:--|