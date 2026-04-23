---
title: set to top
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
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

Setting a message to the top allows you to pin a specific message at the top of the conversation as a reminder. The actions `Set to the top` and `Cancel the message to the top` are distinguished by the `isTop` parameter.

**Interface definition**

```java
/**
 * Set top
 * @param messageId message id
 * @param conversation conversation ID to which the message belongs
 * @param isTop Whether to pin the message to the top
 * @param callback result callback
 */
void setTop(String messageId, Conversation conversation, boolean isTop, ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

Setting a message to the top allows you to pin a specific message at the top of the conversation as a reminder. The actions `Set to the top` and `Cancel the message to the top` are distinguished by the `isTop` parameter.

**Interface definition**

```objectivec
/// Set top
/// - Parameters:
///   - isTop: YES to pin the message to the top, NO to unpin
///   - messageId: message id
///   - conversation: conversation identifier
///   - successBlock: success callback
///   - errorBlock: failure callback
- (void)setTop:(BOOL)isTop
     messageId:(NSString *)messageId
  conversation:(JConversation *)conversation
       success:(void (^)(void))successBlock
         error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

Setting a message to the top allows you to pin a specific message at the top of the conversation as a reminder. The actions `Set to the top` and `Cancel the message to the top` are distinguished by the `isTop` parameter.

![](./top.png)

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, it is the group ID | 1.0.0 |
| message.messageId | String | Yes | | ID of the message to pin | 1.0.0 |
| message.isTop | Boolean | Yes | | Whether to pin the message to the top | 1.0.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the status code if the operation fails. You can check `error.msg` or refer to [Status Code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  isTop: true
};

jim.setTopMessage(msg).then(() => {
  console.log('Message pinned to top successfully.');
}, (error) => {
  console.log(error);
});
```
</TabItem>

<TabItem value="reactnative" label="ReactNative">

Setting a message to the top allows you to pin a specific message at the top of the conversation as a reminder. The actions `Set to the top` and `Cancel the message to the top` are distinguished by the `isTop` parameter.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------------|----------|
| messageId | String | Message ID | 1.0.0 |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| isTop | boolean | Whether to pin the message to the top | 1.0.0 |

**Sample Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const messageId = 'messageId1';
const conversation = {
  type: 1,
  id: 'userId1'
};
const isTop = true;

const success = await JuggleIM.setMessageTop(messageId, conversation, isTop);
console.log('setMessageTop success:', success);
```

</TabItem>
</Tabs>
