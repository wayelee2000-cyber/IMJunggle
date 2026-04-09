---
title: iOS
hide_title: true
sidebar_position: 2
---

### 前期准备{#pre}

1、在 `开发者后台` 创建应用获取 `AppKey` 和 `Secret`。

![](./assets/appkey_secret.png)

2、自己调用服务端 API 获取 Token 或在开发者后台的 -> 选择应用-> 开发工具 -> API -> 用户相关中，调用用户注册接口，获取两个测试 Token。

![](./assets/token.png)

3、根据集成文档逐步集成。

### 使用流程{#flow}

![](assets/flow.png)

### 示例代码{#code}
```objectivec
[JIM.shared setServerUrls:@[@"wss://ws.im.com"]];// "wss://ws.im.com" 替换成部署好的 server url
[JIM.shared initWithAppKey:@"appkey"];
[JIM.shared.connectionManager connectWithToken:@"token1"];
[JIM.shared.connectionManager addDelegate:self];
- (void)connectionStatusDidChange:(JConnectionStatus)status errorCode:(JErrorCode)code extra:(NSString *)extra {
    if (JConnectionStatusConnected == status) {
    	//文本消息
		JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid2"];
		JTextMessage *text = [[JTextMessage alloc] initWithContent:@"test text message"];
		JMessage *m = [JIM.shared.messageManager sendMessage:text
											  inConversation:conversation
													 success:^(JMessage *message) {
				NSLog(@"sendMessage success");
			} error:^(JErrorCode errorCode, JMessage *message) {
				NSLog(@"sendMessage error");
			}];
		NSLog(@"after send, m.clientMsgNo is %lld", m.clientMsgNo);
    }
}
```