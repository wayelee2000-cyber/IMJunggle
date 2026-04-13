---
title: Add message reaction
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
 * Add a reaction to a message
 * @param messageId The ID of the message
 * @param conversation The conversation to which the message belongs
 * @param reactionId The reaction ID
 * @param callback Result callback
 */
void addMessageReaction(String messageId,
                        Conversation conversation,
                        String reactionId,
                        ISimpleCallback callback);
```


</TabItem>
<TabItem value="ios">

**Interface definition**

```objectivec
/// Add a reaction to a message
/// - Parameters:
///   - messageId: The ID of the message
///   - conversation: The conversation to which the message belongs
///   - reactionId: The reaction ID
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)addMessageReaction:(NSString *)messageId
              conversation:(JConversation *)conversation
                reactionId:(NSString *)reactionId
                   success:(void (^)(void))successBlock
                     error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|----------|---------|----------------------------------------------------------------------------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.8.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.8.0 |
| message.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the user ID of the receiver; for `GROUP` sessions, it is the group ID | 1.8.0 |
| message.messageId | String | Yes | | The ID of the message to which the reaction is added | 1.8.0 |
| message.reactionId | String | Yes | | The unique identifier of the reaction. Developers can customize this, but it requires agreement across all clients | 1.8.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the status code and message when the operation fails. You can check `error.msg` or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.8.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  reactionId: ':smile'
};

jim.addMessageReaction(msg).then(() => {
  console.log('Message reaction added successfully.');
}, (error) => {
  console.log(error);
});
```
</TabItem>

<TabItem value="reactnative" label="ReactNative">

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------------|----------|
| messageId | String | The ID of the message | 1.0.0 |
| reactionId | String | The reaction ID | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const messageId = 'messageId1';
const reactionId = ':smile';

const success = await JuggleIM.addMessageReaction(messageId, reactionId);
console.log('addMessageReaction success:', success);
```


</TabItem>
</Tabs>