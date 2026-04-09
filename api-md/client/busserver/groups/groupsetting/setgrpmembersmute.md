---
title: 设置群成员禁言
hide_title: true
sidebar_position: 8
---
### 功能说明{#intro}

被禁言的群成员，将无法再发送群消息

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/management/setgrpmembersmute

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|member_ids|array|是|被禁言的群成员id列表||
|is_mute|int|是|0：解除禁言；1：禁言；||


### 请求示例{#req_demo}
``` js
POST /jim/groups/management/setgrpmembersmute HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id":"groupid1",
  "member_ids":["userid1","userid2"],
  "is_mute":1
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