---
title: Set up session draft
hide_title: true
sidebar_position: 2
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

Set up conversation drafts that are stored locally and will not be synced to the cloud.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|--------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| draft | String | Draft content | 1.0.0 |


**Sample Code**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
JIM.getInstance().getConversationManager().setDraft(conversation, "draft");
```

</TabItem>
<TabItem value="ios">

Set up conversation drafts that are stored locally and will not be synced to the cloud.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|--------|----------|----------|
| draft | NSString | Draft content | 1.0.0 |
| conversation | JConversation | Session identifier | 1.0.0 |

**Sample Code**
```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.conversationManager setDraft:@"draft" inConversation:c];
```

</TabItem>
<TabItem value="js">

Set the session draft, which is stored locally and will not be synchronized to the cloud. The draft will become invalid when you change the browser. After successfully calling the set session draft method, session monitoring will not be triggered. Developers can update the UI as needed.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|-------|--------|----------|----------|
| conversation | Object | Yes | None | Conversation object | 1.0.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.0.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.0.0 |
| conversation.draft | String | Yes | None | Draft content | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01',
  draft: 'I am a session draft'
};

jim.setDraft(conversation).then(() => {
  console.log('Set conversation draft successfully');
});
```
</TabItem>
<TabItem value="harmony" label="Harmony">

Set up conversation drafts that are stored locally and will not be synced to the cloud.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|--------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| draft | String | Draft content | 1.0.0 |


**Sample Code**
```java
JuggleIm.instance.getConversationManager().setDraft(new Conversation("groupid1", 2), "draft");
```

</TabItem>
<TabItem value="flutter" label="Flutter">

Set the session draft, which is stored locally and will not be synchronized across multiple devices. After successfully setting the draft, session change monitoring will be triggered, allowing the UI to update accordingly.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|--------|----------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |
| draft | String | Draft content | 0.6.3 |


**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupid1');
await JuggleIm.instance.setDraft(conversation, 'draft');
```

</TabItem>
<TabItem value="reactnative">

Set the session draft, which is stored locally and will not be synchronized to the cloud. After successfully setting the draft, session change monitoring will be triggered, allowing the UI to update accordingly.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|--------|----------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |
| draft | String | Draft content | 0.6.3 |


**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.setDraft({
  conversationType: 2,
  conversationId: 'groupid1',
  draft: 'draft'
});
```

</TabItem>
</Tabs>