---
title: Conversation model
hide_title: true
sidebar_position: 1
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android' },
{ label: 'iOS', value: 'ios' },
{ label: 'JavaScript', value: 'js' },
{ label: 'Flutter', value: 'flutter' },
{ label: 'ReactNative', value: 'reactnative' },
{ label: 'HarmonyOS', value: 'harmony' }
]}
>
<TabItem value="android">

`ConversationInfo` is the SDK's general conversation object. Its `conversation` property, of type `Conversation`, uniquely identifies a conversation. The `Conversation` object contains two properties: `conversationType`, which indicates the type of conversation, and `conversationId`, which identifies the conversation itself.

| Property Name | Type | Description | Version |
| --- | --- | --- | --- |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| lastMessage | Message | The last message in the conversation | 1.0.0 |
| unreadCount | int | Number of unread messages in the conversation | 1.0.0 |
| sortTime | long | Conversation sort time (server time) | 1.0.0 |
| isTop | boolean | Whether the conversation is pinned | 1.0.0 |
| topTime | long | Time when the conversation was pinned | 1.0.0 |
| mute | boolean | Whether Do Not Disturb is enabled | 1.0.0 |
| draft | String | Conversation draft | 1.0.0 |
| mentionInfo | ConversationMentionInfo | @ mention information | 1.0.0 |
| displayName | String | Conversation name shown by the default display rules | 1.8.39 |
| alias | String | Conversation alias. Group chats use the group alias; one-to-one chats use the friend alias | 1.8.39 |
| name | String | Original conversation name. Group chats use the group name; one-to-one chats use the user name | 1.8.39 |
| portrait | String | Conversation avatar URL | 1.8.39 |

</TabItem>

<TabItem value="ios">

`JConversationInfo` is the SDK's general conversation object. Its `conversation` property, of type `JConversation`, uniquely identifies a conversation. The `JConversation` object contains two properties: `conversationType`, which indicates the type of conversation, and `conversationId`, which identifies the conversation itself.

| Property Name | Type | Description | Version |
| --- | --- | --- | --- |
| conversation | JConversation | Conversation identifier | 1.0.0 |
| lastMessage | JMessage | The last message in the conversation | 1.0.0 |
| unreadCount | int | Number of unread messages in the conversation | 1.0.0 |
| sortTime | long long | Conversation sort time (server time) | 1.0.0 |
| isTop | BOOL | Whether the conversation is pinned | 1.0.0 |
| topTime | long long | Time when the conversation was pinned | 1.0.0 |
| mute | BOOL | Whether Do Not Disturb is enabled | 1.0.0 |
| draft | NSString | Conversation draft | 1.0.0 |
| mentionInfo | JConversationMentionInfo | @ mention information | 1.0.0 |
| displayName | NSString | Conversation name shown by the default display rules | 1.8.39 |
| alias | NSString | Conversation alias. Group chats use the group alias; one-to-one chats use the friend alias | 1.8.39 |
| name | NSString | Original conversation name. Group chats use the group name; one-to-one chats use the user name | 1.8.39 |
| portrait | NSString | Conversation avatar URL | 1.8.39 |

</TabItem>

<TabItem value="js">

| Property Name | Type | Description | Version |
| --- | --- | --- | --- |
| conversationId | String | Conversation ID. For `PRIVATE`, this is the recipient's userId; for `GROUP`, it is the group ID | 1.0.0 |
| conversationType | Number | Conversation type | 1.0.0 |
| conversationTitle | String | Conversation name. To change it, update the user or group name directly | 1.0.0 |
| conversationPortrait | String | Conversation avatar. To change it, update the user or group avatar directly | 1.0.0 |
| conversationExts | Object | Conversation extensions. To change them, update the user or group extensions directly | 1.0.0 |
| conversationAlias | String | Conversation alias. Group chats use the group alias; one-to-one chats use the friend alias | 1.9.7 |
| latestMessage | Message | The last message in the conversation. See [Message](./msg/message.mdx) for details | 1.0.0 |
| draft | String | Conversation draft stored locally and not synchronized across devices | 1.0.0 |
| isTop | Boolean | Whether the conversation is pinned | 1.0.0 |
| latestReadIndex | Number | The highest message index read in the conversation | 1.0.0 |
| latestUnreadIndex | Number | The highest unread message index in the conversation. Used when clearing unread count for a single conversation | 1.0.0 |
| undisturbType | Number | [Do Not Disturb type](../enum/web.md#disturb), used to show the conversation's Do Not Disturb status | 1.0.0 |
| sortTime | Number | Conversation sort time. The conversation list is sorted in descending order by this value | 1.0.0 |
| unreadCount | Number | Number of unread messages in the conversation | 1.0.0 |
| unreadTag | Number | [Conversation unread tag status](../enum/web.md#unreadtag) | 1.0.0 |
| mentions | Object | @ mention information in the conversation. After calling [Clear unread for a single conversation](./conversation/unread/clear_unread.md), `mentions` will be cleared | 1.7.0 |
| mentions.isMentioned | Boolean | Whether there are messages that @ mention the current user | 1.7.0 |
| mentions.senders | Array | List of users who sent @ messages. Can be used to show avatars and names in the conversation | 1.7.0 |
| mentions.msgs | Array | List of @ messages in the conversation | 1.7.0 |
| mentions.count | Number | Number of @ messages in the conversation | 1.7.0 |

**Mentions Data Structure**

```js
{
  conversationId: 'Akd1kdlsf',
  conversationType: 2,
  // ...
  mentions: {
    isMentioned: true,
    senders: [
      { id: 'userId01', name: 'Xs', portrait: 'https://xxx.com/avatar.png', updatedTime: 1726113434045, exts: {} }
    ],
    msgs: [
      { senderId: 'userId01', messageId: 'nut3lupwjgnlukc9', sentTime: 1728964798161 }
    ],
    count: 2
  }
}
```

</TabItem>

<TabItem value="flutter">

`ConversationInfo` is the SDK's general conversation object. Its `conversation` property, of type `Conversation`, uniquely identifies a conversation. The `Conversation` object contains two properties: `conversationType`, which indicates the type of conversation, and `conversationId`, which identifies the conversation itself.

| Property Name | Type | Description | Version |
| --- | --- | --- | --- |
| conversation | Conversation | Conversation identifier | 0.0.63 |
| lastMessage | Message | The last message in the conversation | 0.0.63 |
| unreadCount | int | Number of unread messages in the conversation | 0.0.63 |
| sortTime | int | Conversation sort time (server time) | 0.0.63 |
| isTop | bool | Whether the conversation is pinned | 0.0.63 |
| topTime | int | Time when the conversation was pinned | 0.0.63 |
| mute | bool | Whether Do Not Disturb is enabled | 0.0.63 |
| draft | String | Conversation draft | 0.0.63 |
| mentionInfo | ConversationMentionInfo | @ mention information | 0.0.63 |
| name | String | Original conversation name. Group chats use the group name; one-to-one chats use the user name | 0.0.72 |
| portrait | String | Conversation avatar URL | 0.0.72 |
| displayName | String | Conversation name shown by the default display rules | 0.0.72 |
| alias | String | Conversation alias. Group chats use the group alias; one-to-one chats use the friend alias | 0.0.72 |

</TabItem>

<TabItem value="reactnative">

`ConversationInfo` is the SDK's general conversation object. Its `conversation` property, of type `Conversation`, uniquely identifies a conversation. The `Conversation` object contains two properties: `conversationType`, which indicates the type of conversation, and `conversationId`, which identifies the conversation itself.

| Property Name | Type | Description | Version |
| --- | --- | --- | --- |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| lastMessage | Message | The last message in the conversation | 1.0.0 |
| unreadCount | number | Number of unread messages in the conversation | 1.0.0 |
| sortTime | number | Conversation sort time (server time) | 1.0.0 |
| isTop | boolean | Whether the conversation is pinned | 1.0.0 |
| topTime | number | Time when the conversation was pinned | 1.0.0 |
| isMute | boolean | Whether Do Not Disturb is enabled | 1.0.0 |
| draft | string | Conversation draft | 1.0.0 |
| hasUnread | boolean | Whether there are unread messages | 1.0.0 |
| mentionInfo | ConversationMentionInfo | @ mention information | 1.0.0 |
| name | string | Conversation name | 1.0.0 |
| avatar | string | Conversation avatar | 1.0.0 |
| extra | object | Conversation extension information | 1.0.0 |

**Conversation Object Properties**

| Property Name | Type | Description |
| --- | --- | --- |
| conversationType | number | Conversation type: 1 = private chat, 2 = group chat, 3 = chatroom, 4 = system conversation |
| conversationId | string | Conversation ID |

</TabItem>

<TabItem value="harmony">

`ConversationInfo` is the SDK's general conversation object. Its `conversation` property, of type `Conversation`, uniquely identifies a conversation. The `Conversation` object contains two properties: `conversationType`, which indicates the type of conversation, and `conversationId`, which identifies the conversation itself.

| Property Name | Type | Description | Version |
| --- | --- | --- | --- |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| lastMessage | Message | The last message in the conversation | 1.0.0 |
| unreadCount | number | Number of unread messages in the conversation | 1.0.0 |
| sortTime | number | Conversation sort time (server time) | 1.0.0 |
| isTop | boolean | Whether the conversation is pinned | 1.0.0 |
| topTime | number | Time when the conversation was pinned | 1.0.0 |
| mute | boolean | Whether Do Not Disturb is enabled | 1.0.0 |
| draft | string | Conversation draft | 1.0.0 |
| mentionInfo | ConversationMentionInfo | @ mention information | 1.0.0 |

</TabItem>
</Tabs>
