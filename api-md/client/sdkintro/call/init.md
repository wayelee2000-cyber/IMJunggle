---
title: 初始化
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

初始化音视频通话需要导入即构的库文件。打开根目录下的 setting.gradle（Project 视图）。

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

在应用的 build.gradle 中，添加下面依赖。

```
api 'com.juggle.im:juggle:1.8.13.2'
api 'com.juggle.call.zego:juggle:1.8.13.2'
api 'im.zego:express-video:3.17.3'
```


使用即构的 appId 对音视频引擎进行初始化。

```java
JIM.getInstance().getCallManager().initZegoEngine(appId, context);
```

</TabItem>
<TabItem value="ios">

初始化音视频通话需要引入新的依赖，在 Podfile 中添加下面代码。

```
pod 'JZegoCall', '1.8.13.1'
```

使用即构的 appId 对音视频引擎进行初始化。

```objectivec
[JIM.shared.callManager initZegoEngineWith:xxx appSign:nil];
```



</TabItem>
<TabItem value="js">

使用即构的 AppId 对音视频引擎进行初始化和下载即构 [RTC SDK](https://doc-zh.zego.im/sdk-download/3209)

```javascript
import JuggleCall from "jugglecall-sdk";

let juggle = JIM.init({
  appkey: appkey,
});
let zg = new ZegoExpressEngine('即构的 AppId');
let client = juggle.install({ name: 'call' });
let juggleCall = JuggleCall.init({ client, engine: zg  });
```

</TabItem>

<TabItem value="flutter">

使用即构的 appId 和 appSign 对音视频引擎进行初始化。

```dart
Future<void> initZegoEngine(int appId, String appSign) async
```



</TabItem>

<TabItem value="reactnative">

使用即构的 appId 对音视频引擎进行初始化。

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

JuggleIMCall.initZegoEngine(appId);
```

使用 LiveKit 进行初始化。

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

JuggleIMCall.initLiveKitEngine();
```

使用声网 Agora 的 appId 对音视频引擎进行初始化。

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

JuggleIMCall.initAgoraEngine(appId);
```

</TabItem>

</Tabs>