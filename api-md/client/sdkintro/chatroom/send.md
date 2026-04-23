---
title: Send chatroom message
hide_title: true
sidebar_position: 9
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

Sending chatroom messages is the same as _[sending a single group chat message](../message/msg_send/send.md)_. Just note the following two parameters:

> conversationType: set to `Conversation.ConversationType.CHATROOM`

> conversationId: set to the corresponding `chatroomId`

</TabItem>
<TabItem value="ios">

Sending chatroom messages is the same as _[sending a single group chat message](../message/msg_send/send.md)_. Just note the following two parameters:

> conversationType: set to `JConversationTypeChatroom`

> conversationId: set to the corresponding `chatroomId`

</TabItem>
<TabItem value="js">

Sending chatroom messages is the same as _[sending a single group chat message](../message/msg_send/send.md)_. Just note the following two parameters:

> conversationType: set to `ConversationType.CHATROOM`

> conversationId: set to the corresponding `chatroomId`

</TabItem>
<TabItem value="flutter">

Sending chatroom messages is the same as _[sending a single group chat message](../message/msg_send/send.md)_. Just note the following two parameters:

> conversationType: set to `ConversationType.chatroom`

> conversationId: set to the corresponding `chatroomId`

</TabItem>
<TabItem value="reactnative">

Sending chatroom messages is the same as _[sending a single group chat message](../message/msg_send/send.md)_. Just note the following two parameters:

> conversationType: set to `ConversationType.CHATROOM`

> conversationId: set to the corresponding `chatroomId`

</TabItem>
</Tabs>
