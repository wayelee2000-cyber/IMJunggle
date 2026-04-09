---
title: 获取消息上下文
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
]
}>
<TabItem value="android">

> 暂未提供

</TabItem>
<TabItem value="ios">

> 暂未提供

</TabItem>
<TabItem value="js">

获取消息上下文: 指获取指定时间前后的消息列表，便于业务层展示上下文的消息，此接口适用于首次进入会话时使用，`向下` 或者 `向上` 获取更多的历史消息时，请使用 [获取历史消息](../get_all) 接口获取

:::simple 使用场景

> 进入会话定位到第一条未读消息，并显示未读消息前后的消息内容

> 消息搜索后，点击搜索命中的消息定位到指定会话，展示当前消息的上下文

:::


**参数说明**

| 名称                | 类型    | 必填  | 默认值           | 描述                                                                      | 版本   |
|---------------------|---------|------|------------------|---------------------------------------------------------------------------|--------|
| params              | Object  | 是   |                | 历史消息获取参数                                                           | 1.8.3  |
| params.conversationType | Number  | 是   |                | [会话类型](../../../enum/web#conversation)                                       | 1.8.3  |
| params.conversationId   | String  | 是   |                | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是对方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.8.3  |
| params.time         | Number  | 否   | `第一条未读消息的时间`   | 获取上下文消息的起始时间           | 1.8.3  |
| params.count        | Object  | 否   | 10               | 获取历史上下文消息的条数，会从指定 `time` 时间的前后各取 `count` 条消息，在 `frontMessages` 和 `backMessages` 返回, 范围 1 - 10   | 1.8.3  |

**成功回调**

| 名称                   | 类型    | 描述                                    | 版本   |
|------------------------|---------|-----------------------------------------|--------|
| result                 | Object  |                                         | 1.8.3  |
| result.frontMessages    | Object  | 消息数组，每条消息的属性，请查看 [Message](../../../msg/message) 结构 | 1.8.3  |
| result.isFrontFinished  | Object  | `向前` 是否还有更多的历史消息没有获取 结构 | 1.8.3  |
| result.backMessages     | Object  | 消息数组，每条消息的属性，请查看 [Message](../../../msg/message) 结构 | 1.8.3  |
| result.isBackFinished   | Object  | `向后` 是否还有更多的历史消息没有获取 | 1.8.3  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../status_code/web) | 1.8.3  |

**示例代码**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2',
  count: 10
};

jim.getContextMessages(params).then((result) => {
  let { frontMessages, isFrontFinished, backMessages, isBackFinished } = result;
  console.log(result);
}, (error) => {
  console.log(error);
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
</Tabs>