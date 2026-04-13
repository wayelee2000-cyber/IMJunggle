---
title: automatic destruction
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

When sending a message, you can set its life cycle. Once the message expires, it will be automatically destroyed by IM.

**Sample Code**

```java
MessageOptions o = new MessageOptions();
// The unit is milliseconds. The message will be automatically deleted after 1 day. The default is 0, which means no automatic destruction.
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

After the message is sent successfully, the `getDestroyTime()` of the `Message` object will be automatically set to the message's sending time plus its lifetime. Developers can use this time to update the interface accordingly.

</TabItem>
<TabItem value="ios">

When sending a message, you can set its life cycle. Once the message expires, it will be automatically destroyed by IM.

**Sample Code**

```objectivec
JMessageOptions *o = [[JMessageOptions alloc] init];
// The unit is milliseconds. The message will be automatically deleted after 1 day. The default is 0, which means no automatic destruction.
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

After the message is sent successfully, the `destroyTime` of the `JMessage` object will be automatically set to the message's sending time plus its lifetime. Developers can use this time to update the interface accordingly.

</TabItem>
<TabItem value="js">

> Not yet provided

</TabItem>
<TabItem value="flutter" label="Flutter">

When sending a message, you can set its life cycle. Once the message expires, it will be automatically destroyed by IM.

**Sample Code**

```dart
SendMessageOption option = SendMessageOption();
option.lifeTime = 24 * 60 * 60 * 1000; // Unit: milliseconds

Message message = JuggleIm.instance.sendMessage(content, conversation, callback, option);
```

After the message is sent successfully, the `destroyTime` of the `Message` object will be automatically set to the message's sending time plus its lifetime. Developers can use this time to update the interface accordingly.

</TabItem>
</Tabs>