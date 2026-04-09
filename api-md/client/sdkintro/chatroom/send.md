---
title: 发送聊天室消息
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

:::simple

发送聊天室消息和 _[发送单群聊](../../message/msg_send/send)_ 一致，只需注意两个参数：

> conversatonType: 修改为 `Conversation.ConversationType.CHATROOM`

> conversationId: 修改为对应的 `chatroomId`

:::

</TabItem>
<TabItem value="ios">

:::simple

发送聊天室消息和 _[发送单群聊](../../message/msg_send/send)_ 一致，只需注意两个参数：

> conversatonType: 修改为 `JConversationTypeChatroom`

> conversationId: 修改为对应的 `chatroomId`

:::

</TabItem>
<TabItem value="js">

:::simple

发送聊天室消息和 _[发送单群聊](../../message/msg_send/send)_ 一致，只需注意两个参数：

> conversatonType: 修改为 `ConversationType.CHATROOM`

> conversationId: 修改为对应的 `chatroomId`

:::

</TabItem>
<TabItem value="flutter">

:::simple

发送聊天室消息和 _[发送单群聊](../../message/msg_send/send)_ 一致，只需注意两个参数：

> conversatonType: 修改为 `ConversationType.chatroom`

> conversationId: 修改为对应的 `chatroomId`

:::

</TabItem>
<TabItem value="reactnative">

:::simple

发送聊天室消息和 _[发送单群聊](../../message/msg_send/send)_ 一致，只需注意两个参数：

> conversatonType: 修改为 `ConversationType.CHATROOM`

> conversationId: 修改为对应的 `chatroomId`

:::

</TabItem>
<TabItem value="harmony">

:::simple

发送聊天室消息和 _[发送单群聊](../../message/msg_send/send)_ 一致，只需注意两个参数：

> conversatonType: 修改为 `ConversationType.Chatroom`

> conversationId: 修改为对应的 `chatroomId`

:::

</TabItem>
</Tabs>