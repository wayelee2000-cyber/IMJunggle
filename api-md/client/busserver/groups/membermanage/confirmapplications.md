---
title: 审批邀请入群申请
hide_title: true
sidebar_position: 9
---
### 功能说明{#intro}

管理员审批邀请入群申请

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/groups/grpapplications/confirm

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|application_id|string|是|申请的id||
|is_agree|bool|是|是否同意||


### 请求示例{#req_demo}
``` js
POST /jim/groups/grpapplications/confirm HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "application_id":"xxxxxx",
  "is_agree":true
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