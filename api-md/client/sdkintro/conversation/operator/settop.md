---
title: Pin conversation
hide_title: true
sidebar_position: 4
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
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| isTop | boolean | Whether to pin the conversation to the top | 1.0.0 |
| callback | ISimpleCallback | Result callback | 1.0.0 |

**Sample Code**

```java
JIM.getInstance().getConversationManager().setTop(conversation, true, new IConversationManager.ISimpleCallback() {
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

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| isTop | BOOL | Whether to pin the conversation to the top | 1.0.0 |
| conversation | JConversation | Conversation identifier | 1.0.0 |
| successBlock | | Success callback | 1.0.0 |
| errorBlock | | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
[JIM.shared.conversationManager setTop:YES
                          conversation:conversation
                                success:^{
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">

Pinning the conversation supports multi-end synchronization. After successfully calling the pin method, [conversation change event](../../watcher/conversation.md) will be triggered.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|-------|--------|----------|----------|
| conversation | Object | Yes | None | Conversation object | 1.0.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.0.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.0.0 |
| conversation.isTop | Boolean | Yes | None | Whether to pin the conversation to the top | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01',
  isTop: true
};

jim.setTopConversation(conversation).then(() => {
  console.log('Set conversation top successfully');
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Pinning the conversation supports multi-end synchronization. After successfully calling the pin method, [Conversation change event](../../watcher/conversation.md) will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |
| isTop | bool | Whether to pin the conversation to the top | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.private, 'user1');
await JuggleIm.instance.setTop(conversation, true);
```

</TabItem>
<TabItem value="reactnative">

Pinning the conversation supports multi-end synchronization. After successfully calling the pin method, [Conversation change event](../../watcher/conversation.md) will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Conversation ID | 0.6.3 |
| isTop | Boolean | Whether to pin the conversation to the top | 0.6.3 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.setTop({
  conversationType: 1,
  conversationId: 'user1',
  isTop: true
});
```

</TabItem>
</Tabs>
