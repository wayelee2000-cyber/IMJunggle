---
title: iOS
hide_title: true
sidebar_position: 2
---

# iOS IM SDK Release Notes

## 1.8.39
  ** Release Date **: 2026-01-27
  - Feat: Fetch latest friend information from the server

## 1.8.38
  ** Release Date **: 2026-01-26
  - Feat: Friend remarks

## 1.8.37
  ** Release Date **: 2026-01-20
  - Feat: Stop video call preview

## 1.8.36
  ** Release Date **: 2026-01-20
  - Feat: Added `senderDisplayName` and `senderPortrait` properties to JMessage
  - Feat: Added `displayName` and `portrait` properties to JConversationInfo class
  - Fix: Added index to message table

## 1.8.35
  ** Release Date **: 2026-01-14
  - Feat: Physically delete all local messages before a specified time (to free local storage)
  - Fix: Added index to conversation table

## 1.8.34
  ** Release Date **: 2026-01-05
  - Feat: Fetch latest group information from the server

## 1.8.33
  ** Release Date **: 2026-01-05
  - Feat: Fetch latest user information from the server
  - Feat: Batch fetch user information / batch fetch group information

## 1.8.32
  ** Release Date **: 2026-01-04
  - Fix: Adapted to Xcode 26
  - Fix: On successful connection, set all messages with sending status to failed

## 1.8.31
  ** Release Date **: 2025-12-24
  - Fix: Failed to fetch official account conversations

## 1.8.30
  ** Release Date **: 2025-12-19
  - Feat: Optimized message table indexes
  - Fix: In some cases, message retrieval callback was triggered twice

## 1.8.29
  ** Release Date **: 2025-12-02
  - Feat: Added prefix to built-in SocketRocket source code
  - Fix: Incorrect media type setting in Moments

## 1.8.28
  ** Release Date **: 2025-11-28
  - Feat: Added sub-channel functionality to conversations and messages
  - Feat: Moments feature
  - Feat: Heartbeat interval changed from 15s to 10s
  - Feat: Signaling timeout interval changed from 5s to 8s; reconnect triggered after three timeouts

## 1.8.27
  ** Release Date **: 2025-11-05
  - Feat: Expanded group message read information
  - Feat: Updated Jigu version
  - Feat: Retrieve single chat message read time

## 1.8.25
  ** Release Date **: 2025-10-29
  - Feat: Optimized message table indexes
  - Feat: Support for official accounts
  - Fix: Added reverse message retrieval logic to detect message gaps before the first message

## 1.8.24
  ** Release Date **: 2025-09-26
  - Feat: Added UnknownMessage type

## 1.8.23
  ** Release Date **: 2025-09-25
  - Fix: Resolved Agora-related issues
  - Fix: Fixed duplicate image messages

## 1.8.22
  ** Release Date **: 2025-09-11
  - Feat: Audio and video calls support Agora

## 1.8.21
  ** Release Date **: 2025-09-04
  - Feat: Added binding between audio/video calls and conversations; only one ongoing call per conversation supported

## 1.8.20
  ** Release Date **: 2025-08-27
  - Feat: Added microphone mute callback
  - Feat: Added noise reduction interface

## 1.8.19
  ** Release Date **: 2025-08-20
  - Feat: Link encryption

## 1.8.18
  ** Release Date **: 2025-08-19
  - Feat: Added error codes
  - Fix: Updated user information when pulling favorite messages

## 1.8.17
  ** Release Date **: 2025-08-14
  - Feat: Message favorites
  - Feat: Update user information only if `updatedTime` is greater than cached value

## 1.8.16
  ** Release Date **: 2025-08-05
  - Feat: Message pinning
  - Feat: Support carrying extra information when initiating calls
  - Feat: Added callback for first frame of video rendering
  - Feat: Message auto-destruction
  - Feat: Message self-destruct after reading
  - Feat: Added message pre-processing callback for custom encryption/decryption

## 1.8.15
  ** Release Date **: 2025-07-11
  - Feat: Audio and video calls support LiveKit
  - Feat: Added call volume callback

## 1.8.13
  ** Release Date **: 2025-06-26
  - Feat: Support recall of chatroom messages

## 1.8.12
  ** Release Date **: 2025-06-06
  - Feat: Added user information caching
  - Fix: Do not send messages externally if WebSocket is not created

## 1.8.11
  ** Release Date **: 2025-04-10
  - Feat: Added Jigu event callbacks

## 1.8.10
  ** Release Date **: 2025-03-27
  - Feat: Support deleting and clearing messages for all participants in a conversation

## 1.8.9
  ** Release Date **: 2025-03-07
  - Feat: Support conversation tags
  - Feat: Refactored database version upgrade logic
  - Feat: Added slow SQL log tracking
  - Fix: Fixed issue where some resultSets were not properly closed

## 1.8.7
  ** Release Date **: 2025-02-13
  - Feat: Support group member capabilities

## 1.8.6
  ** Release Date **: 2025-02-08
  - Feat: Added interface to get cached message responses
  - Feat: Support server-side modification of messages after sending

## 1.8.5
  ** Release Date **: 2025-01-16
  - Feat: Added interface to get push language
  - Feat: Added interface to upload images
  - Feat: Support message modification
  - Feat: File upload supports S3
  - Feat: Support message response functionality
  - Fix: Stop video preview when exiting calls

## 1.8.3
  ** Release Date **: 2024-12-16
  - Feat: Set push language
  - Feat: Bind connection session in logs
  - Feat: Added video calls
  - Feat: Added group calls
  - Feat: Added VoIP push notifications
  - Fix: Disconnect call when user is kicked from IM

## 1.8.2
  ** Release Date **: 2024-11-27
  - Feat: Set speakerphone or earpiece output
  - Feat: Added call end message
  - Fix: Fixed cache cleanup issues on connection disconnect

## 1.8.1
  ** Release Date **: 2024-11-14
  - Feat: Refactored connection logic; introduced state machine to handle reconnection during network and foreground/background switches

## 1.8.0
  ** Release Date **: 2024-11-08
  - Feat: Added audio/video call module JuggleCall, supporting Jigu audio and video

## 1.7.7
  ** Release Date **: 2024-10-30
  - Feat: Added parameter to chatroom interface to auto-create chatroom if it does not exist
  - Feat: Use UUID for client-side unique message IDs and deduplicate based on them
  - Fix: After message send timeout, update message status correctly upon receiving server ack

## 1.7.6
  ** Release Date **: 2024-10-29
  - Feat: Support fetching the last n messages before joining a chatroom
  - Feat: Support searching messages by conversation type
  - Feat: Search conversations by keywords in messages

## 1.7.5
  ** Release Date **: 2024-10-22
  - Fix: Fixed missing messages when fetching latest message list
  - Fix: Fixed callback issues in extreme cases during message retrieval

## 1.7.4
  ** Release Date **: 2024-10-16
  - Feat: Set pinned conversation sorting rules
  - Feat: Removed deprecated interfaces

## 1.7.3
  ** Release Date **: 2024-10-15
  - Feat: Integrated log uploading
  - Feat: Added message retrieval interface
  - Fix: Fixed exceptions caused by missing log files

## 1.7.2
  ** Release Date **: 2024-09-27
  - Fix: Fixed missing callbacks for certain messages

## 1.7.1
  ** Release Date **: 2024-09-18
  - Feat: Optimized message synchronization mechanism
  - Feat: Optimized chatroom message synchronization queue
  - Feat: Optimized reconnection interval from fixed 5 seconds to exponential backoff based on retry count
  - Feat: Added retry mechanism for conversation synchronization failures
  - Feat: Added retry mechanism for chatroom attribute failures
  - Feat: Added push data to messages

## 1.7.0
  ** Release Date **: 2024-09-03
  - Feat: Set conversation unread status
  - Feat: Trigger message push when app enters background
  - Feat: Added chatroom functionality
  - Feat: Added interface to get unread message count by conversation type
  - Feat: Added interface to get the first unread message

## 1.3.0
  ** Release Date **: 2024-08-23
  - Feat: Message search
  - Feat: Unified message retrieval interface
  - Fix: Fixed reconnection logic triggering after user is kicked out