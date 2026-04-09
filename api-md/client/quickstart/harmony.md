---
title: 鸿蒙Harmony
hide_title: true
sidebar_position: 4
---

### 前期准备{#pre}

1、在 `开发者后台` 创建应用获取 `AppKey` 和 `Secret`。

![](./assets/appkey_secret.png)

2、自己调用服务端 API 获取 Token 或在开发者后台的 -> 选择应用-> 开发工具 -> API -> 用户相关中，调用用户注册接口，获取两个测试 Token。

![](./assets/token.png)

3、根据集成文档逐步集成。

### 使用流程{#flow}

![](assets/flow.png)

### 示例代码{#code}
```JavaScript

JuggleIm.instance.init("{serverUrl}","{appkey}")
JuggleIm.instance.getConnectionManager().addConnectStatusListener((status,code)=>{
	if(status === ConnStatus.Connected){

	}
})

JuggleIm.instance.getConnectionManager().connect("{token}")
```