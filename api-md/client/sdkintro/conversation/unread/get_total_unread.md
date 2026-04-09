---
title: 获取会话未读总数
hide_title: true
sidebar_position: 7
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

**示例代码**
```java
int count = JIM.getInstance().getConversationManager().getTotalUnreadCount();
```
</TabItem>
<TabItem value="ios">

**示例代码**
```objectivec
int count = [JIM.shared.conversationManager getTotalUnreadCount];
```

</TabItem>
<TabItem value="js">

获取当前用户全部会话的未读总数，同时支持按条件过滤 `conversationTypes` 和 `ignoreConversations` 是 _**并且**_ 的关系。

**参数说明**

| 名称                             | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------------------------|---------|-------|--------|----------|----------|
| params                    | Object | 否     | 无 | 查询条件 | 1.0.0    |
| params.conversationTypes     | Array | 否     | 无 | 指定会话类型 | 1.0.0    |
| params.ignoreConversations   | Array | 否     | 无 | 忽略指定会话 | 1.0.0    |

**示例代码**
```js
// 获取方式一：获取全部会话未读总数
jim.getTotalUnreadcount().then(({ count }) => {
  console.log('当前用户未读总数:', count);
})

/**
  获取方式二：按条件过滤后获取未读总数
  条件解释说明：获取除 userid2 外的全部单聊未读总数
*/ 
let params = {
  conversationTypes: [ConversationType.PRIVATE],
  ignoreConversations: [
    {
      conversationType: ConversationType.PRIVATE,
      conversationId: 'userid2'
    }
  ]
};
jim.getTotalUnreadcount(params).then(({ count }) => {
  console.log('当前用户未读总数:', count);
})
```
</TabItem>
<TabItem value="flutter">

获取当前用户全部会话的未读总数，同时支持按条件过滤 `ConversationType` 过滤。

**示例代码**

```dart
// 获取全部会话的未读总数
int count = await JuggleIm.instance.getTotalUnreadCount();

// 获取全部【单聊】会话的未读总数
int count = await JuggleIm.instance.getTotalUnreadCount([ConversationType.private]);

// 获取全部【群组】会话的未读总数
int count = await JuggleIm.instance.getTotalUnreadCount([ConversationType.group]);

// 获取全部【单聊+群组】会话的未读总数
int count = await JuggleIm.instance.getTotalUnreadCount([ConversationType.private, ConversationType.group]);

```
</TabItem>
<TabItem value="reactnative">

获取当前用户全部会话的��读总数，同时支持按条件过滤。

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

// 获取全部会话的未读总数
const count = await JuggleIM.getTotalUnreadCount();

// 获取全部【单聊】会话的未读总数
const count = await JuggleIM.getTotalUnreadCount([1]);

// 获取全部【群组】会话的未读总数
const count = await JuggleIM.getTotalUnreadCount([2]);

// 获取全部【单聊+群组】会话的未读总数
const count = await JuggleIM.getTotalUnreadCount([1, 2]);

```

</TabItem>
<TabItem value="harmony">

**示例代码**
```java
JuggleIm.instance.getConversationManager().getTotalUnreadCount((code,count)=>{
})
```
</TabItem>
</Tabs>