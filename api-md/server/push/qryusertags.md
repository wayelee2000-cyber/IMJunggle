---
title: 清除用户标签
hide_title: true
sidebar_position: 4
---
### 功能说明{#intro}

删除用户标签

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/usertags/query

> **Content-Type**：`application/json`

### 请求示例{#req_demo}
```js
GET /apigateway/usertags/quer?user_ids=userid1,userid2 HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

```


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|user_id|array|是|要查询用户标签的用户id，多个时：?user_id=userid1&user_id=userid2||

### 响应参数{#res_param}

|参数|数据类型|参数说明||
|:--|:------|:-----|:-------|


### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "user_tags":[
      {
        "user_id":"userid1",
        "tags":["aa","bb"]
      },
      {
        "user_id":"userid2",
        "tags":["aa","bb"]
      }
    ]
  }
}
```

