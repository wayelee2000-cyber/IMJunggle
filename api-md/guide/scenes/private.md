---
title: Private chat/private message
hide_title: true
sidebar_position: 1
---

### Scene introduction{#intro}

Single chat typically refers to one-to-one communication between two users. They can exchange text, files, images, voice messages, friend request notifications, and other message types. In private chat scenarios, the core message delivery requirements are stringent: messages must not be lost, duplicated, or delivered out of order. When a user switches devices, historical messages should automatically synchronize to the new device. Read status, unread counts, and message operations must remain consistent across all of a user's devices. Common message operations include `recall`, `message editing`, and `reply`.

### Applicable scenarios{#match}

> **Private messages between acquaintances**: In social products, acquaintances are usually connected through friend relationships. Users search for each other by phone number or unique identifier, add each other as friends, and then begin interacting online.

> **Private messages from strangers**: In stranger-social scenarios, users often have clear profiles and tags. They are matched based on interests, age, or other attributes, and then communicate via private messaging.

> **Buyer-seller communication**: Buyers and sellers communicate through text and images, typically for pre-sales consultation or after-sales support related to specific orders or products.

> **Streamer-fan interaction**: In live social products with `KOL` or streamer-follow features, users can follow a streamer and then send private messages or a limited number of interactive messages.

> **Additional private chat scenarios**: `Driver and passenger`, `1v1 teaching`, `teacher-student communication`, `home-school communication`, `courier and customer`, and more.

### Scenario features{#sp}

> **Relationship model**: Supports one-way or mutual friend relationships. Fans can follow streamers independently, and the number of friends can scale as needed.

> **Online status**: Users can subscribe to the online status of friends or followed users on demand, enabling the application layer to provide richer prompts and more accurate business matching.

> **Allowlist and blocklist**: Two-way allowlist and blocklist controls can restrict or permit message sending. For example, adding a user to the blocklist prevents further messages, while adding a user to the allowlist explicitly permits communication.

> **Profile synchronization**: When user information changes, the system provides a seamless synchronization mechanism and automatically notifies related users.

> **User info embedded in messages**: Messages include user information, simplifying client-side rendering and reducing integration complexity.

### Related documents{#doc}

> **Basic documents**: [SDK Download](../../client/import.md), [Integration Example](../../client/quickstart/ios.md)

> **User management**: [User registration](../../server/user/register.md), [Update user information](../../server/user/updateuser.md), [Ban user](../../server/user/addbanuser.md), [Mute user](../../server/user/addblockuser.md)

> **Message related**: [Message structure](../../client/sdkintro/msg/message.md), [Send message](../../client/sdkintro/message/msg_send/send.md), [Receive message](../../client/sdkintro/watcher/message.md), [Get historical messages](../../client/sdkintro/message/histories/get_all.md), [Clear historical messages](../../client/sdkintro/message/histories/clear.md), [Message recall](../../client/sdkintro/message/operator/recall.md), [Message read](../../client/sdkintro/message/operator/read.md), [REST API send message](../../server/message/privatemsg.md)

> **Conversation related**: [Conversation structure](../../client/sdkintro/conversation.md), [Get conversation list](../../client/sdkintro/conversation/get_all.md), [Pin a conversation](../../client/sdkintro/conversation/operator/settop.md), [Do not disturb](../../client/sdkintro/conversation/operator/disturb.md), [Get the total number of unreads](../../client/sdkintro/conversation/unread/get_total_unread.md), [Server gets conversation list](../../server/convers/qryconvers.md)

> **Status code**: [Android related](../../client/sdkintro/status_code/android.md), [iOS related](../../client/sdkintro/status_code/ios.md), [Web related](../../client/sdkintro/status_code/web.md), [REST API related](../../server/status.md)
