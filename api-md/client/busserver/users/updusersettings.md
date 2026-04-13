---
title: Update user settings
hide_title: true
sidebar_position: 3
---
### Function description{#intro}

Update a user's settings.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/users/updsettings

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter           | Data type | Required | Description                                                                                          |   |
|:--------------------|:----------|:---------|:-------------------------------------------------------------------------------------------------|:--|
| language            | string    | Yes      | Push language                                                                                      |   |
| friend_verify_type  | int       | Yes      | Friend verification mode. 0: No verification required; can be added as a friend directly. 1: Requires approval to be added as a friend. 2: Refuse all friend requests. |   |
| grp_verify_type     | int       | Yes      | Group join verification mode. 0: No verification required; anyone can add me to a group. 1: Requires my approval before being added to a group. 2: Refuse all group join requests. |   |
| undisturb.switch    | bool      | No       | Whether to enable global Do Not Disturb (DND). If enabled, messages will be silenced during the time period specified in the rules. If no time period is set, DND applies all day. |   |
| undisturb.timezone  | string    | No       | Time zone for the DND period. If empty, the server's default deployment time zone is used.        |   |
| undisturb.rules.start | string  | No       | Start time of DND in HHmm format (24-hour clock).                                                |   |
| undisturb.rules.end  | string   | No       | End time of DND in HHmm format (24-hour clock).                                                  |   |


### Request Example{#req_demo}
``` js
POST /jim/users/updsettings HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "language": "zh_CN",
  "friend_verify_type": 1,
  "grp_verify_type": 1,
  "undisturb": {
    "switch": true,
    "timezone": "",
    "rules": [
      {
        "start": "1100",
        "end": "1500"
      }
    ]
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

### Response code

| Response code | Description |   |
|:--------------|:------------|:--|