---
title: 标签事件监听
hide_title: true
sidebar_position: 1
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

可以设置多个监听。

```java
JIM.getInstance().getConversationManager().addTagListener("main", new IConversationManager.IConversationTagListener() {
  /// 标签中新增会话
  @Override
  public void onConversationsAddToTag(String tagId, List<Conversation> conversations) {
  }

  /// 标签中删除会话
  @Override
  public void onConversationsRemoveFromTag(String tagId, List<Conversation> conversations) {
  }
});

```


</TabItem>
<TabItem value="ios">

可以设置多个代理。

```objectivec
[JIM.shared.conversationManager addTagDelegate:self];

/// 标签中新增会话
- (void)conversationsDidAddToTag:(NSString *)tagId
                   conversations:(NSArray <JConversation *> *)conversationList {
}

/// 标签中删除会话
- (void)conversationsDidRemoveFromTag:(NSString *)tagId
                        conversations:(NSArray <JConversation *> *)conversationList {
}
```


</TabItem>
<TabItem value="js">

```js
let { Event } = JIM;

### 新增标签
jim.on(Event.TAG_ADDED, ({ tags }) => {
  /* tags =>  [{ id: 'tag_01', name: '我的关注' }, ... ] */
});

### 销毁标签
jim.on(Event.TAG_REMOVED, (notify) => {
  /* tags =>  [{ id: 'tag_01' }, ... ] */
});

### 标签变更
jim.on(Event.TAG_CHANGED, (notify) => {
  /* tags =>  [{ id: 'tag_01', name: '我的关注' }, ... ] */
});

### 标签新增会话
jim.on(Event.TAG_CONVERSATION_ADDED, (notify) => {
  /* tags =>  [{ id: 'tag_01', conversations: [ Conversation, ...] }, ... ] */
});

### 标签删除会话
jim.on(Event.TAG_CONVERSATION_REMOVED, (notify) => {
  /* tags =>  [{ id: 'tag_01', conversations: [ Conversation, ...] }, ... ] */
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">


> 暂未提供

</TabItem>
<TabItem value="reactnative">

可以设置多个监听。

```javascript
import JuggleIM from 'juggleim-rnsdk';

// 标签中新增��话
const removeAddToTagListener = JuggleIM.addConversationsAddToTagListener((data) => {
  console.log('conversations added to tag:', data);
});

// 标签中删除会话
const removeRemoveFromTagListener = JuggleIM.addConversationsRemoveFromTagListener((data) => {
  console.log('conversations removed from tag:', data);
});

// 取消监听
removeAddToTagListener();
removeRemoveFromTagListener();
```

</TabItem>
</Tabs>