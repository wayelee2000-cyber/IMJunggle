---
title: Delete specified session
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

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|-------------------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | IConversationManager.ISimpleCallback | Result callback | 1.0.0 |

**Sample Code**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "user1");
JIM.getInstance().getConversationManager().deleteConversationInfo(conversation, new IConversationManager.ISimpleCallback() {
    @Override
    public void onSuccess() {
        // Handle success
    }

    @Override
    public void onError(int errorCode) {
        // Handle error
    }
});
```

</TabItem>
<TabItem value="ios">

**Parameter description**

| Name | Type | Description | Version |
|----------------|---------|-------------------------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |
| successBlock | Block | Success callback | 1.0.0 |
| errorBlock | Block | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"user1"];

[JIM.shared.conversationManager deleteConversationInfoBy:conversation
                                                success:^{
    // Handle success
} error:^(JErrorCode code) {
    // Handle error
}];
```

</TabItem>
<TabItem value="js">

Deleted sessions are synchronized across multiple devices. Both local and cloud data will be deleted. After the session is successfully deleted, [session deletion monitoring](../../../watcher/conversation) will be triggered.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------|---------|----------|---------|------------------------------------------------|----------|
| conversation | Object | Yes | None | Conversation to delete; supports deleting a single conversation or an array of conversations | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

// Delete a single session
jim.removeConversation(conversation).then(() => {
  console.log('Conversation removed successfully');
});

// Delete sessions in batch
let conversations = [conversation];
jim.removeConversation(conversations).then(() => {
  console.log('Conversations removed successfully');
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Deleting a session is synchronized across multiple devices. Both local and cloud data will be deleted. After the session is successfully deleted, [session deletion monitoring](../../../watcher/conversation) will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|-------------------------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.private, 'user1');
Result result = await JuggleIm.instance.deleteConversationInfo(conversation);
```

</TabItem>
<TabItem value="reactnative">

Deleting a session is synchronized across multiple devices. Both local and cloud data will be deleted. After the session is successfully deleted, [session deletion monitoring](../../../watcher/conversation) will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|-------------------------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.deleteConversationInfo({
  conversationType: 1,
  conversationId: 'user1'
});
```

</TabItem>
</Tabs>