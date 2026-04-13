---
title: Android integration
hide_title: true
sidebar_position: 1
---

**Initialization**

When initializing by calling the `JIM.getInstance().init()` method, use the version that accepts an `InitConfig` parameter:

```java
JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder().build())
        .build();

JIM.getInstance().init(appContext, appKey, initConfig);
```

<Tabs
groupId="sdks-push"
values={[
{ label: 'xiaomi', value: 'xiaomi', },
{ label: 'Huawei', value: 'huawei', },
{ label: 'OPPO', value: 'oppo', },
{ label: 'vivo', value: 'vivo', },
{ label: 'FCM', value: 'fcm', },
{ label: 'Aurora', value: 'jiguang'}
]
}>
<TabItem value="xiaomi">

1. Add dependencies.```bash
   implementation files('libs/XMPlugin.aar')
   implementation files('libs/MiPush_SDK_Client_6_0_1-C_3rd.aar')
   ```
2. Set the `appId` and `appKey` provided by Xiaomi when constructing `InitConfig`.```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setXmConfig("appId", "appKey")
                .build())
        .build();
   ```
3. Proguard configuration.```bash
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="huawei">

1. Add dependencies.```bash
   implementation files('libs/HWPlugin.aar')
   implementation 'com.huawei.hms:push:6.10.0.300'
   ```
2. Add the following configuration in the root project's `build.gradle`.```bash
   repositories {
        maven { url 'https://developer.huawei.com/repo/' }
   }

   dependencies {
        classpath 'com.huawei.agconnect:agcp:1.9.1.301'
    }
   ```
3. Add the following in the `build.gradle` of the `app` module.```bash
   plugins {
        id 'com.huawei.agconnect'
   }
   ```
4. Place the Huawei push configuration file `agconnect-services.json` in the `app` module directory.
5. Set the `appId` provided by Huawei when constructing `InitConfig`.```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setHwConfig("appId")
                .build())
        .build();
   ```
6. Proguard configuration.```bash
   -ignorewarnings
   -keepattributes *Annotation*
   -keepattributes Exceptions
   -keepattributes InnerClasses
   -keepattributes Signature
   -keepattributes SourceFile,LineNumberTable
   -keep class com.huawei.hianalytics.**{*;}
   -keep class com.huawei.updatesdk.**{*;}
   -keep class com.huawei.hms.**{*;}
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="oppo">

1. Add dependencies.```bash
   implementation files('libs/OPPOPlugin.aar')
   implementation files('libs/com.heytap.msp_3.5.1.aar')
   implementation 'com.google.code.gson:gson:2.10.1'
   implementation 'commons-codec:commons-codec:1.6'
   implementation 'androidx.annotation:annotation:1.1.0'
   ```
2. Set the `appKey` and `appSecret` provided by OPPO when constructing `InitConfig`.```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setOppoConfig("appKey", "appSecret")
                .build())
        .build();
   ```
3. Proguard configuration.```bash
   -keep public class * extends android.app.Service
   -keep class com.heytap.msp.** { *;}
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="vivo">

1. Add dependencies.```bash
   implementation files('libs/VIVOPlugin.aar')
   implementation files('libs/vivo_pushSDK_v4.0.4.0_504.aar')
   ```
2. Set the `appKey` and `appId` provided by VIVO in the `build.gradle` of the `app` module.```bash
   android {
        defaultConfig {
            manifestPlaceholders = [
                    "VIVO_APPKEY": "appKey",
                    "VIVO_APPID" : "appId",
            ]
        }
   }
   ```
3. Enable VIVO push when constructing `InitConfig`.```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setVivoConfig()
                .build())
        .build();
   ```
4. Proguard configuration.```bash
   -dontwarn com.vivo.push.**
   -keep class com.vivo.push.**{*; }
   -keep class com.vivo.vms.**{*; }
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="fcm">

1. Add dependencies.```bash
   implementation files('libs/GooglePlugin.aar')
   implementation(platform('com.google.firebase:firebase-bom:32.0.0'))
   implementation("com.google.firebase:firebase-messaging")
   ```
2. Add the following configuration in the root project's `build.gradle`.```bash
   repositories {
        google()
   }

   dependencies {
        classpath 'com.google.gms:google-services:4.3.15'
    }
   ```
3. Add the following in the `build.gradle` of the `app` module.```bash
   plugins {
        id 'com.google.gms.google-services'
   }
   ```
4. Place the Google push configuration file `google-services.json` in the `app` module directory.
5. Proguard configuration.```bash
   -dontwarn com.google.android.gms.**
   -keep class com.google.android.gms.** { *; }
   -keep class com.google.firebase.** { *; }
   -keep class com.juggle.im.push.** {*;}
   ```
6. Add intent-filter for push click handling.```xml
   <intent-filter>
         <action android:name="com.j.im.intent.MESSAGE_CLICK" />
   </intent-filter>
   ```

Retrieve parameters and handle navigation based on the parameters and business logic.```java
   Intent intent = getIntent();
   if (intent != null) {
      Bundle bundle = intent.getExtras();
      if (bundle != null) {
            // message id
            String messageId = bundle.getString("msg_id");
            // sender user id
            String senderId = bundle.getString("sender_id");
            // conversation id
            String conversationId = bundle.getString("conver_id");
            // conversation type
            Conversation.ConversationType type = Conversation.ConversationType.setValue(bundle.getInt("conver_type"));
      }
   }
   ```

</TabItem>
<TabItem value="jiguang">

1. Add the following configuration in the `build.gradle` of the `app` module.```bash
   android {

      ......

      defaultConfig {

         applicationId = "com.xxx.xxx" // Package name registered on JPush.
         ......

         ndk {
            // Select the .so libraries corresponding to the CPU architectures to include.
            abiFilters += setOf("armeabi-v7a", "arm64-v8a")
            // You can also add 'x86', 'x86_64', 'mips', 'mips64'
         }

         manifestPlaceholders.apply {
            putAll(
                  mapOf(
                     "JPUSH_PKGNAME" to applicationId!!,
                     // AppKey corresponding to the package name registered on JPush.
                     "JPUSH_APPKEY" to "your Appkey",
                     // Use default values for now.
                     "JPUSH_CHANNEL" to "developer-default",
                  )
            )
         }
         ......
      }
   }

   dependencies {
      implementation(files("libs/JGPlugin.aar"))
      implementation("cn.jiguang.sdk:jpush:5.2.4")
   }
   ```

2. Enable Aurora Push when constructing `InitConfig`.```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
            .setJgConfig()
            .build())
        .build();
   ```

3. Proguard configuration.```bash
   -dontoptimize
   -dontpreverify

   -dontwarn cn.jpush.**
   -keep class cn.jpush.** { *; }
   -keep class * extends cn.jpush.android.service.JPushMessageReceiver { *; }

   -dontwarn cn.jiguang.**
   -keep class cn.jiguang.** { *; }
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
</Tabs>