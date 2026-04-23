---
title: Query global conversation list
hide_title: true
sidebar_position: 5
---

### Function description{#intro}

Querying the conversation list works similarly to the client-side method for retrieving conversations. It is typically used by the server in supervisory scenarios to inspect a user's conversations: first retrieve the conversation list, then fetch the historical messages for those conversations.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/globalconvers/query

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters       | Data type | Required | Description                                                                                      |       |
|:-----------------|:----------|:---------|:------------------------------------------------------------------------------------------------|:------|
| start            | int       | No       | The start timestamp for querying conversations. For the initial query, this can be left blank. By default, results are returned in reverse chronological order from the current time. |       |
| count            | int       | No       | Number of items per page. Default is 100.                                                      |       |
| order            | int       | No       | Query order: 0 for descending (default), 1 for ascending.                                      |       |
| target_id        | string    | No       | Specify the user ID or group ID to filter the conversations.                                        |       |
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

