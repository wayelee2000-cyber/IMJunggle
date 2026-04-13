---
title: Burn after reading
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

When sending a message, you can set the message's burn-after-read duration using `lifeTimeAfterRead`. Once `lifeTimeAfterRead` milliseconds have passed after the message is read, the message will be destroyed.

**Sample Code**

```java
MessageOptions o = new MessageOptions();
// The unit is milliseconds. The message will be automatically deleted 5 minutes after it is read. The default is 0, which means the message will not be automatically deleted after being read.
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

After the message is sent successfully, the receiver calls the `sendReadReceipt()` method to indicate that the message has been read.

For a single chat message, the countdown starts for both the sender and the receiver once the receiver has read it.

For a group chat message, the countdown starts for the receiver after they have read it, and for the sender after all other group members have read it.

When the countdown begins, the SDK will invoke the `onMessageDestroyTimeUpdate()` callback and automatically set the `getDestroyTime()` of the Message object to the read time plus `lifeTimeAfterRead`. Developers can use this time to implement a countdown in the user interface.

**Sample Code**

```java
JIM.getInstance().getMessageManager().addDestroyListener("main", new IMessageManager.IMessageDestroyListener() {
    @Override
    public void onMessageDestroyTimeUpdate(String messageId, Conversation conversation, long destroyTime) {
        
    }
});
```



</TabItem>
<TabItem value="ios">

When sending a message, you can set the message's burn-after-read duration using `lifeTimeAfterRead`. Once `lifeTimeAfterRead` milliseconds have passed after the message is read, the message will be destroyed.

**Sample Code**

```objectivec
JMessageOptions *o = [[JMessageOptions alloc] init];
// The unit is milliseconds. The message will be automatically deleted 5 minutes after it is read. The default is 0, which means the message will not be automatically deleted after being read.
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

After the message is sent successfully, the receiver calls the `sendReadReceipt:inConversation:success:error:` method to indicate that the message has been read.

For a single chat message, the countdown starts for both the sender and the receiver once the receiver has read it.

For a group chat message, the countdown starts for the receiver after they have read it, and for the sender after all other group members have read it.

When the countdown begins, the SDK will invoke the `messageDestroyTimeDidUpdate:inConversation:destroyTime:` callback and automatically set the `destroyTime` of the Message object to the read time plus `lifeTimeAfterRead`. Developers can use this time to implement a countdown in the user interface.

**Sample Code**

```objective
[JIM.shared.messageManager addDestroyDelegate:self];

- (void)messageDestroyTimeDidUpdate:(NSString *)messageId inConversation:(JConversation *)conversation destroyTime:(long long)destroyTime { 

}
```


</TabItem>
<TabItem value="js">

> Not yet provided

</TabItem>
<TabItem value="flutter" label="Flutter">

When sending a message, you can set the message's burn-after-read duration using `lifeTimeAfterRead`. Once `lifeTimeAfterRead` milliseconds have passed after the message is read, the message will be destroyed.

**Sample Code**

```dart
SendMessageOption option = SendMessageOption();
option.lifeTimeAfterRead = 5 * 60 * 1000; // Unit: milliseconds

Message message = JuggleIm.instance.sendMessage(content, conversation, callback, option);
```

After the message is sent successfully, the receiver calls the `sendReadReceipt` method to indicate that the message has been read.

For a single chat message, the countdown starts for both the sender and the receiver once the receiver has read it.

For a group chat message, the countdown starts for the receiver after they have read it, and for the sender after all other group members have read it.

When the countdown begins, the SDK will invoke the `onMessageDestroyTimeUpdate` callback and automatically set the `destroyTime` of the Message object to the read time plus `lifeTimeAfterRead`. Developers can use this time to implement a countdown in the user interface.

**Sample Code**

```dart
JuggleIm.instance.onMessageDestroyTimeUpdate = (messageId, conversation, destroyTime) {

}
```

</TabItem>
</Tabs>