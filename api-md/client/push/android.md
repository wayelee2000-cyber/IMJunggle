---
title: Android 集成
hide_title: true
sidebar_position: 1
---

**初始化**

在调用 `JIM.getInstance().init()` 方法初始化时，使用带有 `InitConfig`参数的方法：

```java
JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder().build())
        .build();

JIM.getInstance().init(appContext, appKey, initConfig);
```

<Tabs
groupId="sdks-push"
values={[
{ label: '小米', value: 'xiaomi', },
{ label: '华为', value: 'huawei', },
{ label: 'OPPO', value: 'oppo', },
{ label: 'vivo', value: 'vivo', },
{ label: 'FCM', value: 'fcm', },
{ label: '极光', value: 'jiguang'}
]
}>
<TabItem value="xiaomi">

1. 添加依赖。

   ```bash
   implementation files('libs/XMPlugin.aar')
   implementation files('libs/MiPush_SDK_Client_6_0_1-C_3rd.aar')
   ```
2. 构造InitConfig时设置小米推送的`appId`和`appKey`。
   ```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setXmConfig("appId", "appKey")
                .build())
        .build();
   ```
3. 混淆配置。
   ```bash
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="huawei">

1. 添加依赖。
   ```bash
   implementation files('libs/HWPlugin.aar')
   implementation 'com.huawei.hms:push:6.10.0.300'
   ```
2. 在项目根目录下的`build.gradle`中增加配置。
   ```bash
   repositories {
        maven { url 'https://developer.huawei.com/repo/' }
   }

   dependencies {
        classpath 'com.huawei.agconnect:agcp:1.9.1.301'
    }
   ```
3. 在`app`模块的`build.gradle`中增加配置。
   ```bash
   plugins {
        id 'com.huawei.agconnect'
   }
   ```
4. 将华为推送配置文件`agconnect-services.json`放在`app`模块目录下。
5. 构造InitConfig时设置华为推送的`appId`。
   ```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setHwConfig("appId")
                .build())
        .build();
   ```
6. 混淆配置。
   ```bash
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

1. 添加依赖。

   ```bash
   implementation files('libs/OPPOPlugin.aar')
   implementation files('libs/com.heytap.msp_3.5.1.aar')
   implementation 'com.google.code.gson:gson:2.10.1'
   implementation 'commons-codec:commons-codec:1.6'
   implementation 'androidx.annotation:annotation:1.1.0'
   ```
2. 构造InitConfig时设置OPPO推送的`appKey`和`appSecret`。
   ```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setOppoConfig("appKey", "appSecret")
                .build())
        .build();
   ```
3. 混淆配置。
   ```bash
   -keep public class * extends android.app.Service
   -keep class com.heytap.msp.** { *;}
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="vivo">

1. 添加依赖。

   ```bash
   implementation files('libs/VIVOPlugin.aar')
   implementation files('libs/vivo_pushSDK_v4.0.4.0_504.aar')
   ```
2. 在`app`模块的`build.gradle`中设VIVO推送的`appKey`和`appId`。
   ```bash
   android {
        defaultConfig {
            manifestPlaceholders = [
                    "VIVO_APPKEY": "appKey",
                    "VIVO_APPID" : "appId",
            ]
        }
   }
   ```
3. 构造InitConfig时设置VIVO推送。
   ```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
                .setVivoConfig()
                .build())
        .build();
   ```
4. 混淆配置。
   ```bash
   -dontwarn com.vivo.push.**
   -keep class com.vivo.push.**{*; }
   -keep class com.vivo.vms.**{*; }
   -keep class com.juggle.im.push.** {*;}
   ```

</TabItem>
<TabItem value="fcm">

1. 添加依赖。

   ```bash
   implementation files('libs/GooglePlugin.aar')
   implementation(platform('com.google.firebase:firebase-bom:32.0.0'))
   implementation("com.google.firebase:firebase-messaging")
   ```
2. 在项目根目录下的`build.gradle`中增加配置。
   ```bash
   repositories {
        google()
   }

   dependencies {
        classpath 'com.google.gms:google-services:4.3.15'
    }
   ```
3. 在`app`模块的`build.gradle`中增加配置。
   ```bash
   plugins {
        id 'com.google.gms.google-services'
   }
   ```
4. 将Google推送配置文件`google-services.json`放在`app`模块目录下。
5. 混淆配置。
   ```bash
   -dontwarn com.google.android.gms.**
   -keep class com.google.android.gms.** { *; }
   -keep class com.google.firebase.** { *; }
   -keep class com.juggle.im.push.** {*;}
   ```
6. 点击推送跳转。

   添加 intent-filter。

   ```xml
   <intent-filter>
         <action android:name="com.j.im.intent.MESSAGE_CLICK" />
   </intent-filter>
   ```

   获取参数，根据参数和业务需求做相应的跳转。

   ```java
   Intent intent = getIntent();
   if (intent != null) {
      Bundle bundle =  intent.getExtras();
      if (bundle != null) {
            // 消息 id
            String messageId = bundle.getString("msg_id");
            // 发送者用户 id
            String senderId = bundle.getString("sender_id");
            // 会话 id
            String conversationId = bundle.getString("conver_id");
            // 会话类型
            Conversation.ConversationType type = Conversation.ConversationType.setValue(bundle.getInt("conver_type");)
      }
   }
   ```



</TabItem>
<TabItem value="jiguang">

1. 在`app`模块的`build.gradle`中增加配置。

   ```bash
   android {

      ......

      defaultConfig {

         applicationId = "com.xxx.xxx" //JPush 上注册的包名。
         ......

         ndk {
            //选择要添加的对应 cpu 类型的 .so 库。
            abiFilters += setOf("armeabi-v7a", "arm64-v8a")
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
         }

         manifestPlaceholders.apply {
            putAll(
                  mapOf(
                     "JPUSH_PKGNAME" to applicationId!!,
                     //JPush 上注册的包名对应的 Appkey。
                     "JPUSH_APPKEY" to "你的 Appkey",
                     //暂时填写默认值即可。
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

2. 构造InitConfig时设置极光推送。
   ```java
   JIM.InitConfig initConfig = new JIM.InitConfig.Builder()
        .setPushConfig(new PushConfig.Builder()
            .setJgConfig()
            .build())
        .build();
   ```

3. 混淆配置。

   ```bash
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