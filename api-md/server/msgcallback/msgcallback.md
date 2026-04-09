---
title: 消息回调
hide_title: true
sidebar_position: 1
---

### 功能说明{#intro}

消息回调，IM服务器收到消息发送请求时，可以回调给客户业务服务器，由业务服务器来决定该消息是否继续分发和发送。可以用于消息审核，权限控制等场景。

### 请求说明{#req}

> **推送鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../api#header)

> **推送结果**：业务服务器响应200，且响应数据中要指定该消息是否继续下发，详见下面文档中参数说明。

> **机制说明**: 消息回调，实在消息实际分发前，给业务服务器一次干预的机会。业务服务器响应的快慢，将直接影响消息的处理延时。另外，通过Server API发送的消息，将不会回调。

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|sender|string|是|消息发送者id||
|receiver|string|是|消息接收者id||
|msg_type|string|是|消息类型标识||
|msg_content|string|是|消息内容，建议json格式||
|mention_info.mention_type|string|否|@消息类型，mention_all:@所有人；mention_someone:@某些人；mention_all_someone:@所有人和某些人；||
|mention_info.target_user_ids|array|否|当@某些人时，这里指定要@的人的userid||

### 请求示例{#req_demo}

```js
POST /message/callback HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "platform":"iOS",// iOS/Android/Web/PC/Server
    "sender": "userid1", //发送uid
    "receiver": "userid2", //接收uid
    "channel_type": 1, //1:private 2:group 3:chatroomstem
    "msg_type": "text",
    "msg_content": "Hello, world!",
    "mention_info":{
      "mention_type":"mention_all",
      "target_user_ids":["userid1","userid2"]
    }
}
```

### 响应示例{#resp_demo}

```js

{
    "result":"PASS",//REJECT, REPLACE, SILENT
    "msg_type":"jg:text",
    "msg_content":"{\"content\":\"hello world!\"}",
    "custom_code":132
}

```
### 响应参数
|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|result|string|是|消息回调结果。PASS：消息继续分发；REJECT:该消息拒绝下发；REPLACE:内容需要替换；SILENT:静默处理，消息拒绝下发，但发送者无感知；||
|msg_type|string|否|result是REPLACE时，该字段有效， 用于替换原消息的消息类型||
|msg_content|string|否|result是REPLACE时，该字段有效， 用于替换原消息的消息内容||
|custom_code|int|否|result是reject时，该字段有效，用于自定义向发送端返回的错误码，如果设置成0，将用im中默认的错误码||