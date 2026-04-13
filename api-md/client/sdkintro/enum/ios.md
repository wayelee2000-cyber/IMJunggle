---
title: iOS
hide_title: true
sidebar_position: 2
---

#### Connection Status

```objectivec
typedef NS_ENUM(NSUInteger, JConnectionStatus) {
    // Not connected
    JConnectionStatusIdle = 0,
    // Connected
    JConnectionStatusConnected = 1,
    // Disconnected (user-initiated)
    JConnectionStatusDisconnected = 2,
    // Connecting
    JConnectionStatusConnecting = 3,
    // Connection failed; users can handle this based on JErrorCode
    JConnectionStatusFailure
};
```

#### Conversation Type

```objectivec
/*!
 Conversation Types
 */
typedef NS_ENUM(NSUInteger, JConversationType) {
    
    JConversationTypeUnknown = 0,
    /*!
     Private chat
     */
    JConversationTypePrivate = 1,

    /*!
     Group chat
     */
    JConversationTypeGroup = 2,

    /*!
     Chatroom
     */
    JConversationTypeChatroom = 3,

    /*!
     System conversation
     */
    JConversationTypeSystem = 4,
};
```

#### Pull Direction

```objectivec
typedef NS_ENUM(NSUInteger, JPullDirection) {
    JPullDirectionNewer = 0,
    JPullDirectionOlder = 1,
};
```