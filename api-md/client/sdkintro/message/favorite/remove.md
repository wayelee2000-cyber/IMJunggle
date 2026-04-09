---
title: 移除收藏
hide_title: true
sidebar_position: 1
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

移除收藏，支持将图片、文件、语音、视频等多种类型消息移除收藏。

**接口定义**

```java
/**
 * 移除消息收藏
 * @param messageIdList 待移除的消息 id 列表
 * @param callback 结果回调
 */
void removeFavorite(List<String> messageIdList, ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

移除收藏，支持将图片、文件、语音、视频等多种类型消息移除收藏。

**接口定义**

```objectivec
/// 移除消息收藏
/// - Parameters:
///   - messageIdList: 待移除的消息 id 列表
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)removeFavorite:(NSArray <NSString *> *)messageIdList
               success:(void (^)(void))successBlock
                 error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

移除收藏，支持将图片、文件、语音、视频等多种类型消息移除收藏。

**参数说明**

| 名称                                 | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|-------------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| params                              | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| params.messages                     | Array   | 是     |        | 收藏消息列表                            | 1.0.0    |
| params.messages[0].conversationType | Number  | 是     |        | [会话类型](../../enum/web#conversation) | 1.0.0    |
| params.messages[0].conversationId   | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| params.messages[0].senderId         | String  | 是     |        | 消息发送人 Id，[Message.sender.id](../../../msg/message) 可获取| 1.0.0    |
| params.messages[0].messageId        | String  | 是     |        | 消息 Id，[Message.messageId](../../../msg/message) 可获取| 1.0.0    |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let params = {
  messages: [{
    conversationType: ConversationType.GROUP,
    conversationId: 'groupz001',
    messageId: 'nwmz3nrps6yj3rk8',
    senderId: "675NdFjkx"
  }] 
};

jim.removeFavoriteMessages(params).then(() => {
  console.log('removeFavoriteMessages successfully.')
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

移除收藏，支持将图片、文件、语音、视频等多种类型消息移除收藏。

**接口定义**

```dart
/// 移除消息收藏
/// - Parameters:
///   - messageIdList: 待移除的消息 id 列表
Future<int> removeFavoriteMessages(List<String> messageIdList) async
```

</TabItem>
</Tabs>