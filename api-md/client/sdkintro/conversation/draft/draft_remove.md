---
title: 删除会话草稿
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|-------|---|----------|----------|
| conversation                    | Conversation | 会话标识 | 1.0.0    |

**示例代码**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
JIM.getInstance().getConversationManager().clearDraft(conversation);
```
</TabItem>
<TabItem value="ios">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|-------|---|----------|----------|
| conversation                    | JConversation | 会话标识 | 1.0.0    |

**示例代码**
```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.conversationManager clearDraftInConversation:c];
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                             | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------------------------|---------|-------|---|----------|----------|
| conversation                    | Object | 是     | 无 | 会话对象 | 1.0.0    |
| conversation.conversationType   | Number | 是     | 无 | 会话类型 | 1.0.0    |
| conversation.conversationId     | String | 是     | 无 | 会话 Id | 1.0.0    |

**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.removeDraft(conversation).then(() => {
  console.log('remove conversation draft successfully');
});
```
</TabItem>
<TabItem value="harmony" label="Harmony">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|-------|---|----------|----------|
| conversation                    | Conversation | 会话标识 | 1.0.0    |

**示例代码**
```java
JuggleIm.instance.getConversationManager().clearDraft(new Conversation("userid1",1))
```
</TabItem>
<TabItem value="flutter" label="Flutter">

删除会话草稿相当于置空会话草稿，仅影响当前端，草稿不会多端同步，设置成功后会触发会话变更监听，可根据会话变更监听更新 UI。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|--------|----------|----------|
| conversation   | Conversation | 会话标识 | 0.6.3    |
| draft          | String     | 草稿内容 | 0.6.3    |


**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupid1');
await JuggleIm.instance.setDraft(conversation, '');
```

</TabItem>
<TabItem value="reactnative">

删除会话草稿相当于置空会话草稿，仅影响当前端，草稿不会多端同步，设置成功后会触发会话变更监听，可根据会话变更监听更新 UI。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|--------|----------|----------|
| conversation   | Object | 会话标识 | 0.6.3    |
| conversationType   | Number | 会话类型 | 0.6.3    |
| conversationId   | String | 会话ID | 0.6.3    |
| draft          | String     | 草稿内容 | 0.6.3    |


**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.clearDraft({
  conversationType: 2,
  conversationId: 'groupid1'
});
```

</TabItem>
</Tabs>