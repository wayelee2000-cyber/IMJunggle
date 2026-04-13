---
title: Web
hide_title: true
sidebar_position: 3
---

# Web IM SDK Release Notes

## 1.9.6
  ** Release Date **: 2025-12-08
  - Feat: Added encryption hook support for msgContent
  - Fix: Added conditional checks in encryption callbacks
  - Fix: Ensured compatibility with non-empty functions in content
  - Fix: Adapted file download URLs provided by the server
  - Fix: Messages not stored no longer update the last message in the conversation list

## 1.9.5
  ** Release Date **: 2025-11-18
  - Feat: When passing wss in serverList, the provided protocol is prioritized
  - Feat: Added utility functions
  - Feat: Added encryption and decryption hooks before and after message sending
  - Feat: Added initialization parameters

## 1.9.4
  ** Release Date **: 2025-11-05
  - Feat: Added read timestamp in single chat history messages
  - Fix: Fixed inaccurate unread count after deleting a conversation and receiving new messages
  - Fix: Supported setting lifeTime field in merged forwarded messages

## 1.9.3
  ** Release Date **: 2025-10-31
  - Feat: Added support for timed deletion and self-destruct after reading
  - Fix: Exposed send and read times in read notifications
  - Fix: Added msgType to modified messages
  - Fix: Added conversation pinning timestamp

## 1.8.8
  ** Release Date **: 2025-10-23
  - Fix: Compatibility improvements for older Webkit kernels

## 1.8.7
  ** Release Date **: 2025-05-04
  - Fix: Adjusted heartbeat interval

## 1.8.6
  ** Release Date **: 2025-05-03
  - Fix: Optimized handling of network disconnections

## 1.8.2
  ** Release Date **: 2025-03-07
  - Feat: Added ability to retrieve unread message context
  - Feat: Added ability to retrieve historical message context

## 1.8.1
  ** Release Date **: 2025-02-26
  - Feat: Added sorting for pinned conversations
  - Feat: Reused existing time synchronization messages when rejoining chat rooms
  - Feat: Reactions now support user information
  - Feat: Added group nicknames
  - Fix: Removed key escaping in Reactions
  - Fix: Fixed garbled content when modifying messages online

## 1.7.25
  ** Release Date **: 2025-01-22
  - Feat: Support for replacing message type and content when sending messages
  - Feat: Added mentionType in conversation list
  - Feat: Adapted for Uniapp
  - Feat: Added message pinning and favorite features
  - Feat: Enabled custom triggers for pinning by the user

## 1.7.23
  ** Release Date **: 2024-12-20
  - Feat: S3 upload supports public-read access
  - Feat: Added streaming messages
  - Feat: Exposed enums
  - Feat: Added user types
  - Feat: Added translation interface
  - Feat: Added support for S3 storage

## 1.7.21
  ** Release Date **: 2024-12-14
  - Feat: Added exception handling for fetching single conversations
  - Feat: Exposed MediaType
  - Feat: Added room media types
  - Feat: Added 1v1 call end signaling

## 1.7.20
  ** Release Date **: 2024-12-03
  - Feat: Consolidated exception handling
  - Feat: Added subscription verification for connections

## 1.7.19
  ** Release Date **: 2024-12-02
  - Feat: Added RTC signaling
  - Fix: Reset connection status when disconnect is called during connection
  - Fix: Improved log uploading

## 1.7.16
  ** Release Date **: 2024-10-28
  - Fix: Corrected unread count
  - Feat: Added client-side message deduplication

## 1.7.15
  ** Release Date **: 2024-10-24
  - Feat: Added security domain validation
  - Feat: Tag event synchronization
  - Feat: Message modification
  - Feat: Message deletion event synchronization
  - Feat: Message recall command synchronization
  - Feat: Clear history message event synchronization
  - Feat: Read message synchronization events
  - Fix: Fixed timeout disconnection followed by timeout return in signaling

## 1.7.14
  ** Release Date **: 2024-10-24
  - Feat: Improved handling of message sending exceptions
  - Feat: Modified timing for binding user information when sending messages
  - Feat: Added support for passing count when joining chat rooms
  - Fix: Disabled connection check before sending messages

## 1.7.12
  ** Release Date **: 2024-10-21
  - Feat: Updated d.ts files
  - Feat: Web client no longer fetches offline messages on first connection
  - Fix: Fixed unreadIndex being 0 in conversations
  - Fix: Corrected descriptor files

## 1.7.9
  ** Release Date **: 2024-10-15
  - Feat: Packaged d.ts files
  - Feat: Added enum values
  - Feat: Packaged abstract configuration

## 1.7.5
  ** Release Date **: 2024-10-09
  - Feat: Tag multi-device synchronization
  - Feat: PC synchronization of Tag List
  - Feat: Compatibility with PC Tag
  - Feat: Conversation grouping
  - Feat: Tag List support
  - Feat: Conversation tags
  - Fix: Added tags in messages and conversations

## 1.7.4
  ** Release Date **: 2024-09-26
  - Fix: Corrected targetId retrieval location
  - Feat: Added message reactions

## 1.7.1
  ** Release Date **: 2024-09-14
  - Fix: Updated conversation mentions after message deletion
  - Fix: Updated conversation after self-deletion
  - Fix: Updated conversation list after recalling @ messages
  - Fix: Fixed video message thumbnails
  - Fix: Added push notification title and text

## 1.6.9
  ** Release Date **: 2024-09-12
  - Fix: Made pinning parameters compatible with arrays
  - Fix: Prioritized conversation list synchronization
  - Fix: Synchronized conversations before messages

## 1.6.6
  ** Release Date **: 2024-09-09
  - Feat: Added SDK version reporting in logs
  - Feat: Chat room compatibility with isSend flag
  - Feat: Retrieve first unread message in specified conversation
  - Feat: Extended search fields
  - Fix: Fixed mentionType handling
  - Fix: Removed @ messages from mention list after recall
  - Fix: Filtered local messages
  - Fix: Fixed retrieval of @ message lists
  - Fix: Merged interfaces
  - Fix: Handled error codes in message synchronization
  - Fix: Handled error codes in conversation synchronization

## 1.0.0
  ** Release Date **: 2024-03-15
  - Feat: Basic connection capabilities
  - Feat: Core message sending capabilities
  - Feat: Core conversation capabilities
  - Feat: Initial release