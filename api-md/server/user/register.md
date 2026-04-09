---
title: 注册用户
hide_title: true
sidebar_position: 1
---

### 功能说明{#intro}

用户注册获得客户端 (Android、iOS、Web) 连接 IM Server 的 Token，Token 默认永久有效，应用管理设置 Token 有效期。
Token 获取成功后可在开发者业务服务端进行缓存，在用户登录时直接返回，可以减少网络请求次数

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../../api#api)/apigateway/users/register

> **Content-Type**：`application/json`

### 请求参数{#param}

| 参数            | 数据类型 | 是否必填     | 说明                            |        |
|-----------------|----------|----------|---------------------------------|------------|
| user_id         | string   | 是       | 用户 id，长度不超过 64 个字符       |            |
| nickname       | string   | 否       | 用户昵称，如果为空可能会导致客户端昵称显示异常     |            |
| user_portrait   | string   | 否       | 用户头像 URL，如果为空可能会导致客户端头像显示异常  |            |
| ext_fields     | map      | 否        | 用户信息的扩展字段，KV 形式 |  | 
| permit_convers| array     | 否        | 权限控制字段，限制该token仅能访问指定的会话，并限定每个会话最大能获取到的历史消息数量||


### 请求示例{#req_demo}

```js
POST /apigateway/users/register HTTP/1.1
appkey: appkey
signature: 2e639ae3600a4sdff61fb88b76f485b
nonce: nonce
timestamp: 1672568121910
Content-Type: application/json

{
  "user_id": "user1",
  "nickname": "nickname",
  "user_portrait": "https://portrait.example.com/avatar.png",
  "ext_fields":{
    "k1":"v1",
    "k2":"v2"
  },
  "permit_convers":[
    {
      "target_id":"groupid1",
      "channel_type":2,
      "max_his_msg_count":100
    }
  ]
}
```

### 响应参数{#res_param}

| 参数      | 数据类型 | 说明                                           |              |
|-----------|----------|---------------------------------------------|--------------|
| code      | int      | 状态码，详细请查看 [状态码](../status)说明       |              |
| user_id   | string   | 用户 id                                      |              |
| token     | string   | 认证 token，返回客户端连接使用                  |              |

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
      "user_id":"user1",
      "token":"tokenStr"
  }
}
```
