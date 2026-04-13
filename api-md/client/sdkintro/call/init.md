---
title: initialization
hide_title: true
sidebar_position: 0
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

To initialize audio and video calls, import the pre-built library file. Open `settings.gradle` (Project view) in the root directory.

```
  dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        maven { url 'https://storage.zego.im/maven' }
    }
  }
```

In your application's `build.gradle`, add the following dependencies:

```
api 'com.juggle.im:juggle:1.8.13.2'
api 'com.juggle.call.zego:juggle:1.8.13.2'
api 'im.zego:express-video:3.17.3'
```

Use your constructed `appId` to initialize the audio and video engine:

```java
JIM.getInstance().getCallManager().initZegoEngine(appId, context);
```

</TabItem>
<TabItem value="ios">

To initialize audio and video calls, add the following dependency to your Podfile:

```
pod 'JZegoCall', '1.8.13.1'
```

Use your constructed `appId` to initialize the audio and video engine:

```objectivec
[JIM.shared.callManager initZegoEngineWith:xxx appSign:nil];
```

</TabItem>
<TabItem value="js">

Use your constructed `appId` to initialize and download the audio and video engine [RTC SDK](https://doc-zh.zego.im/sdk-download/3209):

```javascript
import JuggleCall from "jugglecall-sdk";

let juggle = JIM.init({
  appkey: appkey,
});
let zg = new ZegoExpressEngine('Zego App ID');
let client = juggle.install({ name: 'call' });
let juggleCall = JuggleCall.init({ client, engine: zg });
```

</TabItem>

<TabItem value="flutter">

Use your constructed `appId` and `appSign` to initialize the audio and video engine:

```dart
Future<void> initZegoEngine(int appId, String appSign) async
```

</TabItem>

<TabItem value="reactnative">

Use your constructed `appId` to initialize the audio and video engine:

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

JuggleIMCall.initZegoEngine(appId);
```

To initialize with LiveKit, use:

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

JuggleIMCall.initLiveKitEngine();
```

To initialize the audio and video engine with Agora, use your Agora `appId`:

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

JuggleIMCall.initAgoraEngine(appId);
```

</TabItem>

</Tabs>