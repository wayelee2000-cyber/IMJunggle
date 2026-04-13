---
title: Update user information
hide_title: true
sidebar_position: 9
---
### Function description{#intro}

The IM Server stores user information, which is used to display message sender details or session information. When user information changes, the updated data must be synchronized with the IM service by calling this interface.

:::danger User information synchronization timing
After user information is updated, the IM service **will not proactively notify** the client. Instead, when a session related to the current user generates a message, the IM service will automatically synchronize the latest user information to the client.
:::

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request rate limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/users/update

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter    | Data type | Required | Description             |  |
|:-------------|:----------|:---------|:------------------------|--|
| user_id     | string    | yes      | The user ID to be updated |  |
| nickname    | string    | no       | User nickname           |  |
| user_portrait | string  | no       | User avatar             |  |
| ext_fields  | map       | no       | List of extended fields |  |

### Request Example{#req_demo}

```js
POST /apigateway/users/update HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "userid1",
  "nickname": "user1",
  "user_portrait": "xxxxx",
  "ext_fields": {
    "field1": "aaa",
    "field2": "bbb"
  }
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```