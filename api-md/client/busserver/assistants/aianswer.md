---
title: 智能回复
hide_title: true
sidebar_position: 6
---
### 功能说明{#intro}

生成智能回复

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/assistants/answer

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|conver_id|string|是|会话id||
|channel_type|int|是|会话类型，1：单聊；2：群聊||
|prompt_id |string|否|提示词id||
|msgs|array|否|会话中最新的n条消息||


### 请求示例{#req_demo}
``` js
POST /jim/assistants/answer HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "conver_id":"xx",
  "channel_type":1,
  "prompt_id":"xxx",
  "msgs":[
    {
      "sender_id":"xx",
      "content":"xxxxx",
      "msg_time":1741234567893
    }
  ]
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "answer":"xxxxxxxxx"
  }
}
```

### 响应码

|响应码|说明||
|:--|:---|:--|