---
title: Insert the specified session
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
{ label: 'Hongmeng', value: 'harmony', }
]
}>
<TabItem value="android">

When inserting a session, the SDK automatically inserts it locally and in the cloud, supporting multi-end synchronization.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | ICreateConversationInfoCallback | Result callback | 1.0.0 |


**Sample Code**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
JIM.getInstance().getConversationManager().createConversationInfo(conversation, new IConversationManager.ICreateConversationInfoCallback() {
    @Override
    public void onSuccess(ConversationInfo conversationInfo) {

    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

When inserting a session, the SDK automatically inserts it locally and in the cloud, supporting multi-end synchronization.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |
| successBlock | | Success callback | 1.0.0 |
| errorBlock | | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
[JIM.shared.conversationManager createConversationInfo:conversation success:^(JConversationInfo *) {
    
} error:^(JErrorCode code) {
    
}];

```

</TabItem>
<TabItem value="js">

When inserting a session, the SDK automatically inserts it locally and in the cloud, supporting multi-end synchronization. If the session already exists, the original session will be **overwritten**.

:::info session information

> The Web SDK relies on the user information provided during registration to obtain a token, or on the avatar and group nickname specified when creating a group. If there is no registration or group creation with group information set, session information will not be available.

> Electron follows the Web SDK principles, but specifying `conversationTitle` and `conversationPortrait` will save them in the local database, and retrieving the session list will return these values.
:::


**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|-------|--------|----------|----------|
| conversation | Object | Yes | None | Conversation object | 1.0.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.0.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.0.0 |
| conversation.conversationTitle | String| No | None | Conversation name | 1.0.0 |
| conversation.conversationPortrait | String| No | None | Conversation portrait | 1.0.0 |

**Callback description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.0.0 |
| result.conversation | Object | [Conversation object](../../../conversation), containing user or group information | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.insertConversation(conversation).then((result) => {
  let { conversation } = result;
  console.log(conversation);
});
```
</TabItem>

<TabItem value="flutter" label="Flutter">

Insert sessions automatically into local and cloud storage, supporting synchronization across the current user's devices. If the session already exists, the original session will not be overwritten. After a successful insertion, the session listening event will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|--------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.private, 'userid1');
Result<ConversationInfo> result = await JuggleIm.instance.createConversationInfo(conversation);
```

</TabItem>
<TabItem value="reactnative">

Insert sessions automatically into local and cloud storage, supporting synchronization across the current user's devices. If the session already exists, the original session will not be overwritten. After a successful insertion, the session listening event will be triggered.

**Parameter description**

| Name | Type | Description | Version |
|--------------|---------|----------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const result = await JuggleIM.createConversationInfo({
  conversationType: 1,
  conversationId: 'userid1'
});
```

</TabItem>
<TabItem value="harmony">

Insert sessions automatically into local and cloud storage, supporting synchronization across the current user's devices. If the session already exists, the original session will not be overwritten.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | ConversationInsertCallback | Result callback | 1.0.0 |

**Interface definition**

```java
// Callback definition
export type ConversationInsertCallback = (code: number, conver: ConversationInfo) => void;

insertConversation(conver: Conversation, callback: ConversationInsertCallback);
```

**Sample Code**

```java
let conver = new Conversation("userid1", 1);
JuggleIm.instance.getConversationManager().insertConversation(conver, (converInfo) => {
  
});
```

</TabItem>

</Tabs>