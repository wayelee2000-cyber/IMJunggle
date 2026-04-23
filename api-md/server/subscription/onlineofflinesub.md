---
title: Online and offline subscription
hide_title: true
sidebar_position: 1
---

### Request description{#req}

> **Push Authentication**: The interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Push Result**: When the business party receives the push, it must ensure the corresponding status code is 200 to confirm successful receipt.

> **Mechanism description**: The message CC will attempt to push 3 times, with a 100ms interval between each attempt. If all 3 attempts fail, the push is considered unsuccessful. The push mechanism uses Google's adaptive circuit breaker. If there are too many failures within the sliding time window, the circuit breaker will be triggered, temporarily suspending pushes from CC to the business.

### Parameter description{#params}

| Parameters     | Data type | Required | Parameter description                                                                                  |
| -------------- | --------- | -------- | ---------------------------------------------------------------------------------------------------- |
| type           | int       | yes      | 1 means online, 0 means offline                                                                       |
| user_id        | string    | yes      | User UID                                                                                            |
| device_id      | string    | yes      | Device code                                                                                         |
| platform       | string    | no       | Optional values: iOS, Android, iPad, web                                                            |
| client_ip      | string    | yes      | Client IP address                                                                                     |
| session_id     | string    | yes      | Unique identifier of this long connection                                                           |
| timestamp      | int       | yes      | Timestamp (in milliseconds)                                                                          |
| connection_ext | string    | yes      | Custom extension carried during connection                                                           |
| instance_id    | string    | no       | Used to identify an instance in web/PC multi-open scenarios; leave empty if no multi-open on mobile |

### Request Example{#req_demo}

```js
POST /onlinestatus/notification HTTP/1.1;
appkey: appkey;
signature: 2e639ae3600a4sdff61fb88b76f485b;
nonce: nonce;
timestamp: 1672568121910;
Content-Type: application/json;

{
  "event_type": "online", // Event type message, online
  "timestamp": 1713456000000, // Millisecond timestamp
  "payload": [
    {
      "type": 0, // 1 for online, 0 for offline
      "user_id": "userid1", // User UID
      "device_id": "1fsdf1", // Device code
      "platform": "web", // iOS, Android, iPad, web
      "client_ip": "192.116.1.1",
      "session_id": "123", // Unique identifier of this long connection
      "timestamp": 1713456000000,
      "connection_ext": "ext", // Custom extension carried during connection
      "instance_id": "instance_id" // For web/PC multi-open scenarios, identifies an instance. Note: No multi-open on mobile, so this field is empty.
    }
  ]
}
```