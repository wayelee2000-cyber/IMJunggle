---
title: Disband group
hide_title: true
sidebar_position: 2
---

### Function description{#intro}

After the developer server disbands a group, it synchronizes the disbanded group's information with the IM server. If a dissolution notification message is to be sent, it must be sent before calling this interface, followed by the disbandment operation.

:::danger group disbandment notification
After a group is successfully disbanded, the IM server **will not** send a group disbandment notification. Developers must implement a custom notification message to be sent to the group.
:::

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/del

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters | Data type | Required | Description |  |
|:-----------|:----------|:---------|:------------|:--|
| group_id   | string    | yes      | Group ID    |  |

### Request Example{#req_demo}
```js
POST /apigateway/groups/del HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "groupid1"
}
```

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success"
}
```