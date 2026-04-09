---
title: 阅后即焚
hide_title: true
sidebar_position: 9
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

发送消息时可以设置消息的阅后即焚时间 `lifeTimeAfterRead`，当消息被读后再经过 `lifeTimeAfterRead` 毫秒，消息会被销毁。

**示例代码**

```java
MessageOptions o = new MessageOptions();
// 单位毫秒，该消息被读 5 分钟后会被自动删除。默认为 0，表示消息被读后也不自动删除。
o.setLifeTimeAfterRead(5 * 60 * 1000);
TextMessage textMessage = new TextMessage("Text");
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "111");
JIM.getInstance().getMessageManager().sendMessage(textMessage, conversation, o, new IMessageManager.ISendMessageCallback() {
    @Override
    public void onSuccess(Message message) {

    }

    @Override
    public void onError(Message message, int errorCode) {

    }
});
```

消息发送成功后，接收方通过 sendReadReceipt() 方法来标识消息已读。

单聊消息从接收方已读后开始对发送和接收双方同时进行倒计时。

群聊消息的接收方从自己已读后开始倒计时，发送方从所有其他群成员已读后开始倒计时。

倒计时开始时，SDK 会回调 onMessageDestroyTimeUpdate(), 并把 Message 对象的 getDestroyTime() 自动设置成消息的已读时间加上 `lifeTimeAfterRead`，开发者可以依据这个时间来做界面倒计时。

**示例代码**

```java
JIM.getInstance().getMessageManager().addDestroyListener("main", new IMessageManager.IMessageDestroyListener() {
    @Override
    public void onMessageDestroyTimeUpdate(String messageId, Conversation conversation, long destroyTime) {
        
    }
});
```



</TabItem>
<TabItem value="ios">

发送消息时可以设置消息的阅后即焚时间 `lifeTimeAfterRead`，当消息被读后再经过 `lifeTimeAfterRead` 毫秒，消息会被销毁。

**示例代码**

```objectivec
JMessageOptions *o = [[JMessageOptions alloc] init];
// 单位毫秒，该消息被读 5 分钟后会被自动删除。默认为 0，表示消息被读后也不自动删除。
o.lifeTimeAfterRead = 5 * 60 * 1000;
JTextMessage *textMessage = [[JTextMessage alloc] initWithContent:@"Text"];
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate
                                                                conversationId:@"111"];
[JIM.shared.messageManager sendMessage:textMessage
                         messageOption:o
                        inConversation:conversation
                               success:^(JMessage *message) {
    
} error:^(JErrorCode errorCode, JMessage *message) {
    
}];
```

消息发送成功后，接收方通过 `sendReadReceipt:inConversation:success:error:` 方法来标识消息已读。

单聊消息从接收方已读后开始对发送和接收双方同时进行倒计时。

群聊消息的接收方从自己已读后开始倒计时，发送方从所有其他群成员已读后开始倒计时。

倒计时开始时，SDK 会回调 `messageDestroyTimeDidUpdate:inconversation:destroyTime:`，并把 Message 对象的 `destroyTime` 自动设置成消息的已读时间加上 `lifeTimeAfterRead`，开发者可以依据这个时间来做界面倒计时。

**示例代码**

```objective
[JIM.shared.messageManager addDestroyDelegate:self];

- (void)messageDestroyTimeDidUpdate:(NSString *)messageId inConversation:(JConversation *)conversation destroyTime:(long long)destroyTime { 

}
```


</TabItem>
<TabItem value="js">

> 暂未提供

</TabItem>
<TabItem value="flutter" label="Flutter">

发送消息时可以设置消息的阅后即焚时间 `lifeTimeAfterRead`，当消息被读后再经过 `lifeTimeAfterRead` 毫秒，消息会被销毁。

**示例代码**

```dart
SendMessageOption option = SendMessageOption();
option.lifeTimeAfterRead = 5 * 60 * 1000; //单位毫秒

Message message = JuggleIm.instance.sendMessage(content, conversation, callback, option);
```

消息发送成功后，接收方通过 `sendReadReceipt` 方法来标识消息已读。

单聊消息从接收方已读后开始对发送和接收双方同时进行倒计时。

群聊消息的接收方从自己已读后开始倒计时，发送方从所有其他群成员已读后开始倒计时。

倒计时开始时，SDK 会回调 `onMessageDestroyTimeUpdate`, 并把 Message 对象的 `destroyTime` 自动设置成消息的已读时间加上 `lifeTimeAfterRead`，开发者可以依据这个时间来做界面倒计时。

**示例代码**

```dart
JuggleIm.instance.onMessageDestroyTimeUpdate = (messageId, conversation, destroyTime) {

}
```

</TabItem>
</Tabs>