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

### Features of the plan{#sp}

> **Group entry verification**: Users invited to join the group must actively confirm their participation when the group size is large.

> **Maximum number of participants**: The group size can be configured based on the scenario, ranging from fewer than 10 members to up to 10,000 members.

> **Group information updates**: Notifications for group nickname changes, real-time updates of online members, and automatic synchronization of offline users when they come online.

> **Special behavior notifications**: Member bans are synchronized promptly, with immediate notifications of ban status.

> **Group "Functional Sugar"**: Features include viewing group message read status, group sending assistant, single and two-way message deletion, scheduled message clearing, and message deletion by time.

> **Message binding group information**: Messages contain group information to facilitate client display and reduce integration complexity.

### Related documents{#doc}

>**Basic Documents**: [SDK Download](../../../client/import), [Integration Example](../../../client/quickstart/ios)

>**User Management**: [User Registration](../../../server/user/register), [Update Information](../../../server/user/updateuser), [User Ban](../../../server/user/addbanuser), [Ban User](../../../server/user/addblockuser)

>**Group related**: [Create group](../../../server/group/groupcreate), [Dissolve group](../../../server/group/groupdissolve), [Update group information](../../../server/group/updategroup), [Add group members](../../../server/group/groupaddmember), [Group mute](../../../server/group/groupmute), [Query group members](../../../server/group/qrygroupmember)

>**Message related**: [Message structure](../../../client/sdkintro/msg/message), [Send message](../../../client/sdkintro/message/msg_send/send), [Receive message](../../../client/sdkintro/watcher/message), [Get historical messages](../../../client/sdkintro/message/histories/get_all), [Clear historical messages](../../../client/sdkintro/message/histories/clear), [Message recall](../../../client/sdkintro/message/operator/recall), [Message read](../../../client/sdkintro/message/operator/read), [REST API send message](../../../server/message/privatemsg)

>**Session related**: [Session structure](../../../client/sdkintro/conversation), [Get session list](../../../client/sdkintro/conversation/get_all), [Session top](../../../client/sdkintro/conversation/settop), [Do not disturb](../../../client/sdkintro/conversation/disturb), [Get the total number of unreads](../../../client/sdkintro/conversation/get_total_unread), [Server gets the conversation list](../../../server/convers/qryconvers)

>**Status code**: [Android related](../../../client/sdkintro/status_code/android), [iOS related](../../../client/sdkintro/status_code/ios), [Web related](../../../client/sdkintro/status_code/web), [REST API Related](../../../server/status)