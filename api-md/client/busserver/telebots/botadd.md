---
title: 添加Bot
hide_title: true
sidebar_position: 2
---
### 功能说明{#intro}

添加 Telegram Bot

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/telegrambots/add

> **Content-Type**：`application/json`


### 请求参数{#param}


### 请求示例{#req_demo}
``` js
POST /jim/telegrambots/add HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "bot_name":"xxxxxxxxxxxx",
  "bot_token":"xxxx"
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