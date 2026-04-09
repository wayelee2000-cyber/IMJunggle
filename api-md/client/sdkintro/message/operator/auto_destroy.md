---
title: 自动销毁
hide_title: true
sidebar_position: 8
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{
  label: 'JavaScript', value: 'js', 
},
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

发送消息时可以设置消息的生存周期，当消息到期后，会被 IM 自动销毁。

**示例代码**

```java
MessageOptions o = new MessageOptions();
// 单位毫秒，该消息1天后会被自动删除。默认为 0，表示不自动销毁。
o.setLifeTime(24 * 60 * 60 * 1000);
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

消息发送成功后，Message 对象的 getDestroyTime() 会自动设置成消息的发送时间加上生存周期，开发者可以依据这个时间来做界面渲染。



</TabItem>
<TabItem value="ios">

发送消息时可以设置消息的生存周期，当消息到期后，会被 IM 自动销毁。

**示例代码**

```objectivec
JMessageOptions *o = [[JMessageOptions alloc] init];
// 单位毫秒，该消息1天后会被自动删除。默认为 0，表示不自动销毁。
o.lifeTime = 24 * 60 * 60 * 1000;
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

消息发送成功后，JMessage 对象的 destroyTime 会自动设置成消息的发送时间加上生存周期，开发者可以依据这个时间来做界面渲染。

</TabItem>
<TabItem value="js">

> 暂未提供

</TabItem>
<TabItem value="flutter" label="Flutter">

发送消息时可以设置消息的生存周期，当消息到期后，会被 IM 自动销毁。

**示例代码**

```dart
SendMessageOption option = SendMessageOption();
option.lifeTime = 24 * 60 * 60 * 1000; //单位毫秒

Message message = JuggleIm.instance.sendMessage(content, conversation, callback, option);
```

消息发送成功后，Message 对象的 destroyTime 会自动设置成消息的发送时间加上生存周期，开发者可以依据这个时间来做界面渲染。

</TabItem>
</Tabs>