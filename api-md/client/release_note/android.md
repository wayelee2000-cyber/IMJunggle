---
title: Android
hide_title: true
sidebar_position: 1
---


# Android IM SDK Release Notes

## 1.8.39
  ** Release Date **: 2026-01-27
  - Feat: Fetch latest friend information from the server

## 1.8.38
  ** Release Date **: 2026-01-26
  - Feat: Friend remarks

## 1.8.37
  ** Release Date **: 2026-01-20
  - Feat: Stop video call preview
  - Feat: Added `getSenderDisplayName` and `getSenderPortrait` methods to Message
  - Feat: Added `getDisplayName` and `getPortrait` methods to ConversationInfo class
  - Fix: Added index to message table

## 1.8.35
  ** Release Date **: 2026-01-14
  - Feat: Physically delete all local messages before a specified time (to free local storage)
  - Fix: Added index to conversation table

## 1.8.34
  ** Release Date **: 2026-01-06
  - Feat: Fetch latest group information from the server
  - Feat: Fetch latest user information from the server
  - Feat: Batch fetch user information / batch fetch group information

## 1.8.32
  ** Release Date **: 2026-01-04
  - Fix: Set all messages with sending status to failed upon successful connection

## 1.8.28
  ** Release Date **: 2025-11-28
  - Feat: Added sub-channel functionality for conversations and messages
  - Feat: Moments feature
  - Feat: Heartbeat interval changed from 15s to 10s
  - Feat: Signaling timeout interval changed from 5s to 8s; triggers reconnection after three timeouts

## 1.8.27
  ** Release Date **: 2025-11-05
  - Feat: Expanded group message read information
  - Feat: Retrieve single chat message read time

## 1.8.26
  ** Release Date **: 2025-10-29
  - Feat: Support for public accounts
  - Fix: Added reverse message fetching logic to detect gaps before the first message when retrieving messages

## 1.8.25
  ** Release Date **: 2025-10-13
  - Feat: Audio and video calls support LiveKit
  - Fix: Only saved messages update the last message in the conversation
  - Fix: Handled SQLiteException

## 1.8.24
  ** Release Date **: 2025-09-26
  - Feat: Added UnknownMessage type

## 1.8.22
  ** Release Date **: 2025-09-18
  - Feat: Audio and video calls support Agora

## 1.8.21
  ** Release Date **: 2025-09-04
  - Feat: Added binding between audio/video calls and conversations; only one ongoing call per conversation is supported

## 1.8.20
  ** Release Date **: 2025-09-02
  - Feat: Added microphone mute callback
  - Feat: Added noise reduction interface

## 1.8.19
  ** Release Date **: 2025-08-22
  - Feat: Link encryption

## 1.8.18
  ** Release Date **: 2025-08-19
  - Feat: Added error codes
  - Fix: Updated user information when fetching favorite messages

## 1.8.17
  ** Release Date **: 2025-08-14
  - Feat: Message favorites
  - Feat: Update user information only if `updatedTime` is greater than the cached value

## 1.8.16
  ** Release Date **: 2025-08-05
  - Feat: Message pinning
  - Feat: Support passing extra information when initiating calls
  - Feat: Added callback for the first frame of video rendering
  - Feat: Message auto-destruction
  - Feat: Message self-destruct after reading
  - Feat: Added message pre-processing callback for custom encryption/decryption

## 1.8.15
  ** Release Date **: 2025-07-12
  - Feat: Added call audio volume callback

## 1.8.14
  ** Release Date **: 2025-07-02
  - Feat: Added video calls
  - Feat: Added multi-party calls

## 1.8.13
  ** Release Date **: 2025-06-26
  - Feat: Support revoking chatroom messages
  - Fix: Local path of media messages is not sent externally when sending media messages

## 1.8.12
  ** Release Date **: 2025-06-10
  - Feat: Added group member information cache
  - Fix: Rejoin chatrooms that failed to join upon successful connection

## 1.8.11
  ** Release Date **: 2025-04-10
  - Feat: Added JMessage event callbacks

## 1.8.10
  ** Release Date **: 2025-03-21
  - Feat: Support deleting and clearing messages for all participants in a conversation

## 1.8.9
  ** Release Date **: 2025-03-07
  - Feat: Optimized message table indexes

## 1.8.8
  ** Release Date **: 2025-02-27
  - Feat: Support conversation tags
  - Feat: Added slow SQL log tracking

## 1.8.7
  ** Release Date **: 2025-02-14
  - Feat: Support group member capabilities

## 1.8.6
  ** Release Date **: 2025-02-08
  - Feat: Added interface to get cached message replies
  - Feat: Support server-side modification of messages after sending

## 1.8.5
  ** Release Date **: 2025-01-16
  - Feat: Set push notification language
  - Feat: Added interface to get push notification language
  - Feat: Added interface to upload images
  - Feat: Support message modification
  - Feat: File upload supports S3
  - Feat: Support message reply functionality
  - Fix: Stop video preview when exiting calls
  - Fix: Disconnect calls when user is kicked from IM

## 1.8.2
  ** Release Date **: 2024-11-27
  - Feat: Added call end message

## 1.8.1
  ** Release Date **: 2024-11-14
  - Feat: Refactored connection logic; introduced state machine to handle reconnection during network and foreground/background switches

## 1.8.0
  ** Release Date **: 2024-11-21
  - Feat: Added audio and video call module JuggleCall, supporting JMessage audio and video

## 1.7.7
  ** Release Date **: 2024-10-31
  - Feat: Added parameter to join chatroom interface to auto-create chatroom if it does not exist
  - Feat: Use UUID for client-side unique message ID and deduplicate messages based on this ID
  - Fix: After message send timeout, update message status correctly upon receiving server ack

## 1.7.6
  ** Release Date **: 2024-10-29
  - Feat: Support fetching the last n messages before joining a chatroom
  - Feat: Support searching messages by conversation type
  - Feat: Search conversations by keywords in messages
  - Fix: Fixed missing messages issue when fetching the latest message list

## 1.7.5
  ** Release Date **: 2024-10-16
  - Feat: Set sorting rules for pinned conversations

## 1.7.3
  ** Release Date **: 2024-10-16
  - Feat: Added push channels (OPPO, HONOR, VIVO, Jiguang)
  - Feat: Integrated log uploading
  - Feat: Added message retrieval interface
  - Fix: Fixed exception caused by missing log files

## 1.7.2
  ** Release Date **: 2024-09-23
  - Feat: Trigger message push when app enters background
  - Fix: Fixed missing message callback issues

## 1.7.1
  ** Release Date **: 2024-09-19
  - Feat: Optimized message synchronization mechanism
  - Feat: Optimized chatroom message synchronization queue
  - Feat: Optimized reconnection interval from fixed 5 seconds to exponential backoff based on retry count
  - Feat: Added retry mechanism for conversation sync failures
  - Feat: Added retry mechanism for chatroom attribute failures
  - Feat: Added push data to messages

## 1.7.0
  ** Release Date **: 2024-09-14
  - Feat: Added interface to get unread message count by conversation type
  - Feat: Added interface to get the first unread message
  - Feat: Added interface to get current user ID
  - Feat: Added chatroom functionality

## 1.6.0
  ** Release Date **: 2024-08-23
  - Feat: Set conversation unread status