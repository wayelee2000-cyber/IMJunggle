---
title: 设置会话草稿
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

设置会话草稿，存储在本地，不会同步至云端。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|--------|----------|----------|
| conversation   | Conversation | 会话标识 | 1.0.0    |
| draft                    | String | 草稿内容 | 1.0.0    |


**示例代码**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
JIM.getInstance().getConversationManager().setDraft(conversation, "draft");
```

</TabItem>
<TabItem value="ios">

设置会话草稿，存储在本地，不会同步至云端。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|--------|----------|----------|
| draft                    | NSString | 草稿内容 | 1.0.0    |
| conversation   | JConversation | 会话标识 | 1.0.0    |

**示例代码**
```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.conversationManager setDraft:@"draft" inConversation:c];
```

</TabItem>
<TabItem value="js">

设置会话草稿，存储在本地，不会同步至云端，更换浏览器草稿将失效，设置会话草稿方法调用成功后 **不会触发** 会话监听，开发者按需自行处理 UI

**参数说明**

| 名称                             | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------------------------|---------|-------|--------|----------|----------|
| conversation                    | Object | 是     | 无 | 会话对象 | 1.0.0    |
| conversation.conversationType   | Number | 是     | 无 | 会话类型 | 1.0.0    |
| conversation.conversationId     | String | 是     | 无 | 会话 Id | 1.0.0    |
| conversation.draft              | String | 是     | 无 | 草稿内容 | 1.0.0    |

**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01',
  draft: '我是会话草稿'
};

jim.setDraft(conversation).then(() => {
  console.log('set conversation draft successfully');
});
```
</TabItem>
<TabItem value="harmony" label="Harmony">

设置会话草稿，存储在本地，不会同步至云端。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|--------|----------|----------|
| conversation   | Conversation | 会话标识 | 1.0.0    |
| draft                    | String | 草稿内容 | 1.0.0    |


**示例代码**
```java
JuggleIm.instance.getConversationManager().setDraft(new Conversation("groupid1",2),"draft")
```

</TabItem>
<TabItem value="flutter" label="Flutter">

设置会话草稿，存储在本地且不会多端同步，设置成功后会触发会话变更监听，可根据会话变更监听更新 UI。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|--------|----------|----------|
| conversation   | Conversation | 会话标识 | 0.6.3    |
| draft          | String     | 草稿内容 | 0.6.3    |


**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupid1');
await JuggleIm.instance.setDraft(conversation, 'draft');
```

</TabItem>
<TabItem value="reactnative">

设置会话草稿，存储在本地，不会同步至云端，设置成功后会触发会话变更监听，可根据会话变更监听更新 UI。

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

await JuggleIM.setDraft({
  conversationType: 2,
  conversationId: 'groupid1',
  draft: 'draft'
});
```

</TabItem>
</Tabs>