---
title: 删除消息回应
hide_title: true
sidebar_position: 3
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


**接口定义**

```java
/**
 * 删除消息回应
 * @param messageId 消息 id
 * @param conversation 消息所属会话
 * @param reactionId 回应 id
 * @param callback 结果回调
 */
void removeMessageReaction(String messageId,
                            Conversation conversation,
                            String reactionId,
                            ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

**接口定义** 

```objectivec
/// 删除消息回应
/// - Parameters:
///   - messageId: 消息 id
///   - conversation: 消息所属会话
///   - reactionId: 回应 id
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)removeMessageReaction:(NSString *)messageId
                 conversation:(JConversation *)conversation
                   reactionId:(NSString *)reactionId
                      success:(void (^)(void))successBlock
                        error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.8.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../enum/web#conversation)                            | 1.8.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.8.0    |
| message.messageId              | String  | 是    |         | 被删除回复的消息 Id                                | 1.8.0  |
| message.reactionId             | String  | 是    |         | 回应消息的唯一表示，开发者可自定义，需要多端约定一致  | 1.8.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.8.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  reactionId: ':smile'
};

jim.removeMessageReaction(msg).then(() => {
  console.log('remove message reaction successfully.')
}, (error) => {
  console.log(error)
});
```
</TabItem>
<TabItem value="flutter">


**接口定义**

```dart
/**
 * 删除消息回应
 * @param messageId 消息 id
 * @param conversation 消息所属会话
 * @param reactionId 回应 id
 */
Future<int> removeMessageReaction(String messageId, Conversation conversation, String reactionId) async
```

</TabItem>
</Tabs>