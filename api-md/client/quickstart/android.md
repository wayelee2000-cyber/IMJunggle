---
title: Android
hide_title: true
sidebar_position: 1
---

### Preparation{#pre}

1. Create an application in the `Developer server` to obtain your `AppKey` and `Secret`.

![](./assets/appkey_secret.png)

2. Call the server API to obtain the token yourself, or use the Developer server: Select Application -> Development Tools -> API -> User Related, and call the user registration interface to obtain two test tokens.

![](./assets/token.png)

3. Follow the integration guide step by step.

### Workflow{#flow}

![](assets/flow.png)

### Add dependencies {#install}

In addition to importing the SDK, add the following dependencies:

```
implementation 'org.java-websocket:Java-WebSocket:1.5.5'
implementation 'com.google.protobuf:protobuf-javalite:3.18.0'
implementation 'com.qiniu:qiniu-android-sdk:8.7.0'
```

### Sample code{#code}
```java
List<String> serverList = new ArrayList<>();
serverList.add("wss://ws.im.com"); // Replace "wss://ws.im.com" with your deployed server URL
JIM.getInstance().setServerUrls(serverList);
JIM.getInstance().init(this, "appkey");
JIM.getInstance().getConnectionManager().addConnectionStatusListener("mainActivity", new IConnectionManager.IConnectionStatusListener() {
    @Override
    public void onStatusChange(JIMConst.ConnectionStatus status, int code, String extra) {
        Log.i("TAG", "main activity onStatusChange status is " + status + " code is " + code);
        if (status == JIMConst.ConnectionStatus.CONNECTED) {
            // Handle connection established
        }
    }
    @Override
    public void onDbOpen() {
        // Handle database open event
    }
    @Override
    public void onDbClose() {
        // Handle database close event
    }
});
JIM.getInstance().getConnectionManager().connect("token");
```
