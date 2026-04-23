---
title: Delete conversation draft
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

| Name         | Type         | Description             | Version |
|--------------|--------------|-------------------------|---------|
| conversation | Conversation | Conversation identifier | 1.0.0   |

**Sample Code**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
JIM.getInstance().getConversationManager().clearDraft(conversation);
```
</TabItem>
<TabItem value="ios">

**Parameter description**

| Name         | Type          | Description         | Version |
|--------------|---------------|---------------------|---------|
| conversation | JConversation | Conversation identifier  | 1.0.0   |

**Sample Code**
```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.conversationManager clearDraftInConversation:c];
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name                     | Type   | Required | Default | Description          | Version |
|--------------------------|--------|----------|---------|----------------------|---------|
| conversation             | Object | Yes      | None    | Conversation object  | 1.0.0   |
| conversation.conversationType | Number | Yes      | None    | Conversation type    | 1.0.0   |
| conversation.conversationId   | String | Yes      | None    | Conversation ID      | 1.0.0   |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.removeDraft(conversation).then(() => {
  console.log('Conversation draft removed successfully');
});
```
</TabItem>
<TabItem value="harmony" label="Harmony">

**Parameter description**

| Name         | Type         | Description             | Version |
|--------------|--------------|-------------------------|---------|
| conversation | Conversation | Conversation identifier | 1.0.0   |

**Sample Code**
```java
JuggleIm.instance.getConversationManager().clearDraft(new Conversation("userid1",1));
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Deleting a conversation draft is equivalent to clearing the draft for that conversation and only affects the current device. The draft will not be synchronized across multiple devices. After the operation succeeds, conversation change monitoring will be triggered, allowing the UI to update accordingly.

**Parameter description**

| Name         | Type         | Description             | Version |
|--------------|--------------|-------------------------|---------|
| conversation | Conversation | Conversation identifier | 0.6.3   |
| draft        | String       | Draft content           | 0.6.3   |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupid1');
await JuggleIm.instance.setDraft(conversation, '');
```

</TabItem>
<TabItem value="reactnative">

Deleting a conversation draft is equivalent to clearing the draft for that conversation and only affects the current device. The draft will not be synchronized across multiple devices. After the operation succeeds, conversation change monitoring will be triggered, allowing the UI to update accordingly.

**Parameter description**

| Name             | Type   | Description             | Version |
|------------------|--------|-------------------------|---------|
| conversation     | Object | Conversation identifier | 0.6.3   |
| conversationType | Number | Conversation type       | 0.6.3   |
| conversationId   | String | Conversation ID              | 0.6.3   |
| draft           | String | Draft content           | 0.6.3   |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.clearDraft({
  conversationType: 2,
  conversationId: 'groupid1'
});
```

</TabItem>
</Tabs>
