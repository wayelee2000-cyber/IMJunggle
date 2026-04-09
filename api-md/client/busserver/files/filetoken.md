---
title: 上传token
hide_title: true
sidebar_position: 1
---
### 功能说明{#intro}

获取文件上传token

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/file_cred

> **Content-Type**：`application/json`


### 请求参数{#param}
| 字段名 | 类型 | 说明 |
| --:|:----:|:------|
| file_type | int | 0:默认；1:图片；2: 语音；3: 视频；4: 文件；5: 日志； |
| ext | string | 文件扩展名 |

### 请求示例{#req_demo}
``` js
POST /jim/file_cred HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "file_type":0,
  "ext":"jpg"
}
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "oss_type":0,
    "qiniu_resp":{
      "domain":"xxxxx",
      "token":"xxxxxxx"
    },
    "pre_sign_resp":{
      "url":"xxxxxx",
      "obj_key":"xxx",
      "policy":"policy",
      "sign_version":"xxx",
      "credential":"xxxx",
      "date":"xxx",
      "signature":"xxxx"
    }
  }
}
```

### 响应参数
| 字段名 | 类型 | 说明 |
| --:|:----:|:------|
| oss_type | int | 0:默认；1:qiniu；2: aws s3；3: minio；4: oss； |


### 响应码

|响应码|说明||
|:--|:---|:--|