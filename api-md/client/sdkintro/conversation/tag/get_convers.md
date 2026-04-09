---
title: 获取标签会话列表
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
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

获取标签下的会话列表，支持分页获取。

**示例代码**

```java
GetConversationOptions o = new GetConversationOptions();
o.setCount(20);
o.setTimestamp(0);
o.setPullDirection(JIMConst.PullDirection.OLDER);
o.setTagId("Tag111");
List<ConversationInfo> infoList = JIM.getInstance().getConversationManager().getConversationInfoList(o);
```


</TabItem>
<TabItem value="ios">

获取标签下的会话列表，支持分页获取。

**示例代码**


```objectivec
JGetConversationOptions *o = [[JGetConversationOptions alloc] init];
o.tagId = @"Tag111";
o.count = 20;
o.timestamp = 0;
o.direction = JPullDirectionOlder;
NSArray *arr = [JIM.shared.conversationManager getConversationInfoListWith:o];
```

</TabItem>
<TabItem value="js">

获取标签下的会话列表，支持分页获取。

![](./list.png)

**参数说明**

| 名称          | 类型    | 必填     | 默认值                               | 描述                                           | 版本     |
|--------------|---------|----------|--------------------------------------|------------------------------------------------|----------|
| option        | Object  | 是       |                                    |  | 1.7.5    |
| option.tag    | String  | 是       |                                    |  | 1.7.5    |
| option.count  | Number  | 否       | 50                                   | 获取指定数量的会话列表，单次最多获取 100 个会话 | 1.0.0    |
| option.order  | Number  | 否       | [FORWARD](../../../enum/web#conversation) | 获取方向，支持获取更早的会话或者更（四声）新的会话，配合 `time` 属性一起使用 | 1.0.0    |
| option.time   | Number  | 否       | 0                                    | 从指定时间点开始获取会话，可以配合 `order` 获取新老会话 | 1.0.0    |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.0.0    |
| result.conversations | Array | 会话数组，单个会话对象结构请查看 [Conversation](../../conversation.mdx) | 1.0.0    |
| result.isFinished | Boolean | 标志会话是否获取完成 | 1.0.0    |

**示例代码**
```js
/* 
  假设当前用户有 199 个会话，每页获取 50 条，会话列表按时间倒序排列，实现会话列表分页逻辑如下：
  1、加载第 1 页获取参数： { count: 50, time: 0 }
  2、加载第 2 页获取参数： { count: 50, time: '获取第 1 页会话数组中最小的 sortTime（数组下标最大的会话）' }
  3、加载第 3 页获取参数： { count: 50, time: '获取第 2 页会话数组中最小的 sortTime（数组下标最大的会话）' }
  4、加载第 4 页获取参数： { count: 50, time: '获取第 3 页会话数组中最小的 sortTime（数组下标最大的会话）' }
  5、结束：isFinished 返回 true，停止加载
*/

let option = {
  tag: 'tag_01'
}
jim.getConversations(option).then((result) => {
  let { conversations, isFinished } = result;
  console.log(isFinished, conversations);
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
<TabItem value="reactnative">

获取标签下的会话列表，支持分页获取。

**参数说明**

| 名称          | 类型    | 必填     | 默认值       | 描述                                           | 版本     |
|--------------|---------|----------|------------|------------------------------------------------|----------|
| tag  | String     | 是       | 无         | 标签ID | 0.6.3    |
| count  | Number  | 否       | 50       | 获取指定数量的会话列表，单次最多获取 100 个会话 | 0.6.3    |
| timestamp  | Number  | 否       | 0       | 从指定时间点开始获取会话 | 0.6.3    |
| direction  | Number  | 否       | 1      | 获取方向，0: 拉取 timestamp 之后的会话，1: 拉取 timestamp 之前的会话 | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversations = await JuggleIM.getConversationInfoList({
  tag: 'tag_01',
  count: 50,
  timestamp: 0,
  direction: 1
});
```

</TabItem>
</Tabs>