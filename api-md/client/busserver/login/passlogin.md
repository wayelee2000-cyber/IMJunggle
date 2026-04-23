---
title: Account and password login
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Account and password login interface, used for **account/mobile phone number/email + password** login.

You can choose one from `account`, `phone`, or `email`.

### Request description{#req}

> **Request Authentication**: This interface does not require prior login and only needs to include the `appkey` request header; `Authorization` is not required. After a successful login, an `authorization` token will be returned for use with subsequent interfaces that require authentication.

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 times/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/login

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| account   | string    | No       | Account identifier, recommended to be a combination of letters and numbers, length **6~20** characters; Note: choose one of `account`, `phone`, or `email` |  |
| phone     | string    | No       | Mobile phone number |  |
| email     | string    | No       | Email address |  |
| password  | string    | Yes      | Account password (plain text) |  |

#### Password usage rules{#password_rule}

- The client sends the **plain text password** (e.g., `123456`), and the server applies `SHA1(password)` (hex lowercase) to compare it with the `LoginPass` stored in the database.
- **Do not** apply `md5` or `sha1` hashing to the `password` on the client side before sending it; otherwise, the server will hash it again with `SHA1()`, causing verification to fail.

Example: `SHA1("123456") = 7c4a8d09ca3762af61e59520943dc26494f8941b` (provided only to illustrate the server-side verification method; the request parameter should still be sent as plain text `123456`).

### Request Example{#req_demo}

```js
POST /jim/login HTTP/1.1
appkey: appkey
Content-Type: application/json

{
  "account": "username",
  "password": "123456"
}
```

You can also use `curl` to call:

```bash
curl -X POST 'https://$api/jim/login' \
-H 'appkey: <your appkey>' \
-H 'Content-Type: application/json' \
-d '{"account":"username","password":"123456"}'
```

JS `fetch` example:

```js
await fetch("https://$api/jim/login", {
  method: "POST",
  headers: {
    appkey: "<your appkey>",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    account: "username",
    password: "123456",
  }),
});
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "user_id": "userid1",
    "authorization": "xxxxxxxxx",
    "nickname": "user1",
    "avatar": "xxxxxxxx",
    "status": 0,
    "im_token": "xxxxxxxxx"
  }
}
```

### Common error codes{#errors}

| code  | Meaning                                | Typical trigger conditions                                                                 |
|:------|:-------------------------------------|:-------------------------------------------------------------------------------------------|
| 17001 | Missing appkey                        | The request header does not include `appkey` (verified by server-side authentication middleware) |
| 17002 | appkey does not exist/application does not exist | The application corresponding to `appkey` does not exist, or the server cannot obtain the IM SDK instance |
| 17003 | Illegal request parameter             | JSON parsing failed; or `password` is empty; or all of `account`, `phone`, and `email` are empty |
| 17012 | User does not exist                   | User not found for the provided `account`, `phone`, or `email`                             |
| 17013 | Password error                       | Server-side verification of `SHA1(password)` does not match the user's `LoginPass`        |
| 17004 | Internal service timeout/call failure | Server failed to call IM Server to register or exchange token (network issues, timeout, etc.) |
