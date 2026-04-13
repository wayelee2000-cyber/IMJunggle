---
title: Interface description
hide_title: true
sidebar_position: 1
---

The IM RESTful API provides developers with interfaces for IM business operations. The client and server API capabilities are symmetrical. Developers can implement features such as `user management` and `group management` through these API interfaces. For more details, please refer to the interface list in [RESTful API](./apilist).

> For communication security, the API authenticates requests via a custom public [header](#header).

### Format Description{#api}

```js
https://$api/$version/$command
```
| Parameter  | Name             | Description                                         |       |
|------------|------------------|-----------------------------------------------------|-------|
| $api       | Request domain   | The request address, which can be obtained after private cloud deployment |       |
| $version   | Version          | API version number                                  |       |
| $command   | Request command  | Specific interface endpoint                         |       |


### Request header{#header}

| Request header | Required | Description                                         | Remarks |
|----------------|----------|-----------------------------------------------------|---------|
| appkey         | Yes      | The unique identifier of the application            |         |
| nonce          | Yes      | Random number, 8 characters long                     |         |
| timestamp      | Yes      | Timestamp, accurate to milliseconds                  |         |
| signature      | Yes      | Signature calculated using SHA1, strictly following the [signature](#signature) calculation rules |         |

### Signature calculation {#signature}

To calculate the signature, the appsecret corresponding to the appkey must be created and obtained by the application.

```js
// The order must be strictly followed: appsecret -> nonce -> timestamp
signature = SHA1({appsecret}{nonce}{timestamp})
```