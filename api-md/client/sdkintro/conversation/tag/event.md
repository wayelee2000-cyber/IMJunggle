---
title: Label event listening
hide_title: true
sidebar_position: 1
---

<Tabs
groupId="sdks-language"
values={[
  { label: 'Android', value: 'android' },
  { label: 'iOS', value: 'ios' },
  { label: 'JavaScript', value: 'js' },
  { label: 'Flutter', value: 'flutter' },
  { label: 'ReactNative', value: 'reactnative' }
]}
>
<TabItem value="android">

Multiple listeners can be registered.

```java
JIM.getInstance().getConversationManager().addTagListener("main", new IConversationManager.IConversationTagListener() {
  /// Called when new conversations are added to the tag
  @Override
  public void onConversationsAddToTag(String tagId, List<Conversation> conversations) {
  }

  /// Called when conversations are removed from the tag
  @Override
  public void onConversationsRemoveFromTag(String tagId, List<Conversation> conversations) {
  }
});
```

</TabItem>
<TabItem value="ios">

Multiple delegates can be registered.

```objectivec
[JIM.shared.conversationManager addTagDelegate:self];

/// Called when new conversations are added to the tag
- (void)conversationsDidAddToTag:(NSString *)tagId
                   conversations:(NSArray <JConversation *> *)conversationList {
}

/// Called when conversations are removed from the tag
- (void)conversationsDidRemoveFromTag:(NSString *)tagId
                        conversations:(NSArray <JConversation *> *)conversationList {
}
```

</TabItem>
<TabItem value="js">

```js
let { Event } = JIM;

### Add new tag
jim.on(Event.TAG_ADDED, ({ tags }) => {
  /* tags => [{ id: 'tag_01', name: 'My attention' }, ... ] */
});

### Remove tag
jim.on(Event.TAG_REMOVED, (notify) => {
  /* tags => [{ id: 'tag_01' }, ... ] */
});

### Tag updated
jim.on(Event.TAG_CHANGED, (notify) => {
  /* tags => [{ id: 'tag_01', name: 'My attention' }, ... ] */
});

### Conversation added to tag
jim.on(Event.TAG_CONVERSATION_ADDED, (notify) => {
  /* tags => [{ id: 'tag_01', conversations: [ Conversation, ... ] }, ... ] */
});

### Conversation removed from tag
jim.on(Event.TAG_CONVERSATION_REMOVED, (notify) => {
  /* tags => [{ id: 'tag_01', conversations: [ Conversation, ... ] }, ... ] */
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet available

</TabItem>
<TabItem value="reactnative">

Multiple listeners can be registered.

```javascript
import JuggleIM from 'juggleim-rnsdk';

// Listen for conversations added to a tag
const removeAddToTagListener = JuggleIM.addConversationsAddToTagListener((data) => {
  console.log('Conversations added to tag:', data);
});

// Listen for conversations removed from a tag
const removeRemoveFromTagListener = JuggleIM.addConversationsRemoveFromTagListener((data) => {
  console.log('Conversations removed from tag:', data);
});

// Remove listeners
removeAddToTagListener();
removeRemoveFromTagListener();
```

</TabItem>
</Tabs>