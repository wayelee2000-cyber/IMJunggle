---
title: 加入聊天室
hide_title: true
sidebar_position: 3
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

加入指定聊天室，加入聊天室前必须先创建，集成开发可使用 API 调试创建：`开发者后台` -> 选择应用 -> 开发调试

加入聊天室后 SDK 会自动将房间内最新的 50 条消息和全量属性信息同步至本地，并通过 [聊天室监听](../event) 返回给开发者业务层

_**多设备登录**_:

> 多设备情况一：支持一个用户在一个设备加入多个聊天室，消息相互隔离，通过 [消息监听](../../watcher/message) 返回

> 多设备情况二：支持一个用户多个设备（例如 Web 和 iOS）加入多个聊天室，收发消息多设备自动同步

**示例代码**

```java
//加入结果通过聊天室监听回调
String chatroomId = "chatroomId1";
int count = 10;
JIM.getInstance().getChatroomManager().joinChatroom(chatroomId, count);
```

</TabItem>
<TabItem value="ios">

加入指定聊天室，加入聊天室前必须先创建，集成开发可使用 API 调试创建：`开发者后台` -> 选择应用 -> 开发调试

加入聊天室后 SDK 会自动将房间内最新的 50 条消息和全量属性信息同步至本地，并通过 [聊天室监听](../event) 返回给开发者业务层

_**多设备登录**_:

> 多设备情况一：支持一个用户在一个设备加入多个聊天室，消息相互隔离，通过 [消息监听](../../watcher/message) 返回

> 多设备情况二：支持一个用户多个设备（例如 Web 和 iOS）加入多个聊天室，收发消息多设备自动同步

**示例代码**

```objectivec
//加入结果通过聊天室监听回调
NSString *chatroomId = @"chatroomId1";
int count = 10;
[JIM.shared.chatroomManager joinChatroom:chatroomId
                            prevMessageCount:count];
```

</TabItem>
<TabItem value="js">

加入指定聊天室，加入聊天室前必须先创建，集成开发可使用 API 调试创建：`开发者后台` -> 选择应用 -> 开发调试

加入聊天室后 SDK 会自动将房间内最新的 50 条消息和全量属性信息同步至本地，并通过 [聊天室监听](../event) 返回给开发者业务层

_**多设备登录**_:

> 多设备情况一：支持一个用户在一个设备加入多个聊天室，消息相互隔离，通过 [消息监听](../../watcher/message) 返回，注意区分 `message.conversationId`

> 多设备情况二：支持一个用户多个设备（例如 Web 和 iOS）加入多个聊天室，收发消息多设备自动同步

<br/>

**参数说明**

| 名称                    | 类型     | 必填   | 默认值  | 描述| 版本     |
|-------------------------|---------|-------|---|----------|----------|
| chatroom                | Object | 是     | 无 | 聊天室对象 | 1.6.0    |
| chatroom.id             | String | 是     | 无 | 聊天室 ID | 1.6.0    |
| chatroom.count          | Number | 是     | 无 | 加入聊天室获取最近的消息条数，通过消息监听返回， 返回 `1-50` 条 | 1.6.0    |


**示例代码**

```js
let chatroom = {
  id: 'chatroom1001',
  count: 10
};

jim.joinChatroom(chatroom).then(() => {
  console.log('join chatroom successfully');
}, (error) => {
  console.log('error', error);
});
```

</TabItem>
<TabItem value="flutter">

加入指定聊天室，加入聊天室前必须先创建，集成开发可使用 API 调试创建：`开发者后台` -> 选择应用 -> 开发调试

加入聊天室后 SDK 会自动将房间内最新的 50 条消息和全量属性信息同步至本地，并通过 [聊天室监听](../event) 返回给开发者业务层

**示例代码**

```dart
String chatroomId = "chatroomId1";
int count = 10;
await JuggleIm.instance.getChatroomManager().joinChatroom(chatroomId, count);
```

</TabItem>
<TabItem value="reactnative">

加入指定聊天室，加入聊天室前必须先创建，集成开发可使用 API 调试创建：`开发者后台` -> 选择应用 -> 开发调试

加入聊天室后 SDK 会自动将房间内最新的 50 条消息和全量属性信息同步至本地，并通过 [聊天室监听](../event) 返回��开发者业务层

**示例代码**

```ts
import JuggleIM from 'juggleim-rnsdk';

const chatroomId = "chatroomId1";
const count = 10;
await JuggleIM.joinChatroom(chatroomId, count);
```

</TabItem>
<TabItem value="harmony">

加入指定聊天室，加入聊天室前必须先创建，集成开发可使用 API 调试创建：`开发者后台` -> 选择应用 -> 开发调试

加入聊天室后 SDK 会自动将房间内最新的 50 条消息和全量属性信息同步至本地，并通过 [聊天室监听](../event) 返回给开发者业务层

**示例代码**

```js
let chatroomId = "chatroomId1";
let count = 10;
JuggleIm.instance.getChatroomManager().joinChatroom(chatroomId, count);
```

</TabItem>
</Tabs>