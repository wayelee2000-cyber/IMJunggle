---
title: 新人入群是否可查看历史消息
hide_title: true
sidebar_position: 4
---
### 功能说明{#intro}

新人入群是否可查看历史消息，默认不可查看

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/management/sethismsgvisible

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|group_his_msg_visible|int|是|0:不可查看；1：可查看；默认0||


### 请求示例{#req_demo}
``` js
POST /jim/groups/management/sethismsgvisible HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id":"groupid1",
  "group_his_msg_visible":1
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