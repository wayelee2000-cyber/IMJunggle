---
title: Get a single session
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

Retrieve the specified session information based on the session ID `Conversation`. Returning an empty object indicates that no session information exists.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |

**Sample Code**
```java
ConversationInfo info = JIM.getInstance().getConversationManager().getConversationInfo(conversation);
```

</TabItem>
<TabItem value="ios">

Retrieve the specified session information based on the session ID `JConversation`. Returning an empty object indicates that no session information exists.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |

**Sample Code**
```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
JConversationInfo *info = [JIM.shared.conversationManager getConversationInfo:conversation];
```

</TabItem>
<TabItem value="js">

Retrieve the specified session based on `conversationType` and `conversationId`. If the session does not exist locally, it will be fetched from the cloud. An empty object indicates that no session information exists.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------|---------|-------|---|------------------------------------------------|----------|
| conversation | Object | Yes | None | Conversation object to retrieve | 1.0.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.0.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.0.0 |

**Callback Parameters**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | Object | Return value | 1.0.0 |
| result.conversation | Object | An empty object indicates the conversation does not exist. See [Conversation](../../conversation) for properties. | 1.0.0 |


**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.getConversation(conversation).then(({ conversation }) => {
  console.log(conversation);
});

```
</TabItem>

<TabItem value="flutter" label="Flutter">

Retrieve the specified session information. Returning an empty object indicates that no session information exists. This method only retrieves session information from the local database and does not fetch it from the cloud.

**Parameter description**

| Name | Type | Description | Version |
|------------------|--------------|----------|----------|
| conversationType | int | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
ConversationInfo? conversationInfo = await JuggleIm.instance.getConversationInfo(conversation);
```

</TabItem>
<TabItem value="reactnative">

Retrieve the specified session information. Returning an empty object indicates that no session information exists. This method only retrieves session information from the local database and does not fetch it from the cloud.

**Parameter description**

| Name | Type | Description | Version |
|------------------|--------------|----------|----------|
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversationInfo = await JuggleIM.getConversationInfo({
  conversationType: 2,
  conversationId: 'groupId1'
});
```

</TabItem>
</Tabs>