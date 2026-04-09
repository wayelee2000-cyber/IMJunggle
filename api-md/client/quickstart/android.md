---
title: Android
hide_title: true
sidebar_position: 1
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

```
implementation 'org.java-websocket:Java-WebSocket:1.5.5'
implementation 'com.google.protobuf:protobuf-javalite:3.18.0'
implementation 'com.qiniu:qiniu-android-sdk:8.7.0'
```

### 示例代码{#code}
```java
List<String> serverList = new ArrayList<>();
serverList.add("wss://ws.im.com");// "wss://ws.im.com" 替换成部署好的 server url
JIM.getInstance().setServerUrls(serverList);
JIM.getInstance().init(this, "appkey");
JIM.getInstance().getConnectionManager().addConnectionStatusListener("mainActivity", new IConnectionManager.IConnectionStatusListener() {
		@Override
		public void onStatusChange(JIMConst.ConnectionStatus status, int code, String extra) {
		Log.i("TAG", "main activity onStatusChange status is " + status + " code is " + code);
		if (status == JIMConst.ConnectionStatus.CONNECTED) {
			
		}
	}
	@Override
	public void onDbOpen() {

	}
	@Override
	public void onDbClose() {

	}
});
JIM.getInstance().getConnectionManager().connect("token");
```