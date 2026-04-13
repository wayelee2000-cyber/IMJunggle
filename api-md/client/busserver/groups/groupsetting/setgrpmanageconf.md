---
title: Set up group configuration
hide_title: true
sidebar_position: 9
---
### Function description{#intro}

Configure management settings for the group dimension.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api.md#header).

> **Request Type**: `POST`

> **Request rate limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api#api)/jim/groups/management/set

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter               | Data type | Required | Description                                                                                              |  |
|:------------------------|:----------|:---------|:-----------------------------------------------------------------------------------------------------|--|
| group_id                | string    | Yes      | Group ID                                                                                              |  |
| group_edit_msg_right    | int       | No       | Permission to edit group messages: <br>0: No permission; 1: Group owner; 2: Administrator; 3: Group owner + administrator; 4: Group member; 5: Group owner + group member; 6: Administrator + group member; 7: Group owner + administrator + group member |  |
| group_add_member_right  | int       | No       | Permission to add group members: <br>0: No permission; 1: Group owner; 2: Administrator; 3: Group owner + administrator; 4: Group member; 5: Group owner + group member; 6: Administrator + group member; 7: Group owner + administrator + group member |  |
| group_mention_all_right | int       | No       | Permission to mention all members: <br>0: No permission; 1: Group owner; 2: Administrator; 3: Group owner + administrator; 4: Group member; 5: Group owner + group member; 6: Administrator + group member; 7: Group owner + administrator + group member |  |
| group_top_msg_right     | int       | No       | Permission to pin messages: <br>0: No permission; 1: Group owner; 2: Administrator; 3: Group owner + administrator; 4: Group member; 5: Group owner + group member; 6: Administrator + group member; 7: Group owner + administrator + group member |  |
| group_send_msg_right    | int       | No       | Permission to send messages: <br>0: No permission; 1: Group owner; 2: Administrator; 3: Group owner + administrator; 4: Group member; 5: Group owner + group member; 6: Administrator + group member; 7: Group owner + administrator + group member |  |
| group_set_msg_life_right| int       | No       | Permission to set message lifespan: <br>0: No permission; 1: Group owner; 2: Administrator; 3: Group owner + administrator; 4: Group member; 5: Group owner + group member; 6: Administrator + group member; 7: Group owner + administrator + group member |  |

### Request Example{#req_demo}
``` js
POST /jim/groups/management/set HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id": "groupid1",
  "group_edit_msg_right": 7,
  "group_add_member_right": 7,
  "group_mention_all_right": 7,
  "group_top_msg_right": 7,
  "group_send_msg_right": 7,
  "group_set_msg_life_right": 7
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

| Response code | Description |  |
|:--------------|:------------|:--|