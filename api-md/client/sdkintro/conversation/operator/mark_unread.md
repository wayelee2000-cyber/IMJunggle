---
title: Mark conversation status
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

This method sets the unread status of a conversation and supports marking it as `unread`. To clear the unread status, you can call the [Clear Single Conversation Unread](../unread/clear_unread.md) interface. The SDK will automatically synchronize the mark status across all devices of the current user.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.3.0 |
| callback | ISimpleCallback | Result callback | 1.3.0 |

**Sample Code**

```java
Conversation c = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
JIM.getInstance().getConversationManager().setUnread(c, new IConversationManager.ISimpleCallback() {
    @Override
    public void onSuccess() {
        
    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

This method sets the unread status of a conversation and supports marking it as `unread`. To clear the unread status, you can call the [Clear Single Conversation Unread](../unread/clear_unread.md) interface. The SDK will automatically synchronize the mark status across all devices of the current user.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | JConversation | Conversation identifier | 1.3.0 |
| successBlock | | Success callback | 1.3.0 |
| errorBlock | | Failure callback | 1.3.0 |

**Sample Code**

```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
[JIM.shared.conversationManager setUnread:c
                                  success:^{
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">

This method sets the unread status of a conversation and supports marking it as `unread`. To clear the unread status, you can call the [Clear Single Conversation Unread](../unread/clear_unread.md) interface. The SDK will automatically synchronize the mark status across all devices of the current user.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------|---------|-------|---|------------------------------------------------|----------|
| conversation | Object | Yes | None | Conversation object | 1.5.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.5.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.5.0 |
| conversation.unreadTag | Number | Yes | | [Conversation Tag Status](../../enum/web.md#unreadtag) | 1.5.0 |

**Sample Code**

```js
jim.markUnread({
  conversationId: '7KeH8fjCO',
  conversationType: 2,
  unreadTag: UnreadTag.UNREAD,
}).then(() => {
  console.log('Marked as unread successfully');
}, (error) => {
  console.log(error);
});
```
</TabItem>

<TabItem value="flutter" label="Flutter">

This method sets the unread status of a conversation and supports marking it as `unread`. To clear the unread status, you can call the [Clear Single Conversation Unread](../unread/clear_unread.md) interface. The SDK will automatically synchronize the mark status across all devices of the current user. After a successful update, a conversation change event will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
await JuggleIm.instance.setUnread(conversation);
```

</TabItem>
<TabItem value="reactnative">

This method sets the unread status of a conversation and supports marking it as `unread`. To clear the unread status, you can call the [Clear Single Conversation Unread](../unread/clear_unread.md) interface. The SDK will automatically synchronize the mark status across all devices of the current user. After a successful update, a conversation change event will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Conversation ID | 0.6.3 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.setUnread({
  conversationType: 2,
  conversationId: 'groupId1'
});
```

</TabItem>
</Tabs>
