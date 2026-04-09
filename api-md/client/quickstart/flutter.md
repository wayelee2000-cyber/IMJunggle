---
title: Flutter
hide_title: true
sidebar_position: 3
---

### 前期准备{#pre}

1、在 `开发者后台` 创建应用获取 `AppKey` 和 `Secret`。

![](./assets/appkey_secret.png)

2、自己调用服务端 API 获取 Token 或在开发者后台的 -> 选择应用-> 开发工具 -> API -> 用户相关中，调用用户注册接口，获取两个测试 Token。

![](./assets/token.png)

3、根据集成文档逐步集成。

### 使用流程{#flow}

![](assets/flow.png)

### 添加依赖{#install}

导入 SDK 之外，还需要额外添加下面依赖。

```sh
# pubspec.yaml
dependencies:
  juggle_im: 0.0.63
```

### 示例代码{#code}

```dart
await JuggleIm.instance.setServers(["wss://ws.im.com"]);// "wss://ws.im.com" 替换成部署好的 server url
await JuggleIm.instance.init("appkey");
JuggleIm.instance.onConnectionStatusChange = (int connectionStatus, int code, String extra){
  if(connectionStatus == SDKConnectionStatus.CONNECTED){
    // 连接成功
  }
  if(connectionStatus == SDKConnectionStatus.CONNECTING){
    // 连接中
  }
  if(connectionStatus == SDKConnectionStatus.DISCONNECTED){
    // 连接断开
  }
  if(connectionStatus == SDKConnectionStatus.FAILURE){
    // 连接失败 ，code 为错误码，extra 为错误信息
  }
};
await JuggleIm.instance.connect("token");
```

:::simple
连接失败时，`code` 详细说明请查看 [连接错误码](../../client/sdkintro/status_code/ios.mdx) 
:::