---
title: 获取置顶会话
hide_title: true
sidebar_position: 4
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
|---------------------------------|---------|----------|----------|
| count | int | 拉取数量 | 1.0.0    |
| timestamp     | long | 时间戳，以毫秒为单位，0 表示当前时间 | 1.0.0    |
| direction | JIMConst.PullDirection | 拉取方向 | 1.0.0    |

**示例代码**

```java
List<ConversationInfo> list = JIM.getInstance().getConversationManager().getTopConversationInfoList(100, 0, JIMConst.PullDirection.OLDER);
```

</TabItem>
<TabItem value="ios">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| count | int | 拉取数量 | 1.0.0    |
| timestamp     | long long | 时间戳，以毫秒为单位，0 表示当前时间 | 1.0.0    |
| direction | JPullDirection | 拉取方向 | 1.0.0    |

**示例代码**

```objectivec
NSArray <JConversationInfo *> *conversationList = [JIM.shared.conversationManager getTopConversationInfoListByCount:100 timestamp:0 direction:JPullDirectionOlder];
```

</TabItem>
<TabItem value="js">

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.0.0    |
| result.conversations | Array | 会话数组，单个会话对象结构请查看 [Conversation](../../conversation.mdx) | 1.0.0    |
| result.isFinished | Boolean | 标志会话是否获取完成 | 1.0.0    |

**示例代码**
```js
jim.getTopConversations().then((result) => {
  let { conversations, isFinished } = result;
  console.log(isFinished, conversations);
})
```
</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| sortType | TopConverSortType | 枚举值。ByTopTime:按置顶时间排序；BySortTime:按会话时间排序|1.0.0|
| start | number |起始时间戳，以毫秒为单位，0 表示当前时间 | 1.0.0    |
| isPositive | boolean | 是否正向拉取 | 1.0.0    |

**示例代码**

```java 
JuggleIm.instance.getConversationManager().getTopConversations(TopConverSortType.ByTopTime,0,true,(convers)=>{

})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
<TabItem value="reactnative">

获取置顶会话列表。

**参数说明**

| 名称          | 类型    | 必填     | 默认值       | 描述                                           | 版本     |
|--------------|---------|----------|------------|------------------------------------------------|----------|
| count  | Number     | 否       | 100         | 拉取数量 | 0.6.3    |
| timestamp  | Number  | 否       | 0       | 时间戳，以毫秒为单位，0 表示当前时间 | 0.6.3    |
| direction  | Number  | 否       | 1      | 拉取方向，0: 拉取 timestamp 之后的会话，1: 拉取 timestamp 之前的会话 | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversations = await JuggleIM.getTopConversationInfoList({
  count: 100,
  timestamp: 0,
  direction: 1
});
```

</TabItem>
</Tabs>