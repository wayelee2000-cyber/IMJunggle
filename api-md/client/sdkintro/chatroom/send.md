---
title: Send chat room message
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

:::simple

Sending chat room messages is the same as _[sending a single group chat message](../../message/msg_send/send)_. Just note the following two parameters:

> conversationType: set to `Conversation.ConversationType.CHATROOM`

> conversationId: set to the corresponding `chatroomId`

:::

</TabItem>
<TabItem value="ios">

:::simple

Sending chat room messages is the same as _[sending a single group chat message](../../message/msg_send/send)_. Just note the following two parameters:

> conversationType: set to `JConversationTypeChatroom`

> conversationId: set to the corresponding `chatroomId`

:::

</TabItem>
<TabItem value="js">

:::simple

Sending chat room messages is the same as _[sending a single group chat message](../../message/msg_send/send)_. Just note the following two parameters:

> conversationType: set to `ConversationType.CHATROOM`

> conversationId: set to the corresponding `chatroomId`

:::

</TabItem>
<TabItem value="flutter">

:::simple

Sending chat room messages is the same as _[sending a single group chat message](../../message/msg_send/send)_. Just note the following two parameters:

> conversationType: set to `ConversationType.chatroom`

> conversationId: set to the corresponding `chatroomId`

:::

</TabItem>
<TabItem value="reactnative">

:::simple

Sending chat room messages is the same as _[sending a single group chat message](../../message/msg_send/send)_. Just note the following two parameters:

> conversationType: set to `ConversationType.CHATROOM`

> conversationId: set to the corresponding `chatroomId`

:::

</TabItem>
</Tabs>