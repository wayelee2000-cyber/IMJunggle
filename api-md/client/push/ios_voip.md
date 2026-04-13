---
title: iOS VoIP Push
hide_title: true
sidebar_position: 3
---

Starting with iOS 13, Apple requires integration with CallKit when using VoIP push notifications for security reasons. Without this integration, the iOS system will terminate the app process upon receiving a VoIP push. 

Due to regulations from the Ministry of Industry and Information Technology, apps listed on the App Store in China are prohibited from using Apple's CallKit functionality. Developers publishing in China are advised not to use the VoIP push feature.

### Import PushKit and Set Up PKPushRegistry

```objectivec
#import <PushKit/PushKit.h>

@interface AppDelegate () <PKPushRegistryDelegate>
@end

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Initialize PKPushRegistry
    PKPushRegistry *pushRegistry = [[PKPushRegistry alloc] initWithQueue:dispatch_get_main_queue()];
    pushRegistry.delegate = self;
    pushRegistry.desiredPushTypes = [NSSet setWithObject:PKPushTypeVoIP];
    return YES;
}
```

### Register VoIP Push and Handle Callbacks

```objectivec
#pragma mark - PKPushRegistryDelegate

// Called when the VoIP token is generated
- (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(PKPushType)type {
    // Use the SDK interface to send the VoIP token to the IM server
    [JIM.shared.connectionManager registerVoIPToken:credentials.token];
}

// Called when the device receives a VoIP push
- (void)pushRegistry:(PKPushRegistry *)registry didReceiveIncomingPushWithPayload:(PKPushPayload *)payload forType:(PKPushType)type withCompletionHandler:(void (^)(void))completion {
    NSLog(@"VoIP push received: %@", payload.dictionaryPayload);

    // Handle business logic based on the push content, such as displaying the incoming call interface
    [self handleIncomingCallWithPayload:payload.dictionaryPayload];
}

// Handle incoming calls
- (void)handleIncomingCallWithPayload:(NSDictionary *)payload {
    // Parse the push content and display the incoming call interface

    // Call ID
    NSString *callId = payload[@"room_id"];
    // Inviter user ID
    NSString *inviterId = payload[@"inviter_id"];
    // Is this a multi-person call?
    BOOL isMulti;
    // Call type
    JCallMediaType mediaType;
    id obj = payload[@"is_multi"];
    if ([obj isKindOfClass:[NSNumber class]]) {
        isMulti = [(NSNumber *)obj boolValue];
    }
    obj = payload[@"media_type"];
    if ([obj isKindOfClass:[NSNumber class]]) {
        mediaType = [(NSNumber *)obj integerValue];
    }

    // TODO: Use system CallKit or a custom interface to display the incoming call notification
}
```