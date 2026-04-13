---
title: iOS normal push
hide_title: true
sidebar_position: 2
---

### Request permission{#setting}

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

### Set push token{#device}

Set the device token in the SDK within the `application:didRegisterForRemoteNotificationsWithDeviceToken:` callback.

```objectivec
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    [JIM.shared.connectionManager registerDeviceToken:deviceToken];
}
```