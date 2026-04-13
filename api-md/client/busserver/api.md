---
title: Interface description
hide_title: true
sidebar_position: 1
---

The App Server interface provided to the client supports business functions such as registration and login, group creation, and friend management.

> For communication security, the API authenticates via a custom public [header](#header).

### Format Description{#api}

```js
https://$api/$version/$command
```

| Parameter  | Name             | Description                                              |       |
|------------|------------------|----------------------------------------------------------|-------|
| $api       | Request domain   | The request address obtained after private cloud deployment |       |
| $version   | Version          | API version number                                       |       |
| $command   | Request command  | Specific interface endpoint                              |       |

### Request header{#header}

| Request header | Required | Description                              | Remarks |
|----------------|----------|----------------------------------------|---------|
| appkey         | Yes      | The unique identifier of the application |         |
| Authorization  | Yes      | Obtained from the response after successful login |         |

### Error code enumeration description {#error_code}

Description:

- The business interface typically returns HTTP 200. Success or failure is determined by the `code` in the response body.
- The table below lists error codes that may be returned by the external API. The meanings and "typical trigger conditions" are derived from the server source code logic (`apis`/`services`/`commons/errs`).

| code   | Constant name                     | Meaning                          | Typical trigger conditions (logically derived from source code)                                                                                  |
|--------|---------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | IMErrorCode_SUCCESS              | Success                         | Request processed successfully                                                                                                                   |
| 1      | IMErrorCode_PBILLEGAL            | PB parsing failed (internal error code) | Internal use only (no direct HTTP API path currently found)                                                                                      |
| 2      | IMErrorCode_DEFAULT              | Default error                   | General fallback error (no clear return path currently found; `APP_DEFAULT` used in more scenarios)                                              |
| 17000  | IMErrorCode_APP_DEFAULT          | Application-side default error  | General internal error code; common in DB access exceptions, QR code generation/query failures, etc.                                             |
| 17001  | IMErrorCode_APP_APPKEY_REQUIRED  | Missing appkey                  | The request header does not include `appkey` (`apis/validate.go`)                                                                                |
| 17002  | IMErrorCode_APP_NOT_EXISTED      | Application does not exist or is not configured | The application corresponding to `appkey` does not exist, or the server cannot obtain the IM SDK instance (e.g., login/SMS/email/QR code interfaces) |
| 17003  | IMErrorCode_APP_REQ_BODY_ILLEGAL | Illegal request body or parameters | JSON parsing failed; required fields missing; or parameter format is invalid (e.g., `account` does not match `^[a-zA-Z0-9]{6,20}$` during registration) |
| 17004  | IMErrorCode_APP_INTERNAL_TIMEOUT | Internal service timeout or call failure | The server failed or timed out when calling external dependencies such as the IM Server (e.g., registering with IM Server to obtain `im_token` during login) |
| 17005  |                                 |                                 |                                                                                                                                                  |
| 17006  | IMErrorCode_APP_CONTINUE         | Continue polling or incomplete  | QR code login: QR code is not confirmed (QR code status is Default in `login.go`)                                                                |
| 17007  | IMErrorCode_APP_QRCODE_EXPIRED   | QR code expired                 | The QR code was created more than 10 minutes ago (`login.go`)                                                                                    |
| 17008  | IMErrorCode_APP_SMS_SEND_FAILED  | Failed to send verification code | Failed to send SMS/email verification code, or failed to log the verification code record in the database (`services/smsservice.go`, `services/mailservice.go`) |
| 17009  | IMErrorCode_APP_SMS_CODE_EXPIRED | Verification code invalid or expired | Verification code does not exist, verification failed, or validity period exceeded 5 minutes (error code reused for SMS/email)                   |
| 17010  | IMErrorCode_APP_TRANS_NOTRANSENGINE | No translation engine configured | Translation interface called but no available translation engine configured (`services/transservice.go`)                                         |
| 17011  | IMErrorCode_APP_USER_EXISTED     | User already exists             | Conflict writing to user table during registration or account setup (e.g., account already taken)                                                |
| 17012  | IMErrorCode_APP_USER_NOT_EXIST   | User does not exist             | User not found by account/mobile/email/user ID (e.g., account password login, password change, QR code login confirmed but user missing)          |
| 17013  | IMErrorCode_APP_LOGIN_ERR_PASS   | Password error                 | Password verification failed (server compares `SHA1(password)` with database `LoginPass`)                                                        |
| 17014  | IMErrorCode_APP_PHONE_EXISTED    | Mobile number already exists    | Mobile number already in use when binding or setting the mobile number (`services/userservice.go`)                                               |
| 17015  | IMErrorCode_APP_EMAIL_EXIST      | Email already exists            | Email already in use when binding or setting the email (`services/userservice.go`)                                                               |
| 17016  | IMErrorCode_APP_Sensitive        | Contains sensitive content      | User nickname, group name, or other text contains sensitive words (`services/userservice.go`, `services/groupservice.go`)                        |
| 17100  | IMErrorCode_APP_FRIEND_DEFAULT   | Friend default error            | Reserved / no clear return path found                                                                                                           |
| 17101  | IMErrorCode_APP_FRIEND_APPLY_DECLINE | The other party refuses friend request | The other party's "Friend Verification Settings" is set to refuse friend requests (`services/friendservice.go`)                                  |
| 17102  | IMErrorCode_APP_FRIEND_APPLY_REPEATED | Repeated friend application    | Reserved / no clear return path found                                                                                                           |
| 17103  | IMErrorCode_APP_FRIEND_CONFIRM_EXPIRED | Friend confirmation expired    | Reserved / no clear return path found                                                                                                           |
| 17200  | IMErrorCode_APP_GROUP_DEFAULT    | Group default error             | General group error; e.g., disbanding group when not the owner or query failure (`services/groupservice.go`)                                     |
| 17201  | IMErrorCode_APP_GROUP_MEMBEREXISTED | Group member already exists    | Already a group member when applying to join the group (`services/groupservice.go`)                                                              |
| 17202  | IMErrorCode_APP_GROUP_NORIGHT    | No group operation permission   | Insufficient permissions (e.g., verification failure in message/group management logic; `services/messageservice.go`)                           |
| 17300  | IMErrorCode_APP_ASSISTANT_PROMPT_DBERROR | Assistant prompt word DB error | Reserved / no clear return path found                                                                                                           |
| 17401  | IMErrorCode_APP_FILE_NOOSS       | Object storage not configured   | File upload credentials: OSS/Minio/S3/Qiniu and other storage (`services/fileservice.go`)                                                        |
| 17402  | IMErrorCode_APP_FILE_SIGNERR     | Signing failed                  | File upload credentials: Failed to generate pre-signed URL or signing failed (`services/fileservice.go`)                                         |
| 17500  | IMErrorCode_APP_POST_DEFAULT     | Dynamic default error           | General error for dynamic/like functions (`posts/services/reactionservice.go`, etc.)                                                             |
| 17501  | IMErrorCode_APP_POST_NOTEXISTED  | Dynamic content does not exist  | Dynamic content missing when updating/commenting/reacting (`posts/services/postservice.go`, `postcommentservice.go`)                             |
| 17502  | IMErrorCode_APP_POST_NORIGHT     | No permission for dynamic operation | Not author or lacks permission when updating/commenting/reacting (`posts/services/postservice.go`, `postcommentservice.go`)                      |