---
title: 查询全局会话列表
hide_title: true
sidebar_position: 5
---

### 功能说明{#intro}

查询会话列表，与客户端获取会话列表功能一致，通常用于服务端以超管的身份查看某个用户的全部会话消息，优先获取会话，再通过会话获取历史消息。

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`GET`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/globalconvers/query

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|start|int|是|查询会话的起始时间戳, 初次查询可以留空，默认从当前时间倒序查询||
|count|int|否|分页一页的数据条数，默认100||
|order|int|否|查询顺序，0：降序查询；1：增序查询；默认是0||
|target_id|string|否|指定要查询会话的用户id或群id||
|channel_type|int|否|指定要查询会话的类型，1:单聊；2:群聊；||
|exclude_user_id|array|否|填入要排除的用户id，多个时样例：?exclude_user_id=userid1&exclude_user_id=userid2||

### 请求示例{#req_demo}
```js
GET /apigateway/globalconvers/query?start=xxx&count=20&user_id=xxx HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "items":[
      {
        "id":"xxxx",
        "channel_type":1,
        "user_id":"userid1",
        "target_id":"userid2",
        "time":1713786448549
      },
      {
        "id":"yyyy",
        "channel_type":2,
        "user_id":"userid1",
        "target_id":"groupid1",
        "time":1713786449549,
      }
    ]
  }
}
```