---
title: Delete conversation from label
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

Remove a conversation from a label. This action automatically synchronizes across all devices of the current user.

**Interface definition**

```java
/**
 * Remove conversation from label
 * @param conversations List of conversations
 * @param tagId Tag ID
 * @param callback Result callback
 */
void removeConversationsFromTag(List<Conversation> conversations, String tagId, ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

Remove a conversation from a label. This action automatically synchronizes across all devices of the current user.

**Interface definition**

```objectivec
/// Remove conversations from a label
/// - Parameters:
///   - conversationList: List of conversations to be removed
///   - tagId: Tag ID
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)removeConversationList:(NSArray <JConversation *> *)conversationList
                       fromTag:(NSString *)tagId
                       success:(void (^)(void))successBlock
                         error:(void (^)(JErrorCode code))errorBlock;
```
</TabItem>
<TabItem value="js">

Remove a conversation from a label. This action automatically synchronizes across all devices of the current user.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|--------|--------|-----------------------------------------------|----------|
| tag | Object | Yes | | Tag object | 1.7.5 |
| tag.id | String | Yes | | Tag ID, customizable by the developer, maximum length 64 characters | 1.7.5 |
| tag.conversations | Array | Yes | | List of conversations, see code example | 1.7.5 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code if the operation fails. You can access `error.msg` directly or refer to [Status Code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let tag = {
  id: 'tag_01',
  conversations: [
    { conversationType: ConversationType.PRIVATE, conversationId: 'userId01' }
  ]
};

jim.removeConversationsFromTag(tag).then(() => {
  console.log('removeConversationsFromTag succeeded');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
<TabItem value="reactnative">

Remove a conversation from a label. This action automatically synchronizes across all devices of the current user.

**Interface definition**

```typescript
/**
 * Remove conversation from label
 * @param tagId Tag ID
 * @param conversations List of conversations
 */
removeConversationsFromTag(tagId: string, conversations: Array<{
  conversationType: number;
  conversationId: string;
}>): Promise<void>;
```

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.removeConversationsFromTag('tag_01', [
  {
    conversationType: 1,
    conversationId: 'userId01'
  }
]);
```

</TabItem>
</Tabs>
