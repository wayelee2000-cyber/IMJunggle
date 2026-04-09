---
title: 新增提示词
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

给AI助理新增提示词

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/assistants/prompts/add

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|prompts|string|是|提示词内容(prompt)||


### 请求示例{#req_demo}
``` js
POST /jim/assistants/prompts/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "prompts":"xxxxxxxxxxxx"
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
|17300|添加失败||