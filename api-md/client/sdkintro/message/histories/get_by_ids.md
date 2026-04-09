---
title: 通过 Id 获取历史消息
hide_title: true
sidebar_position: 8
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

根据 messageId 数组获取对应的本地消息。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| messageIdList                   | List  | 消息 id 列表                          | 1.0.0    |

**示例代码**

```java
List<Message> messageList = JIM.getInstance().getMessageManager().getMessagesByMessageIds(messageIds);
```
</TabItem>
<TabItem value="ios">

根据 messageId 数组获取对应的本地消息。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| messageIds                   | NSArray  | 消息 id 列表                          | 1.0.0    |

**示例代码**

```objectivec
NSArray *messages = [JIM.shared.messageManager getMessagesByMessageIds:messageIds];
```

</TabItem>
<TabItem value="js">

通过消息 Id 获取消息内容，支持一次性查询多条消息，需要保证传入的 messageIds 属于同一个会话

**参数说明**

| 名称                | 类型    | 必填  | 默认值           | 描述                                                                      | 版本   |
|---------------------|---------|------|------------------|---------------------------------------------------------------------------|--------|
| params              | Object  | 是   |                | 历史消息获取参数                                                           | 1.0.0  |
| params.conversationType | Number  | 是   |                | [会话类型](../../enum/web#conversation)                                       | 1.0.0  |
| params.conversationId   | String  | 是   |                | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0  |
| message.messageIds      | Array   | 是     |               | 获取的消息 Id 数组                              | 1.0.0    |

**成功回调**

| 名称                   | 类型    | 描述                                    | 版本   |
|------------------------|---------|-----------------------------------------|--------|
| result                 | Object  |                                        | 1.0.0  |
| result.messages        | Object  | 消息数组，每条消息的属性，请查看 [Message](../msg/message) 结构 | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2',
  messageIds: ['nnx3axfbglsgv6fp', 'nnx3aw5wglqgv6fp']
};

jim.getMessagesByIds(params).then((result) => {
  let { messages } = result;
  console.log(messages);
}, (error) => {
  console.log(error);
})
```
</TabItem>
<TabItem value="harmony">

根据 messageId 数组获取对应的本地消息。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| msgIds                   | string[]  | 消息 id 列表                          | 1.0.0    |

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getMessageManager().getMessagesByIds(conver,["message_id1","message_id2"],(code,msgs)=>{
  
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

根据 messageId 数组获取对应的本地消息。

**参数说明**

| 名称                 | 类型    | 描述                              | 版本     |
|----------------------|---------|------------------------------------|----------|
| messageIdList        | `List<String>`  | 消息 id 列表                          | 0.6.3    |

**示例代码**

```dart
List<String> messageIds = ["msg_id_01", "msg_id_02"];
List<Message> messages = await JuggleIm.instance.getMessagesByMessageIdList(messageIds);
```

`messages` 消息数组，每条消息的属性，请查看 [Message](../../../msg/message) 结构

</TabItem>
</Tabs>