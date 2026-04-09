---
title: 修改消息
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
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', },
]
}>
<TabItem value="android">

只允许修改自己发送的消息。修改成功后，对应会话中的其他用户会收到 onMessageUpdate 回调（需要添加[消息监听](../../../watcher/message)）

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| messageId                        | String  | 消息 id                           | 1.8.4    |
| messageContent               | MessageContent | 修改后的消息实体                             | 1.8.4 |
|conversation | Conversation | 会话 | 1.8.4 |
| callback         | IMessageCallback  | 结果回调 | 1.8.4    |

**示例代码**

```java
TextMessage text = new TextMessage("update message");
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "conversationId1");
JIM.getInstance().getMessageManager().updateMessage("messageId1", text, conversation, new IMessageManager.IMessageCallback() {
    @Override
    public void onSuccess(Message message) {
        
    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

只允许修改自己发送的消息。修改成功后，对应会话中的其他用户会收到 messageDidUpdate: 回调（需要添加[消息监听](../../../watcher/message)）

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| messageContent               | JMessageContent | 修改后的消息实体                             | 1.8.4 |
| messageId                        | NSString  | 消息 id                           | 1.8.4    |
|conversation | JConversation | 会话 | 1.8.4 |
| successBlock         |   | 成功回调 | 1.8.4    |
| errorBlock                   |   | 失败回调 | 1.8.4    |

**示例代码**

```objectivec
JTextMessage *text = [[JTextMessage alloc] initWithContent:@"update message"];
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate
                                                                conversationId:@"conversationId1"];
[JIM.shared.messageManager updateMessage:text
                                messageId:@"messageId1"
                          inConversation:conversation
                                  success:^(JMessage *message) {
    
} error:^(JErrorCode errorCode) {
    
}];
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.content                | Object  | 是     |        | 消息内容，构建 `message.name` 消息                              | 1.0.0    |
| message.tid                     | String  | 是    |         |被修改的消息的本地 Id                                       | 1.0.0  |
| message.messageId              | String   | 是    |         |被修改的消息 Id                                       | 1.0.0  |
| message.sentTime               | Number   | 是    |         |被修改的消息的发送时间                                | 1.0.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  tid: 'dkaadjdk30dls',
  messageId: 'xxxdkadhdsa',
  sentTime: 1702180128970,
  content: {
    content: 'new hello world'
  }
};

jim.updateMessage(msg).then(() => {
  console.log('update message successfully.')
}, (error) => {
  console.log(error)
});
```
</TabItem>

<TabItem value="harmony">

只允许修改自己发送的消息。修改成功后，对应会话中的其他用户会收到 onMessageUpdate 回调（需要添加[消息监听](../../../watcher/message)）

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conver  | Conversation | 会话 | 1.8.4 |
| msgId                        | string  | 消息 id                           | 1.8.4    |
| msg               | MessageContent | 修改后的消息实体                             | 1.8.4 |
| callback         | MessageCallback  | 结果回调 | 1.8.4    |

**示例代码**

```java
let conver = new Conversation("userid1",1)
let txt = new TextMessage("new content","")
JuggleIm.instance.getMessageManager().modifyMessage(conver,"messageid1",txt,(code,msg)=>{

})
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

只允许修改自己发送的消息。修改成功后，对应会话中的其他用户会收到 onMessageUpdate 回调（需要添加消息监听）

**参数说明**

| 名称                           | 类型    | 描述          | 版本     |
|-------------------------------|---------|----------------|----------|
| conversation   | Conversation  | 会话标识     | 1.0.0    |
| messageId      | String        | 消息 id     | 1.0.0    |
| messageContent | MessageContent| 修改后的消息实体 | 1.0.0    |
| callback | UpdateMessageCallback | 结果回调 | 1.0.0    |


**示例代码**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1,
  id: 'userId1'
};

const textMessage = {
  contentType: 'jg:text',
  content: 'update message'
};

const messageId = 'messageId1';

const callback = (message: any, errorCode: number) => {
  if (errorCode === 0) {
    console.log('updateMessage success, messageId is ' + message.messageId);
  } else {
    console.log('updateMessage error, errorCode is ' + errorCode.toString());
  }
};

JuggleIM.updateMessage(messageId, textMessage, conversation, callback);
```

</TabItem>
</Tabs>