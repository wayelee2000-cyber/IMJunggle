---
title: 查询置顶
hide_title: true
sidebar_position: 2
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
 * 获取置顶消息
 * 进入会话的时候，可以通过会话信息查询当前会话的置顶消息
 * @param conversation 会话标识
 * @param callback 结果回调
 */
JIM.getInstance().getMessageManager().getTopMessage(conversation, new IMessageManager.IGetTopMessageCallback() {
            @Override
            public void onSuccess(Message message, UserInfo userInfo, long l) {
            }

            @Override
            public void onError(int i) {
            }
        });

// 进入会话后，如何实时获取置顶消息
/**
 * 监听会话置顶消息
 * 通过这个监听实时获取置顶消息的变化，进行消息页面的更新，例如通过EventBus广播的方式
 * @param listener 监听器
 */
JIM.getInstance().getMessageManager().addListener("msg", new IMessageManager.IMessageListener() {
            @Override
            /**
             * 置顶消息
             * @param message 消息对象
             * @param userInfo 操作人
             * @param b 是否置顶
             */
            public void onMessageSetTop(Message message, UserInfo userInfo, boolean b) {
                Log.d(tag, "onMessageSetTop: " + message.toString());
                EventBus.getDefault().post(new MessageTopEvent(message, userInfo, b));
            }
        });        
```

</TabItem>
<TabItem value="ios">

**接口定义**

```objectivec
/// 获取置顶消息
/// - Parameters:
///   - conversation: 会话标识
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)getTopMessage:(JConversation *)conversation
              success:(void (^)(JMessage *message, JUserInfo *userInfo, long long timestamp))successBlock
                error:(void (^)(JErrorCode code))errorBlock;
```


</TabItem>
<TabItem value="js">

查询指定会话的置顶消息，点击进入会话页面后请调用查询置顶消息接口获取当前会话的置顶消息。

![](./top.png)

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |

**成功回调**

| 名称                 | 类型    | 描述                                    | 版本   |
|---------------------|---------|-----------------------------------------|--------|
| result              | Object  |                                        | 1.0.0  |
| result.message      | Object  | 被置顶的消息对象            | 1.0.0  |
| result.isTop        | Boolean | 是否置顶 | 1.0.0  |
| result.operator     | Object  | 操作人 | 1.0.0  |
| result.createdTime  | Number  | 操作置顶时间 | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
};

jim.getTopMessage(conversation).then((result) => {

  let { message, isTop, operator, createdTime } = result;
  
  // message => 被置顶或取消置顶的原始消息，想系可查看 Message 对象
  
  // isTop => 是否置顶
  
  // operator => 操作人 { id: '', name: '', portrait: '' }
  
  // createdTime => 操作时间
  
}, (error) => {
  console.log(error)
});
```
</TabItem>

<TabItem value="flutter">

**接口定义**

```dart
/// 获取置顶消息
/// - Parameters:
///   - conversation: 会话标识
Future<Result<TopMessageResult>> getTopMessage(Conversation conversation) async
```

</TabItem>

</Tabs>