---
title: 设置入群验证类型
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

设置入群验证方式

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/management/setgrpverifytype

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|group_id|string|是|群组id||
|verify_type|int|是|0:不需要验证；1：需要管理员确认；2：拒绝新人入群；默认0||


### 请求示例{#req_demo}
``` js
POST /jim/groups/management/setgrpverifytype HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "group_id":"groupid1",
  "verify_type":1
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