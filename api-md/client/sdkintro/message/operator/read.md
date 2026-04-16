---
title: Mark as read
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
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

**Mark as read**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid2");
List<String> messageIds = new ArrayList<>(2);
messageIds.add("messageId1");
messageIds.add("messageId2");
JIM.getInstance().getMessageManager().sendReadReceipt(conversation, messageIds, new IMessageManager.ISendReadReceiptCallback() {
	@Override
	public void onSuccess() {
		Log.d("TAG", "send read receipt success");
	}

	@Override
	public void onError(int errorCode) {
		Log.e("TAG", "send read receipt error, code is " + errorCode);
	}
});
```

**Get group reading status**

```java
/**
 * Get group message reading status
 * @param conversation The conversation containing the message
 * @param messageId The group message ID to query
 * @param callback Result callback
 */
void getGroupMessageReadDetail(Conversation conversation,
                                String messageId,
                                IGetGroupMessageReadDetailCallback callback);
```

</TabItem>
<TabItem value="ios">

**Mark as read**

```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
NSArray *messageIds = @[@"messageId1", @"messageId2"];
[JIM.shared.messageManager sendReadReceipt:messageIds
                            inConversation:c
                                   success:^{
	NSLog(@"sendReadReceipt success");
} error:^(JErrorCode code) {
	NSLog(@"sendReadReceipt error, code is %d", code);
}];
```

**Get group reading status**

```objectivec
/// Get group message reading status
/// - Parameters:
///   - messageId: The group message ID to query
///   - conversation: The conversation containing the message
///   - successBlock: Success callback; readMembers contains the list of users who have read the message, unreadMembers contains those who have not
///   - errorBlock: Failure callback
- (void)getGroupMessageReadDetail:(NSString *)messageId
                   inConversation:(JConversation *)conversation
                          success:(void (^)(NSArray<JUserInfo *> *readMembers, NSArray<JUserInfo *> *unreadMembers))successBlock
                            error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, it is the group ID | 1.0.0 |
| message.messageId | String | Yes | | Message UID | 1.0.0 |
| message.unreadIndex | Number | Yes | | Message index, available from `message.messageIndex` | 1.0.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the error status code on failure. You can view `error.msg` or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

// Method 1: Mark a single message as read
let message = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  unreadIndex: 1
};
jim.readMessage(message).then(() => {
  console.log('Message marked as read successfully.');
}, (error) => {
  console.log(error);
});

// Method 2: Mark multiple messages as read
let msgs = [
  {
    conversationType: ConversationType.GROUP,
    conversationId: 'groupid1',
    messageId: 'xxxdkadhdsa',
    unreadIndex: 2
  }
];
jim.readMessage(msgs).then(() => {
  console.log('Messages marked as read successfully.');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| messageIds | string[] | List of message IDs for which to send read receipts | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1,
  id: 'userId1'
};

const messageIds = ['messageId1', 'messageId2'];

JuggleIM.sendReadReceipt(conversation, messageIds).then((success) => {
  console.log('sendReadReceipt success:', success);
});
```
</TabItem>


</Tabs>