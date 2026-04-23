---
title: Group membership application list
hide_title: true
sidebar_position: 8
---
### Function description{#intro}

This endpoint provides a list of group membership applications, including users who have actively applied to join the group as well as those who have been invited to join.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `GET`

> **Request Frequency Limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../../api.md#api)/jim/groups/grpapplications

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter  | Data type | Required | Description                                                                                  |   |
|:-----------|:----------|:---------|:---------------------------------------------------------------------------------------------|---|
| group_id   | string    | Yes      | The ID of the group                                                                         |   |
| start      | int       | No       | The start timestamp for the query. When querying in reverse order, defaults to the current time; when querying forward, defaults to 0. |   |
| count      | int       | No       | Number of items per page. Default is 20; maximum is 50.                                    |   |
| order      | int       | No       | Query order: 0 for reverse order (default), 1 for forward order.                           |   |


### Request Example{#req_demo}
``` js
GET /jim/groups/grpapplications?group_id=group1&start=1734407505753&count=50 HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
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
        "apply_type": 1,   // 0: Invitation; 1: Active application
        "sponsor": {       // Information of the applicant when actively applying to join the group
          "user_id": "userid1"
        },
        "inviter": {       // Information of the inviter when inviting to the group
          "user_id": "userid2"
        },
        "recipient": {     // Information of the invitee when inviting to the group
          "user_id": "userid3"
        },
        "operator": {      // Information of the administrator handling the request
          "user_id": "userid4"
        },
        "status": 1,       // 0: Applying; 1: Application approved; 2: Application rejected; 3: Application expired; 10: Inviting; 11: Invitation accepted; 12: Invitation declined; 13: Invitation expired
        "apply_time": 1734407505000  // Application initiation timestamp
      }
    ]
  }
}
```
