---
title: Query pinned messages
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

**Interface definition**

```java
/**
 * Get pinned messages
 * When entering a session, you can query the pinned message of the current session through the session information.
 * @param conversation conversation identifier
 * @param callback result callback
 */
JIM.getInstance().getMessageManager().getTopMessage(conversation, new IMessageManager.IGetTopMessageCallback() {
            @Override
            public void onSuccess(Message message, UserInfo userInfo, long l) {
            }

            @Override
            public void onError(int i) {
            }
        });

// How to get pinned messages in real time after entering a conversation
/**
 * Listen for session pinned messages
 * By monitoring this, you can receive real-time updates on changes to the pinned message and update the message page accordingly, for example, via EventBus broadcast.
 * @param listener listener
 */
JIM.getInstance().getMessageManager().addListener("msg", new IMessageManager.IMessageListener() {
            @Override
            /**
             * Pinned message event
             * @param message message object
             * @param userInfo operator
             * @param b Whether the message is pinned to the top
             */
            public void onMessageSetTop(Message message, UserInfo userInfo, boolean b) {
                Log.d(tag, "onMessageSetTop: " + message.toString());
                EventBus.getDefault().post(new MessageTopEvent(message, userInfo, b));
            }
        });        
```

</TabItem>
<TabItem value="ios">

**Interface definition**

```objectivec
/// Get the pinned message
/// - Parameters:
///   - conversation: conversation identifier
///   - successBlock: success callback
///   - errorBlock: failure callback
- (void)getTopMessage:(JConversation *)conversation
              success:(void (^)(JMessage *message, JUserInfo *userInfo, long long timestamp))successBlock
                error:(void (^)(JErrorCode code))errorBlock;
```


</TabItem>
<TabItem value="js">

Query the pinned messages of a specified session. After entering the session page, call the query pinned messages interface to retrieve the pinned messages for the current session.

![](./top.png)

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the userId of the receiver; for `GROUP` sessions, it is the group ID | 1.0.0 |

**Successful callback**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | Object | | 1.0.0 |
| result.message | Object | The pinned message object | 1.0.0 |
| result.isTop | Boolean | Whether the message is pinned to the top | 1.0.0 |
| result.operator | Object | Operator information | 1.0.0 |
| result.createdTime | Number | Timestamp when the message was pinned | 1.0.0 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code if the request fails. You can check `error.msg` or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
};

jim.getTopMessage(conversation).then((result) => {

  let { message, isTop, operator, createdTime } = result;
  
  // message => The original message that was pinned or unpinned. You can inspect the Message object if needed.
  
  // isTop => Indicates whether the message is pinned to the top.
  
  // operator => Operator info { id: '', name: '', portrait: '' }
  
  // createdTime => Time of the pinning operation.
  
}, (error) => {
  console.log(error)
});
```
</TabItem>

<TabItem value="flutter">

**Interface definition**

```dart
/// Get the pinned message
/// - Parameters:
///   - conversation: conversation identifier
Future<Result<TopMessageResult>> getTopMessage(Conversation conversation) async
```

</TabItem>

</Tabs>