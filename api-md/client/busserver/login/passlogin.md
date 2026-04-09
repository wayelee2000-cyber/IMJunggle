---
title: 账户密码登录
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

账户密码登录接口，用于 **账号/手机号/邮箱 + 密码** 登录。

其中 `account`、`phone`、`email` 三选一即可。

### 请求说明{#req}

> **请求鉴权**：该接口为免登录接口，仅需携带 `appkey` 请求头；`Authorization` 不需要。登录成功后会在返回值中下发 `authorization`，供后续需要鉴权的接口使用。

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/login

> **Content-Type**：`application/json`

### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|account|string|否|账号，建议字母+数字组合，长度 **6~20** 位；注：`account`、`phone`、`email` 三选一即可||
|phone|string|否|手机号||
|email|string|否|邮箱地址||
|password|string|是|账号密码（明文）||

#### password 使用规则{#password_rule}

- 客户端传 **明文密码**（例如 `123456`），服务端会执行 `SHA1(password)`（hex 小写）后与数据库中的 `LoginPass` 比对。
- **不要**在客户端先对 `password` 做 `md5/sha1` 再传，否则服务端会再次 `SHA1()`，导致校验不通过。

示例：`SHA1("123456") = 7c4a8d09ca3762af61e59520943dc26494f8941b`（仅用于理解服务端校验方式；请求参数仍传明文 `123456`）。

### 请求示例{#req_demo}

```js
POST /jim/login HTTP/1.1
appkey: appkey
Content-Type: application/json

{
  "account":"username",
  "password":"123456"
}
```

也可以使用 `curl` 调用：

```bash
curl -X POST 'https://$api/jim/login' \
  -H 'appkey: <你的appkey>' \
  -H 'Content-Type: application/json' \
  -d '{"account":"username","password":"123456"}'
```

JS `fetch` 示例：

```js
await fetch("https://$api/jim/login", {
  method: "POST",
  headers: {
    appkey: "<你的appkey>",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    account: "username",
    password: "123456",
  }),
});
```

### 响应示例{#res_demo}

```json
{
  "code":0,
  "msg":"sucess",
  "data":{
    "user_id":"userid1",
    "authorization":"xxxxxxxxx",
    "nickname":"user1",
    "avatar":"xxxxxxxx",
    "status":0,
    "im_token":"xxxxxxxxx"
  }
}
```

### 常见错误码{#errors}

|code|含义|典型触发条件|
|:--|:--|:--|
|17001|缺少 appkey|请求头未携带 `appkey`（在服务端鉴权中间件校验）|
|17002|appkey 不存在/应用不存在|`appkey` 对应应用不存在，或服务端无法获取 IM SDK 实例|
|17003|请求参数非法|JSON 解析失败；或 `password` 为空；或 `account/phone/email` 同时为空|
|17012|用户不存在|按 `account/phone/email` 未找到用户|
|17013|密码错误|服务端校验 `SHA1(password)` 与用户 `LoginPass` 不一致|
|17004|内部服务超时/调用失败|服务端调用 IM Server 注册/换取 token 失败（网络/超时等）|

