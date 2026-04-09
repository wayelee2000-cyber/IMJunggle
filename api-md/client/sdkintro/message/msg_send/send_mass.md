---
title: 群发助手
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

群发助手支持向批量会话中发送消息，并且该消息在发送端不影响会话的排序。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| content                        | MessageContent  | 消息实体                                           | 1.0.0    |
| conversations                   | List[] | 目标会话列表                         | 1.0.0    |
| callback         | IMessageManager.IBroadcastMessageCallback  | 回调 | 1.0.0    |

**示例代码**

```java
Conversation c1 = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
Conversation c2 = new Conversation(Conversation.ConversationType.PRIVATE, "userid2");
Conversation c3 = new Conversation(Conversation.ConversationType.PRIVATE, "userid3");
Conversation c4 = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
List<Conversation> conversations = new ArrayList<>();
conversations.add(c1);
conversations.add(c2);
conversations.add(c3);
conversations.add(c4);
TextMessage text = new TextMessage("broadcast");
JIM.getInstance().getMessageManager().broadcastMessage(text, conversations, new IMessageManager.IBroadcastMessageCallback() {
    @Override
    public void onProgress(Message message, int errorCode, int processCount, int totalCount) {
        
    }

    @Override
    public void onComplete() {

    }
});
```

</TabItem>
<TabItem value="ios">

群发助手支持向批量会话中发送消息，并且该消息在发送端不影响会话的排序。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| content                        | JMessageContent  | 消息实体                                           | 1.0.0    |
| conversations                   | NSArray `<JConversation *>` | 目标会话列表                         | 1.0.0    |
| progressBlock         |   | 进度回调 | 1.0.0    |
| completeBlock         |   | 完成回调 | 1.0.0    |

**示例代码**

```objectivec
JConversation *c1 = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
JConversation *c2 = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId2"];
JConversation *c3 = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId3"];
JConversation *c4 = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];

NSArray *conversations = @[c1, c2, c3, c4];
JTextMessage *text = [[JTextMessage alloc] initWithContent:@"broadcast"];
[JIM.shared.messageManager broadcastMessage:text
                            inConversations:conversations
                                    progress:^(JMessage *sentMessage, JErrorCode code, int processCount, int totalCount) {
    
} complete:^{
    
}];
```

</TabItem>
<TabItem value="js">

消息群发助手支持一次性向 `100` 群组或者用户发送消息，同时支持设置群发的消息是否影响会话列表的排序，开发者在做多人广播时可以使用 

**参数说明**

_参数 messages 支持传入数组，每一项 message 说明如下：_

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.name                   | String  | 是     |        | 消息名称，根据实际需要发送不同消息类型，详细枚举请查看 [MessageType](../../../enum/web#message) | 1.0.0    |
| message.content                | Object  | 是     |        | 消息内容，构建 `message.name` 消息                              | 1.0.0    |
| message.isMass                 | Boolean | 否     |  true  | 表示群发消息，默认为 `true` 群发后**不影响**会话列表排序     | 1.0.0    |
| lifeTime                   | Number    | 否    |  0    |消息的销毁时间段，必须大于 `0`, 单位 `ms`, 例如 60s: `1 * 60 * 1000`   | 1.9.0    |
| lifeTimeAfterRead             | Number    | 否    |  0    |消息的阅后即焚的时间段，必须大于 0, 单位 `ms`, 例如 60s: `1 * 60 * 1000`  | 1.9.0    |

**发送回调**

| 名称                   | 类型    | 描述                                                                      | 版本   |
|-----------------------|---------|---------------------------------------------------------------------------|--------|
| callbaks              | Object  | 群发接口与其他接口返回 `Promise` 不同，结果通过 Callback 方式返回 | 1.0.0  |
| callbacks.onbefore    | Function  | 群发过程中会触发多次，返回将要发送的消息内容，包含 `tid` [Message](../../../msg/message) | 1.0.0  |
| callbacks.onprogress   | Function  | 群发过程中会触发多次，返回已发送条数、总条数、和当前发送成功的 [Message](../../../msg/message) | 1.0.0  |
| callbacks.oncompleted   | Function  | 群发结束后触发，只会触发一次，返回本次所有群发消息数组，每条消息结构请查看 [Message](../../../msg/message)  | 1.0.0  |

**发送失败**

参数不合法会通过 `Promise` 返回，每条消息的发送失败状态会在 `callbacks.onprogress` 中返回，具体可查看返回消息中 `message.error`, 根据 [状态码](../../../status_code/web) 判断一场情况

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| result | Object  | 发送失败后会返回对象中包含 `tid` 属性信息，同时包含 `error` 信息，可以直接查看 `error.msg`，或者查看 [状态码](../../../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType, MessageType } = JIM;

let messages = [];
// 群发给 userid1 ～ userid10
for (let i = 1; i < 11; i++) {
  let message = {
    conversationType: ConversationType.PRIVATE,
    conversationId: `userid${i}`,
    content: { content: `Hello JIM ${Date.now()}` },
    name: MessageType.TEXT,
    isMass: true
  };
  messages.push(message)
}

jim.sendMassMessage(messages, {
  onprogress: ({ message, count, total }) => {
    console.log(`${count}/${total}`, message);
  },
  oncompleted: ({ messages }) => {
    console.log('send mass messages completed.', messages);
  },
}).then(() => {
  console.log('send mass messages successfully');
}, (result) => {
  let { error, tid } = result;
  // 可根据 tid 修改消息发送失败的状态, Web 端消息失败仅在 SDK 内存中保存，刷新后将无法获取到发送失败的消息
  console.log(tid, error);
});;
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

> 暂未提供

</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
</Tabs>