---
title: 删除帖子
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

删除帖子

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/posts/del

> **Content-Type**：`application/json`


### 请求参数{#param}


### 请求示例{#req_demo}
``` js
POST /jim/posts/del HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "post_ids":["xxxxxxxx","xxxxxx"]
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