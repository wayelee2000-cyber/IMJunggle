---
title: Get the total number of unread sessions
hide_title: true
sidebar_position: 7
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
{ label: 'Hongmeng', value: 'harmony', }
]
}>
<TabItem value="android">

**Sample Code**
```java
int count = JIM.getInstance().getConversationManager().getTotalUnreadCount();
```
</TabItem>
<TabItem value="ios">

**Sample Code**
```objectivec
int count = [JIM.shared.conversationManager getTotalUnreadCount];
```

</TabItem>
<TabItem value="js">

Retrieve the total unread count across all sessions for the current user. Supports conditional filtering when both `conversationTypes` and `ignoreConversations` are provided.

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|-------|--------|----------|----------|
| params | Object | No | None | Query conditions | 1.0.0 |
| params.conversationTypes | Array | No | None | Specifies the conversation types to include | 1.0.0 |
| params.ignoreConversations | Array | No | None | Specifies conversations to exclude | 1.0.0 |

**Sample Code**
```js
// Method 1: Get the total number of unread messages across all sessions
jim.getTotalUnreadcount().then(({ count }) => {
  console.log('Current user total unread count:', count);
})

/**
Method 2: Get the total unread count filtered by conditions
Condition explanation: Get the total unread count for single chats excluding userid2
*/ 
let params = {
  conversationTypes: [ConversationType.PRIVATE],
  ignoreConversations: [
    {
      conversationType: ConversationType.PRIVATE,
      conversationId: 'userid2'
    }
  ]
};
jim.getTotalUnreadcount(params).then(({ count }) => {
  console.log('Current user total unread count:', count);
})
```
</TabItem>
<TabItem value="flutter">

Retrieve the total unread count across all conversations for the current user, with optional filtering by `ConversationType`.

**Sample Code**

```dart
// Get the total number of unread messages across all sessions
int count = await JuggleIm.instance.getTotalUnreadCount();

// Get the total unread count for all [Single Chat] conversations
int count = await JuggleIm.instance.getTotalUnreadCount([ConversationType.private]);

// Get the total unread count for all [Group] conversations
int count = await JuggleIm.instance.getTotalUnreadCount([ConversationType.group]);

// Get the total unread count for all [Single Chat + Group] conversations
int count = await JuggleIm.instance.getTotalUnreadCount([ConversationType.private, ConversationType.group]);

```
</TabItem>
<TabItem value="reactnative">

Retrieve the total unread count across all sessions for the current user, with optional filtering by conversation types.

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

// Get the total number of unread messages across all sessions
const count = await JuggleIM.getTotalUnreadCount();

// Get the total unread count for all [Single Chat] conversations
const count = await JuggleIM.getTotalUnreadCount([1]);

// Get the total unread count for all [Group] conversations
const count = await JuggleIM.getTotalUnreadCount([2]);

// Get the total unread count for all [Single Chat + Group] conversations
const count = await JuggleIM.getTotalUnreadCount([1, 2]);

```

</TabItem>
<TabItem value="harmony">

**Sample Code**
```java
JuggleIm.instance.getConversationManager().getTotalUnreadCount((code, count) => {
})
```
</TabItem>
</Tabs>