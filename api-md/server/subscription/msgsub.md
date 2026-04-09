---
title: 聊天消息订阅
hide_title: true
sidebar_position: 2
---

### 请求说明{#req}

> **推送鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **推送结果**：业务方收到推送，需保证相应状态码200视为接收推送成功。

> **机制说明**: 消息抄送会尝试推送3次， 每次间隔100ms， 如果3次都失败， 视为一次推送失败。推送采用Google自适应的熔断机制，如果滑动时间窗口内失败过多会触发熔断机制，暂时停止向业务抄送。

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
POST /message/notification HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "event_type": "message", //事件类型 message, online, offline
  "timestamp": 1713456000000, //毫秒时间戳
  "payload": [
    {
      "platform":"iOS",// iOS/Android/Web/PC/Server
      "sender": "userid1", //发送uid
      "receiver": "userid2", //接收uid
      "conver_type": 1, // 1:private 2:group 3:chatroomstem
      "msg_type": "text",
      "msg_content": "Hello, world!",
      "mention_info":{
        "mention_type":"mention_all",
        "target_user_ids":["userid1","userid2"]
      },
      "msg_id": "123",
      "msg_time": 1718980832156
    }
  ]
}
```