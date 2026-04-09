---
title: 获取 @ 消息
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
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation   | Conversation  | 会话标识     | 1.0.0    |
| count | int  | 拉取数量                          | 1.0.0    |
| time  | long  | 消息时间戳，如果传 0 为当前时间 | 1.0.0    |
| direction| JIMConst.PullDirection | 拉取方向| 1.0.0    |
| callback | IMessageManager.IGetMessagesWithFinishCallback| 拉取回调 | 1.0.0 |

**示例代码**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
JIM.getInstance().getMessageManager().getMentionMessageList(conversation, 100, 0, JIMConst.PullDirection.OLDER, new IMessageManager.IGetMessagesWithFinishCallback() {
    @Override
    public void onSuccess(List<Message> messages, boolean isFinished) {

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
| conversation   | JConversation  | 会话标识     | 1.0.0    |
| count | int  | 拉取数量                          | 1.0.0    |
| time  | long  | 消息时间戳，如果传 0 为当前时间 | 1.0.0    |
| direction| JPullDirection | 拉取方向| 1.0.0    |
| successBlock | | 成功回调 | 1.0.0 |
| errorBlock | | 失败回调| 1.0.0|

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
[JIM.shared.messageManager getMentionMessages:conversation
                                        count:100
                                          time:0
                                    direction:JPullDirectionOlder
                                      success:^(NSArray<JMessage *> *messages, BOOL isFinished) {

} error:^(JErrorCode code) {

}];
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                              | 类型    | 必填     | 默认值 | 描述      | 版本     |
|----------------------------------|---------|----------|------|-----------|----------|
| conversation                     | Object  | 是     |        | 会话对象   | 1.0.0    |
| conversation.conversationType     | Number  | 是     |        | 会话类型   | 1.0.0    |
| conversation.conversationId       | String  | 是     |        | 会话 Id    | 1.0.0    |
| conversation.messageIndex         | Number  | 否     |   0    | 消息索引，查询 @ 消息会以 messageIndex 为起始点向前或向后获取 `count` 条消息   | 1.0.0    |
| conversation.count                | Number  | 否     |  20    | 获取消息条数    | 1.0.0    |
| conversation.order                | Number  | 否     |  [BACKWARD](../../../enum/web#mention_order) | 获取方向    | 1.0.0    |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.0.0    |
| result.isFinished | Boolean | @ 消息是否查询完成，false 表示服务端还有更多的 @ 消息列表 | 1.0.0    |
| result.msgs      | Array | @ 消息列表，获取消息内容可通过 [按 ID 查询消息](../get_by_ids) 获取 | 1.0.0    |

**示例代码**
```js
let { ConversationType, MentionOrder } = JIM;

let conversation = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  count: 10,
  messageIndex: 0,
  order: MentionOrder.BACKWARD
};

jim.getMentionMessages(conversation).then((result) => {
  let { isFinished, msgs } = result;
  console.log(isFinished, msgs);
})
```
</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conver   | Conversation  | 会话标识     | 1.0.0    |
| count | number  | 拉取数量                          | 1.0.0    |
| startTime  | number  | 消息时间戳，如果传 0 为当前时间 | 1.0.0    |
| isPositive| boolean | 拉取方向,true:正序；false：倒序| 1.0.0    |
| callback | QryMessagesCallback| 拉取回调 | 1.0.0 |

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getMessageManager().queryMentionMessages(conver,100,0,false,(code,msgs,hasMore)=>{
})
```

</TabItem>

<TabItem value="flutter" label="Flutter">

获取指定会话里的 @ 自己的消息列表，支持分页拉取。

**参数说明**

| 名称                           | 类型    | 描述          | 版本     |
|-------------------------------|---------|----------------|----------|
| conversation   | Conversation  | 会话标识     | 0.6.3    |
| count | int  | 拉取数量                          | 0.6.3    |
| startTime  | int  | 消息时间戳，如果传 0 为当前时间 | 0.6.3    |
| direction | int | 拉取方向,0: 拉取开始时间之后的消息；1: 拉取开始时间之前的消息| 0.6.3    |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
int count = 20;
int startTime = 0;
int direction = PullDirection.older;

GetMessageResult<List<Message>> result = await JuggleIm.instance.getMentionMessages(
  conversation,
  count,
  startTime,
  direction
);
```


**回调说明**

| 名称                   | 类型    | 描述                                    | 版本   |
|------------------------|---------|-----------------------------------------|--------|
| result                 | `GetMessageResult<List<Message>>` |  | 0.6.3  |
| result.hasMore      | bool  | 是否还有更多的 @ 消息   | 0.6.3  |
| result.t        | `List<Message>`  | 消息数组，每条消息的属性，请查看 [Message](../../../msg/message) 结构 | 0.6.3  |

</TabItem>
</Tabs>