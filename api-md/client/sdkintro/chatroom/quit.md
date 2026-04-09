---
title: 退出聊天室
hide_title: true
sidebar_position: 4
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

退出聊天室，用户多设备登录时其中一个设备退出，所有设备都会退出，会触发 [聊天室监听](../event)

**示例代码**

```java
//退出结果通过聊天室监听回调
String chatroomId = "chatroomId1";
JIM.getInstance().getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="ios">

退出聊天室，用户多设备登录时其中一个设备退出，所有设备都会退出，会触发 [聊天室监听](../event)

**示例代码**

```objectivec
//退出结果通过聊天室监听回调
NSString *chatroomId = @"chatroomId1";
[JIM.shared.chatroomManager quitChatroom:chatroomId];
```

</TabItem>
<TabItem value="js">

退出聊天室，用户多设备登录时其中一个设备退出，所有设备都会退出，会触发聊天室 [成员变更监听](../event)

**参数说明**

| 名称                    | 类型     | 必填   | 默认值  | 描述| 版本     |
|-------------------------|---------|-------|---|----------|----------|
| chatroom                | Object | 是     | 无 | 聊天室对象 | 1.6.0    |
| chatroom.id             | String | 是     | 无 | 聊天室 ID | 1.6.0    |


**示例代码**

```js
let chatroom = {
  id: 'chatroom1001',
};

jim.quitChatroom(chatroom).then(() => {
  console.log('quit chatroom successfully');
}, (error) => {
  console.log('error', error);
});
```

</TabItem>
<TabItem value="flutter">

退出聊天室，用户多设备登录时其中一个设备退出，所有设备都会退出，会触发 [聊天室监听](../event)

**示例代码**

```dart
String chatroomId = "chatroomId1";
await JuggleIm.instance.getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="reactnative">

退出聊天室，用户多设备登录时其中一个设备退出，所有设备都会退出，会触发 [聊天室监听](../event)

**示例代码**

```ts
import JuggleIM from 'juggleim-rnsdk';

const chatroomId = "chatroomId1";
await JuggleIM.quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="harmony">

退出聊天室，用户多设备登录时其中一个设备退出，所有设备都会退出，会触发 [聊天室监听](../event)

**示例代码**

```js
let chatroomId = "chatroomId1";
JuggleIm.instance.getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
</Tabs>