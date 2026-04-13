---
title: Remove message reaction
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
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">


**Interface definition**

```java
/**
 * Delete a message reaction
 * @param messageId The ID of the message
 * @param conversation The conversation to which the message belongs
 * @param reactionId The ID of the reaction to remove
 * @param callback Result callback
 */
void removeMessageReaction(String messageId,
                            Conversation conversation,
                            String reactionId,
                            ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

**Interface definition**

```objectivec
/// Delete a message reaction
/// - Parameters:
///   - messageId: The ID of the message
///   - conversation: The conversation to which the message belongs
///   - reactionId: The ID of the reaction to remove
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)removeMessageReaction:(NSString *)messageId
                 conversation:(JConversation *)conversation
                   reactionId:(NSString *)reactionId
                      success:(void (^)(void))successBlock
                        error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.8.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.8.0 |
| message.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the user ID of the receiver; for `GROUP` sessions, it is the group ID | 1.8.0 |
| message.messageId | String | Yes | | The ID of the message whose reaction is being removed | 1.8.0 |
| message.reactionId | String | Yes | | The unique identifier of the reaction. Developers can customize this, but multi-end agreement is required | 1.8.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the status code if the operation fails. You can check `error.msg` or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.8.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  reactionId: ':smile'
};

jim.removeMessageReaction(msg).then(() => {
  console.log('Message reaction removed successfully.');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="flutter">


**Interface definition**

```dart
/**
 * Delete a message reaction
 * @param messageId The ID of the message
 * @param conversation The conversation to which the message belongs
 * @param reactionId The ID of the reaction to remove
 */
Future<int> removeMessageReaction(String messageId, Conversation conversation, String reactionId) async
```

</TabItem>
</Tabs>