---
title: 上下线订阅
hide_title: true
sidebar_position: 1
---

### 请求说明{#req}

> **推送鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **推送结果**：业务方收到推送，需保证相应状态码200视为接收推送成功。

> **机制说明**: 消息抄送会尝试推送3次， 每次间隔100ms， 如果3次都失败， 视为一次推送失败。推送采用Google自适应的熔断机制，如果滑动时间窗口内失败过多会触发熔断机制，暂时停止向业务抄送。


### 参数说明{#params}

|参数|数据类型|是否必填|参数说明|
| ---- | ---- | ---- | ---- |
|type|int|是|1表示上线，0表示下线|
|user_id|string|是|用户uid|
|device_id|string|是|设备码|
|platform|string|是|可选值为iOS、Android、iPad、web|
|client_ip|string|是|客户端IP地址|
|session_id|string|是|此次长连接的唯一标识|
|timestamp|int|是|时间戳（毫秒级）|
|connection_ext|string|是|链接时携带的自定义扩展|
|instance_id|string|否|针对web/pc多开情况，用于标识一个实例；移动端无多开情况，此字段为空|

### 请求示例{#req_demo}

```js
POST /onlinestatus/notification HTTP/1.1;
appkey: appkey;
signature: 2e639ae3600a4sdff61fb88b76f485b;
nonce: nonce;
timestamp: 1672568121910;
Content-Type: application/json;

{
  "event_type": "online", //事件类型 message, online
  "timestamp": 1713456000000, //毫秒时间戳
  "payload": [
    {
      "type": 0, //1上线 0下线
      "user_id": "userid1", //用户uid
      "device_id": "1fsdf1", // 设备码
      "platform": "web", //iOS,Android,iPad,web
      "client_ip": "192.116.1.1",
      "session_id": "123",//此次长连接的唯一标识
      "timestamp": 1713456000000,
      "connection_ext":"ext",//链接时携带的自定义扩展
      "instance_id":"instance_id" //针对web/pc多开情况，用于标识一个实例。注：移动端无多开情况，此字段为空
    }
  ]
}
```
