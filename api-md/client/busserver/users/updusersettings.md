---
title: 更新用户设置
hide_title: true
sidebar_position: 3
---
### 功能说明{#intro}

更新用户的设置

### 请求说明{#req}

> **请求鉴权**：接口需要增加验证 Header，请查看 [鉴权说明](../../api#header)

> **请求类型**：`POST`

> **请求限频**：`100次/秒`

> **请求地址**：https://[请求域名](../api#api)/jim/users/updsettings

> **Content-Type**：`application/json`


### 请求参数{#param}

|参数|数据类型|是否必填|参数说明||
|:--|:------|:-----|:-------|:--|
|language|string|是|推送语言||
|friend_verify_type|int|是|好友验证。0：不需要验证，可直接被加好友；1：需要同意才能被加好友；2：拒绝任何人加我好友；||
|grp_verify_type|int|是|进群验证。0：不需要验证，任何人都可拉我入群；1：需要我同意，才能被拉入群；2：拒绝任何人拉我入群；||
|undisturb.switch|bool|否|是否开启全局免打扰，如果开启，rules中设置的时段期间，消息为免打扰状态，如果rules没设置时段，则全天免打扰||
|undisturb.timezone|string|否|时段对应的时区，为空时使用服务器部署所在地的默认时区||
|undisturb.rules.start|string|否|设置免打扰的开始时间，HHmm格式，24小时制||
|undisturb.rules.end|string|否|设置免打扰的结束时间，HHmm格式，24小时制||


### 请求示例{#req_demo}
``` js
POST /jim/users/updsettings HTTP/1.1
appkey: appkey
Authorization: xxxxxxxxxxxxxxxxxx
Content-Type: application/json

{
  "language":"zh_CN",
  "friend_verify_type":1,
  "grp_verify_type":1,
  "undisturb":{
    "switch":true,
    "timezone":"",
    "rules":[
      {
        "start":"1100",
        "end":"1500"
      }
    ]
  }
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