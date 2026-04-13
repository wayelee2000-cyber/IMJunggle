---
title: Android
hide_title: true
sidebar_position: 2
---

```java
public class JErrorCode {
    public static final int NONE = 0;
    // AppKey not provided
    public static final int APP_KEY_EMPTY = 11001;
    // Token not provided
    public static final int TOKEN_EMPTY = 11002;
    // AppKey does not exist
    public static final int APP_KEY_INVALID = 11003;
    // Token is invalid
    public static final int TOKEN_ILLEGAL = 11004;
    // Token is unauthorized
    public static final int TOKEN_UNAUTHORIZED = 11005;
    // Token has expired
    public static final int TOKEN_EXPIRED = 11006;
    // App is banned
    public static final int APP_PROHIBITED = 11009;
    // User is banned
    public static final int USER_PROHIBITED = 11010;
    // User was kicked offline by another client
    public static final int USER_KICKED_BY_OTHER_CLIENT = 11011;
    // User logged out
    public static final int USER_LOG_OUT = 11012;

    // Not a friend
    public static final int NOT_FRIEND = 12009;
    // No permission to perform operation
    public static final int NO_OPERATION_PERMISSION = 12010;
    // Message does not exist
    public static final int REMOTE_MESSAGE_NOT_EXIST = 12011;
    // Duplicate favorite message
    public static final int ADD_DUPLICATE_FAVORITE_MESSAGE = 12012;

    // Group does not exist
    public static final int GROUP_NOT_EXIST = 13001;
    // Not a group member
    public static final int NOT_GROUP_MEMBER = 13002;

    // Default chatroom error
    public static final int CHATROOM_UNKNOWN_ERROR = 14000;
    // Not a chatroom member
    public static final int NOT_CHATROOM_MEMBER = 14001;
    // Chatroom attributes limit exceeded (maximum 100)
    public static final int CHATROOM_ATTRIBUTES_COUNT_EXCEED = 14002;
    // No permission to modify chatroom attribute (key not set by current user)
    public static final int CHATROOM_KEY_UNAUTHORIZED = 14003;
    // Chatroom attribute does not exist
    public static final int CHATROOM_ATTRIBUTE_NOT_EXIST = 14004;
    // Chatroom does not exist
    public static final int CHATROOM_NOT_EXIST = 14005;
    // Chatroom has been destroyed
    public static final int CHATROOM_DESTROYED = 14006;

    public static final int INVALID_PARAM = 21003;
    public static final int OPERATION_TIMEOUT = 21004;
    public static final int CONNECTION_UNAVAILABLE = 21005;
    public static final int SERVER_SET_ERROR = 21006;
    public static final int CONNECTION_ALREADY_EXIST = 21007;

    public static final int MESSAGE_NOT_EXIST = 22001;
    public static final int MESSAGE_ALREADY_RECALLED = 22002;
    public static final int MESSAGE_UPLOAD_ERROR = 22003;
    // Not a media message
    public static final int MESSAGE_DOWNLOAD_ERROR_NOT_MEDIA_MESSAGE = 23001;
    // Media message URL is empty
    public static final int MESSAGE_DOWNLOAD_ERROR_URL_EMPTY = 23002;
    // appKey or userId is null
    public static final int MESSAGE_DOWNLOAD_ERROR_APP_KEY_OR_USERID_EMPTY = 23004;
    public static final int MESSAGE_DOWNLOAD_ERROR_SAVE_PATH_EMPTY = 23005;
    public static final int MESSAGE_DOWNLOAD_ERROR = 23006;
    public static final int FILE_SAVED_FAILED = 23007;
    // Failed to batch set chatroom attributes
    public static final int CHATROOM_BATCH_SET_ATTRIBUTE_FAIL = 24001;
}
```