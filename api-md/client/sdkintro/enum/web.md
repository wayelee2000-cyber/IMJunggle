---
title: Web
hide_title: true
sidebar_position: 3
---

### Listening Enumeration {#listener}

| Name | Description | Version |
|----------------------------------|----------------------------------------|----------|
| Event.STATE_CHANGED | Monitors connection status; uses [connection monitoring](../watcher/connect.md) | 1.0.0 |
| Event.MESSAGE_RECEIVED | Monitors message reception; uses [Message Listening](../watcher/message.md) | 1.0.0 |
| Event.CONVERSATION_CHANGED | Monitors session changes; uses [Session Monitoring](../watcher/conversation.md) | 1.0.0 |

### Connection Enumeration {#connection}

| Name | Description | Version |
|----------------------------------|------------------|----------|
| ConnectionState.CONNECTED | Connection established successfully | 1.0.0 |
| ConnectionState.CONNECTING | Connecting | 1.0.0 |
| ConnectionState.DISCONNECTED | Connection has been disconnected. This indicates a complete disconnection. The SDK will not attempt any reconnection. The developer's business layer can notify that the connection is disconnected. | 1.0.0 |
| ConnectionState.DB_OPENED | Local database is open; valid only in Electron | 1.7.0 |
| ConnectionState.DB_CLOSED | Local database is closed; valid only in Electron | 1.7.0 |
| ConnectionState.RECONNECTING | The SDK is reconnecting internally. By default, the SDK sends a heartbeat packet every 30 seconds. If the server does not respond to three consecutive heartbeat packets, it will attempt to reconnect. If a single request (e.g., message sending) times out after 10 seconds, a timeout is triggered and reconnection logic is attempted. The default maximum reconnection attempts is 100, with intervals of 1s, 2s, 4s, 8s, 16s, and so on. | 1.7.0 |

### Conversation Related {#conversation}

| Name | Description | Version |
|----------------------------------|--------------------------------------------------|----------|
| ConversationType.PRIVATE | Single chat session between two users | 1.0.0 |
| ConversationType.GROUP | Group chat session for group communication | 1.0.0 |
| ConversationType.CHATROOM | Chat room conversation, similar to a live broadcast room; used in room-based communication scenarios | 1.0.0 |
| ConversationOrder.FORWARD | Conversation retrieval direction: retrieves earlier conversations in reverse chronological order | 1.0.0 |
| ConversationOrder.BACKWARD | Conversation retrieval direction: retrieves newer conversations in reverse chronological order | 1.0.0 |

### Message Related {#message}

| Name | Description | Version |
|----------------------------------|--------------|----------|
| MessageType.TEXT | Text message | 1.0.0 |
| MessageType.IMAGE | Image message | 1.0.0 |
| MessageType.VOICE | Voice message | 1.0.0 |
| MessageType.VIDEO | Short video message | 1.0.0 |
| MessageType.FILE | File message | 1.0.0 |
| MessageType.RECALL | Recall message | 1.0.0 |
| MessageType.READ_MSG | Message withdrawal notification | 1.0.0 |
| MessageType.UPDATE_MSG | Message modification notification | 1.0.0 |
| MessageOrder.FORWARD | Retrieves newer messages; used when scrolling the message page toward the input box | 1.0.0 |
| MessageOrder.BACKWARD | Retrieves earlier messages; used when scrolling the message page to the top | 1.0.0 |

### Status Code Enumeration {#state}

| Name | Description | Version |
|----------------------------------|--------------|----------|
| ErrorType | Status code enumeration; see [Status Code](./web.md) for details | 1.0.0 |

### @Message Enumeration {#mention}

| Name | Description | Version |
|----------------------------------|--------------|----------|
| MentionType.ALL | @Everyone | 1.0.0 |
| MentionType.SOMEONE | @ specific user | 1.0.0 |
| MentionType.ALL_SOMEONE | @Everyone plus specific users | 1.0.0 |

### Do Not Disturb Conversation {#disturb}

| Name | Description | Version |
|----------------------------------|--------------------------------|----------|
| UndisturbType.DISTURB | Do Not Disturb enabled | 1.0.0 |
| UndisturbType.UNDISTURB | Do Not Disturb disabled | 1.0.0 |

### Session Tag Status {#unreadtag}

| Name | Description | Version |
|----------------------------------|--------------------------------|----------|
| UnreadTag.UNREAD | Mark a session as unread | 1.0.0 |

### Message Sending Status {#msg_sent}

| Name | Description | Version |
|----------------------------------|--------------|----------|
| MESSAGE_SENT_STATE.NONE | Initial state | 1.0.0 |
| MESSAGE_SENT_STATE.SENDING | Message is being sent | 1.0.0 |
| MESSAGE_SENT_STATE.SUCCESS | Message sent successfully | 1.0.0 |
| MESSAGE_SENT_STATE.FAILED | Message sending failed | 1.0.0 |
| MESSAGE_SENT_STATE.UPLOADING | Files, images, or other media are being uploaded | 1.0.0 |

### @Message Acquisition Direction {#mention_order}

| Name | Description | Version |
|----------------------------------|--------------------------------|----------|
| MENTION_ORDER.BACKWARD | Retrieves earlier messages; used when scrolling the message page to the top | 1.0.0 |
| MENTION_ORDER.FORWARD | Retrieves newer messages; used when scrolling the message page toward the input box | 1.0.0 |

### Moments Retrieval Direction {#moment_order}

| Name | Description | Version |
|----------------------------------|--------------------------------|----------|
| MOMENT_ORDER.ASC | Retrieve earlier Moments | 1.9.6 |
| MOMENT_ORDER.DESC | Retrieve newer Moments | 1.9.6 |

### Moments Type Enumeration {#moment_type}

| Name | Description | Version |
|----------------------------------|--------------------------------|----------|
| MOMENT_TYPE.IMAGE | Image type | 1.9.6 |
| MOMENT_TYPE.VIDEO | Video type | 1.9.6 |

### Comment Retrieval Direction {#comment_order}

| Name | Description | Version |
|----------------------------------|--------------------------------|----------|
| COMMENT_ORDER.ASC | Retrieve older comments | 1.9.6 |
| COMMENT_ORDER.DESC | Retrieve newer comments | 1.9.6 |