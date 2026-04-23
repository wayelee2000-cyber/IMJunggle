---
title: Query group information
hide_title: true
sidebar_position: 4
---

### Function description{#intro}

Query the information of a single group to compare it with the group information used on the developer server. The group information on the developer server takes precedence. After any changes are made to the group information on the developer server, it must be synchronized to the IM server promptly.

Request description{#req}

> <strong>Request Authentication</strong>: This interface requires an authentication header. Please refer to [Authentication Instructions](../api.md#header).

> <strong>Request Type</strong>: `GET`

> <strong>Request Frequency Limit</strong>: `100 requests/second`

> <strong>Request URL</strong>: https://[request domain name](../api.md#api)/apigateway/groups/info

> <strong>Content-Type</strong>: `application/json`

### Request parameters {#param}

| Parameter  | Data type | Required | Description   |  |
|:-----------|:----------|:---------|:--------------|:--|
| group_id   | string    | yes      | Group ID      |  |

### Request Example{#req_demo}
```js
GET /apigateway/groups/info?group_id=group1 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```

### Response parameters {#res_param}

| Parameter   | Data type | Description                  |  |
|:------------|:----------|:-----------------------------|:--|
| group_id    | string    | Group ID                    |  |
| group_name  | string    | Group nickname              |  |
| is_mute    | int       | 0: not muted; 1: muted       |  |
| ext_fields  | map       | Group extension fields      |  |

### Response example{#res_demo}

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "group_id": "group1",
    "group_name": "group1",
    "is_mute": 0,
    "ext_fields": {
      "field1": "aaa",
      "field2": "bbb"
    }
  }
}
```


