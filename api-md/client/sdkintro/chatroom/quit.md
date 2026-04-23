---
title: Exit chatroom
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
]
}>
<TabItem value="android">

Exit the chatroom. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and the [Chartroom event](./event.md) will be triggered.

**Sample Code**

```java
// The exit result is monitored through the chatroom callback
String chatroomId = "chatroomId1";
JIM.getInstance().getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="ios">

Exit the chatroom. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and the [Chartroom event](./event.md) will be triggered.

**Sample Code**

```objectivec
// The exit result is monitored through the chatroom callback
NSString *chatroomId = @"chatroomId1";
[JIM.shared.chatroomManager quitChatroom:chatroomId];
```

</TabItem>
<TabItem value="js">

Exit the chatroom. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and the chatroom [Member Change event](./event.md) will be triggered.

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

Exit the chatroom. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and the [Chartroom event](./event.md) will be triggered.

**Sample Code**

```dart
String chatroomId = "chatroomId1";
await JuggleIm.instance.getChatroomManager().quitChatroom(chatroomId);
```

</TabItem>
<TabItem value="reactnative">

Exit the chatroom. When a user is logged in on multiple devices and one device exits, all devices will be logged out, and the [Chartroom event](./event.md) will be triggered.

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const chatroomId = "chatroomId1";
await JuggleIM.quitChatroom(chatroomId);
```

</TabItem>
</Tabs>
