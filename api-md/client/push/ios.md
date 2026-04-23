---
title: iOS push notifications
hide_title: true
sidebar_position: 2
---

### Request notification permission{#setting}

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

### Register the device token{#device}

Register the device token with the SDK in the `application:didRegisterForRemoteNotificationsWithDeviceToken:` callback.

```objectivec
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    [JIM.shared.connectionManager registerDeviceToken:deviceToken];
}
```
