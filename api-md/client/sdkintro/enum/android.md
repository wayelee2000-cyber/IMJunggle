---
title: Android
hide_title: true
sidebar_position: 1
---

#### Connection Status

```java
public enum ConnectionStatus {
    IDLE(0),
    CONNECTED(1),
    DISCONNECTED(2),
    CONNECTING(3),
    FAILURE(4);
}
```

#### Conversation Type

```java
public enum ConversationType {
    UNKNOWN(0),
    /// Private chat
    PRIVATE(1),
    /// Group chat
    GROUP(2),
    /// Chatroom
    CHATROOM(3),
    /// System conversation
    SYSTEM(4);
}
```

#### Pull Direction

```java
public enum PullDirection {
	NEWER, OLDER
}
```

#### Message Direction

```java
public enum MessageDirection {
    SEND(1),
    RECEIVE(2);
}
```

#### Message State

```java
public enum MessageState {
    UNKNOWN(0),
    SENDING(1),
    SENT(2),
    FAIL(3),
    UPLOADING(4);
}
```

#### Call Status

```java
public enum CallStatus {
    // No call
    IDLE(0),
    // Incoming call
    INCOMING(1),
    // Outgoing call
    OUTGOING(2),
    // Connecting
    CONNECTING(3),
    // Connected
    CONNECTED(4),
    // Joined actively
    JOIN(5);
}
```

#### Call Media Type

```java
public enum CallMediaType {
    // Voice call
    VOICE(0),
    // Video call
    VIDEO(1);
}
```

#### Call Finish Reason

```java
public enum CallFinishReason {
        /// Unknown reason
        UNKNOWN(0),
        /// Current user hung up an answered call
        HANGUP(1),
        /// Current user declined the call
        DECLINE(2),
        /// Current user is busy
        BUSY(3),
        /// Current user did not answer
        NO_RESPONSE(4),
        /// Current user canceled the call
        CANCEL(5),
        /// Remote user hung up an answered call
        OTHER_SIDE_HANGUP(6),
        /// Remote user declined the call
        OTHER_SIDE_DECLINE(7),
        /// Remote user is busy
        OTHER_SIDE_BUSY(8),
        /// Remote user did not answer
        OTHER_SIDE_NO_RESPONSE(9),
        /// Remote user canceled the call
        OTHER_SIDE_CANCEL(10),
        /// Room was destroyed
        ROOM_DESTROY(11),
        /// Network error
        NETWORK_ERROR(12),
        /// Current user answered the call on another device
        ACCEPT_ON_OTHER_CLIENT(13),
        /// Current user hung up the call on another device
        HANGUP_ON_OTHER_CLIENT(14);
}
```