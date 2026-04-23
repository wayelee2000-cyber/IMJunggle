---
title: Group sending assistant
hide_title: true
sidebar_position: 2
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

The mass sending assistant enables sending messages to multiple conversations simultaneously without affecting the order of conversations on the sender's side.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | MessageContent | Message entity | 1.0.0 |
| conversations | List[] | Target conversation list | 1.0.0 |
| callback | IMessageManager.IBroadcastMessageCallback | Callback interface | 1.0.0 |

**Sample Code**

```java
Conversation c1 = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
Conversation c2 = new Conversation(Conversation.ConversationType.PRIVATE, "userid2");
Conversation c3 = new Conversation(Conversation.ConversationType.PRIVATE, "userid3");
Conversation c4 = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
List<Conversation> conversations = new ArrayList<>();
conversations.add(c1);
conversations.add(c2);
conversations.add(c3);
conversations.add(c4);
TextMessage text = new TextMessage("broadcast");
JIM.getInstance().getMessageManager().broadcastMessage(text, conversations, new IMessageManager.IBroadcastMessageCallback() {
    @Override
    public void onProgress(Message message, int errorCode, int processCount, int totalCount) {
        
    }

    @Override
    public void onComplete() {

    }
});
```

</TabItem>
<TabItem value="ios">

The mass sending assistant allows sending messages to multiple conversations at once without affecting the order of conversations on the sender's side.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | JMessageContent | Message entity | 1.0.0 |
| conversations | NSArray `<JConversation *>` | Target conversation list | 1.0.0 |
| progressBlock | | Progress callback | 1.0.0 |
| completeBlock | | Completion callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *c1 = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
JConversation *c2 = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId2"];
JConversation *c3 = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId3"];
JConversation *c4 = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];

NSArray *conversations = @[c1, c2, c3, c4];
JTextMessage *text = [[JTextMessage alloc] initWithContent:@"broadcast"];
[JIM.shared.messageManager broadcastMessage:text
                            inConversations:conversations
                                    progress:^(JMessage *sentMessage, JErrorCode code, int processCount, int totalCount) {
    
} complete:^{
    
}];
```

</TabItem>
<TabItem value="js">

The group message assistant supports sending messages to up to `100` groups or users simultaneously. It also allows configuring whether group messages affect the sorting of the conversation list. Developers can use this feature for multi-person broadcasts.

**Parameter description**

_Note: The `messages` parameter accepts an array. Each message item is described as follows:_

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, it is the group ID | 1.0.0 |
| message.name | String | Yes | | Message name. Different message types can be sent as needed. For detailed enumeration, see [MessageType](../../enum/web.md#message) | 1.0.0 |
| message.content | Object | Yes | | Message content, constructed according to the `message.name` type | 1.0.0 |
| message.isMass | Boolean | No | true | Indicates whether the message is sent in mass. Defaults to `true`. Mass sending does not affect the sorting of the conversation list | 1.0.0 |
| lifeTime | Number | No | 0 | Message self-destruction time in milliseconds, must be greater than `0`. For example, 60 seconds: `1 * 60 * 1000` | 1.9.0 |
| lifeTimeAfterRead | Number | No | 0 | Time in milliseconds for the message to disappear after being read, must be greater than `0`. For example, 60 seconds: `1 * 60 * 1000` | 1.9.0 |

**Send callback**

| Name | Type | Description | Version |
|-----------------------|---------|-------------------------------------------------------------------------------|--------|
| callbacks | Object | The mass sending interface returns a `Promise` differently from other interfaces; results are returned via callbacks | 1.0.0 |
| callbacks.onbefore | Function | Triggered multiple times during mass sending, returning the message content to be sent, including `tid` in the [message object](../../msg/message.md) | 1.0.0 |
| callbacks.onprogress | Function | Triggered multiple times during mass sending, returning the number of messages sent, total messages, and the current successfully sent [message object](../../msg/message.md) | 1.0.0 |
| callbacks.oncompleted | Function | Triggered once after mass sending completes, returning an array of all messages sent this time. See the [message object](../../msg/message.md) for the structure of each message | 1.0.0 |

**Failed to send**

Invalid parameters will cause the `Promise` to reject, and the sending failure status of each message will be returned in `callbacks.onprogress`. You can check the `message.error` in the returned message and handle the situation according to the [status code](../../status_code/web.md).

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| result | Object | On failure, the returned object contains `tid` and `error` information. You can view `error.msg` directly or refer to [status code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType, MessageType } = JIM;

let messages = [];
// Send in bulk to userid1 through userid10
for (let i = 1; i < 11; i++) {
  let message = {
    conversationType: ConversationType.PRIVATE,
    conversationId: `userid${i}`,
    content: { content: `Hello JIM ${Date.now()}` },
    name: MessageType.TEXT,
    isMass: true
  };
  messages.push(message);
}

jim.sendMassMessage(messages, {
  onprogress: ({ message, count, total }) => {
    console.log(`${count}/${total}`, message);
  },
  oncompleted: ({ messages }) => {
    console.log('Mass message sending completed.', messages);
  },
}).then(() => {
  console.log('Mass messages sent successfully');
}, (result) => {
  let { error, tid } = result;
  // You can handle message sending failures based on tid. On the web, failed messages are only stored in SDK memory and will be lost after refreshing.
  console.log(tid, error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

> Not yet provided

</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
</Tabs>
