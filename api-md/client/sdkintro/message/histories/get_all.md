---
title: Get historical messages
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

**Interface definition**

```java
/**
 * Retrieves messages arranged in chronological order (oldest first, newest last). 
 * If messages are missing and there is a network issue, locally cached messages are returned.
 * @param conversation Conversation object
 * @param direction Pull direction
 * @param options Options for retrieving messages
 * @param callback Callback interface
 */
void getMessages(Conversation conversation,
                  JIMConst.PullDirection direction,
                  GetMessageOptions options,
                  IGetMessagesCallbackV3 callback);

interface IGetMessagesCallbackV3 {
    /**
     * Result callback
     * @param messages List of messages
     * @param timestamp Message timestamp, used for pulling the next batch of messages
     * @param hasMore Indicates if there are more messages
     * @param code Result code; 0 indicates success. If code is not 0 and cached messages exist locally, local messages will be returned in messages
     */
    void onGetMessages(List<Message> messages, long timestamp, boolean hasMore, int code);
}
```

**Sample Code**

```java
GetMessageOptions options = new GetMessageOptions();
options.setCount(100);
options.setStartTime(0);
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid2");
JIM.getInstance().getMessageManager().getMessages(conversation, JIMConst.PullDirection.OLDER, options, new IMessageManager.IGetMessagesCallbackV3() {
    @Override
    public void onGetMessages(List<Message> messages, long timestamp, boolean hasMore, int code) {
        Log.d("TAG", "messageList count is " + messages.size());
    }
});
```

</TabItem>
<TabItem value="ios">

**Interface definition**

```objectivec
/// Retrieves messages arranged by message time (oldest first, newest last). 
/// If messages are missing and there is a network issue, locally cached messages are returned.
/// - Parameters:
///   - conversation: Conversation object
///   - direction: Pull direction
///   - option: Options for retrieving messages
///   - completeBlock: Callback with messages: list of messages, timestamp: message timestamp for pulling next batch, hasMore: whether more messages exist,
///     code: error code (if code is not 0 and cached messages exist locally, local messages will be returned)
- (void)getMessages:(JConversation *)conversation
          direction:(JPullDirection)direction
             option:(JGetMessageOptions *)option
           complete:(void (^)(NSArray <JMessage *> *messages, long long timestamp, BOOL hasMore, JErrorCode code))completeBlock;
```

**Sample Code**

```objectivec
JGetMessageOptions *options = [[JGetMessageOptions alloc] init];
options.count = 100;
options.startTime = 0;
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid2"];
[JIM.shared.messageManager getMessages:conversation
                            direction:JPullDirectionOlder
                                option:options
                              complete:^(NSArray<JMessage *> *messages, long long timestamp, BOOL hasMore, JErrorCode code) {
    NSLog(@"getMessages count is %ld", messages.count);
}];
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------------------------------------------|--------|
| params | Object | Yes | | Parameters for retrieving historical messages | 1.0.0 |
| params.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| params.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the userId of the other party; for `GROUP` sessions, it is the group ID | 1.0.0 |
| params.count | Number | No | 20 | Number of historical messages to retrieve, range: 1 - 20 | 1.0.0 |
| params.time | Number | No | 0 | Starting point for retrieving historical messages. Can be used to fetch messages before or after a specific message | 1.0.0 |
| params.order | Number | No | [BACKWARD](../../enum/web.md#message) | Direction for retrieving historical messages; BACKWARD fetches earlier messages | 1.0.0 |

**Successful callback**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | Object | | 1.0.0 |
| result.isFinished | Boolean | Indicates whether there are more historical messages to retrieve | 1.0.0 |
| result.messages | Array | Array of messages; see the [message object](../../msg/message.md) for details | 1.0.0 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains error information. You can check `error.msg` or refer to [status codes](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2'
};

jim.getMessages(params).then((result) => {
  let { messages, isFinished } = result;
  console.log(messages, isFinished);
}, (error) => {
  console.log(error);
});
```
</TabItem>

<TabItem value="reactnative" label="ReactNative">

Retrieve historical messages for a specified session. Supports fetching from the latest message or retrieving earlier or later messages relative to a specific point in time. The returned message list is sorted in ascending order by message timestamp.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------|--------|
| conversation | Conversation | Yes | | Conversation object. For conversation type 1, the conversation ID is the userId of the other party; for type 2, it is the group ID | 1.0.0 |
| direction | number | No | 1 | Direction to retrieve messages: earlier or later | 1.0.0 |
| options | GetMessageOptions | Yes | | Options for retrieving historical messages | 1.0.0 |

**GetMessageOptions parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------|--------|
| count | number | Yes | 20 | Number of historical messages to retrieve, range: 1 - 20 | 1.0.0 |
| startTime | number | No | 0 | Starting point for retrieving historical messages. Can be used to fetch messages before or after a specific message | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1,
  id: 'userId1'
};

const options = {
  count: 20,
  startTime: 0
};

const direction = 1;

try {
  const result = await JuggleIM.getMessageList(conversation, direction, options);
  console.log('hasMore:', result.hasMore);
  console.log('messages:', result.messages);
} catch (error) {
  console.error('getMessageList error:', error);
}
```

</TabItem>
<TabItem value="flutter" label="Flutter">

Retrieve historical messages for a specified session. Supports fetching from the latest message or retrieving earlier or later messages relative to a specific point in time. The returned message list is sorted in ascending order by message timestamp.

**Query condition parameter description**

`GetMessageOption option = GetMessageOption();`

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------|--------|
| option.count | int | Yes | 20 | Number of historical messages to retrieve, range: 1 - 20 | 0.6.3 |
| option.startTime | int | No | 0 | Starting point for retrieving historical messages. Can be used to fetch messages before or after a specific message | 0.6.3 |

**Query direction parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------|--------|
| direction | int | No | PullDirection.older | Direction to retrieve messages: earlier or later | 0.6.3 |

**Query session parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------|--------|
| conversation | Conversation | Yes | | Conversation object. For `private` type, the conversation ID is the userId of the other party; for `group` type, it is the group ID | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');

GetMessageOption option = GetMessageOption();
option.count = 20;
option.startTime = 0;

int direction = PullDirection.older;

GetMessageResult<List<Message>> result = await JuggleIm.instance.getMessages(conversation, direction, option);
bool hasMore = result.hasMore;
List<Message> messages = result.t as List<Message>;
```

**Callback description**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | `GetMessageResult<List<Message>>` | | 0.6.3 |
| result.hasMore | bool | Indicates whether there are more historical messages | 0.6.3 |
| result.t | `List<Message>` | Array of messages; see the [message object](../../msg/message.md) for details | 0.6.3 |

</TabItem>
</Tabs>
