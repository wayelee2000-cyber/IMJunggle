---
title: All members/label push
hide_title: true
sidebar_position: 5
---
### Function description{#intro}

Initiate a push to all members or users with specific labels.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request Rate Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/push

> **Content-Type**: `application/json`

### Request Example{#req_demo}
```js
POST /apigateway/push HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "from_user_id": "userid1",
    "condition": {
        "tags_and": ["tag1", "tag2"],
        "tags_or": ["tag1", "tag2"]
    },
    "msg_body": {
        "msg_type": "jg:text",
        "msg_content": "{\"content\":\"Hello World!\"}"
    },
    "notification": {
        "title": "title",
        "push_text": "Push details"
    }
}
```

### Request parameters {#param}

| Parameter     | Data type | Required | Description                                                                 |  |
|:--------------|:----------|:---------|:----------------------------------------------------------------------------|--|
| from_user_id  | string    | Yes      | The sender's user ID                                                        |  |
| condition     | object    | Yes      | Filtering criteria for target users                                         |  |
| tags_and     | array     | No       | Filter users who have all tags in this list; must be used with `tags_or`    |  |
| tags_or      | array     | No       | Filter users who have any tag in this list; must be used with `tags_and`    |  |
| msg_body      | object    | No       | The message payload to send; sends a system message to the target users. Use either this or the `notification` field |  |
| notification  | object    | No       | Sends a remote push notification to the target users. Use either this or the `msg_body` field |  |

### Response parameters {#res_param}

| Parameter | Data type | Description |
|:----------|:----------|:------------|

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "push_id": "xxxxx"
  }
}
```