---
title: ReactNative
hide_title: true
sidebar_position: 5
---

#### Connection Status

```ts
type ConnectionStatus = "connected" | "connecting" | "disconnected" | "failure" | "dbOpen" | "dbClose"
```

#### Conversation Types

```ts
enum ConversationType {
  PRIVATE = 1,    // Private chat
  GROUP = 2,      // Group
  CHATROOM = 3,   // Chatroom
  SYSTEM = 4      // System conversation
}
```

#### Message Direction

```ts
enum MessageDirection {
  SEND = 1,    // Sent
  RECEIVE = 2  // Received
}
```

#### Message Status

```ts
enum MessageState {
  UNKNOWN = 0,      // Unknown
  SENDING = 1,      // Sending
  SENT = 2,         // Sent
  SEND_FAILED = 3,  // Send failed
  UPLOADING = 4     // Uploading
}
```

#### Listeners {#listener}

**Connection Status Listener Type:**

```typescript
type ConnectionStatusListener = (
  status: ConnectionStatus,
  code: number,
  extra: string
) => void;
```

**Message Listener Type:**

```typescript
type MessageListener = {
  onMessageReceive?: (message: Message) => void;
  onMessageRecall?: (message: Message) => void;
  onMessageUpdate?: (message: Message) => void;
  onMessageDelete?: (
    conversation: Conversation,
    clientMsgNos: number[]
  ) => void;
  onMessageClear?: (
    conversation: Conversation,
    timestamp: number,
    senderId: string
  ) => void;
  onMessageReactionAdd?: (
    conversation: Conversation,
    reaction: MessageReaction
  ) => void;
  onMessageReactionRemove?: (
    conversation: Conversation,
    reaction: MessageReaction
  ) => void;
  onMessageSetTop?: (
    message: Message,
    operator: UserInfo,
    isTop: boolean
  ) => void;
}
```

**Conversation Listener Type:**

```typescript
type ConversationListener = {
  onConversationInfoAdd?: (conversations: ConversationInfo[]) => void;
  onConversationInfoUpdate?: (conversations: ConversationInfo[]) => void;
  onConversationInfoDelete?: (conversations: ConversationInfo[]) => void;
  onTotalUnreadMessageCountUpdate?: (count: number) => void;
}
```