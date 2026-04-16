---
title: Join and create a chat room
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

You do not need to call the `IM Server API` to create a chat room before joining it. The chat room will be automatically created upon joining the specified room. This is useful in scenarios where the live broadcast room ID is predetermined.

After joining the chat room, the SDK automatically synchronizes the latest 50 messages and the complete attribute information of the room to the local device, and returns this data to the developer's business layer via [Chat Room Monitoring](../event).

_**Multi-device login:**_

> Multi-device scenario 1: Supports a single user joining multiple chat rooms on one device, with messages isolated between rooms. Messages are returned through the [Message Listener](../../watcher/message).

> Multi-device scenario 2: Supports a single user joining multiple chat rooms across multiple devices (such as Web and iOS), with messages sent and received automatically synchronized across devices.

**Sample Code**

```java
// Join the chat room and listen for callbacks
String chatroomId = "chatroomId1";
int count = 10;
boolean isAutoCreate = true;
JIM.getInstance().getChatroomManager().joinChatroom(chatroomId, count, isAutoCreate);
```

</TabItem>
<TabItem value="ios">

You do not need to call the `IM Server API` to create a chat room before joining it. The chat room will be automatically created upon joining the specified room. This is useful in scenarios where the live broadcast room ID is predetermined.

After joining the chat room, the SDK automatically synchronizes the latest 50 messages and the complete attribute information of the room to the local device, and returns this data to the developer's business layer via [Chat Room Monitoring](../event).

_**Multi-device login:**_

> Multi-device scenario 1: Supports a single user joining multiple chat rooms on one device, with messages isolated between rooms. Messages are returned through the [Message Listener](../../watcher/message).

> Multi-device scenario 2: Supports a single user joining multiple chat rooms across multiple devices (such as Web and iOS), with messages sent and received automatically synchronized across devices.

**Sample Code**

```objectivec
// Join the chat room and listen for callbacks
NSString *chatroomId = @"chatroomId1";
int count = 10;
BOOL isAutoCreate = YES;
[JIM.shared.chatroomManager joinChatroom:chatroomId
                            prevMessageCount:count
                            isAutoCreate:isAutoCreate];
```

</TabItem>
<TabItem value="js">

You do not need to call the `IM Server API` to create a chat room before joining it. The chat room will be automatically created upon joining the specified room. This is useful in scenarios where the live broadcast room ID is predetermined.

After joining the chat room, the SDK automatically synchronizes the latest 50 messages and the complete attribute information of the room to the local device, and returns this data to the developer's business layer via [Chat Room Monitoring](../event).

_**Multi-device login:**_

> Multi-device scenario 1: Supports a single user joining multiple chat rooms on one device, with messages isolated between rooms. Messages are returned through the [Message Listener](../../watcher/message). Note to distinguish `message.conversationId`.

> Multi-device scenario 2: Supports a single user joining multiple chat rooms across multiple devices (such as Web and iOS), with messages sent and received automatically synchronized across devices.

<br/>

**Parameter description**

| Name           | Type   | Required | Default | Description                                                                 | Version |
|----------------|--------|----------|---------|-----------------------------------------------------------------------------|---------|
| chatroom       | Object | Yes      | None    | Chatroom object                                                             | 1.6.0   |
| chatroom.id    | String | Yes      | None    | Chatroom ID                                                                 | 1.6.0   |
| chatroom.count | Number | Yes      | None    | Number of recent messages to retrieve upon joining (1-50), returned via message listener | 1.6.0   |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001',
  count: 10,
};

jim.joinAndCreateChatroom(chatroom).then(() => {
  console.log('Joined chatroom successfully');
}, (error) => {
  console.log('Error', error);
});
```

</TabItem>
<TabItem value="flutter">

You do not need to call the `IM Server API` to create a chat room before joining it. The chat room will be automatically created upon joining the specified room. This is useful in scenarios where the live broadcast room ID is predetermined.

After joining the chat room, the SDK automatically synchronizes the latest 50 messages and the complete attribute information of the room to the local device, and returns this data to the developer's business layer via [Chat Room Monitoring](../event).

**Sample Code**

```dart
String chatroomId = "chatroomId1";
int count = 10;
bool isAutoCreate = true;
await JuggleIm.instance.getChatroomManager().joinChatroom(chatroomId, count, isAutoCreate);
```

</TabItem>
<TabItem value="reactnative">

You do not need to call the `IM Server API` to create a chat room before joining it. The chat room will be automatically created upon joining the specified room. This is useful in scenarios where the live broadcast room ID is predetermined.

After joining the chat room, the SDK automatically synchronizes the latest 50 messages and the complete attribute information of the room to the local device, and returns this data to the developer's business layer via [Chat Room Monitoring](../event).

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const chatroomId = "chatroomId1";
const count = 10;
const isAutoCreate = true;
await JuggleIM.joinChatroom(chatroomId, count, isAutoCreate);
```

</TabItem>
</Tabs>