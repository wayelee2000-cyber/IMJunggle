---
title: 合并消息
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

MergeMessage is a built-in message type in the SDK, with the corresponding contentType @"jg:merge".

| Property       | Type          | Description                                         | Version  |
|----------------|---------------|-----------------------------------------------------|----------|
| title          | String        | Title of the merged message                          | 1.0.0    |
| conversation   | Conversation  | Identifier of the conversation containing merged messages | 1.0.0    |
| messageIdList  | List          | List of all merged message IDs, limited to 100 items | 1.0.0    |
| previewList    | List          | List of merged messages used for preview in the message bubble, limited to 10 items | 1.0.0 |
| extra          | String        | Extension field                                      | 1.0.0    |

</TabItem>
<TabItem value="ios">

JMergeMessage is a built-in message type in the SDK, with the corresponding contentType @"jg:merge".

| Property       | Type          | Description                                         | Version  |
|----------------|---------------|-----------------------------------------------------|----------|
| title          | NSString      | Title of the merged message                          | 1.0.0    |
| conversation   | JConversation | Identifier of the conversation containing merged messages | 1.0.0    |
| messageIdList  | NSArray       | List of all merged message IDs, limited to 100 items | 1.0.0    |
| previewList    | NSArray       | List of merged messages used for preview in the message bubble, limited to 10 items | 1.0.0 |
| extra          | NSString      | Extension field                                      | 1.0.0    |

</TabItem>
<TabItem value="js">

Merged forward message is a built-in message type in the SDK, corresponding to the enum _[MessageType.MERGE](../../enum/web#message)_.

| Property       | Type          | Description                                         | Version  |
|----------------|---------------|-----------------------------------------------------|----------|
| title          | String        | Title of the merged message                          | 1.0.0    |
| previewList    | Array         | Summary list of the merged messages                  | 1.0.0    |
| messageIdList  | Array         | List of messageIds of the merged messages            | 1.0.0    |
| extra          | String        | Additional message content, supports JSON string; once set, it cannot be modified | 1.0.0    |

```js
let mergeMsg = {
  title: 'Chat history between Xiao J and A Luo',
  previewList: [{ content: '[File]', senderName: 'A Luo' }],
  messageIdList: ['ns7c4mzpsa4g7sb5', 'ns6wbh472ayg7sb5']
}

let message = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId1',
  name: MessageType.MERGE,
  content: mergeMsg
};
```

</TabItem>

<TabItem value="flutter">

MergeMessage is a built-in message type in the SDK, with the corresponding contentType @"jg:merge".

| Property       | Type          | Description                                         | Version  |
|----------------|---------------|-----------------------------------------------------|----------|
| title          | String        | Title of the merged message                          | 0.6.3    |
| conversation   | Conversation  | Identifier of the conversation containing merged messages | 0.6.3    |
| messageIdList  | List          | List of all merged message IDs, limited to 100 items | 0.6.3    |
| previewList    | List          | List of merged messages used for preview in the message bubble, limited to 10 items | 0.6.3 |
| extra          | String        | Extension field                                      | 0.6.3    |

</TabItem>

<TabItem value="reactnative">

MergeMessageContent is a built-in message type in the SDK, with the corresponding contentType "jg:merge".

| Property       | Type             | Description                                         | Version  |
|----------------|------------------|-----------------------------------------------------|----------|
| title          | string           | Title of the merged message                          | 1.0.0    |
| conversation   | Conversation     | Identifier of the conversation containing merged messages | 1.0.0    |
| messageIdList  | string[]         | List of all merged message IDs, limited to 100 items | 1.0.0    |
| previewList    | PreviewUnit[]    | List of merged messages used for preview in the message bubble, limited to 10 items | 1.0.0 |
| extra          | string           | Extension field                                      | 1.0.0    |

</TabItem>

</Tabs>