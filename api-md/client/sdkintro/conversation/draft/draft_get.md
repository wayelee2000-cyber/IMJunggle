---
title: 获取会话草稿
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
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', },
]
}>
<TabItem value="android">

每个会话包含 `draft` 属性，获取会话列表时会一起返回，详细请参看 [会话对象](../../../conversation)
</TabItem>
<TabItem value="ios">

每个会话包含 `draft` 属性，获取会话列表时会一起返回，详细请参看 [会话对象](../../../conversation)

</TabItem>
<TabItem value="js">

会话列表展示草稿状态，无需调用此方法，每个会话包含 `draft` 属性，获取会话列表时会一起返回，详细请参看 [会话对象](../../../conversation)

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

jim.getDraft(conversation).then((draft) => {
  console.log('get conversation draft successfully', draft);
});
```
</TabItem>
<TabItem value="harmony">

每个会话包含 `draft` 属性，获取会话列表时会一起返回，详细请参看 [会话对象](../../../conversation)
</TabItem>
<TabItem value="flutter">

每个会话包含 `draft` 属性，获取会话列表时会一起返回，详细请参看 [会话对象](../../../conversation)

</TabItem>
<TabItem value="reactnative">

每个会话包含 `draft` 属性，获取会话列表时会一起返回，详细请参看 [会话对象](../../../conversation)

</TabItem>
</Tabs>