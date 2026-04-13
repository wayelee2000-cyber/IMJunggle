---
title: Processing friend requests
hide_title: true
sidebar_position: 2
---
### Function description{#intro}

Handles the processing of friend requests.

### Request description{#req}

> **Request Authentication**: This endpoint requires an authentication header. Please refer to [Authentication Instructions](../../api#header).

> **Request Type**: `POST`

> **Request frequency limit**: `100 requests/second`

> **Request URL**: https://[request domain name](../api.md#api)/jim/friends/confirm

> **Content-Type**: `application/json`


### Request parameters {#param}

| Parameter    | Data type | Required | Description                     |   |
|:-------------|:----------|:---------|:--------------------------------|---|
| sponsor_id   | string    | Yes      | The applicant’s user ID         |   |
| is_agree     | bool      | Yes      | Whether to agree or not. `false`: reject; `true`: accept |   |


### Request Example{#req_demo}
``` js
POST /jim/friends/confirm HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "sponsor_id": "userid1",
  "is_agree": true
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

| Response code | Description                  |   |
|:--------------|:-----------------------------|---|
| 17103         | Friend request has expired   |   |