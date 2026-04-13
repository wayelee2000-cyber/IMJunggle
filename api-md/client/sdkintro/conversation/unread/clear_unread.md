---
title: Clear unread data from a single session
hide_title: true
sidebar_position: 9
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

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|--------|------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | IConversationManager.ISimpleCallback | Result callback | 1.0.0 |

**Sample Code**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
JIM.getInstance().getConversationManager().clearUnreadCount(conversation, new IConversationManager.ISimpleCallback() {
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

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|--------|------------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |

**Sample Code**
```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.conversationManager clearUnreadCountByConversation:conversation
                                                        success:^{
    
} error:^(JErrorCode code) {

}];
```

</TabItem>
<TabItem value="js">

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|---------|--------|--------|------------|----------|
| conversation | Object | Yes | | | 1.0.0 |
| conversation.conversationType | Number | Yes | | Conversation type | 1.0.0 |
| conversation.conversationId | String | Yes | | Conversation ID | 1.0.0 |
| conversation.unreadIndex | Number | Yes | | The index of the last unread message in the conversation, available at `conversation.latestUnreadIndex` | 1.0.0 |
| conversation.messageId | String | Yes | | The last message ID in the conversation, available at `conversation.latestMessage` | 1.0.0 |
| conversation.messageSentTime | Number | Yes | | The timestamp when the last message was sent, available at `conversation.latestMessage` | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId02',
  messageSentTime: 1724675506002,
  messageId: 'djdjakdk394alkjda',
  unreadIndex: 9
};

jim.clearUnreadcount(conversation).then(() => {
  console.log('Cleared unread count successfully');
});
```
</TabItem>
<TabItem value="flutter">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|--------|------------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |

**Sample Code**
```dart
Conversation conversation = Conversation(ConversationType.private, 'user1');
Result result = await JuggleIm.instance.clearUnreadCount(conversation);
```

</TabItem>
<TabItem value="reactnative">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|--------|------------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |

**Sample Code**
```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.clearUnreadCount({
  conversationType: 1,
  conversationId: 'user1'
});
```

</TabItem>
<TabItem value="harmony">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|--------|------------|----------|
| conver | Conversation | Session ID | 1.0.0 |
| callback | CommonCallback | Result callback | 1.0.0 |

**Sample Code**
```java
let conver = new Conversation("userid1", 1);
JuggleIm.instance.getConversationManager().clearUnreadCount(conver, (code) => {
  
});
```

</TabItem>
</Tabs>