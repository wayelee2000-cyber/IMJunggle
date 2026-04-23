---
title: Update user information
hide_title: true
sidebar_position: 9
---
### Function description{#intro}

The IM Server stores user information, which is used to display message sender details or session information. When user information changes, the updated data must be synchronized with the IM service by calling this interface.

<div style="margin: 1rem 0; padding: 1rem 1.25rem; border-left: 4px solid #e5484d; background: #fff1f2; border-radius: 0 16px 16px 0;">
<p style="margin: 0 0 0.75rem; font-size: 1rem; font-weight: 700; color: #b42318;">User information synchronization timing</p>
<p style="margin: 0; color: #344054;">After user information is updated, the IM service **will not proactively notify** the client. Instead, when a conversation related to the current user generates a message, the IM service will automatically synchronize the latest user information to the client.</p>
</div>
Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> **Request Type**: `POST`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/apigateway/users/update

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



