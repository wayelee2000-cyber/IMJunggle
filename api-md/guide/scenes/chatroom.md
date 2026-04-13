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

### Features of the plan{#sp}

> **Flexible and easy to use**: Users can freely join and leave the room to interact at any time.

> **Global Broadcast**: Broadcast and send trending messages to a single live broadcast room or all live broadcast rooms within the application.

> **High performance**: Supports high concurrency with billions of messages and no upper limit on the number of participants in a live broadcast room.

> **Room Data Consistency**: Operations such as mic position management and product listings share the room’s lifecycle. Signaling is delivered to users within seconds, allowing flexible front-end and back-end control.

> **Real-time room status updates**: The number of people in the room, mic position status, and rankings are updated in real time.

### Related documents{#doc}

> **Basic Documents**: [SDK Download](../../../client/import), [Integration Example](../../../client/quickstart/ios)

> **User Management**: [User Registration](../../../server/user/register), [Update Information](../../../server/user/updateuser), [User Ban](../../../server/user/addbanuser), [Ban User](../../../server/user/addblockuser)

> **Message related**: [Message structure](../../../client/sdkintro/msg/message), [Send message](../../../client/sdkintro/message/msg_send/send), [Receive message](../../../client/sdkintro/watcher/message), [Get historical messages](../../../client/sdkintro/message/histories/get_all), [Clear historical messages](../../../client/sdkintro/message/histories/clear), [Message recall](../../../client/sdkintro/message/operator/recall), [Message read](../../../client/sdkintro/message/operator/read), [REST API send message](../../../server/message/privatemsg)

> **Session related**: [Session structure](../../../client/sdkintro/conversation), [Get session list](../../../client/sdkintro/conversation/get_all), [Session top](../../../client/sdkintro/conversation/settop), [Do not disturb](../../../client/sdkintro/conversation/disturb), [Get the total number of unreads](../../../client/sdkintro/conversation/get_total_unread), [Server gets the conversation list](../../../server/convers/qryconvers)

> **Status code**: [Android related](../../../client/sdkintro/status_code/android), [iOS related](../../../client/sdkintro/status_code/ios), [Web related](../../../client/sdkintro/status_code/web), [REST API Related](../../../server/status)