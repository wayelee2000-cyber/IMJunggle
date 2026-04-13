---
title: 消息监听
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
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

**消息相关监听**

可以设置多个监听。

```java
JIM.getInstance().getMessageManager().addListener("main", new IMessageManager.IMessageListener() {
    /// 接收消息的回调
    @Override
    public void onMessageReceive(Message message) {
        Log.d("TAG", "onMessageReceive, conversationType is " + message.getConversation().getConversationType() + ", conversationId is " + message.getConversation().getConversationId());
        MessageContent content = message.getContent();
        if (content instanceof TextMessage) {
            Log.d("TAG", "text message received, content is " + ((TextMessage) content).getContent());
        } else if (content instanceof ImageMessage) {
            Log.d("TAG", "image message received, url is " + ((ImageMessage) content).getUrl());
        } else if (content instanceof FileMessage) {
            Log.d("TAG", "file message received, name is " + ((FileMessage) content).getName());
        } else if (content instanceof VoiceMessage) {
            Log.d("TAG", "voice message received");
        }
    }

    /// 消息撤回回调
    @Override
    public void onMessageRecall(Message message) {
        Log.d("TAG", "onMessageRecall, messageId is " + message.getMessageId());
    }

    /// 消息修改回调
    @Override
    public void onMessageUpdate(Message message) {
        Log.d("TAG", "onMessageUpdate, messageId is " + message.getMessageId());
    }

    /// 消息删除回调
    /// conversation: 会话标识
    /// clientMsgNos: 列表（本端消息唯一编号）
    @Override
    public void onMessageDelete(Conversation conversation, List<Long> clientMsgNos) {
        Log.d("TAG", "onMessageDelete, conversation is " + conversation.getConversationId() + ", clientMsgNos are " + clientMsgNos);
    }

    /// 消息清除回调，表示清除特定会话中某个时间点之前的所有消息
    /// conversation: 会话标识
    /// timestamp: 时间戳（毫秒），timestamp 之前的消息被清除
    /// senderId: 若不为空，表示只清除发送者 id 为 senderId 的消息
    @Override
    public void onMessageClear(Conversation conversation, long timestamp, String senderId) {
        Log.d("TAG", "onMessageClear, conversation is " + conversation.getConversationId() + ", timestamp is " + timestamp + ", senderId is " + senderId);
    }

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

    /// 消息置顶的回调
    /// message: 对应的消息
    /// operator: 操作置顶的用户
    /// isTop: true 表示置顶，false 表示取消置顶
    void onMessageSetTop(Message message, UserInfo operator, boolean isTop) {

    }
});
```

**消息阅读状态相关监听**

可以设置多个监听。

```java
JIM.getInstance().getMessageManager().addReadReceiptListener("main", new IMessageManager.IMessageReadReceiptListener() {
  /// 单聊消息阅读回调
  /// conversation: 所在会话
  /// messageIds: 消息 id 列表
	@Override
	public void onMessagesRead(Conversation conversation, List<String> messageIds) {
		Log.d("TAG", "onMessagesRead, count is " + messageIds.size() + ", conversationType is " + conversation.getConversationType() + ", conversationId is " + conversation.getConversationId());
	}

  /// 群消息阅读回调
  /// conversation: 所在会话
  /// messages: key 为 messageId
	@Override
	public void onGroupMessagesRead(Conversation conversation, Map<String, GroupMessageReadInfo> messages) {
		Log.d("TAG", "onGroupMessagesRead, conversationType is " + conversation.getConversationType() + ", id is " + conversation.getConversationId() + ", count is " + messages.size());
	}
});
```

**消息销毁相关监听**

可以设置多个监听。

```java
JIM.getInstance().getMessageManager().addDestroyListener("main", new IMessageManager.IMessageDestroyListener() {
  /**
    * 消息销毁时间更新回调（通常用于阅后即焚场景）
    * @param messageId 消息 id
    * @param conversation 所在会话
    * @param destroyTime 更新后的销毁时间
    */
	@Override
	public void onMessageDestroyTimeUpdate(String messageId, Conversation conversation, long destroyTime) {

	}
});
```

**消息加解密相关回调**

消息加解密只能设置一个监听。

```java
JIM.getInstance().getMessageManager().setPreprocessor(new IMessageManager.IMessagePreprocessor() {
  /**
    * 消息加密回调
    * 触发时机：消息入库后，发送前
    * @param content 待发送的消息内容，已序列化为 byte[]
    * @param conversation 所在会话
    * @param contentType 消息类型
    * @return 处理后的消息内容
    */
	@Override
	public byte[] encryptMessageContent(byte[] content, Conversation conversation, String contentType) {

	}

  /**
    * 消息解密回调
    * 触发时机：接收到消息，入库前
    * @param content 接收到的消息内容，byte[] 类型，尚未反序列化
    * @param conversation 所在会话
    * @param contentType 消息类型
    * @return 处理后的消息内容
    */
	@Override
	public byte[] decryptMessageContent(byte[] content, Conversation conversation, String contentType) {

	}
});
```

</TabItem>
<TabItem value="ios">

**消息相关监听**

可以设置多个代理。

```objectivec
[JIM.shared.messageManager addDelegate:self];

/// 接收消息回调
- (void)messageDidReceive:(JMessage *)message {
    NSLog(@"messageDidReceive conversationType is %d, conversationId is %@", message.conversation.conversationType, message.conversation.conversationId);
    JMessageContent *content = message.content;
    if ([content isKindOfClass:[JTextMessage class]]) {
        NSLog(@"text message received, content is %@", ((JTextMessage *)content).content);
    } else if ([content isKindOfClass:[JImageMessage class]]) {
        NSLog(@"image message received, url is %@", ((JImageMessage *)content).url);
    } else if ([content isKindOfClass:[JFileMessage class]]) {
        NSLog(@"file message received");
    } else if ([content isKindOfClass:[JVoiceMessage class]]) {
        NSLog(@"voice message received");
    }
}

/// 消息撤回回调
- (void)messageDidRecall:(JMessage *)message {
    NSLog(@"messageDidRecall");
}

/// 消息修改回调
- (void)messageDidUpdate:(JMessage *)message {
    NSLog(@"messageDidUpdate");
}

/// 消息删除回调
- (void)messageDidDelete:(JConversation *)conversation
            clientMsgNos:(NSArray <NSNumber *> *)clientMsgNos {

}

/// 消息清除回调，表示清除特定会话中某个时间点之前的所有消息
/// - Parameters:
///   - conversation: 被清除消息所属的会话标识
///   - timestamp: 时间戳（毫秒），timestamp 之前的消息被清除
///   - senderId: 若不为空，表示只清除发送者 id 为 senderId 的消息
- (void)messageDidClear:(JConversation *)conversation
              timestamp:(long long)timestamp
               senderId:(NSString *)senderId {

}

/// 新增消息回应回调
/// - Parameter reaction: 新增的消息回应
/// - Parameter conversation: 所属会话
- (void)messageReactionDidAdd:(JMessageReaction *)reaction
               inConversation:(JConversation *)conversation {

}

/// 删除消息回应回调
/// - Parameter reaction: 删除的消息回应
/// - Parameter conversation: 所属会话
- (void)messageReactionDidRemove:(JMessageReaction *)reaction
                  inConversation:(JConversation *)conversation {
  
}

/// 消息置顶回调
/// - Parameters:
///   - isTop: YES 表示置顶，NO 表示取消置顶
///   - message: 对应的消息
///   - userInfo: 操作置顶的用户
- (void)messageDidSetTop:(BOOL)isTop
                 message:(JMessage *)message
                    user:(JUserInfo *)userInfo {
  
}
```

**消息阅读状态相关监听**

可以设置多个代理。

```objectivec
[JIM.shared.messageManager addReadReceiptDelegate:self];

/// 单聊消息阅读回调
/// - Parameters:
///   - messageIds: 消息 id 列表
///   - conversation: 所在会话
- (void)messagesDidRead:(NSArray<NSString *> *)messageIds inConversation:(JConversation *)conversation {
    NSLog(@"messagesDidRead");
}

/// 群消息阅读回调
/// - Parameters:
///   - msgs: key 为 messageId
///   - conversation: 所在会话
- (void)groupMessagesDidRead:(NSDictionary<NSString *,JGroupMessageReadInfo *> *)msgs inConversation:(JConversation *)conversation {
    NSLog(@"groupMessagesDidRead, groupId is %@", conversation.conversationId);
}
```

**消息销毁相关监听**

可以设置多个代理。

```objectivec
[JIM.shared.messageManager addDestroyDelegate:self];

/// 消息销毁时间更新回调（通常用于阅后即焚场景）
/// - Parameters:
///   - messageId: 消息 id
///   - conversation: 所在会话
///   - destroyTime: 更新后的销毁时间
- (void)messageDestroyTimeDidUpdate:(NSString *)messageId
                     inConversation:(JConversation *)conversation
                        destroyTime:(long long)destroyTime {
  
}
```

**消息加解密相关回调**

消息加解密只能设置一个代理。

```objectivec
[JIM.shared.messageManager setPreprocessor:self];

/// 消息加密回调
/// 触发时机：消息入库后，发送前
/// - Parameter content: 待发送的消息内容，已序列化为 NSData
/// - Parameter conversation: 所在会话
/// - Parameter contentType: 消息类型
/// - Returns: 处理后的消息内容
- (NSData *)encryptMessageContent:(NSData *)content
                   inConversation:(JConversation *)conversation
                      contentType:(NSString *)contentType {
  
}

/// 消息解密回调
/// 触发时机：接收到消息，入库前
/// - Parameter content: 接收到的消息内容，NSData 格式，尚未反序列化
/// - Parameter conversation: 所在会话
/// - Parameter contentType: 消息类型
/// - Returns: 处理后的消息内容
- (NSData *)decryptMessageContent:(NSData *)content
                   inConversation:(JConversation *)conversation
                      contentType:(NSString *)contentType {
  
}
```

</TabItem>
<TabItem value="js">

Global listeners only need to be set once; multiple settings will override previous ones. When others send messages to the current user, the message listener will be triggered. For message format, see [Message 结构](../../../msg/message). For event descriptions, see [监听枚举](../../../enum/web#listener).

```js
let { Event } = JIM;

### 消息接收监听

jim.on(Event.MESSAGE_RECEIVED, (message) => {
  console.log(message);
});


### 消息已读监听

jim.on(Event.MESSAGE_READ, (notify) => {
  /*
    Handling logic:
      1. Update the in-memory message's isRead status to true here.
      2. The SDK automatically handles message status in historical messages.
      3. Fetching historical messages returns the latest read status.
      
    Example notify:
      {
        conversationType: 1,
        conversationId: "dDshdk1d4",
        // List of message IDs that have been read by the other party; update message read status by messageId
        messages: [{ 
          messageId:"na4d4nfa2d6gnn28",
          
          // Only group conversations have readCount and unreadCount; their sum equals the total group members at message send time
          readCount: 1,
          unreadCount: 2
        }],
        // Whether the notification message was sent from another device of the current user
        isSender: false,
        // User ID of the sender of the notification message
        senderId: 'dadkdks',
        // Read time
        readTime: 1761912175539
      }
  */ 
 console.log(notify);
  /* 
    Notes on using read-after-view self-destruct feature:
    
    1. Prerequisites
      
      (1) Online received or historical message with message.lifeTimeAfterRead > 0 indicates a self-destruct message.

      (2) Destroy time calculation: notify.messages[0].readTime + message.lifeTimeAfterRead

    2. Messages displayed that include messageIds in notify.messages and have message.lifeTimeAfterRead > 0 should start a countdown to remove the message from the page.

    3. If displayed messages do not include messageIds in notify.messages, ignore; the server will automatically delete them.

    4. Typical handling for single and group chat self-destruct messages:

    (1) Single chat sender: after receiving read notification from the other party, start countdown based on message.lifeTimeAfterRead to clear.

    (2) Single chat receiver: after sending read notification, start countdown based on message.lifeTimeAfterRead to clear.

    (3) Group chat sender: when notify.messages[0].unreadCount is 0, all have read; sender clears message based on message.lifeTimeAfterRead.

    (4) Group chat receiver: after sending read receipt, clear based on message.lifeTimeAfterRead.
  */
});


### 消息清除监听

jim.on(Event.MESSAGE_CLEAN, (notify) => {
  /* 
  Example notify:
    {
      conversationType: 1,
      conversationId: "dDshdk1d4",
      cleanTime: 1716471002135
    }
  */
  console.log(notify);
});


### 消息撤回监听

jim.on(Event.MESSAGE_RECALLED, (notify) => {
  /* 
  Handling logic: Developers only need to update the in-memory message recall status; the SDK automatically handles local and server-side historical message storage.

  Example notify:
    {
      conversationType: 1,
      conversationId: "dDshdk1d4",
      content: {
        // UID of the recalled message
        messageId: "nq4d9xsfgeghvtnd",
        // Timestamp of the recalled message
        sentTime: 1712903378965
      },
      sender: {
        id: 'dkdosd',
        name: 'chater',
        portrait: 'https://xxx.example.com/avatar.png'
      }
    }
  */
  console.log(notify);
});


### 消息删除监听

jim.on(Event.MESSAGE_REMOVED, (notify) => {
  /* 
    Example notify:
      {
       conversationType: 1,
        conversationId: "dDshdk1d4",
        content: {
          messages: [{ messageId: "nq4d9xsfgeghvtnd" }],
        }
      }
    */
  console.log(notify);
});


### 消息修改监听

jim.on(Event.MESSAGE_UPDATED, (notify) => {
  /*
    Handling logic:
      1. Developers should update the in-memory message's isUpdated flag to true.
      2. The SDK automatically sets isUpdated to true when fetching historical messages.
      3. Update the in-memory message here; if no modified message exists in memory, this can be ignored.

    Example notify:
      {
        conversationType: 1,
        conversationId: "dDshdk1d4",
        // ID of the modified message; update the UI for displayed messages by message ID
        messageId: 'nq4d9xsfgeghvtnd',
        content: {
          // Latest message content
          content: 'new content'
        },
      }
   */ 
  console.log(notify);
});
```
</TabItem>
<TabItem value="harmony">

可以设置多个监听。

```js
// 收到新消息
JuggleIm.instance.getMessageManager().addMsgReceivedListener((msg) => {

});

// 消息撤回监听
JuggleIm.instance.getMessageManager().addMsgRecalledListener((msg) => {

});

// 消息修改监听
JuggleIm.instance.getMessageManager().addMsgModifiedListener((msg) => {

});

// 消息删除监听
JuggleIm.instance.getMessageManager().addMsgDeletedListener((conver, msgIds) => {

});

// 消息清除监听
JuggleIm.instance.getMessageManager().addMsgCleanedListener((conver, cleanTime, senderId) => {

});
```
</TabItem>
<TabItem value="reactnative">

**消息相关监听**

可以设置多个监听，每个监听需要指定唯一的 key，返回的函数可用于取消监听。

```typescript
import JuggleIM from 'juggleim-rnsdk';

// 添加消息监听，返回取消监听的函数
const unsubscribeMessage = JuggleIM.addMessageListener('message_key', {
  // 接收消息回调
  onMessageReceive: (message) => {
    console.log('Received message:', message);
  },

  // 消息撤回回调
  onMessageRecall: (message) => {
    console.log('Message recalled:', message);
  },

  // 消息修改回调
  onMessageUpdate: (message) => {
    console.log('Message updated:', message);
  },

  // 消息删除回调
  // conversation: 会话标识
  // clientMsgNos: 列表（本端消息唯一编号）
  onMessageDelete: (conversation, clientMsgNos) => {
    console.log('Messages deleted:', conversation, clientMsgNos);
  },

  // 消息清除回调，表示清除特定会话中某个时间点之前的所有消息
  // conversation: 会话标识
  // timestamp: 时间戳（毫秒），timestamp 之前的消息被清除
  // senderId: 若不为空，表示只清除发送者 id 为 senderId 的消息
  onMessageClear: (conversation, timestamp, senderId) => {
    console.log('Messages cleared:', conversation, timestamp, senderId);
  },

  // 新增消息回应回调
  // conversation: 所属会话
  // reaction: 新增的消息回应
  onMessageReactionAdd: (conversation, reaction) => {
    console.log('Message reaction added:', conversation, reaction);
  },

  // 删除消息回应回调
  // conversation: 所属会话
  // reaction: 删除的消息回应
  onMessageReactionRemove: (conversation, reaction) => {
    console.log('Message reaction removed:', conversation, reaction);
  },

  // 消息置顶回调
  // message: 对应的消息
  // operator: 操作置顶的用户
  // isTop: true 表示置顶，false 表示取消置顶
  onMessageSetTop: (message, operator, isTop) => {
    console.log('Message set top:', message, operator, isTop);
  }
});

// 取消监听
// unsubscribeMessage();
```

**消息阅读状态相关监听**

```typescript
// 添加消息阅读状态监听，返回取消监听的函数
const unsubscribeReadReceipt = JuggleIM.addMessageReadReceiptListener('read_receipt_key', {
  // 单聊消息阅读回调
  // conversation: 所在会话
  // messageIds: 消息 id (messageId) 列表
  onMessagesRead: (conversation, messageIds) => {
    console.log('Messages read:', conversation, messageIds);
  },

  // 群消息阅读回调
  // conversation: 所在会话
  // messages: key 为 messageId，value 为阅读状态
  onGroupMessagesRead: (conversation, messages) => {
    console.log('Group messages read info updated:', conversation, messages);
  }
});

// 取消监听
// unsubscribeReadReceipt();
```

**消息销毁相关监听**

```typescript
// 添加消息销毁监听，返回取消监听的函数
const unsubscribeDestroy = JuggleIM.addMessageDestroyListener('destroy_key', {
  // 消息销毁时间更新回调（通常用于阅后即焚场景）
  // messageId: 消息 id
  // conversation: 所在会话
  // destroyTime: 更新后的销毁时间
  onMessageDestroyTimeUpdate: (messageId, conversation, destroyTime) => {
    console.log('Message destroy time updated:', messageId, conversation, destroyTime);
  }
});

// 取消监听
// unsubscribeDestroy();
```

</TabItem>
<TabItem value="flutter" label="Flutter">

**消息相关监听**

连接监听仅支持设置一次，多次设置会覆盖之前的监听。如果有多个监听点，建议在一个监听中处理所有状态，并在业务层进行二次事件分发。

```dart
// 接收消息回调
JuggleIm.instance.onMessageReceive = (Message message) {
};

// 消息撤回回调
JuggleIm.instance.onMessageRecall = (Message message) {
};

// 消息修改回调
JuggleIm.instance.onMessageUpdate = (Message message) {
};

// 消息删除回调
// conversation: 会话标识
// clientMsgNoList: 列表（本端消息唯一编号 clientMsgNo）
JuggleIm.instance.onMessageDelete = (Conversation conversation, List<int> clientMsgNoList) {
};

// 消息清除回调，表示清除特定会话中某个时间点之前的所有消息
// conversation: 会话标识
// timestamp: 时间戳（毫秒），timestamp 之前的消息被清除
// senderId: 若不为空，表示只清除发送者 id 为 senderId 的消息
JuggleIm.instance.onMessageClear = (Conversation conversation, int timestamp, String? senderId) {
};

// 新增消息回应回调
// conversation: 所属会话
// reaction: 新增的消息回应
JuggleIm.instance.onMessageReactionAdd = (Conversation conversation, MessageReaction reaction) {
};

// 删除消息回应回调
// conversation: 所属会话
// reaction: 删除的消息回应
JuggleIm.instance.onMessageReactionRemove = (Conversation conversation, MessageReaction reaction) {
};

// 消息置顶回调
// message: 对应的消息
// operator: 操作置顶的用户
// isTop: true 表示置顶，false 表示取消置顶
JuggleIm.instance.onMessageSetTop = (Message message, String operator, bool isTop) {
};
```

**消息阅读状态相关监听**

```dart
// 单聊消息阅读回调
// conversation: 所在会话
// messageIdList: 消息 id (messageId) 列表
JuggleIm.instance.onMessagesRead = (Conversation conversation, List<String> messageIdList) {
};

// 群消息阅读回调
// conversation: 所在会话
// messages: key 为 messageId，value 为阅读状态
JuggleIm.instance.onGroupMessagesRead = (Conversation conversation, Map<String, GroupMessageReadInfo> messages) {
};
```

**消息销毁相关监听**

```dart
// 消息销毁时间更新回调（通常用于阅后即焚场景）
// messageId: 消息 id
// conversation: 所在会话
// destroyTime: 更新后的销毁时间
JuggleIm.instance.onMessageDestroyTimeUpdate = (String messageId, Conversation conversation, int destroyTime) {
};
```

</TabItem>
</Tabs>