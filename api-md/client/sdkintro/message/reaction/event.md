---
title: 回应事件监听
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
]
}>
<TabItem value="android">

消息回应是指针对消息通过表情或特殊符号进行回复，例如 `点赞`、`苦笑` 等。

消息回应的回调合并在[消息监听](../../../watcher/message)。

```java
JIM.getInstance().getMessageManager().addListener("main", new IMessageManager.IMessageListener() {
    /// 新增消息回应的回调
    /// conversation: 所属会话
    /// reaction: 新增的消息回应
    @Override
    public void onMessageReactionAdd(Conversation conversation, MessageReaction reaction) {

    }

    /// 删除消息回应的回调
    /// conversation: 所属会话
    /// reaction: 删除的消息回应
    void onMessageReactionRemove(Conversation conversation, MessageReaction reaction) {

    }
});

```


</TabItem>
<TabItem value="ios">

消息回应是指针对消息通过表情或特殊符号进行回复，例如 `点赞`、`苦笑` 等。

消息回应的回调合并在[消息监听](../../../watcher/message)。

```objectivec
[JIM.shared.messageManager addDelegate:self];

/// 新增消息回应的回调
/// - Parameter reaction: 新增的消息回应
/// - Parameter conversation: 所属会话
- (void)messageReactionDidAdd:(JMessageReaction *)reaction
               inConversation:(JConversation *)conversation {

}

/// 删除消息回应的回调
/// - Parameter reaction: 删除的消息回应
/// - Parameter conversation: 所属会话
- (void)messageReactionDidRemove:(JMessageReaction *)reaction
                  inConversation:(JConversation *)conversation {
  
}
```


</TabItem>
<TabItem value="js">

消息回应是指针对消息通过表情或特殊符号进行回复，例如 `点赞`、`苦笑` 等，设置消息回应后，消息中会自动携带 `reactions` 属性，所有人针对当前消息的回应都在数组中体现，
开发者通过 `reactions` 属性展示 UI 即可，如下图所示

![](./reaction_web.png)

消息回应有两处可获取：`历史消息` 和 `消息回应事件`，区别如下：

> **历史消息**: 获取是全量的消息回应最新列表，用户不在线时云端会自动更新维护

> **回应事件**: 用户在线时增量同步变更，有用户增加或移除回应会触发，_自己增加或删除回应 `不触发` 回应事件_

**示例代码**

```js
let { Event } = JIM;

// 全局只需注册一次，与消息监听位置一致即可，放到此处方便阅读

jim.on(Event.MESSAGE_REACTION_CHANGED, (notify) => {
  /* 
    处理逻辑：开发者只需更新内存中的消息回应，云端和本地 SDK 会自动更新，再次获取历史消息会返回最新的回应数据
    notify 示例:
      {
        conversationId: "qEqA0i9C2pg"
        conversationType: 2
        messageId: "nxe3swhgabukvd8k",
        reactions: [
          {
            isRemove: false,
            //新增或删除时的 Key
            key: ':simle',
            value: '用户 Id',
            timestamp: 1740177311973
            user: {
              id: '用户 Id',
              name: '昵称',
              portrait: '头像'
            }
          }
        ]
      }
    */
  console.log(notify);
});

```
</TabItem>

<TabItem value="flutter">

消息回应是指针对消息通过表情或特殊符号进行回复，例如 `点赞`、`苦笑` 等。

消息回应的回调合并在[消息监听](../../../watcher/message)。

```java
/// 新增消息回应的回调
/// conversation: 所属会话
/// reaction: 新增的消息回应
JuggleIm.instance.onMessageReactionAdd = (conversation, reaction) {

};
/// 删除消息回应的回调
/// conversation: 所属会话
/// reaction: 删除的消息回应
JuggleIm.instance.onMessageReactionRemove = (conversation, reaction) {

};

```


</TabItem>
</Tabs>