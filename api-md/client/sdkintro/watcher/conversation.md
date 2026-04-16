---
title: 会话监听
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

Multiple listeners can be set.

```java
JIM.getInstance().getConversationManager().addListener("main", new IConversationManager.IConversationListener() {
  /// Callback for conversation addition
  @Override
  public void onConversationInfoAdd(List<ConversationInfo> conversationInfoList) {
      Log.i("TAG", "onConversationInfoAdd, count is " + conversationInfoList.size());
  }

  /// Callback for conversation updates; triggered on any change to conversation info
  @Override
  public void onConversationInfoUpdate(List<ConversationInfo> conversationInfoList) {
      Log.i("TAG", "onConversationInfoUpdate, count is " + conversationInfoList.size());
  }

  /// Callback for conversation deletion
  @Override
  public void onConversationInfoDelete(List<ConversationInfo> conversationInfoList) {
      Log.i("TAG", "onConversationInfoDelete, count is " + conversationInfoList.size());
  }

  /// Callback for total unread message count changes
  @Override
  public void onTotalUnreadMessageCountUpdate(int count) {
      Log.i("TAG", "onTotalUnreadMessageCountUpdate, count is " + count);
  }
});

```

</TabItem>

<TabItem value="ios">

Multiple delegates can be set.

```objectivec
[JIM.shared.conversationManager addDelegate:self];

/// Callback for conversation addition
- (void)conversationInfoDidAdd:(NSArray<JConversationInfo *> *)conversationInfoList {
    NSLog(@"conversationInfoDidAdd");
}

/// Callback for conversation updates; triggered on any change to conversation info
- (void)conversationInfoDidUpdate:(NSArray<JConversationInfo *> *)conversationInfoList {
    NSLog(@"conversationInfoDidUpdate");
}

/// Callback for conversation deletion
- (void)conversationInfoDidDelete:(NSArray<JConversationInfo *> *)conversationInfoList {
    NSLog(@"conversationInfoDidDelete");
}

/// Callback for total unread message count changes
- (void)totalUnreadMessageCountDidUpdate:(int)count {
    NSLog(@"totalUnreadMessageCountDidUpdate");
}

```

</TabItem>
<TabItem value="js">

**Interface Description**: Listeners for conversation addition, deletion, and updates need to be set only once globally; multiple settings will overwrite previous ones.

**Related Enums**: [Conversation](../../../conversation), [Event](../../../enum/web#listener)

```js
let { Event } = JIM;

// Listener for conversation addition: triggered on first message sent/received, local conversation insertion, and multi-device conversation synchronization
jim.on(Event.CONVERSATION_ADDED, ({ conversations }) => {
  console.log(conversations);
});

// Listener for conversation deletion: triggered when deleting conversations locally or synchronizing deletions from other devices
jim.on(Event.CONVERSATION_REMOVED, ({ conversations }) => {
  console.log(conversations);
});

// Listener for conversation updates: triggered on non-initial message send/receive (initial triggers addition event), message deletion/modification, do-not-disturb, pinning, and multi-device synchronization
jim.on(Event.CONVERSATION_CHANGED, ({ conversations }) => {
  console.log(conversations);
});
```
</TabItem>

<TabItem value="reactnative">

Multiple listeners can be set, each requiring a unique key. The returned function can be used to remove the listener.

**Example Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

// Add a conversation listener; returns a function to unsubscribe
const unsubscribeConversation = JuggleIM.addConversationListener('conversation_key', {
  // Callback for conversation addition: triggered on first message sent/received, local insertion, and multi-device synchronization
  onConversationInfoAdd: (conversations) => {
    console.log('New conversations:', conversations);
  },

  // Callback for conversation updates: triggered on non-initial message send/receive (initial triggers addition event), message deletion/modification, do-not-disturb, pinning, and multi-device synchronization
  onConversationInfoUpdate: (conversations) => {
    console.log('Updated conversations:', conversations);
  },

  // Callback for conversation deletion: triggered when deleting conversations locally or synchronizing deletions from other devices
  onConversationInfoDelete: (conversations) => {
    console.log('Deleted conversations:', conversations);
  },

  // Callback for total unread message count changes: triggered by receiving counted messages (e.g., text, images), clearing unread counts, and other operations affecting unread counts
  onTotalUnreadMessageCountUpdate: (count) => {
    console.log('Total unread count updated:', count);
  }
});

// To unsubscribe
// unsubscribeConversation();
```

</TabItem>
<TabItem value="flutter" label="Flutter">

Connection listeners support only a single setting; multiple settings will overwrite previous listeners. If multiple listeners are needed, it is recommended to handle all states within one listener and perform secondary event dispatching at the business logic layer.

```dart
// Callback for conversation addition: triggered on first message sent/received, local insertion, and multi-device synchronization
JuggleIm.instance.onConversationInfoAdd = (List<ConversationInfo> conversations) {
};

// Callback for conversation updates: triggered on non-initial message send/receive (initial triggers addition event), message deletion/modification, do-not-disturb, pinning, and multi-device synchronization
JuggleIm.instance.onConversationInfoUpdate = (List<ConversationInfo> conversations) {
};

// Callback for conversation deletion: triggered when deleting conversations locally or synchronizing deletions from other devices
JuggleIm.instance.onConversationInfoDelete = (List<ConversationInfo> conversations) {
};

// Callback for total unread message count changes: triggered by receiving counted messages (e.g., text, images), clearing unread counts, and other operations affecting unread counts
JuggleIm.instance.onTotalUnreadMessageCountUpdate = (list) {
};
```

</TabItem>
</Tabs>