---
title: Update group information
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

The IM Server stores group information, which is used to display session details. When group information changes, the updated data must be synchronized with the IM service by calling this interface.

<div style="margin: 1rem 0; padding: 1rem 1.25rem; border-left: 4px solid #e5484d; background: #fff1f2; border-radius: 0 16px 16px 0;">
<p style="margin: 0 0 0.75rem; font-size: 1rem; font-weight: 700; color: #b42318;">Group information synchronization timing</p>
<p style="margin: 0; color: #344054;">After the group information is updated, the IM service <strong>will not proactively notify</strong> the client. Instead, when new messages arrive in the current group, the IM service will automatically synchronize the latest group information to the client.</p>
</div>
Request description{#req}

> <strong>Request Authentication</strong>: This interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `POST`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/update

> <strong>Content-Type</strong>: `application/json`

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


