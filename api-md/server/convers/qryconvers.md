---
title: Query global session list
hide_title: true
sidebar_position: 5
---

### Function description{#intro}

Querying the session list functions similarly to the client's method of retrieving the session list. It is typically used by the server to view all session messages of a user in a supervisory role—first obtaining the sessions, then retrieving historical messages through those sessions.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/globalconvers/query

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters       | Data type | Required | Description                                                                                      |       |
|:-----------------|:----------|:---------|:------------------------------------------------------------------------------------------------|:------|
| start            | int       | No       | The start timestamp for querying sessions. For the initial query, this can be left blank. By default, results are returned in reverse chronological order from the current time. |       |
| count            | int       | No       | Number of items per page. Default is 100.                                                      |       |
| order            | int       | No       | Query order: 0 for descending (default), 1 for ascending.                                      |       |
| target_id        | string    | No       | Specify the user ID or group ID to filter the sessions.                                        |       |
| channel_type     | int       | No       | Specify the conversation type to query: 1 for single chat, 2 for group chat.                   |       |
| exclude_user_id  | array     | No       | User IDs to exclude from the results. For multiple users, use: `?exclude_user_id=userid1&exclude_user_id=userid2` |       |

### Request Example{#req_demo}
```js
GET /apigateway/globalconvers/query?start=xxx&count=20&user_id=xxx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "xxxx",
        "channel_type": 1,
        "user_id": "userid1",
        "target_id": "userid2",
        "time": 1713786448549
      },
      {
        "id": "yyyy",
        "channel_type": 2,
        "user_id": "userid1",
        "target_id": "groupid1",
        "time": 1713786449549
      }
    ]
  }
}
```