---
title: 清空历史消息
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
{ label: '鸿蒙', value: 'harmony', },
]
}>
<TabItem value="android">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation                   | Conversation  | 会话标识                          | 1.0.0    |
|startTime| long | startTime 之前的消息将被清除，传 0 表示当前时间| 1.0.0|
|callback | IMessageManager.ISimpleCallback| 结果回调| 1.0.0|

**示例代码**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
JIM.getInstance().getMessageManager().clearMessages(conversation, 0, new IMessageManager.ISimpleCallback() {
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

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation                   | JConversation  | 会话标识                          | 1.0.0    |
|startTime| long long | startTime 之前的消息将被清除，传 0 表示当前时间| 1.0.0|
|successBlock | | 成功回调| 1.0.0|
|errorBlock | | 失败回调| 1.0.0|

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
[JIM.shared.messageManager clearMessagesIn:conversation
                                  startTime:0
                                   success:^{
    
} error:^(JErrorCode errorCode) {
    
}];
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                     | 类型    | 是否必需 | 默认值 | 描述                                                  | 版本   |
|--------------------------|---------|----------|--------|-------------------------------------------------------|--------|
| params                   | Object  | 是       | -      | 清理历史消息                                           | 1.0.0  |
| params.conversationType  | Number  | 是       | -      | [会话类型](../../../enum/web#conversation)                    | 1.0.0  |
| params.conversationId    | String  | 是       | -      | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0  |
| params.time              | Number  | 是       | -      | 清理指定时间之前的历史消息, 清理全部可传入会话最后一条消息的 sentTime | 1.0.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2',
  time: 1702180128970
};

jim.clearMessage(params).then((result) => {
  console.log('clear messages successfully');
}, (error) => {
  console.log(error);
})
```
</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation                   | Conversation  | 会话标识                          | 1.0.0    |
|startTime| long | startTime 之前的消息将被清除| 1.0.0|
|callback | CommonCallback| 结果回调| 1.0.0|

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getMessageManager().clearMessages(conver,new Date().getTime(),(code)=>{

})
```

</TabItem>
<TabItem value="flutter">

**参数说明**

| 名称                | 类型    | 必填  | 默认值           | 描述                                       | 版本   |
|---------------------|---------|------|------------------|-----------------------------------------|--------|
| conversation        | Conversation  | 是   |         | 会话对象，会话类型是 `private` 时，会话 Id 是对方的 userId，会话类型是 `group` 时是群组 Id | 0.6.3  |
| startTime           | int  | 是   |         | 时间戳，比这个时间更早的消息将被清除。0 表示默认的当前时间 | 0.6.3  |
| forAllUsers         | bool  | 否   | false  | 清除消息作用域，`true` 清理所有用户的历史消息，`false` 仅清理当前用户的历史消息 | 0.6.3  |

**forAllUsers 适用场景**

> 群组场景：分权限控制清理按钮，例如管理员可显示清空全员历史消息，普通成员仅可显示清空自己的历史消息。

> 单聊场景：通常会显示仅清空自己和对方的历史消息

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
int startTime = 0;
bool forAllUsers = false;

await JuggleIm.instance.clearMessages(conversation, startTime, forAllUsers);
```

</TabItem>
</Tabs>