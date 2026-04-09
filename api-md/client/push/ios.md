---
title: iOS 普通推送
hide_title: true
sidebar_position: 2
---

### 请求权限{#setting}

```objectivec
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [[UNUserNotificationCenter currentNotificationCenter] getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
        switch ([settings authorizationStatus]) {
            case UNAuthorizationStatusAuthorized:
                dispatch_async(dispatch_get_main_queue(), ^{
                    [[UIApplication sharedApplication] registerForRemoteNotifications];
                });
                break;
            case UNAuthorizationStatusNotDetermined:
                [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:(UNAuthorizationOptionBadge | UNAuthorizationOptionSound | UNAuthorizationOptionAlert) completionHandler:^(BOOL granted, NSError * _Nullable error) {
                    if (granted) {
                        dispatch_async(dispatch_get_main_queue(), ^{
                            [[UIApplication sharedApplication] registerForRemoteNotifications];
                        });
                    }
                }];
                break;
            default:
                break;
        }
    }];
    [UNUserNotificationCenter currentNotificationCenter].delegate = self;
}
```

### 设置推送Token{#device}

在 application:didRegisterForRemoteNotificationsWithDeviceToken: 回调中把 Device Token 设置给 SDK。

```objectivec
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    [JIM.shared.connectionManager registerDeviceToken:deviceToken];
}
```
