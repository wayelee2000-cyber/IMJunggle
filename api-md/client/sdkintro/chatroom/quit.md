---
title: Exit chat room
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
{ label: 'Hongmeng', value: 'harmony', }
]
}>
<TabItem value="android">

Exit the chat room. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and [Chat Room Monitoring](../event) will be triggered.

**Sample Code**

```java
// The exit result is monitored through the chat room callback
String chatroomId = "chatroomId1";
JIM.getInstance().getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="ios">

Exit the chat room. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and [Chat Room Monitoring](../event) will be triggered.

**Sample Code**

```objectivec
// The exit result is monitored through the chat room callback
NSString *chatroomId = @"chatroomId1";
[JIM.shared.chatroomManager quitChatroom:chatroomId];
```

</TabItem>
<TabItem value="js">

Exit the chat room. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and the chat room [Member Change Monitoring](../event) will be triggered.

**Parameter description**

| Name       | Type   | Required | Default | Description     | Version |
|------------|--------|----------|---------|-----------------|---------|
| chatroom   | Object | Yes      | None    | Chatroom object | 1.6.0   |
| chatroom.id| String | Yes      | None    | Chatroom ID     | 1.6.0   |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001',
};

jim.quitChatroom(chatroom).then(() => {
  console.log('Quit chatroom successfully');
}, (error) => {
  console.log('Error', error);
});
```

</TabItem>
<TabItem value="flutter">

Exit the chat room. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and [Chat Room Monitoring](../event) will be triggered.

**Sample Code**

```dart
String chatroomId = "chatroomId1";
await JuggleIm.instance.getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="reactnative">

Exit the chat room. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and [Chat Room Monitoring](../event) will be triggered.

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const chatroomId = "chatroomId1";
await JuggleIM.quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="harmony">

Exit the chat room. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and [Chat Room Monitoring](../event) will be triggered.

**Sample Code**

```js
let chatroomId = "chatroomId1";
JuggleIm.instance.getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
</Tabs>