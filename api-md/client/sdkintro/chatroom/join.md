---
title: Join chat room
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
]
}>
<TabItem value="android">

Join the specified chat room. You must create the chat room before joining it. For integrated development, you can create it using API debugging: `Developer server` -> Select Application -> Development and Debugging.

After joining the chat room, the SDK will automatically synchronize the latest 50 messages and the full attribute information of the room locally, and return this data to the developer's business layer through [Chat Room Monitoring](../event).

_**Multi-device login:**_

> Multi-device scenario 1: Supports a single user joining multiple chat rooms on one device, with messages isolated from each other. Messages are returned through the [Message Listener](../../watcher/message).

> Multi-device scenario 2: Supports a single user joining multiple chat rooms across multiple devices (such as Web and iOS), with messages sent and received automatically synchronized across devices.

**Sample Code**

```java
// Join the chat room and listen for callbacks
String chatroomId = "chatroomId1";
int count = 10;
JIM.getInstance().getChatroomManager().joinChatroom(chatroomId, count);
```

</TabItem>
<TabItem value="ios">

Join the specified chat room. You must create the chat room before joining it. For integrated development, you can create it using API debugging: `Developer server` -> Select Application -> Development and Debugging.

After joining the chat room, the SDK will automatically synchronize the latest 50 messages and the full attribute information of the room locally, and return this data to the developer's business layer through [Chat Room Monitoring](../event).

_**Multi-device login:**_

> Multi-device scenario 1: Supports a single user joining multiple chat rooms on one device, with messages isolated from each other. Messages are returned through the [Message Listener](../../watcher/message).

> Multi-device scenario 2: Supports a single user joining multiple chat rooms across multiple devices (such as Web and iOS), with messages sent and received automatically synchronized across devices.

**Sample Code**

```objectivec
// Join the chat room and listen for callbacks
NSString *chatroomId = @"chatroomId1";
int count = 10;
[JIM.shared.chatroomManager joinChatroom:chatroomId
                            prevMessageCount:count];
```

</TabItem>
<TabItem value="js">

Join the specified chat room. You must create the chat room before joining it. For integrated development, you can create it using API debugging: `Developer server` -> Select Application -> Development and Debugging.

After joining the chat room, the SDK will automatically synchronize the latest 50 messages and the full attribute information of the room locally, and return this data to the developer's business layer through [Chat Room Monitoring](../event).

_**Multi-device login:**_

> Multi-device scenario 1: Supports a single user joining multiple chat rooms on one device, with messages isolated from each other. Messages are returned through the [Message Listener](../../watcher/message). Note that you should distinguish messages by `message.conversationId`.

> Multi-device scenario 2: Supports a single user joining multiple chat rooms across multiple devices (such as Web and iOS), with messages sent and received automatically synchronized across devices.

<br/>

**Parameter Description**

| Name           | Type   | Required | Default | Description                                                                 | Version |
|----------------|--------|----------|---------|-----------------------------------------------------------------------------|---------|
| chatroom       | Object | Yes      | None    | Chatroom object                                                             | 1.6.0   |
| chatroom.id    | String | Yes      | None    | Chatroom ID                                                                 | 1.6.0   |
| chatroom.count | Number | Yes      | None    | Number of recent messages to retrieve upon joining the chat room, returned via message listener, range `1-50` | 1.6.0   |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001',
  count: 10
};

jim.joinChatroom(chatroom).then(() => {
  console.log('Joined chatroom successfully');
}, (error) => {
  console.log('Error', error);
});
```

</TabItem>
<TabItem value="flutter">

Join the specified chat room. You must create the chat room before joining it. For integrated development, you can create it using API debugging: `Developer server` -> Select Application -> Development and Debugging.

After joining the chat room, the SDK will automatically synchronize the latest 50 messages and the full attribute information of the room locally, and return this data to the developer's business layer through [Chat Room Monitoring](../event).

**Sample Code**

```dart
String chatroomId = "chatroomId1";
int count = 10;
await JuggleIm.instance.getChatroomManager().joinChatroom(chatroomId, count);
```

</TabItem>
<TabItem value="reactnative">

Join the specified chat room. You must create the chat room before joining it. For integrated development, you can create it using API debugging: `Developer server` -> Select Application -> Development and Debugging.

After joining the chat room, the SDK will automatically synchronize the latest 50 messages and the full attribute information of the room locally, and return this data to the developer's business layer through [Chat Room Monitoring](../event).

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const chatroomId = "chatroomId1";
const count = 10;
await JuggleIM.joinChatroom(chatroomId, count);
```

</TabItem>
</Tabs>