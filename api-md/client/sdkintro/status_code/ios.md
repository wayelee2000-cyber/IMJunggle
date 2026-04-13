---
title: iOS
hide_title: true
sidebar_position: 2
---


```objectivec
typedef NS_ENUM(NSUInteger, JErrorCode) {
    JErrorCodeNone = 0,
    // AppKey not provided
    JErrorCodeAppKeyEmpty = 11001,
    // Token not provided
    JErrorCodeTokenEmpty = 11002,
    // AppKey does not exist
    JErrorCodeAppKeyInvalid = 11003,
    // Token is invalid
    JErrorCodeTokenIllegal = 11004,
    // Token unauthorized
    JErrorCodeTokenUnauthorized = 11005,
    // Token expired
    JErrorCodeTokenExpired = 11006,
    // App is banned
    JErrorCodeAppProhibited = 11009,
    // User is banned
    JErrorCodeUserProhibited = 11010,
    // User was kicked offline
    JErrorCodeUserKickedByOtherClient = 11011,
    // User logged out
    JErrorCodeUserLogOut = 11012,
    
    // Not a friend
    JErrorCodeNotFriend = 12009,
    // No permission to perform operation
    JErrorCodeNoOperationPermission = 12010,
    // Message does not exist
    JErrorCodeRemoteMessageNotExist = 12011,
    // Duplicate favorite message
    JErrorCodeAddDuplicateFavoriteMessage = 12012,
    
    // Group does not exist
    JErrorCodeGroupNotExist = 13001,
    // Not a group member
    JErrorCodeNotGroupMember = 13002,
    
    // Default chatroom error
    JErrorCodeChatroomUnknownError = 14000,
    // Not a chatroom member
    JErrorCodeNotChatroomMember = 14001,
    // Chatroom attributes limit exceeded (maximum 100)
    JErrorCodeChatroomAttributeCountExceed = 14002,
    // No permission to modify chatroom attribute (key not set by current user)
    JErrorCodeChatroomKeyUnauthorized = 14003,
    // Chatroom attribute does not exist
    JErrorCodeChatroomAttributeNotExist = 14004,
    // Chatroom does not exist
    JErrorCodeChatroomNotExist = 14005,
    // Chatroom has been destroyed
    JErrorCodeChatroomDestroyed = 14006,
    
    // Invalid parameter
    JErrorCodeInvalidParam = 21003,
    // Operation timed out
    JErrorCodeOperationTimeOut = 21004,
    // Connection unavailable
    JErrorCodeConnectionUnavailable = 21005,
    // Server configuration error
    JErrorCodeServerSetError = 21006,
    // Connection already exists
    JErrorCodeConnectionAlreadyExist = 21007,
    
    // Message does not exist
    JErrorCodeMessageNotExist = 22001,
    // Message already recalled
    JErrorCodeMessageAlreadyRecalled = 22002,
    // Message upload failed
    JErrorCodeMessageUploadError = 22003,
    // Recall message extras key and value are not NSString
    JErrorCodeRecallExtrasTypeNotString = 22004,
    // Downloaded message is not a media message
    JErrorCodeDownloadNotMediaMessage = 23001,
    // Message download failed
    JErrorCodeMessageDownloadError = 23006,
    // Message download already exists
    JErrorCodeDownloadAlreadyExist = 23008,
    // Message download canceled
    JErrorCodeDownloadCanceled = 23009,
    
    // Batch setting chatroom attributes failed
    JErrorCodeChatroomBatchSetAttributeFail = 24001,
    
    // Failed to join LiveKit room
    JErrorCodeJoinLiveKitFail = 25001
};
