---
title: send message
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

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | MessageContent | Message entity | 1.0.0 |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | ISendMessageCallback | Callback | 1.0.0 |

**Sample Code**

```java
TextMessage text = new TextMessage("Text message");
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
IMessageManager.ISendMessageCallback callback = new IMessageManager.ISendMessageCallback() {
    @Override
    public void onSuccess(Message message) {
        Log.i("TAG", "send message success");
    }

    @Override
    public void onError(Message message, int errorCode) {
        Log.i("TAG", "send message error, code is " + errorCode);
    }
};
Message message = JIM.getInstance().getMessageManager().sendMessage(text, conversation, callback);
Log.i("TAG", "after send, clientMsgNo is " + message.getClientMsgNo());
```

</TabItem>
<TabItem value="ios">


**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | JMessageContent | Message entity | 1.0.0 |
| conversation | JConversation | Session identifier | 1.0.0 |
| successBlock | | Success callback | 1.0.0 |
| errorBlock | | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
// Text message
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid2"];
JTextMessage *text = [[JTextMessage alloc] initWithContent:@"test text message"];
JMessage *m = [JIM.shared.messageManager sendMessage:text
                                      inConversation:conversation
                                             success:^(JMessage *message) {
        NSLog(@"sendMessage success");
    } error:^(JErrorCode errorCode, JMessage *message) {
        NSLog(@"sendMessage error");
    }];
NSLog(@"after send, m.clientMsgNo is %lld", m.clientMsgNo);
```

</TabItem>
<TabItem value="js">

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../../enum/web#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. When the session type is `PRIVATE`, the session ID is the userId of the receiver; when the session type is `GROUP`, it is the group ID | 1.0.0 |
| message.name | String | Yes | | Message name. Different message types are sent according to actual needs. For detailed enumeration, see [MessageType](../../../enum/web#message) | 1.0.0 |
| message.content | Object | Yes | | Message content, constructed based on the `message.name` message type | 1.0.0 |
| message.referMsg | Object | No | None | Reference reply message. The parameters must be complete as per [Message](../../../msg/message) | 1.0.0 |
| message.mentionInfo | Object | No | None | Valid when conversationType is `GROUP`. Setting mentionInfo indicates this message is an @ message | 1.0.0 |
| mentionInfo.mentionType | Number | No | None | @ type. See [@ message enumeration](../../../enum/web#mention) for details | 1.0.0 |
| mentionInfo.members | Array | No | None | List of specified @ members. The SDK prioritizes determining the @ type of the message based on [@ message enumeration](../../../enum/web#mention) | 1.0.0 |
| lifeTime | Number | No | 0 | Message destruction time period, must be greater than `0`, unit: `ms`. For example, 60s: `1 * 60 * 1000` | 1.9.0 |
| lifeTimeAfterRead | Number | No | 0 | Time period for the message to disappear after being read, must be greater than 0, unit: `ms`. For example, 60s: `1 * 60 * 1000` | 1.9.0 |

**Callbacks Parameter Description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| callbacks | Object | No | | Callback object | 1.0.0 |
| callbacks.onbefore | Function | No | | Callback before the message is sent. After this method is triggered, it returns a temporary message ID `tid`, which can be used to render the message on the page. If the message is sent successfully, the backend will update the message status based on `tid` | 1.0.0 |

**Successful Callback**

| Name | Type | Description | Version |
|-----------|----------|-------------------------------------------------------------------------------|--------|
| message | Object | After successful sending, returns a message object with `messageId` and `sentTime`. See the message structure [Message](../../../msg/message) | 1.0.0 |

:::simple Special Instructions
The IM Server supports intercepting and replacing messages when sending, such as sending `picture messages`. The IM Server can replace `picture messages` with `text messages`. The behavior for sender and receiver is as follows:

> Receiver: The replaced `text message` is displayed.

> Sender: When the current client receives the replaced new message, it is returned in the message success callback. The `message.name` and `message.content` will be replaced with the new content, while the handling of `messageId` and `sentTime` remains unchanged.
:::

**Failure Callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| result | Object | After failure to send, the returned object contains `tid` attribute information and `error` details. You can view `error.msg` directly or refer to [status code](../../../status_code/web) | 1.0.0 |

**Sample Code**
```js
let { ConversationType, MessageType, MentionType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  name: MessageType.TEXT,
  content: {
    content: 'hello world'
  },
  mentionInfo: {
    mentionType: MentionType.ALL,
    members: [{ id: 'userid2' }]
  }
};

let callbacks = {
  onbefore: (message) => {
    // Rendered to the page, uniquely identified by message.tid
  }
};

jim.sendMessage(msg, callbacks).then((message) => {
  console.log(message);
}, (result) => {
  let { error, tid } = result;
  // The status of message sending failure can be updated based on tid. On the web, failed messages are only saved in SDK memory and cannot be retrieved after refreshing.
  console.log(tid, error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

Since sending messages is asynchronous, calling `sendMessage` returns the `message` object synchronously. At this point, the message can be displayed on the page immediately, and `message.clientMsgNo` can be used as a unique identifier. After the `callback` is triggered, the message status can be updated based on `clientMsgNo`.

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | MessageContent | Message entity | 1.0.0 |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | SendMessageCallback | Callback | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1, // 1: Single chat, 2: Group chat
  id: 'userId1'
};

const textMessage = {
  contentType: 'jg:text',
  content: 'Text message'
};

const callback = (message: any, errorCode: number) => {
  if (errorCode === 0) {
    console.log('sendMessage success, messageId is ' + message.messageId);
  } else {
    console.log('sendMessage error, errorCode is ' + errorCode.toString() + ', clientMsgNo is ' + message.clientMsgNo.toString());
  }
};

JuggleIM.sendMessage({
  conversation: conversation,
  content: textMessage
}, callback).then((message) => {
  console.log('after send, clientMsgNo is ' + message.clientMsgNo);
});
```

</TabItem>
<TabItem value="flutter" label="Flutter">

Since sending messages is asynchronous, calling `sendMessage` returns the `message` object synchronously. At this point, the message can be displayed on the page immediately, and `message.clientMsgNo` can be used as a unique identifier. After the `callback` is triggered, the message status can be updated based on `clientMsgNo`.

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | MessageContent | Message entity | 0.6.3 |
| conversation | Conversation | Conversation identifier | 0.6.3 |
| callback | DataCallback | Callback | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
TextMessage textMessage = TextMessage.content('Text message');
DataCallback<Message> callback = (m, errorCode) {
  if (errorCode == 0) {
    print("sendMessage success, messageId is " + m.messageId);
  } else {
    print('sendMessage error, errorCode is ' + errorCode.toString() + ', clientMsgNo is ' + m.clientMsgNo!.toString());
  }
};

Message message = await JuggleIm.instance.sendMessage(textMessage, conversation, callback);
```

</TabItem>
</Tabs>