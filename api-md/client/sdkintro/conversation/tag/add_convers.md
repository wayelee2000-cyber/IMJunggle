---
title: Add conversation to label
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

Add a conversation to an existing tag and perform a session action to automatically synchronize across the current user's multiple devices.

**Interface definition**

```java
/**
 * Add conversation to label
 * @param conversations List of conversations
 * @param tagId Tag ID
 * @param callback Result callback
 */
void addConversationsToTag(List<Conversation> conversations, String tagId, ISimpleCallback callback);
```


</TabItem>
<TabItem value="ios">

Add a conversation to an existing tag and perform a session action to automatically synchronize across the current user's multiple devices.

**Interface definition**

```objectivec
/// Add conversations to a label
/// - Parameters:
///   - conversationList: List of conversations
///   - tagId: Tag ID
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)addConversationList:(NSArray <JConversation *> *)conversationList
                      toTag:(NSString *)tagId
                    success:(void (^)(void))successBlock
                      error:(void (^)(JErrorCode code))errorBlock;
```


</TabItem>
<TabItem value="js">

Add a conversation to an existing tag and perform a session action to automatically synchronize across the current user's multiple devices.

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
| error | Object | Contains a status code if the operation fails. You can access `error.msg` or refer to [Status Code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let tag = {
  id: 'tag_01',
  conversations: [
    { conversationType: ConversationType.PRIVATE, conversationId: 'userId01' }
  ]
};

jim.addConversationsToTag(tag).then(() => {
  console.log('addConversationsToTag succeeded');
}, (error) => {
  console.log(error);
});
```

</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
<TabItem value="reactnative">

Add a conversation to an existing tag and perform a session action to automatically synchronize across the current user's multiple devices.

**Interface definition**

```typescript
/**
 * Add conversations to a label
 * @param tagId Tag ID
 * @param conversations List of conversations
 */
addConversationsToTag(tagId: string, conversations: Array<{
  conversationType: number;
  conversationId: string;
}>): Promise<void>;
```

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.addConversationsToTag('tag_01', [
  {
    conversationType: 1,
    conversationId: 'userId01'
  }
]);
```

</TabItem>
</Tabs>
