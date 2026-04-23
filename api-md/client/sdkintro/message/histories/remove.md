---
title: Delete historical messages
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

Delete your own historical messages locally and in the cloud; the deletion will be synchronized across all your devices. After the interface is called successfully, it will not affect the other party or other group members' ability to continue viewing messages. Batch deletion of multiple messages within the same conversation is supported.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| clientMsgNoList | List[] | List of local message unique numbers | 1.0.0 |
| callback | IMessageManager.ISimpleCallback | Result callback | 1.0.0 |

**Sample Code**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
List<Long> clientMsgNoList = new ArrayList<>();
clientMsgNoList.add(111L);
clientMsgNoList.add(222L);
clientMsgNoList.add(333L);
JIM.getInstance().getMessageManager().deleteMessagesByClientMsgNoList(conversation, clientMsgNoList, new IMessageManager.ISimpleCallback() {
    @Override
    public void onSuccess() {

    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

Delete your own historical messages locally and in the cloud; the deletion will be synchronized across all your devices. After the interface is called successfully, it will not affect the other party or other group members' ability to continue viewing messages. Batch deletion of multiple messages within the same conversation is supported.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |
| clientMsgNoList | ```NSArray <NSNumber *>``` | List of local message unique numbers | 1.0.0 |
| successBlock |  | Success callback | 1.0.0 |
| errorBlock |  | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
NSArray <NSNumber *> *clientMsgNoList = @[@(111), @(222), @(333)];
[JIM.shared.messageManager deleteMessagesByClientMsgNoList:clientMsgNoList
                                              conversation:conversation
                                                    success:^{
    
} error:^(JErrorCode errorCode) {
    
}];
```

</TabItem>
<TabItem value="js">

Delete your own historical messages locally and in the cloud; the deletion will be synchronized across all your devices. After the interface is called successfully, it will not affect the other party or other group members' ability to continue viewing messages. Batch deletion of multiple messages within the same session is supported. The parameter _messages_ is an array of message objects, each with the following properties:

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------|---------|----------|--------|----------------------------------------------------------|--------|
| message | Object | Yes | - | Object representing the message to delete | 1.0.0 |
| message.conversationType | Number | Yes | - | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | - | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, it is the group ID | 1.0.0 |
| message.messageIndex | Number | Yes | - | Message index, available in the [message object](../../msg/message.md) | 1.0.0 |
| message.sentTime | Number | Yes | - | Message sending time, available in the [message object](../../msg/message.md) | 1.0.0 |
| message.tid | String | Yes | - | Message ID, available in the [message object](../../msg/message.md) | 1.0.0 |
| message.messageId | String | Yes | - | Unique message ID, available in the [message object](../../msg/message.md) | 1.0.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the corresponding status code if the operation fails. You can view `error.msg` or refer to [status code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

// The example uses simulated data; actual calls can obtain this from the historical message interface
let messages = [
  {
    conversationType: ConversationType.PRIVATE, 
    conversationId: 'userid1', 
    messageIndex: 128, 
    sentTime: 1714235241490, 
    messageId: 'nreayt7ha4ggqlcv',
    tid: 'nreayt7ha4ggqlcv',
  },
  //...
];

jim.removeMessages(messages).then(() => {
  console.log('Messages removed successfully.');
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|----------|---------|------------------------------------------|--------|
| conversation | Conversation | Yes |  | Conversation object. For `private` conversations, the conversation ID is the other party's userId. For `group` conversations, it is the group ID. | 0.6.3 |
| startTime | int | Yes |  | Timestamp; messages older than this time will be deleted. 0 represents the current time by default. | 0.6.3 |
| forAllUsers | bool | No | false | Scope of deletion. `true` deletes historical messages for all users; `false` deletes only the current user's historical messages. | 0.6.3 |

**Applicable scenarios for forAllUsers**

> Group scenario: Control the delete button based on permissions. For example, administrators can display and delete historical messages of all members, while regular members can only display and delete their own messages.

> Single chat scenario: Typically, only the historical messages of yourself and the other party are deleted.

**Sample Code**

```dart
Conversation conversation = Conversation(2, 'groupId1');
List<int> clientMsgNoList = [1000, 10001];
bool forAllUsers = false;
await JuggleIm.instance.deleteMessagesByClientMsgNoList(conversation, clientMsgNoList, forAllUsers);
```
</TabItem>
</Tabs>
