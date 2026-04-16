---
title: System notification
hide_title: true
sidebar_position: 3
---

### Scene introduction{#intro}

System notification refers to the one-way push of messages from the server to users in IM products. Both `System notification` and `Pingalong chat` involve two-party communication. The difference is that single chat supports bidirectional messaging, while system notifications can only be sent via the server API and are only received by end users. System notifications support sending text, images, voice, files, and custom messages.

### Applicable scenarios{#match}

> **Official account**: The official account is used to broadcast and push notifications about official activities, operational strategies, version updates, and more within the application. It serves as the communication channel between the official entity and end users.

> **Operation Activity Notification**: Used to manage and organize temporary operational activity notifications, featuring capabilities such as tag-based notifications and delivering messages to online users, enabling precise message targeting.

> **Application-wide broadcast**: Sends messages to all users within the application. The content can be dynamically tailored based on user profiles. This is a powerful tool for refined operations in message notification.

### Scenario features{#sp}

> **High timeliness and large volume**: Operational activities often have strict timeliness requirements, and notification messages must be broadcast to all users as quickly as possible, demanding a high QPS (queries per second) from the system notification service API.

> **Flexible notifications**: To support refined operations, notification messages require precise targeting for "thousands of users individually," which places demands on the flexibility of the IM system notification platform.

### Related documents{#doc}

> **Basic documents**: [SDK Download](../../client/import.md), [Integration Example](../../client/quickstart/ios.md)

> **User management**: [User registration](../../server/user/register.md), [Update user information](../../server/user/updateuser.md), [Ban user](../../server/user/addbanuser.md), [Mute user](../../server/user/addblockuser.md)

> **System notification**: [System notification message](../../server/message/sysmsg.md), [Broad Cast message](../../server/message/broadcastmsg.md)

> **Conversation related**: [Conversation structure](../../client/sdkintro/conversation.md), [Get conversation list](../../client/sdkintro/conversation/get_all.md), [Pin a conversation](../../client/sdkintro/conversation/operator/settop.md), [Do not disturb](../../client/sdkintro/conversation/operator/disturb.md), [Get the total number of unreads](../../client/sdkintro/conversation/unread/get_total_unread.md), [Server gets conversation list](../../server/convers/qryconvers.md)

> **Status code**: [Android related](../../client/sdkintro/status_code/android.md), [iOS related](../../client/sdkintro/status_code/ios.md), [Web related](../../client/sdkintro/status_code/web.md), [REST API related](../../server/status.md)
