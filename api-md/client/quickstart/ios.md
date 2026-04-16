---
title: iOS
hide_title: true
sidebar_position: 2
---

### Preparation{#pre}

1. Create an application in the `Developer server` to obtain your `AppKey` and `Secret`.

![](./assets/appkey_secret.png)

2. Call the server API to obtain a token yourself, or in the Developer server, navigate to Select Application -> Development Tools -> API -> User Related, and call the user registration interface to obtain two test tokens.

![](./assets/token.png)

3. Follow the integration steps as outlined in the integration documentation.

### Workflow{#flow}

![](assets/flow.png)

### Sample code{#code}
```objectivec
[JIM.shared setServerUrls:@[@"wss://ws.im.com"]]; // Replace "wss://ws.im.com" with your deployed server URL
[JIM.shared initWithAppKey:@"appkey"];
[JIM.shared.connectionManager connectWithToken:@"token1"];
[JIM.shared.connectionManager addDelegate:self];

- (void)connectionStatusDidChange:(JConnectionStatus)status errorCode:(JErrorCode)code extra:(NSString *)extra {
    if (JConnectionStatusConnected == status) {
        // Send a text message
        JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid2"];
        JTextMessage *text = [[JTextMessage alloc] initWithContent:@"test text message"];
        JMessage *m = [JIM.shared.messageManager sendMessage:text
                                              inConversation:conversation
                                                     success:^(JMessage *message) {
            NSLog(@"sendMessage success");
        } error:^(JErrorCode errorCode, JMessage *message) {
            NSLog(@"sendMessage error");
        }];
        NSLog(@"After sending, m.clientMsgNo is %lld", m.clientMsgNo);
    }
}
```
