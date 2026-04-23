---
title: Initialization
hide_title: true
sidebar_position: 0
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android' },
{ label: 'iOS', value: 'ios' },
{ label: 'JavaScript', value: 'js' },
{ label: 'Flutter', value: 'flutter' },
{ label: 'ReactNative', value: 'reactnative' }
]}
>
<TabItem value="android">

The SDK uses a singleton pattern and only needs to be initialized once globally.

**Parameter Description**

| Parameter | Type | Description | Minimum Version |
| --- | --- | --- | --- |
| appkey | String | The unique application identifier obtained when the app is created. Data is isolated between different appkeys, and multiple platforms can share the same appkey | 1.0.0 |

**Example Code**

```java
List<String> serverList = new ArrayList<>();
serverList.add("wss://ws.im.com"); // Replace with your deployed server URL
JIM.getInstance().setServerUrls(serverList);
JIM.getInstance().init(this, "appkey");
```

</TabItem>
<TabItem value="ios">

The SDK uses a singleton pattern and only needs to be initialized once globally.

**Parameter Description**

| Parameter | Type | Description | Minimum Version |
| --- | --- | --- | --- |
| appKey | NSString | The unique application identifier obtained when the app is created. Data is isolated between different appkeys, and multiple platforms can share the same appkey | 1.0.0 |

**Example Code**

```objectivec
[JIM.shared setServerUrls:@[@"wss://ws.im.com"]]; // Replace with your deployed server URL
[JIM.shared initWithAppKey:@"appkey"];
```

</TabItem>
<TabItem value="js">

The Web SDK uses a singleton pattern and only needs to be initialized once globally. APIs related to connection, conversations, and messages are all exposed on the instance object. For first-time integration and debugging, see **[Quickstart Integration](../quickstart/web/quickstart.md)** for a faster setup.

**Parameter Description**

| Parameter | Type | Required | Default | Description | Minimum Version |
| --- | --- | --- | --- | --- | --- |
| appkey | String | Yes | None | The unique application identifier obtained when the app is created. Data is isolated between different appkeys | 1.0.0 |
| serverList | Array | Yes | None | IM server addresses obtained after deployment (`Server Url`) | 1.0.0 |
| isSync | Boolean | No | true | Whether to synchronize offline messages after connection. Offline messages are retained for the last 24 hours. Synchronizing offline messages does not affect conversation state or unread counts | 1.0.0 |
| upload | Object | No | None | Upload component supporting Qiniu and Alibaba Cloud storage. See [Send File Message Example](../quickstart/web/send_file.md) for details | 1.0.0 |

**Example Code**

```js
let jim = JIM.init({
  appkey: 'Your AppKey',
  serverList: ['Your deployed Server Url']
});
```

</TabItem>

<TabItem value="flutter">

The SDK uses a singleton pattern and only needs to be initialized once globally. Before initialization, you must set the server address. The server address is the deployed IM Server URL and must be set by calling `setServers` before `init`.

**Parameter Description**

| Parameter | Type | Description | Minimum Version |
| --- | --- | --- | --- |
| appkey | String | The unique application identifier obtained when the app is created. Data is isolated between different appkeys, and multiple platforms can share the same appkey | 1.0.0 |

**Example Code**

```dart
// Step 1: Replace with your deployed IM Server address
await JuggleIm.instance.setServers(["wss://ws.im.com"]);

// Step 2: Initialize the SDK
await JuggleIm.instance.init('appkey');
```

</TabItem>

<TabItem value="reactnative">

The SDK uses a singleton pattern and only needs to be initialized once globally. Before initialization, you must set the server address.

**Parameter Description**

| Parameter | Type | Description | Minimum Version |
| --- | --- | --- | --- |
| appkey | String | The unique application identifier obtained when the app is created. Data is isolated between different appkeys, and multiple platforms can share the same appkey | 1.0.0 |
| serverList | String[] | List of server addresses | 1.0.0 |

**Example Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

// Step 1: Set the server address list
JuggleIM.setServerUrls(['wss://ws.im.com']);

// Step 2: Initialize the SDK
JuggleIM.init('your-appkey');
```

</TabItem>

</Tabs>
