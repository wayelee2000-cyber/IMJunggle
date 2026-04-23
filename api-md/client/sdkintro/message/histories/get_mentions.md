---
title: Get @ message
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

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| count | int | Number of messages to pull | 1.0.0 |
| time | long | Message timestamp; if 0 is passed, the current time is used | 1.0.0 |
| direction| JIMConst.PullDirection | Pull direction | 1.0.0 |
| callback | IMessageManager.IGetMessagesWithFinishCallback| Pull callback | 1.0.0 |

**Sample Code**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
JIM.getInstance().getMessageManager().getMentionMessageList(conversation, 100, 0, JIMConst.PullDirection.OLDER, new IMessageManager.IGetMessagesWithFinishCallback() {
    @Override
    public void onSuccess(List<Message> messages, boolean isFinished) {

    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |
| count | int | Number of messages to pull | 1.0.0 |
| time | long | Message timestamp; if 0 is passed, the current time is used | 1.0.0 |
| direction| JPullDirection | Pull direction | 1.0.0 |
| successBlock | | Success callback | 1.0.0 |
| errorBlock | | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
[JIM.shared.messageManager getMentionMessages:conversation
                                        count:100
                                          time:0
                                    direction:JPullDirectionOlder
                                      success:^(NSArray<JMessage *> *messages, BOOL isFinished) {

} error:^(JErrorCode code) {

}];
```

</TabItem>
<TabItem value="js">

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|----------|------|-----------|----------|
| conversation | Object | Yes | | Conversation object | 1.0.0 |
| conversation.conversationType | Number | Yes | | Conversation type | 1.0.0 |
| conversation.conversationId | String | Yes | | Conversation ID | 1.0.0 |
| conversation.messageIndex | Number | No | 0 | Message index; when querying @ messages, this is the starting point to retrieve `count` messages forward or backward | 1.0.0 |
| conversation.count | Number | No | 20 | Number of messages to retrieve | 1.0.0 |
| conversation.order | Number | No | [BACKWARD](../../enum/web.md#mention_order) | Retrieval direction | 1.0.0 |

**Callback Description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.0.0 |
| result.isFinished | Boolean | Indicates whether the @ message query is complete; false means more @ messages are available on the server | 1.0.0 |
| result.msgs | Array | List of @ messages; message content can be accessed via [Query message by ID](./get_by_ids.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType, MentionOrder } = JIM;

let conversation = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  count: 10,
  messageIndex: 0,
  order: MentionOrder.BACKWARD
};

jim.getMentionMessages(conversation).then((result) => {
  let { isFinished, msgs } = result;
  console.log(isFinished, msgs);
})
```
</TabItem>

<TabItem value="flutter" label="Flutter">

Retrieve the list of @ messages in the specified conversation, supporting paginated retrieval.

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |
| count | int | Number of messages to pull | 0.6.3 |
| startTime | int | Message timestamp; if 0 is passed, the current time is used | 0.6.3 |
| direction | int | Pull direction; 0: pull messages after the start time; 1: pull messages before the start time | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
int count = 20;
int startTime = 0;
int direction = PullDirection.older;

GetMessageResult<List<Message>> result = await JuggleIm.instance.getMentionMessages(
  conversation,
  count,
  startTime,
  direction
);
```

**Callback Description**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | `GetMessageResult<List<Message>>` | Result object | 0.6.3 |
| result.hasMore | bool | Indicates whether there are more @ messages | 0.6.3 |
| result.t | `List<Message>` | List of messages; see the [message object](../../msg/message.md) for message properties | 0.6.3 |

</TabItem>
</Tabs>
