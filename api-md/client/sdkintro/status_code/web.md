---
title: Web
hide_title: true
sidebar_position: 2
---

| Name                        | Code  | Description                      |
|-----------------------------|-------|---------------------------------|
| CONNECT_SUCCESS             | 0     | Connection successful           |
| CONNECT_ERROR               | 11000 | Default error                  |
| CONNECT_APPKEY_IS_REQUIRE    | 11001 | Appkey not provided            |
| CONNECT_TOKEN_NOT_EXISTS     | 11002 | Token not provided             |
| CONNECT_APPKEY_NOT_EXISTS    | 11003 | Appkey does not exist          |
| CONNECT_TOKEN_ILLEGAL        | 11004 | Invalid token                  |
| CONNECT_TOKEN_UNAUTHORIZED   | 11005 | Token unauthorized             |
| CONNECT_TOKEN_EXPIRE         | 11006 | Token expired                 |
| CONNECT_UNSUPPORT_PLATFORM   | 11008 | Unsupported platform type      |
| CONNECT_APP_BLOCKED          | 11009 | App is blocked                 |
| CONNECT_USER_BLOCKED         | 11010 | User is blocked                |
| CONNECT_USER_KICKED          | 11011 | User was kicked offline        |
| CONNECT_USER_LOGOUT          | 11012 | User logged out                |
| PB_ERROR                     | 11100 | Failed to parse input PB       |
| GROUP_NOT_EXISTS             | 13001 | Group does not exist           |
| ILLEGAL_PARAMS               | 25000 | Missing parameters, please check input |
| CONNECTION_EXISTS            | 25001 | Connection already exists      |
| CONNECTION_NOT_READY         | 25002 | Connection does not exist      |
| ILLEGAL_TYPE_PARAMS          | 25003 | Incorrect parameter type       |
| COMMAND_FAILED               | 25004 | Send timeout, connection error |
| UPLOAD_PLUGIN_ERROR          | 25005 | Upload component is empty      |
| UPLOAD_PLUGIN_NOTMATCH       | 25006 | Upload component does not match OSS storage |
| UPLOADING_FILE_ERROR         | 25007 | File upload failed, please retry |
| TRANSFER_MESSAGE_COUNT_EXCEED| 25008 | Maximum 20 messages allowed per batch forward |
| DATABASE_NOT_OPENED          | 25009 | Local database connection not established, please call connect method first |
| SDK_FUNC_NOT_DEFINED         | 25010 | Method not implemented, please verify SDK version |
| SEND_REFER_MESSAGE_ERROR     | 25011 | Referenced message must be a complete Message object |
| IM_SERVER_CONNECT_ERROR      | 25012 | IM service connection failed, please check device network availability |
| ILLEGAL_PARAMS_EMPTY         | 25013 | Parameters cannot be empty, please check input |
| REPREAT_CONNECTION           | 25014 | SDK is already connecting, no need to call connect again |
| MESSAGE_SEND_REPETITION      | 25015 | Duplicate message sending: same tid is already sending, no need to resend |
| MESSAGE_RECALL_SUCCESS       | 21200 | Message recalled successfully  |