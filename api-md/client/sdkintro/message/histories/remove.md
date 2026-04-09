---
title: 删除历史消息
hide_title: true
sidebar_position: 4
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

删除本地和云端的己方历史消息，自己的多设备会同步删除，接口调用成功后不影响对方或群里的其他成员继续查看消息，支持批量删除同一会话的多条消息。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation                   | Conversation  | 会话标识                          | 1.0.0    |
|clientMsgNoList| List[] | 本端消息唯一编号列表| 1.0.0|
|callback | IMessageManager.ISimpleCallback| 结果回调| 1.0.0|

**示例代码**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
List<Long> clientMsgNoList = new ArrayList<>();
clientMsgNoList.add(111L);
clientMsgNoList.add(222L);
clientMsgNoList.add(333L);
JIM.getInstance().getMessageManager().deleteMessagesByClientMsgNoList(conversation, clientMsgNoList, new IMessageManager.ISimpleCallback() {
    @Override
    public void onSuccess() {

    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

删除本地和云端的己方历史消息，自己的多设备会同步删除，接口调用成功后不影响对方或群里的其他成员继续查看消息，支持批量删除同一会话的多条消息。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation                   | JConversation  | 会话标识                          | 1.0.0    |
|clientMsgNoList| ```NSArray <NSNumber *>``` | 本端消息唯一编号列表| 1.0.0|
|successBlock | | 成功回调| 1.0.0|
|errorBlock | | 失败回调| 1.0.0|

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
NSArray <NSNumber *> *clientMsgNoList = @[@(111), @(222), @(333)];
[JIM.shared.messageManager deleteMessagesByClientMsgNoList:clientMsgNoList
                                              conversation:conversation
                                                    success:^{
    
} error:^(JErrorCode errorCode) {
    
}];
```

</TabItem>
<TabItem value="js">

删除本地和云端的己方历史消息，自己的多设备会同步删除，接口调用成功后**不影响**对方或群里的其他成员继续查看消息，支持批量删除同一会话的多条消息，参数 _messages_ 是消息数组，每一项 `message` 说明如下：

**参数说明**

| 名称                     | 类型    | 是否必需 | 默认值 | 描述                                                  | 版本   |
|--------------------------|---------|----------|--------|-------------------------------------------------------|--------|
| message                   | Object  | 是       | -      | 清理历史消息                                           | 1.0.0  |
| message.conversationType  | Number  | 是       | -      | [会话类型](../../../enum/web#conversation)                    | 1.0.0  |
| message.conversationId    | String  | 是       | -      | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0  |
| message.messageIndex      | Number  | 是       | -      | 消息的索引，可在 [Message](../../../msg/message) 中获取 | 1.0.0  |
| message.sentTime          | Number  | 是       | -      | 消息的发送时间，可在 [Message](../../../msg/message) 中获取 | 1.0.0  |
| message.tid         | String  | 是       | -      | 消息的 ID ，可在 [Message](../../../msg/message) 中获取 | 1.0.0  |
| message.messageId         | String  | 是       | -      | 消息的唯一 ID ，可在 [Message](../../../msg/message) 中获取 | 1.0.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

// 示例为模拟数据，实际调用可从历史消息接口中获取
let messages = [
  {
    conversationType: ConversationType.PRIVATE, 
    conversationId: 'userid1', 
    messageIndex: 128, 
    sentTime: 1714235241490, 
    messageId: 'nreayt7ha4ggqlcv',
    tid: 'nreayt7ha4ggqlcv',
  },
  //...
];

jim.removeMessages(messages).then(() => {
  console.log('remove messages successfully.')
});
```
</TabItem>
<TabItem value="harmony">

删除本地和云端的己方历史消息，自己的多设备会同步删除，接口调用成功后不影响对方或群里的其他成员继续查看消息，支持批量删除同一会话的多条消息。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conver                   | Conversation  | 会话标识                          | 1.0.0    |
|msgIds| string[] | 本端消息唯一编号列表| 1.0.0|
|delScope|number|0:只删除自己一侧；1:双向删除，会话中其他用户也无法看到|1.0.0|
|callback | CommonCallback| 结果回调| 1.0.0|

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getMessageManager().delMessages(conver,["message_id1","message_id2"],1,(code)=>{})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

**参数说明**

| 名称                | 类型    | 必填  | 默认值           | 描述                                       | 版本   |
|---------------------|---------|------|------------------|-----------------------------------------|--------|
| conversation        | Conversation  | 是   |         | 会话对象，会话类型是 `private` 时，会话 Id 是对方的 userId，会话类型是 `group` 时是群组 Id | 0.6.3  |
| startTime           | int  | 是   |         | 时间戳，比这个时间更早的消息将被删除。0 表示默认的当前时间 | 0.6.3  |
| forAllUsers         | bool  | 否   | false  | 删除消息作用域，`true` 删除所有用户的历史消息，`false` 仅删除当前用户的历史消息 | 0.6.3  |

**forAllUsers 适用场景**

> 群组场景：分权限控制删除按钮，例如管理员可显示删除全员历史消息，普通成员仅可显示删除自己的历史消息。

> 单聊场景：通常会显示仅删除自己和对方的历史消息


**示例代码**

```dart
Conversation conversation = Conversation(2, 'groupId1');
List<int> clientMsgNoList = [1000, 10001];
bool forAllUsers = false;
await JuggleIm.instance.deleteMessagesByClientMsgNoList(conversation, clientMsgNoList, forAllUsers);
```
</TabItem>
</Tabs>