---
title: iOS VoIP 推送
hide_title: true
sidebar_position: 3
---

从 iOS 13 开始，苹果基于安全考虑在使用 VoIP 推送时必须配合苹果 CallKit 使用，否则 iOS 系统将在收到 VoIP 推送后杀掉 App 进程。
而由于工信部的要求，在中国区 App Store 上架的应用不允许使用苹果 CallKit 功能，请在中国区上架的开发者不要使用 VoIP 推送功能。

### 导入 PushKit 并设置 PKPushRegistry

```objectivec
#import <PushKit/PushKit.h>

@interface AppDelegate () <PKPushRegistryDelegate>
@end

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // 初始化 PKPushRegistry
    PKPushRegistry *pushRegistry = [[PKPushRegistry alloc] initWithQueue:dispatch_get_main_queue()];
    pushRegistry.delegate = self;
    pushRegistry.desiredPushTypes = [NSSet setWithObject:PKPushTypeVoIP];
    return YES;
}
```

### 注册 VoIP 推送并处理回调

```objectivec
#pragma mark - PKPushRegistryDelegate

// 当 VoIP token 生成时调用
- (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(PKPushType)type {
    // 调用 SDK 接口将 VoIP token 发送给 IM 服务器
    [JIM.shared.connectionManager registerVoIPToken:pushCredentials.token];
}

// 当设备接收到 VoIP 推送时调用
- (void)pushRegistry:(PKPushRegistry *)registry didReceiveIncomingPushWithPayload:(PKPushPayload *)payload forType:(PKPushType)type withCompletionHandler:(void (^)(void))completion {
    NSLog(@"收到 VoIP 推送：%@", payload.dictionaryPayload);

    // 根据推送内容处理业务逻辑，比如显示来电界面
    [self handleIncomingCallWithPayload:payload.dictionaryPayload];
}

// 处理来电
- (void)handleIncomingCallWithPayload:(NSDictionary *)payload {
    // 解析推送内容并显示来电界面

    //通话 id
    NSString *callId = payload[@"room_id"];
    //邀请者用户 id
    NSString *inviterId = payload[@"inviter_id"];
    //是否多人通话
    BOOL isMulti;
    //通话类型
    JCallMediaType mediaType;
    id obj = payload[@"is_multi"];
    if ([obj isKindOfClass:[NSNumber class]]) {
        isMulti = [(NSNumber *)obj boolValue];
    }
    obj = payload[@"media_type"];
    if ([obj isKindOfClass:[NSNumber class]]) {
        mediaType = [(NSNumber *)obj integerValue];
    }

    // TODO: 调用系统 CallKit 或自定义界面，显示来电通知
}
```
