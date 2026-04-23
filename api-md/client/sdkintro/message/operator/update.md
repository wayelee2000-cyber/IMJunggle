---
title: Modify message
hide_title: true
sidebar_position: 1
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

You can only modify messages that you have sent. After a successful modification, other users in the corresponding session will receive the `onMessageUpdate` callback (make sure to add the [message event listener](../../watcher/message.md)).

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| messageId | String | Message ID | 1.8.4 |
| messageContent | MessageContent | Modified message entity | 1.8.4 |
| conversation | Conversation | Session | 1.8.4 |
| callback | IMessageCallback | Result callback | 1.8.4 |

**Sample Code**

```java
TextMessage text = new TextMessage("update message");
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "conversationId1");
JIM.getInstance().getMessageManager().updateMessage("messageId1", text, conversation, new IMessageManager.IMessageCallback() {
    @Override
    public void onSuccess(Message message) {
        
    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

You can only modify messages that you have sent. After a successful modification, other users in the corresponding session will receive the `messageDidUpdate:` callback (make sure to add the [message event listener](../../watcher/message.md)).

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| messageContent | JMessageContent | Modified message entity | 1.8.4 |
| messageId | NSString | Message ID | 1.8.4 |
| conversation | JConversation | Session | 1.8.4 |
| successBlock | | Success callback | 1.8.4 |
| errorBlock | | Failure callback | 1.8.4 |

**Sample Code**

```objectivec
JTextMessage *text = [[JTextMessage alloc] initWithContent:@"update message"];
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate
                                                                conversationId:@"conversationId1"];
[JIM.shared.messageManager updateMessage:text
                                messageId:@"messageId1"
                          inConversation:conversation
                                  success:^(JMessage *message) {
    
} error:^(JErrorCode errorCode) {
    
}];
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. When the session type is `PRIVATE`, this is the user ID of the receiver; when the session type is `GROUP`, it is the group ID | 1.0.0 |
| message.content | Object | Yes | | Message content, constructed from the `message.name` message | 1.0.0 |
| message.tid | String | Yes | | Local ID of the modified message | 1.0.0 |
| message.messageId | String | Yes | | Modified message ID | 1.0.0 |
| message.sentTime | Number | Yes | | Sending time of the modified message | 1.0.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the corresponding status code if the transmission fails. You can view `error.msg` directly or refer to [Status Code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  tid: 'dkaadjdk30dls',
  messageId: 'xxxdkadhdsa',
  sentTime: 1702180128970,
  content: {
    content: 'new hello world'
  }
};

jim.updateMessage(msg).then(() => {
  console.log('Message updated successfully.');
}, (error) => {
  console.log(error);
});
```
</TabItem>

<TabItem value="reactnative" label="ReactNative">

You can only modify messages that you have sent. After a successful modification, other users in the corresponding session will receive the `onMessageUpdate` callback (the message event listener needs to be enabled).

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| messageId | String | Message ID | 1.0.0 |
| messageContent | MessageContent | Modified message entity | 1.0.0 |
| callback | UpdateMessageCallback | Result callback | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1,
  id: 'userId1'
};

const textMessage = {
  contentType: 'jg:text',
  content: 'update message'
};

const messageId = 'messageId1';

const callback = (message: any, errorCode: number) => {
  if (errorCode === 0) {
    console.log('updateMessage success, messageId is ' + message.messageId);
  } else {
    console.log('updateMessage error, errorCode is ' + errorCode.toString());
  }
};

JuggleIM.updateMessage(messageId, textMessage, conversation, callback);
```

</TabItem>
</Tabs>
