---
title: 消息订阅
hide_title: true
sidebar_position: 6
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

> 敬请期待

</TabItem>
<TabItem value="ios">

> 敬请期待

</TabItem>
<TabItem value="js">

> 适用场景: 用户不在群组中可查看群内的实时消息，订阅成功后指定会话有新消息会通过消息监听返回

> _使用此功能需提前在自己的打开配置私有 `IM 后台` -> `功能配置` -> `不进群获取历史消息`_

<br/>

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| conversation                   | Object  | 是     |        | 会话对象                                                      | 1.7.18    |
| conversation.conversationType  | Number  | 是     |        | [会话类型](../../enum/web#conversation)                            | 1.7.18    |
| conversation.conversationId    | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.7.18    |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../status_code/web) | 1.7.18  |

**示例代码**
```js
let { ConversationType } = JIM;

let convesation = {
  conversationType: ConversationType.GROUP,
  conversationId: 'group02',
};
// 订阅消息，若连接断开请主动调用 unsubscribeMessage 取消订阅
jim.subscribeMessage(convesation).then(() => {
  console.log('subscribeMsg successfully.')
}, (error) => {
  console.log(error)
});


// 取消订阅
jim.unsubscribeMessage(convesation).then(() => {
  console.log('unsubscribeMsg successfully.')
}, (error) => {
  console.log(error)
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

> 敬请期待

</TabItem>
</Tabs>