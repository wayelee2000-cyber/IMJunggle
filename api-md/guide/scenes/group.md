---
title: Group chat
hide_title: true
sidebar_position: 2
---

### Scene introduction{#intro}

Group chat typically involves two or more people communicating within a group, interacting through text, files, images, and voice messages. A key characteristic of group chat interactive messages is that they are neither lost, duplicated, nor delivered out of order. When switching devices, message backups can be automatically synchronized to the new device. Features such as `read status`, `read proportion`, `unread count`, `@ message`, and `message operations` for each message in the group require strict consistency across all devices of a user. Message operations include `Withdraw`, `Message modification`, and `Reply message`.

### Applicable scenarios{#match}

> **Fans Group**: Fan groups typically rely on `KOL` social applications, where fans interact with anchors and are brought into a group for communication to manage a private domain.

> **Car Friends Group**: Car Friends Groups are multi-person chats organized by car forums or car manufacturers for owners of the same brand and model series. These groups mainly discuss automotive industry information, pros and cons of car models, and related topics.

> **Parent Group**: Parent groups are usually formed by school teachers and parents of students in a class to share students' learning progress or inform parents about the latest school policies.

> **Company Group**: Company groups generally include all employees and serve as communication channels to promptly share company policies, such as vacation arrangements and welfare updates.

> **Acquaintance Group Chat**: Acquaintance group chats coexist with private messages among friends. After users add friends, they can add them to a group for interaction and communication.

> **Multiple scenarios**: `Class Group`, `Department Group`, `After-sales Group`, `Takeaway Group`, `Support Group`, `Customer Group`, `Wisdom Group`, and more.

### Scenario features{#sp}

> **Group entry verification**: Users invited to join the group must actively confirm their participation when the group size is large.

> **Maximum number of participants**: The group size can be configured based on the scenario, ranging from fewer than 10 members to up to 10,000 members.

> **Group information updates**: Notifications for group nickname changes, real-time updates of online members, and automatic synchronization of offline users when they come online.

> **Special behavior notifications**: Member bans are synchronized promptly, with immediate notifications of ban status.

> **Group "Functional Sugar"**: Features include viewing group message read status, group sending assistant, single and two-way message deletion, scheduled message clearing, and message deletion by time.

> **Message binding group information**: Messages contain group information to facilitate client display and reduce integration complexity.

### Related documents{#doc}

> **Basic documents**: [SDK Download](../../client/import.md), [Integration Example](../../client/quickstart/ios.md)

> **User management**: [User registration](../../server/user/register.md), [Update user information](../../server/user/updateuser.md), [Ban user](../../server/user/addbanuser.md), [Mute user](../../server/user/addblockuser.md)

> **Group related**: [Create group](../../server/group/groupcreate.md), [Dissolve group](../../server/group/groupdissolve.md), [Update group information](../../server/group/updategroup.md), [Add group members](../../server/group/groupaddmember.md), [Mute group](../../server/group/groupmute.md), [Query group members](../../server/group/qrygroupmember.md)

> **Message related**: [Message structure](../../client/sdkintro/msg/message.md), [Send message](../../client/sdkintro/message/msg_send/send.md), [Receive message](../../client/sdkintro/watcher/message.md), [Get historical messages](../../client/sdkintro/message/histories/get_all.md), [Clear historical messages](../../client/sdkintro/message/histories/clear.md), [Message recall](../../client/sdkintro/message/operator/recall.md), [Message read](../../client/sdkintro/message/operator/read.md), [REST API send message](../../server/message/groupmsg.md)

> **Conversation related**: [Conversation structure](../../client/sdkintro/conversation.md), [Get conversation list](../../client/sdkintro/conversation/get_all.md), [Pin a conversation](../../client/sdkintro/conversation/operator/settop.md), [Do not disturb](../../client/sdkintro/conversation/operator/disturb.md), [Get the total number of unreads](../../client/sdkintro/conversation/unread/get_total_unread.md), [Server gets conversation list](../../server/convers/qryconvers.md)

> **Status code**: [Android related](../../client/sdkintro/status_code/android.md), [iOS related](../../client/sdkintro/status_code/ios.md), [Web related](../../client/sdkintro/status_code/web.md), [REST API related](../../server/status.md)
