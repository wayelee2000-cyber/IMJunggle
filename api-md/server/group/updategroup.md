---
title: Update group information
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

The IM Server stores group information, which is used to display session details. When group information changes, the updated data must be synchronized with the IM service by calling this interface.

:::danger Group information synchronization timing
After the group information is updated, the IM service **will not proactively notify** the client. Instead, when new messages arrive in the current group, the IM service will automatically synchronize the latest group information to the client.
:::


### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/update

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameter     | Data type | Required | Description               |   |
|:--------------|:----------|:---------|:--------------------------|---|
| group_id      | string    | Yes      | The ID of the group to update |   |
| group_name    | string    | No       | Group nickname            |   |
| group_portrait| string    | No       | Group avatar              |   |
| ext_fields    | map       | No       | List of extended fields   |   |


### Request Example{#req_demo}
```js
POST /apigateway/groups/update HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "group_id": "group1",
  "group_name": "group1",
  "group_portrait": "xxx",
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