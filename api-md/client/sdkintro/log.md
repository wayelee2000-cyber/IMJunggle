---
title: 日志相关
hide_title: true
sidebar_position: 11
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

By default, the SDK does not output logs to ADB. If you need to enable logging during development, you can pass the following parameter when initializing the SDK.

```java
JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
                .setJLogConfig(new JLogConfig.Builder(getApplicationContext()).setLogConsoleLevel(JLogLevel.JLogLevelVerbose).build())
                .build();
JIM.getInstance().init(this, "appKey", initConfig);
```

You can filter SDK-related logs using the keyword "JLogger".


</TabItem>


<TabItem value="ios">

By default, the SDK does not output logs to the console. To enable logging during development, set the log level before initializing the SDK.

```objectivec
[JIM.shared setConsoleLogLevel:JLogLevelVerbose];
```

You can filter SDK-related logs using the keyword "JLogger".

</TabItem>
<TabItem value="js">

</TabItem>
<TabItem value="flutter">

</TabItem>
<TabItem value="reactnative">

The React Native SDK outputs logs through the Metro console. In the development environment, the SDK will output relevant log information.

You can filter SDK-related logs by searching for the keyword "JuggleIM" in the console.

```typescript
// The SDK automatically outputs logs in the development environment
// You can view them in the Metro console
```

</TabItem>
</Tabs>