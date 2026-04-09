---
title: 添加好友备注
hide_title: true
sidebar_position: 6
---

### 功能说明{#intro}

添加好友备注

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/friends/setdisplayname

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|friend_id|string|是|好友的用户id||
|friend_display_name|string|是|好友备注||


### 请求示例{#req_demo}
``` js
POST /jim/friends/setdisplayname HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "friend_id":"friend1",
  "friend_display_name":"displayname"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```