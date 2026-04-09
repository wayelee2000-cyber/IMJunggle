---
title: 置顶监听
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

消息置顶的回调合并在[消息监听](../../../watcher/message)。

```java
JIM.getInstance().getMessageManager().addListener("main", new IMessageManager.IMessageListener() {
    /// 消息置顶的回调
    /// message: 对应的消息
    /// operator: 操作置顶的用户
    /// isTop: true false 表示取消置顶
    void onMessageSetTop(Message message, UserInfo operator, boolean isTop) {

    }
});
```

</TabItem>
<TabItem value="ios">

消息置顶的回调合并在[消息监听](../../../watcher/message)。

```objectivec
[JIM.shared.messageManager addDelegate:self];

/// 消息置顶的回调
/// - Parameters:
///   - isTop: YES 表示置顶，NO 表示取消置顶
///   - message: 对应的消息
///   - userInfo: 操作置顶的用户
- (void)messageDidSetTop:(BOOL)isTop
                 message:(JMessage *)message
                    user:(JUserInfo *)userInfo {
  
}
```

</TabItem>
<TabItem value="js">

置顶消息回调，会话内消息被置顶后触发，会话中自己和会话内其他人置顶消息都会触发置顶监听，在监听中可处理 UI 置顶逻辑。

![](./top.png)

```js
let { Event } = JIM;

jim.on(Event.MESSAGE_SET_TOP, ({ message, isTop, operator, createdTime }) => {
  
  // message => 被置顶或取消置顶的原始消息，想系可查看 Message 对象
  
  // isTop => 是否置顶
  
  // operator => 操作人 { id: '', name: '', portrait: '' }
  
  // createdTime => 操作时间

});
```

</TabItem>
<TabItem value="flutter">

消息置顶的回调合并在[消息监听](../../../watcher/message)。

```dart
/// 消息置顶的回调
/// message: 对应的消息
/// operator: 操作置顶的用户
/// isTop: true false 表示取消置顶
JuggleIm.instance.onMessageSetTop = (message, operator, isTop) {

};
```

</TabItem>
</Tabs>