---
title: 申请添加好友
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

申请添加好友

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/friends/apply

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|friend_id|string|是|要添加好友的对方用户id||


### 请求示例{#req_demo}
``` js
POST /jim/friends/apply HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "friend_id":"userid1"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess"
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|
|17101|对方拒绝任何人加好友||
|17102|好友申请重复，或对方已经是你的好友||