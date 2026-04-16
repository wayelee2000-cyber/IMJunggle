---
title: Live chat room
hide_title: true
sidebar_position: 4
---

### Scene introduction{#intro}

The live chat room is an interactive communication scene based on IM instant messaging within "live social" environments. Its main features include sending barrage messages, gifting, liking, real-time room population tracking, and detailed listings. The chat room supports up to 100,000 concurrent users and can handle tens of billions of message distributions. It provides data storage with a lifecycle matching that of the room, suitable for live broadcast scenarios across various fields. Additionally, it includes its own synchronization mechanisms—such as real-time room population counts and shopping carts—enabling developers to flexibly combine capabilities at the business layer and easily create live broadcast experiences.

### Applicable scenarios{#match}

> **Game live broadcast**: Game platforms share mobile or client game processes with audiences through a live broadcast room, where game anchors provide commentary or gameplay, enhancing the gaming atmosphere.

> **E-commerce live broadcast**: E-commerce platforms sell products via live broadcasts, featuring functions such as anchors linking to shopping carts, audience comment consultations, and order placement.

> **Event live broadcast**: Typically for sports events like the Winter Olympics, NBA, or World Cup, fans watch live broadcasts and discuss the events together online.

> **News live broadcast**: An innovative form distinct from traditional news broadcasts, allowing users to watch real-time news commentary on their mobile devices through live broadcasts within the application client.

> **More Live Broadcasts**: `Chat Room`, `Talent Live Broadcast`, `Show Live Broadcast`, and others.

### Scenario features{#sp}

> **Flexible and easy to use**: Users can freely join and leave the room to interact at any time.

> **Global Broadcast**: Broadcast and send trending messages to a single live broadcast room or all live broadcast rooms within the application.

> **High performance**: Supports high concurrency with billions of messages and no upper limit on the number of participants in a live broadcast room.

> **Room Data Consistency**: Operations such as mic position management and product listings share the room’s lifecycle. Signaling is delivered to users within seconds, allowing flexible front-end and back-end control.

> **Real-time room status updates**: The number of people in the room, mic position status, and rankings are updated in real time.

### Related documents{#doc}

> **Basic documents**: [SDK Download](../../client/import.md), [Integration Example](../../client/quickstart/ios.md)

> **User management**: [User registration](../../server/user/register.md), [Update user information](../../server/user/updateuser.md), [Ban user](../../server/user/addbanuser.md), [Mute user](../../server/user/addblockuser.md)

> **Chatroom related**: [Join chatroom](../../client/sdkintro/chatroom/join.md), [Send chatroom message](../../client/sdkintro/chatroom/send.md), [Chatroom events](../../client/sdkintro/chatroom/event.md), [Create chatroom](../../server/chatroom/createchatroom.md), [Get chatroom info](../../server/chatroom/qrychrminfo.md), [REST API send message](../../server/message/chatroommsg.md)

> **Conversation related**: [Conversation structure](../../client/sdkintro/conversation.md), [Get conversation list](../../client/sdkintro/conversation/get_all.md), [Pin a conversation](../../client/sdkintro/conversation/operator/settop.md), [Do not disturb](../../client/sdkintro/conversation/operator/disturb.md), [Get the total number of unreads](../../client/sdkintro/conversation/unread/get_total_unread.md), [Server gets conversation list](../../server/convers/qryconvers.md)

> **Status code**: [Android related](../../client/sdkintro/status_code/android.md), [iOS related](../../client/sdkintro/status_code/ios.md), [Web related](../../client/sdkintro/status_code/web.md), [REST API related](../../server/status.md)
