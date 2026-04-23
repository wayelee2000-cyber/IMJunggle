---
title: Merge and forward
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

First, create the MergeMessage, then send it using the sendMessage interface.

**MergeMessage structure**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| title | String | The title of the merged message | 1.0.0 |
| conversation | Conversation | Session ID; all merged messages must originate from the same conversation | 1.0.0 |
| messageIdList | List | List of all merged message IDs, up to 100 | 1.0.0 |
| previewList | List | List of merged messages used for preview on the message bubble, limited to 10 | 1.0.0 |


**Sample Code**

```java
// The conversation where the merged message is located
Conversation srcConversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");

List<String> messageIdList = new ArrayList<>();
messageIdList.add("messageId1");
messageIdList.add("messageId2");
messageIdList.add("messageId3");

List<MergeMessagePreviewUnit> previewList = new ArrayList<>();
for (int i = 0; i < 3; i++) {
    MergeMessagePreviewUnit unit = new MergeMessagePreviewUnit();
    unit.setPreviewContent("previewContent" + i);
    UserInfo userInfo = new UserInfo();
    userInfo.setUserId("userId" + i);
    userInfo.setUserName("userName" + i);
    unit.setSender(userInfo);
    previewList.add(unit);
}
MergeMessage merge = new MergeMessage("title", srcConversation, messageIdList, previewList);

// The target conversation to forward to
Conversation dstConversation = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
Message m = JIM.getInstance().getMessageManager().sendMessage(merge, dstConversation, new IMessageManager.ISendMessageCallback() {
    @Override
    public void onSuccess(Message message) {
    }

    @Override
    public void onError(Message message, int errorCode) {
    }
});
```

**Get the merged message list**

```java
/**
 * Retrieve a list of merged messages
 * @param containerMsgId Merge message ID
 * @param callback Result callback
 */
void getMergedMessageList(String containerMsgId,
                          IGetMessagesCallback callback);
```

</TabItem>

<TabItem value="ios">

First, create the JMergeMessage, then send it using the sendMessage interface.

**JMergeMessage structure**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| title | NSString | The title of the merged message | 1.0.0 |
| conversation | JConversation | Session ID; all merged messages must originate from the same conversation | 1.0.0 |
| messageIdList |```NSArray <NSString *>```| List of all merged message IDs, up to 100 | 1.0.0 |
| previewList |```NSArray <JMergeMessagePreviewUnit *>```| List of merged messages used for preview on the message bubble, limited to 10 | 1.0.0 |

**Sample Code**

```objectivec
NSArray *messageIdList = @[@"messageId1", @"messageId2", @"messageId3", @"messageId4"];
NSMutableArray *previewList = [NSMutableArray array];

for (int i = 0; i < 4; i++) {
    JMergeMessagePreviewUnit *unit = [[JMergeMessagePreviewUnit alloc] init];
    unit.previewContent = [NSString stringWithFormat:@"previewContent%d", i];
    JUserInfo *userInfo = [[JUserInfo alloc] init];
    userInfo.userId = [NSString stringWithFormat:@"userId%d", i];
    userInfo.userName = [NSString stringWithFormat:@"name%d", i];
    userInfo.portrait = @"portrait";
    unit.sender = userInfo;
    [previewList addObject:unit];
}
// The conversation where the merged message is located
JConversation *srcConversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid1"];
JMergeMessage *merge = [[JMergeMessage alloc] initWithTitle:@"title"
                                                conversation:srcConversation
                                              MessageIdList:messageIdList
                                                previewList:previewList];
// The target conversation to forward to
JConversation *dstConversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.messageManager sendMessage:merge
                        inConversation:dstConversation
                                success:^(JMessage *message) {
    
} error:^(JErrorCode errorCode, JMessage *message) {
    
}];
```

**Get the merged message list**

```objectivec
/// Retrieve the merged message list
/// - Parameters:
///   - messageId: Merge message ID
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)getMergedMessageList:(NSString *)messageId
                     success:(void (^)(NSArray<JMessage *> *mergedMessages))successBlock
                       error:(void (^)(JErrorCode code))errorBlock;
```


</TabItem>
<TabItem value="js">

**messages parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. When the session type is `PRIVATE`, the session ID is the userId of the receiver; when the session type is `GROUP`, it is the group ID | 1.0.0 |
| message.messages | Array | Yes | | List of merged and forwarded messages, format shown in the example below | 1.0.0 |
| message.previewList | Array | Yes | | Customized message content preview; the array content can be agreed upon across platforms | 1.0.0 |
| message.title | String | Yes | | The title of the forwarded message | 1.0.0 |
| lifeTime | Number | No | 0 | Message destruction time in milliseconds; must be greater than `0`. For example, 60s: `1 * 60 * 1000` | 1.9.0 |
| lifeTimeAfterRead | Number | No | 0 | Time for the message to disappear after being read, in milliseconds; must be greater than 0. For example, 60s: `1 * 60 * 1000` | 1.9.0 |

**callbacks parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| callbacks | Object | No | | Callback object | 1.0.0 |
| callbacks.onbefore | Function| No | | Callback before the message is sent. After this method is triggered, it returns a temporary message ID `tid`, which can be used to render the message on the page. If the message is sent successfully, the backend updates the message status based on `tid` | 1.0.0 |

**Successful callback**

| Name | Type | Description | Version |
|-----------|----------|-------------------------------------------------------------------------------|--------|
| message | Object | After successful sending, returns a message object with `messageId` and `sentTime`. See the [message object](../../msg/message.md) | 1.0.0 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| result | Object | After failure, the returned object contains `tid` and `error` information. You can view `error.msg` directly or refer to [status codes](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = jetim;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid02',
  // message is a message object received through historical messages or message listening
  messageIdList: [message],
  previewList: [
    { content: 'Hello Chat', sender: { name: 'Xiao Ke', other: 'Multi-end extension as agreed' } }
  ],
  title: 'Chat records of Little J and Little G'
};

let callbacks = {
  onbefore: (message) => {
    // Rendered to the page; can be uniquely identified by message.tid
  }
};
jetim.sendMergeMessage(params, callbacks).then((msg) => {
  console.log('send merge message successfully', msg);
}, (result) => {
  let { error, tid } = result;
  // You can update the message sending failure status based on tid. On the web, failed messages are only saved in SDK memory and will be lost after refresh.
  console.log(tid, error);
});
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

First, create the MergeMessage, then send it using the sendMergeMessage interface.

**MergeMessage structure**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| title | String | The title of the merged message | 1.0.0 |
| conversation | Conversation | Session ID; all merged messages must originate from the same conversation | 1.0.0 |
| messageIdList | string[] | List of all merged message IDs, up to 100 | 1.0.0 |
| previewList | string[] | List of merged messages used for preview on the message bubble, limited to 10 | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

// The conversation where the merged message is located
const srcConversation = {
  type: 1,
  id: 'userId1'
};

const messageIdList = ['messageId1', 'messageId2', 'messageId3'];

const previewList = [
  {
    previewContent: 'previewContent0',
    sender: {
      userId: 'userId0',
      userName: 'userName0'
    }
  },
  {
    previewContent: 'previewContent1',
    sender: {
      userId: 'userId1',
      userName: 'userName1'
    }
  }
];

const mergeMessage = {
  title: 'title',
  conversation: srcConversation,
  messageIdList: messageIdList,
  previewList: previewList
};

// The target conversation to forward to
const dstConversation = {
  type: 2,
  id: 'groupId1'
};

const callback = (message: any, errorCode: number) => {
  if (errorCode === 0) {
    console.log('sendMergeMessage success, messageId is ' + message.messageId);
  } else {
    console.log('sendMergeMessage error, errorCode is ' + errorCode.toString());
  }
};

JuggleIM.sendMergeMessage(mergeMessage, dstConversation, callback).then((message) => {
  console.log('after send, clientMsgNo is ' + message.clientMsgNo);
});
```

**Get the merged message list**

```typescript
const mergedMessages = await JuggleIM.getMergedMessageList('messageId');
```

</TabItem>
<TabItem value="flutter">

**MergeMessage structure**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| title | String | The title of the merged message | 0.6.3 |
| conversation | Conversation | Session ID; all merged messages must originate from the same conversation | 0.6.3 |
| messageIdList | List | List of all merged message IDs, up to 100 | 0.6.3 |
| previewList | List | List of merged messages used for preview on the message bubble, limited to 10 | 0.6.3 |


**Sample Code**

```dart
// The conversation where messages will be merged (original conversation)
Conversation srcConversation = Conversation(ConversationType.group, 'groupId1');
// messages is a list of messages selected in the original conversation
List<Message> messages = [];

List<MergeMessagePreviewUnit> previewList = [];
List<String> messageIdList = [];
String title = 'xxx\'s chat history';
for (Message message in messages) {
  messageIdList.add(message.messageId);
  // Assuming all are text messages; for image messages, usually replaced with [picture]
  previewList.add(MergeMessagePreviewUnit(message.content.content, message.sender));
}
MergeMessage mergeMessage = MergeMessage.create(title, srcConversation, messageIdList, previewList);
// The target conversation to forward to
Conversation dstConversation = Conversation(ConversationType.private, 'userId1');

DataCallback<Message> callback = (m, errorCode) {
  if (errorCode == 0) {
    print("sendMessage success, messageId is " + m.messageId);
  } else {
    print('sendMessage error, errorCode is ' + errorCode.toString() + ', clientMsgNo is ' + m.clientMsgNo!.toString());
  }
};

Message message = await JuggleIm.instance.sendMessage(mergeMessage, dstConversation, callback);
```

**Get the merged message list**

```dart
Result<List<Message>> result = await JuggleIm.instance.getMergedMessageList('messageId');
```

</TabItem>
</Tabs>
