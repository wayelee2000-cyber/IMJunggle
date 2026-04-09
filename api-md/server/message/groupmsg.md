---
title: 发送群聊消息
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

开发者在服务端发送群消息，支持发送 `@ 消息`、普通`文本`、`图片`、`语音` 等消息类型。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/messages/group/send

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|sender_id|string|是|消息发送者id||
|target_ids|array|是|群组id列表||
|msg_type|string|是|消息类型标识||
|msg_content|string|是|消息内容，建议json格式||
|to_user_ids|array|否|定向消息，只给群中指定的成员发送||
|push_data.push_text|string|否|指定推送的内容||
|push_data.push_extra|string|否|指定推送的自定义扩展，建议json字符串||
|push_data.push_level|number|否|推送优先级；0：默认；1：忽略推送控速；2：忽略免打扰；||
|is_storage|bool|否|设置该消息是否存储到历史消息里面，默认 true||
|is_count|bool|否|设置该消息是否记录未读数，默认true，记入未读数||
|is_notify_sender|bool|否|设置该消息是否通知消息的发送者，默认 true||
|is_state|bool|否|状态消息，该消息有极高的发送性能||
|mention_info.mention_type|string|否|@消息类型，mention_all:@所有人；mention_someone:@某些人；mention_all_someone:@所有人和某些人；||
|mention_info.target_user_ids|array|否|当@某些人时，这里指定要@的人的userid||
|refer_msg|obj|否|被引用的消息||
|life_time|int|否|消息的存活时间，单位到毫秒，0标识永久存活||
|life_time_after_read|int|否|消息阅读后的存活周期，单位到毫秒||

### 请求示例{#req_demo}
```js
POST /apigateway/messages/group/send HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "sender_id":"userid1",
  "target_ids":["groupid1","groupid2"],
  "msg_type":"text",
  "msg_content":"{\"content\":\"aabbcc\"}",
  "to_user_ids":["userid1"]
  "push_data":{
    "push_text":"push content",
    "push_extra":"extra",
    "push_level":0
  },
  "is_storage":true,
  "is_notify_sender":true,
  "is_state":false,
  "mention_info":{
    "mention_type":"mention_all",
    "target_user_ids":["userid1","userid2"]
  },
  "refer_msg":{
    "msg_id":"xxx",
    "sender_id":"xxx",
    "target_id":"xxx",
    "channel_type":1,
    "msg_type":"xxx",
    "msg_content":"xxxxx"
  }
}
```

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|
|msg_id|string|消息的唯一标识||


### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":[
    {
      "target_id":"groupid1",
      "msg_id":"aaaaaaa"
    },
    {
      "target_id":"groupid2",
      "msg_id":"bbbbbbb"
    }
  ]
}
```
