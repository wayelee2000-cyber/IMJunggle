---
title: 接口说明
hide_title: true
sidebar_position: 1
---

IM RESTful API 提供给开发者 IM 业务的接口，客户端和服务端 API 能力对称，开发者可通过 API 接口实现`用户管理`、`群组管理` 等，详细请参考接口清单 [RESTful API](./apilist)

> 为了通信安全，API 通过自定义公共 [header](#header) 进行鉴权

### 格式说明{#api}

```js
https://$api/$version/$command
```
| 参数      | 名称         | 描述                                         |    |
|----------|--------------|---------------------------------------------|---|
| $api      | 请求域名       | 私有云部署服务后可获得请求地址  |  |
| $version  | 版本          | API 的版本号                                |   |
| $command  | 请求指令       | 具体的接口地址                               |   |


### 请求头{#header}

| 请求头      | 必填 | 描述                                 | 备注  |
|------------|------|--------------------------------------|------|
| appkey     | 是   | 应用的唯一标识 |      |
| nonce      | 是   | 随机数字，长度 8 位                   |      |
| timestamp  | 是   | 时间戳，精确到毫秒                   |      |
| signature  | 是   | sha1 计算的签名，向严格按照 [签名](#signature) 计算规则 |      |

### 签名计算{#signature}

签名计算，需要与 appkey 对应的 appsecret 创建应用获取

```js
// 顺序必须必须严格按：appsecret -> nonce -> timestamp
signature = SHA1({appsecret}{nonce}{timestamp})
```