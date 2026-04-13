---
title: Query group members
hide_title: true
sidebar_position: 9
---

### Function description{#intro}

Query the information of a single group member to compare it with the group member information stored on the developer server. The group member information on the developer server takes precedence. After any changes are made to the group member information on the developer server, it must be synchronized to the IM server promptly.

### Request description{#req}

> **Request Authentication**: This interface requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `GET`

> **Request frequency limit**: `100 times/second`

> **Request URL**: https://[request domain name](../../api#api)/apigateway/groups/members/query

> **Content-Type**: `application/json`

### Request parameters {#param}

| Parameters | Data type | Required | Description       |      |
|:-----------|:----------|:---------|:------------------|:-----|
| group_id   | string    | Yes      | Group ID          |      |
| limit      | int       | No       | Paging parameter  |      |
| offset     | string    | No       | Paging offset     |      |

### Request Example{#req_demo}
```js
GET /apigateway/groups/members/query?group_id=group1&limit=50&offset=aabb HTTP/1.1
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
        "member_id": "member1",
        "is_mute": 0,
        "is_allow": 0,
        "grp_display_name": "Group Nickname",
        "ext_fields": {
          "k1": "v1",
          "k2": "v2"
        }
      },
      {
        "member_id": "member2",
        "is_mute": 0,
        "is_allow": 0
      }
    ],
    "offset": "aabbcc"
  }
}
```