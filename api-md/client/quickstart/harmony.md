---
title: Harmony
hide_title: true
sidebar_position: 4
---

### Preparation{#pre}

1. Create an application in the `Developer server` to obtain your `AppKey` and `Secret`.

![](./assets/appkey_secret.png)

2. Call the server API to obtain the token yourself, or navigate to Developer server -> Select Application -> Development Tools -> API -> User Related, and call the user registration interface to get two test tokens.

![](./assets/token.png)

3. Follow the integration steps as outlined in the integration documentation.

### Workflow{#flow}

![](assets/flow.png)

### Sample code{#code}
```JavaScript
JuggleIm.instance.init("{serverUrl}", "{appkey}");
JuggleIm.instance.getConnectionManager().addConnectStatusListener((status, code) => {
	if (status === ConnStatus.Connected) {
		// Connection established
	}
});

JuggleIm.instance.getConnectionManager().connect("{token}");
```