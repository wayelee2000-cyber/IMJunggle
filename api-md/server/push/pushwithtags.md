---
title: 全员/标签推送
hide_title: true
sidebar_position: 5
---
### 功能说明{#intro}

发起全员/标签推送

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/push

> **Content-Type**：`application/json`

### 请求示例{#req_demo}
```js
POST /apigateway/push HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
    "from_user_id":"userid1",
    "condition":{
        "tags_and":["tag1","tag2"],
        "tags_or":["tag1","tag2"]
    },
    "msg_body":{
        "msg_type":"jg:text",
        "msg_content":"{\"content\":\"Hello World!\"}"
    },
    "notification":{
        "title":"title",
        "push_text":"推送详情内容"
    }
}
```


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|from_user_id|string|是|发送者的用户id||
|condition|object|是|目标用户的筛选条件||
|tags_and|array|否|筛选同时拥有列表中标签的用户，与tags_or二选一||
|tags_or|array|否|筛选拥有列表中任一标签的用户，与tags_and二选一||
|msg_body|object|否|要发送的实体消息，这里会给目标用户发送一条实体的系统消息，与notification字段二选一||
|notification|object|否|仅向目标用户发送远程推送，与msg_body二选一||

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|


### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "push_id":"xxxxx"
  }
}
```

