---
title: ReactNative
hide_title: true
sidebar_position: 5
---

```ts
export enum ErrorCode {
  NONE = 0,
  // AppKey not provided
  APP_KEY_EMPTY = 11001,
  // Token not provided
  TOKEN_EMPTY = 11002,
  // AppKey does not exist
  APP_KEY_INVALID = 11003,
  // Token is invalid
  TOKEN_ILLEGAL = 11004,
  // Token unauthorized
  TOKEN_UNAUTHORIZED = 11005,
  // Token expired
  TOKEN_EXPIRED = 11006,
  // App is banned
  APP_PROHIBITED = 11009,
  // User is banned
  USER_PROHIBITED = 11010,
  // User was kicked offline
  USER_KICKED_BY_OTHER_CLIENT = 11011,
  // User logged out
  USER_LOG_OUT = 11012,

  // Not a friend
  NOT_FRIEND = 12009,
  // No permission to perform operation
  NO_OPERATION_PERMISSION = 12010,
  // Message does not exist
  REMOTE_MESSAGE_NOT_EXIST = 12011,
  // Duplicate favorite message
  ADD_DUPLICATE_FAVORITE_MESSAGE = 12012,

  // Group does not exist
  GROUP_NOT_EXIST = 13001,
  // Not a group member
  NOT_GROUP_MEMBER = 13002,

  // Chatroom default error
  CHATROOM_UNKNOWN_ERROR = 14000,
  // Not a chatroom member
  NOT_CHATROOM_MEMBER = 14001,
  // Chatroom attributes limit exceeded (maximum 100)
  CHATROOM_ATTRIBUTES_COUNT_EXCEED = 14002,
  // No permission to modify chatroom attribute (key not set by current user)
  CHATROOM_KEY_UNAUTHORIZED = 14003,
  // Chatroom attribute does not exist
  CHATROOM_ATTRIBUTE_NOT_EXIST = 14004,
  // Chatroom does not exist
  CHATROOM_NOT_EXIST = 14005,
  // Chatroom has been destroyed
  CHATROOM_DESTROYED = 14006,

  INVALID_PARAM = 21003,
  OPERATION_TIMEOUT = 21004,
  CONNECTION_UNAVAILABLE = 21005,
  SERVER_SET_ERROR = 21006,
  CONNECTION_ALREADY_EXIST = 21007,

  MESSAGE_NOT_EXIST = 22001,
  MESSAGE_ALREADY_RECALLED = 22002,
  MESSAGE_UPLOAD_ERROR = 22003,
  // Not a media message
  MESSAGE_DOWNLOAD_ERROR_NOT_MEDIA_MESSAGE = 23001,
  // Media message URL is empty
  MESSAGE_DOWNLOAD_ERROR_URL_EMPTY = 23002,
  // appKey or userid is null
  MESSAGE_DOWNLOAD_ERROR_APP_KEY_OR_USERID_EMPTY = 23004,
  MESSAGE_DOWNLOAD_ERROR_SAVE_PATH_EMPTY = 23005,
  MESSAGE_DOWNLOAD_ERROR = 23006,
  FILE_SAVED_FAILED = 23007,
  // Failed to batch set chatroom attributes
  CHATROOM_BATCH_SET_ATTRIBUTE_FAIL = 24001
}
```