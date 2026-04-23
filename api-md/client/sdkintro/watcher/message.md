---
title: Message Event Listener
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
]}
>
<TabItem value="android">

**Message-related listeners**

You can set multiple listeners.
```java
JIM.getInstance().getMessageManager().addListener("main", new IMessageManager.IMessageListener() {
    /// Callback for receiving messages
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

    /// Message recall callback
    @Override
    public void onMessageRecall(Message message) {
        Log.d("TAG", "onMessageRecall, messageId is " + message.getMessageId());
    }

    /// Message update callback
    @Override
    public void onMessageUpdate(Message message) {
        Log.d("TAG", "onMessageUpdate, messageId is " + message.getMessageId());
    }

    /// Message deletion callback
    /// conversation: Conversation identifier
    /// clientMsgNos: List of client-side unique message numbers
    @Override
    public void onMessageDelete(Conversation conversation, List<Long> clientMsgNos) {
        Log.d("TAG", "onMessageDelete, conversation is " + conversation.getConversationId() + ", clientMsgNos are " + clientMsgNos);
    }

    /// Message clear callback, indicating all messages before a certain timestamp in a specific conversation are cleared
    /// conversation: Conversation identifier
    /// timestamp: Timestamp in milliseconds; messages before timestamp are cleared
    /// senderId: If not empty, only clear messages sent by senderId
    @Override
    public void onMessageClear(Conversation conversation, long timestamp, String senderId) {
        Log.d("TAG", "onMessageClear, conversation is " + conversation.getConversationId() + ", timestamp is " + timestamp + ", senderId is " + senderId);
    }

    /// Callback when a message reaction is added
    /// conversation: The conversation it belongs to
    /// reaction: The newly added message reaction
    @Override
    public void onMessageReactionAdd(Conversation conversation, MessageReaction reaction) {

    }

    /// Callback when a message reaction is removed
    /// conversation: The conversation it belongs to
    /// reaction: The removed message reaction
    void onMessageReactionRemove(Conversation conversation, MessageReaction reaction) {

    }

    /// Message pin callback
    /// message: The corresponding message
    /// operator: The user who pinned/unpinned the message
    /// isTop: true means pinned, false means unpinned
    void onMessageSetTop(Message message, UserInfo operator, boolean isTop) {

    }
});
```

**Message read status listeners**

You can set multiple listeners.
```java
JIM.getInstance().getMessageManager().addReadReceiptListener("main", new IMessageManager.IMessageReadReceiptListener() {
  /// One-to-one message read callback
  /// conversation: The conversation
  /// messageIds: List of message IDs
	@Override
	public void onMessagesRead(Conversation conversation, List<String> messageIds) {
		Log.d("TAG", "onMessagesRead, count is " + messageIds.size() + ", conversationType is " + conversation.getConversationType() + ", conversationId is " + conversation.getConversationId());
	}

  /// Group message read callback
  /// conversation: The conversation
  /// messages: key is messageId
	@Override
	public void onGroupMessagesRead(Conversation conversation, Map<String, GroupMessageReadInfo> messages) {
		Log.d("TAG", "onGroupMessagesRead, conversationType is " + conversation.getConversationType() + ", id is " + conversation.getConversationId() + ", count is " + messages.size());
	}
});
```

**Message destruction listeners**

You can set multiple listeners.
```java
JIM.getInstance().getMessageManager().addDestroyListener("main", new IMessageManager.IMessageDestroyListener() {
  /**
    * Callback when the message destruction time is updated (commonly used for burn-after-reading scenarios)
    * @param messageId Message ID
    * @param conversation The conversation
    * @param destroyTime Updated destruction time
    */
	@Override
	public void onMessageDestroyTimeUpdate(String messageId, Conversation conversation, long destroyTime) {

	}
});
```

**Message encryption/decryption callbacks**

Only one listener can be set for message encryption/decryption.
```java
JIM.getInstance().getMessageManager().setPreprocessor(new IMessageManager.IMessagePreprocessor() {
  /**
    * Message encryption callback
    * Trigger timing: after the message is stored, before sending
    * @param content The message content to send, serialized as byte[]
    * @param conversation The conversation
    * @param contentType Message type
    * @return Processed message content
    */
	@Override
	public byte[] encryptMessageContent(byte[] content, Conversation conversation, String contentType) {

	}

  /**
    * Message decryption callback
    * Trigger timing: after receiving the message, before storing it
    * @param content The received message content, of type byte[], not yet deserialized
    * @param conversation The conversation
    * @param contentType Message type
    * @return Processed message content
    */
	@Override
	public byte[] decryptMessageContent(byte[] content, Conversation conversation, String contentType) {

	}
});
```

</TabItem>
<TabItem value="ios">

**Message-related listeners**

You can set multiple delegates.
```objectivec
[JIM.shared.messageManager addDelegate:self];

/// Message receive callback
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

/// Message recall callback
- (void)messageDidRecall:(JMessage *)message {
    NSLog(@"messageDidRecall");
}

/// Message update callback
- (void)messageDidUpdate:(JMessage *)message {
    NSLog(@"messageDidUpdate");
}

/// Message deletion callback
- (void)messageDidDelete:(JConversation *)conversation
            clientMsgNos:(NSArray <NSNumber *> *)clientMsgNos {

}

/// Message clear callback, indicating all messages before a certain timestamp in a specific conversation are cleared
/// - Parameters:
///   - conversation: Identifier of the conversation whose messages were cleared
///   - timestamp: Timestamp in milliseconds; messages before timestamp are cleared
///   - senderId: If not empty, only clear messages sent by senderId
- (void)messageDidClear:(JConversation *)conversation
              timestamp:(long long)timestamp
               senderId:(NSString *)senderId {

}

/// Callback when a message reaction is added
/// - Parameter reaction: The newly added message reaction
/// - Parameter conversation: The conversation it belongs to
- (void)messageReactionDidAdd:(JMessageReaction *)reaction
               inConversation:(JConversation *)conversation {

}

/// Callback when a message reaction is removed
/// - Parameter reaction: The removed message reaction
/// - Parameter conversation: The conversation it belongs to
- (void)messageReactionDidRemove:(JMessageReaction *)reaction
                  inConversation:(JConversation *)conversation {
  
}

/// Message pin callback
/// - Parameters:
///   - isTop: YES means pinned, NO means unpinned
///   - message: The corresponding message
///   - userInfo: The user who pinned/unpinned the message
- (void)messageDidSetTop:(BOOL)isTop
                 message:(JMessage *)message
                    user:(JUserInfo *)userInfo {
  
}
```

**Message read status listeners**

You can set multiple delegates.
```objectivec
[JIM.shared.messageManager addReadReceiptDelegate:self];

/// One-to-one message read callback
/// - Parameters:
///   - messageIds: List of message IDs
///   - conversation: The conversation
- (void)messagesDidRead:(NSArray<NSString *> *)messageIds inConversation:(JConversation *)conversation {
    NSLog(@"messagesDidRead");
}

/// Group message read callback
/// - Parameters:
///   - msgs: key is messageId
///   - conversation: The conversation
- (void)groupMessagesDidRead:(NSDictionary<NSString *,JGroupMessageReadInfo *> *)msgs inConversation:(JConversation *)conversation {
    NSLog(@"groupMessagesDidRead, groupId is %@", conversation.conversationId);
}
```

**Message destruction listeners**

You can set multiple delegates.
```objectivec
[JIM.shared.messageManager addDestroyDelegate:self];

/// Callback when the message destruction time is updated (commonly used for burn-after-reading scenarios)
/// - Parameters:
///   - messageId: Message ID
///   - conversation: The conversation
///   - destroyTime: Updated destruction time
- (void)messageDestroyTimeDidUpdate:(NSString *)messageId
                     inConversation:(JConversation *)conversation
                        destroyTime:(long long)destroyTime {
  
}
```

**Message encryption/decryption callbacks**

Only one delegate can be set for message encryption/decryption.
```objectivec
[JIM.shared.messageManager setPreprocessor:self];

/// Message encryption callback
/// Trigger timing: after the message is stored, before sending
/// - Parameter content: The message content to send, serialized as NSData
/// - Parameter conversation: The conversation
/// - Parameter contentType: Message type
/// - Returns: Processed message content
- (NSData *)encryptMessageContent:(NSData *)content
                   inConversation:(JConversation *)conversation
                      contentType:(NSString *)contentType {
  
}

/// Message decryption callback
/// Trigger timing: after receiving the message, before storing it
/// - Parameter content: The received message content in NSData format, not yet deserialized
/// - Parameter conversation: The conversation
/// - Parameter contentType: Message type
/// - Returns: Processed message content
- (NSData *)decryptMessageContent:(NSData *)content
                   inConversation:(JConversation *)conversation
                      contentType:(NSString *)contentType {
  
}
```

</TabItem>
<TabItem value="js">

Global listeners only need to be set once; multiple settings will override previous ones. When others send messages to the current user, the message event listener will be triggered. For message format, see [Message Structure](../msg/message.md). For event descriptions, see [Listener Enum](../enum/web.md#listener).

```js
let { Event } = JIM;

### Message Receive Listener

jim.on(Event.MESSAGE_RECEIVED, (message) => {
  console.log(message);
});


### Message Read Listener

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


### Message Clear Listener

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


### Message Recall Listener

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


### Message Delete Listener

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


### Message Update Listener

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
<TabItem value="reactnative">

**Message-related listeners**

You can set multiple listeners. Each listener must specify a unique `key`, and the returned function can be used to remove the listener.
```typescript
import JuggleIM from 'juggleim-rnsdk';

// Add a message event listener and return the unsubscribe function
const unsubscribeMessage = JuggleIM.addMessageListener('message_key', {
  // Callback for receiving messages
  onMessageReceive: (message) => {
    console.log('Received message:', message);
  },

  // Message recall callback
  onMessageRecall: (message) => {
    console.log('Message recalled:', message);
  },

  // Message update callback
  onMessageUpdate: (message) => {
    console.log('Message updated:', message);
  },

  // Message deletion callback
  // conversation: Conversation identifier
  // clientMsgNos: List of client-side unique message numbers
  onMessageDelete: (conversation, clientMsgNos) => {
    console.log('Messages deleted:', conversation, clientMsgNos);
  },

  // Message clear callback, indicating all messages before a certain timestamp in a specific conversation are cleared
  // conversation: Conversation identifier
  // timestamp: Timestamp in milliseconds; messages before timestamp are cleared
  // senderId: If not empty, only clear messages sent by senderId
  onMessageClear: (conversation, timestamp, senderId) => {
    console.log('Messages cleared:', conversation, timestamp, senderId);
  },

  // Callback when a message reaction is added
  // conversation: The conversation it belongs to
  // reaction: The newly added message reaction
  onMessageReactionAdd: (conversation, reaction) => {
    console.log('Message reaction added:', conversation, reaction);
  },

  // Callback when a message reaction is removed
  // conversation: The conversation it belongs to
  // reaction: The removed message reaction
  onMessageReactionRemove: (conversation, reaction) => {
    console.log('Message reaction removed:', conversation, reaction);
  },

  // Message pin callback
  // message: The corresponding message
  // operator: The user who pinned/unpinned the message
  // isTop: true means pinned, false means unpinned
  onMessageSetTop: (message, operator, isTop) => {
    console.log('Message set top:', message, operator, isTop);
  }
});

// Remove the listener
// unsubscribeMessage();
```

**Message read status listeners**

```typescript
// Add a message read receipt listener and return the unsubscribe function
const unsubscribeReadReceipt = JuggleIM.addMessageReadReceiptListener('read_receipt_key', {
  // One-to-one message read callback
  // conversation: The conversation
  // messageIds: List of message IDs (messageId)
  onMessagesRead: (conversation, messageIds) => {
    console.log('Messages read:', conversation, messageIds);
  },

  // Group message read callback
  // conversation: The conversation
  // messages: key is messageId, value is the read status
  onGroupMessagesRead: (conversation, messages) => {
    console.log('Group messages read info updated:', conversation, messages);
  }
});

// Remove the listener
// unsubscribeReadReceipt();
```

**Message destruction listeners**

```typescript
// Add a message destruction listener and return the unsubscribe function
const unsubscribeDestroy = JuggleIM.addMessageDestroyListener('destroy_key', {
  // Callback when the message destruction time is updated (commonly used for burn-after-reading scenarios)
  // messageId: Message ID
  // conversation: The conversation
  // destroyTime: Updated destruction time
  onMessageDestroyTimeUpdate: (messageId, conversation, destroyTime) => {
    console.log('Message destroy time updated:', messageId, conversation, destroyTime);
  }
});

// Remove the listener
// unsubscribeDestroy();
```

</TabItem>
<TabItem value="flutter" label="Flutter">

**Message-related listeners**

Connection listeners can only be set once. Setting them multiple times will override the previous listener. If there are multiple listening points, it is recommended to handle all states in a single listener and then perform secondary event dispatching at the business layer.
```dart
// Message receive callback
JuggleIm.instance.onMessageReceive = (Message message) {
};

// Message recall callback
JuggleIm.instance.onMessageRecall = (Message message) {
};

// Message update callback
JuggleIm.instance.onMessageUpdate = (Message message) {
};

// Message deletion callback
// conversation: Conversation identifier
// clientMsgNoList: List of client-side unique message numbers (clientMsgNo)
JuggleIm.instance.onMessageDelete = (Conversation conversation, List<int> clientMsgNoList) {
};

// Message clear callback, indicating all messages before a certain timestamp in a specific conversation are cleared
// conversation: Conversation identifier
// timestamp: Timestamp in milliseconds; messages before timestamp are cleared
// senderId: If not empty, only clear messages sent by senderId
JuggleIm.instance.onMessageClear = (Conversation conversation, int timestamp, String? senderId) {
};

// Callback when a message reaction is added
// conversation: The conversation it belongs to
// reaction: The newly added message reaction
JuggleIm.instance.onMessageReactionAdd = (Conversation conversation, MessageReaction reaction) {
};

// Callback when a message reaction is removed
// conversation: The conversation it belongs to
// reaction: The removed message reaction
JuggleIm.instance.onMessageReactionRemove = (Conversation conversation, MessageReaction reaction) {
};

// Message pin callback
// message: The corresponding message
// operator: The user who pinned/unpinned the message
// isTop: true means pinned, false means unpinned
JuggleIm.instance.onMessageSetTop = (Message message, String operator, bool isTop) {
};
```

**Message read status listeners**

```dart
// One-to-one message read callback
// conversation: The conversation
// messageIdList: List of message IDs (messageId)
JuggleIm.instance.onMessagesRead = (Conversation conversation, List<String> messageIdList) {
};

// Group message read callback
// conversation: The conversation
// messages: key is messageId, value is the read status
JuggleIm.instance.onGroupMessagesRead = (Conversation conversation, Map<String, GroupMessageReadInfo> messages) {
};
```

**Message destruction listeners**

```dart
// Callback when the message destruction time is updated (commonly used for burn-after-reading scenarios)
// messageId: Message ID
// conversation: The conversation
// destroyTime: Updated destruction time
JuggleIm.instance.onMessageDestroyTimeUpdate = (String messageId, Conversation conversation, int destroyTime) {
};
```

</TabItem>
</Tabs>
