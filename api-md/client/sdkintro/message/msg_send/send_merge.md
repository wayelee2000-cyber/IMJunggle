---
title: 合并转发
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

先构建 MergeMessage，再使用 sendMessage 接口发送。

**MergeMessage 结构**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| title                        | String  | 合并消息的标题                                           | 1.0.0    |
| conversation                   | Conversation  | 会话标识，所有被合并的消息必须来自同一会话           | 1.0.0    |
| messageIdList         | List  | 所有被合并的消息 id 列表，不能超过 100 条 | 1.0.0    |
| previewList         |  List | 消息气泡上用来预览的被合并消息列表，不能超过 10 条 | 1.0.0    |


**示例代码**

```java
// 被合并的消息所处的会话
Conversation srcConversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");

List<String> messageIdList = new ArrayList<>();
messageIdList.add("messageId1");
messageIdList.add("messageId2");
messageIdList.add("messageId3");

List<MergeMessagePreviewUnit> previewList = new ArrayList<>();
for (int i = 0; i < 3; i++) {
    MergeMessagePreviewUnit unit = new MergeMessagePreviewUnit();
    unit.setPreviewContent("previewContent" + i);
    UserInfo userInfo = new UserInfo();
    userInfo.setUserId("userId" + i);
    userInfo.setUserName("userName" + i);
    unit.setSender(userInfo);
    previewList.add(unit);
}
MergeMessage merge = new MergeMessage("title", srcConversation, messageIdList, previewList);

// 将要转发的目标会话
Conversation dstConversation = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
Message m = JIM.getInstance().getMessageManager().sendMessage(merge, dstConversation, new IMessageManager.ISendMessageCallback() {
    @Override
    public void onSuccess(Message message) {
    }

    @Override
    public void onError(Message message, int errorCode) {
    }
});
```

**获取被合并的消息列表**

```java
/**
 * 获取被合并的消息列表
 * @param containerMsgId 合并消息 id
 * @param callback 结果回调
 */
void getMergedMessageList(String containerMsgId,
                          IGetMessagesCallback callback);
```

</TabItem>

<TabItem value="ios">

先构建 JMergeMessage，再使用 sendMessage 接口发送。

**JMergeMessage 结构**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| title                        | NSString  | 合并消息的标题                                           | 1.0.0    |
| conversation                   | JConversation  | 会话标识，所有被合并的消息必须来自同一会话           | 1.0.0    |
| messageIdList         | ```NSArray <NSString *>```  | 所有被合并的消息 id 列表，不能超过 100 条 | 1.0.0    |
| previewList         |  ```NSArray <JMergeMessagePreviewUnit *>``` | 消息气泡上用来预览的被合并消息列表，不能超过 10 条 | 1.0.0    |

**示例代码**

```objectivec
NSArray *messageIdList = @[@"messageId1", @"messageId2", @"messageId3", @"messageId4"];
NSMutableArray *previewList = [NSMutableArray array];

for (int i = 0; i < 4; i++) {
    JMergeMessagePreviewUnit *unit = [[JMergeMessagePreviewUnit alloc] init];
    unit.previewContent = [NSString stringWithFormat:@"previewContent%d", i];
    JUserInfo *userInfo = [[JUserInfo alloc] init];
    userInfo.userId = [NSString stringWithFormat:@"userId%d", i];
    userInfo.userName = [NSString stringWithFormat:@"name%d", i];
    userInfo.portrait = @"portait";
    unit.sender = userInfo;
    [previewList addObject:unit];
}
// 被合并的消息所处的会话
JConversation *srcConversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid1"];
JMergeMessage *merge = [[JMergeMessage alloc] initWithTitle:@"title"
                                                conversation:srcConversation
                                              MessageIdList:messageIdList
                                                previewList:previewList];
// 将要转发的目标会话
JConversation *dstConversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.messageManager sendMessage:merge
                        inConversation:dstConversation
                                success:^(JMessage *message) {
    
} error:^(JErrorCode errorCode, JMessage *message) {
    
}];
```

**获取被合并的消息列表**

```objectivec
/// 获取被合并的消息列表
/// - Parameters:
///   - messageId: 合并消息 id
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)getMergedMessageList:(NSString *)messageId
                     success:(void (^)(NSArray<JMessage *> *mergedMessages))successBlock
                       error:(void (^)(JErrorCode code))errorBlock;
```


</TabItem>
<TabItem value="js">

**messages 参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.messages               | Array   | 是     |        | 合并转发的消息列表，格式见下方示例                                       | 1.0.0    |
| message.previewList            | Array    | 是     |       | 自定义的消息内容简介，数组内容和多端约定好即可               | 1.0.0    |
| message.title                  | String  | 是     |        | 转发消息的标题   | 1.0.0    |
| lifeTime                   | Number    | 否    |  0    |消息的销毁时间段，必须大于 `0`, 单位 `ms`, 例如 60s: `1 * 60 * 1000`   | 1.9.0    |
| lifeTimeAfterRead             | Number    | 否    |  0    |消息的阅后即焚的时间段，必须大于 0, 单位 `ms`, 例如 60s: `1 * 60 * 1000`  | 1.9.0    |

**callbacks 参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| callbacks                      | Object  | 否     |        | 回调对象                                                      | 1.0.0    |
| callbacks.onbefore             | Function| 否     |        | 消息发送前回调，此方法触发后会返回临时消息标识 `tid`，可向页面渲染消息，消息发送成功后台根据 `tid` 更新消息状态| 1.0.0    |

**成功回调**

| 名称      | 类型    | 描述                                                                      | 版本   |
|-----------|---------|---------------------------------------------------------------------------|--------|
| message   | Object  | 发送成功后返回带 `messageId` 和 `sentTime` 消息对象，消息结构请查看 [Message](../../../msg/message) | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| result | Object  | 发送失败后会返回对象中包含 `tid` 属性信息，同时包含 `error` 信息，可以直接查看 `error.msg`，或者查看 [状态码](../../../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = jetim;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid02',
  // message 是通过历史消息或在消息监听收到的消息对象
  messageIdList: [message],
  previewList: [
    { content: 'Hello Chat', sender: { name: '小可', other: '可多端约定扩展' } }
  ],
  title: '小 J 和小 G 的聊天记录'
};

let callbacks = {
  onbefore: (message) => {
    // 渲染至页面，可通过 message.tid 做唯一标识
  }
};
jetim.sendMergeMessage(params, callbacks).then((msg) => {
  console.log('send merge message successfully', msg);
}, (result) => {
  let { error, tid } = result;
  // 可根据 tid 修改消息发送失败的状态, Web 端消息失败仅在 SDK 内存中保存，刷新后将无法获取到发送失败的消息
  console.log(tid, error);
});
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

先构建 MergeMessage，再使用 sendMergeMessage 接口发送。

**MergeMessage 结构**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| title                        | String  | 合并消息的标题                                           | 1.0.0    |
| conversation           | Conversation  | 会话标识，所有被合并的消息必须来自同一会话           | 1.0.0    |
| messageIdList         | string[]  | 所有被合并的消息 id 列表，不能超过 100 条 | 1.0.0    |
| previewList         |  string[] | 消息气泡上用来预览的被合并消息列表，不能超过 10 条 | 1.0.0    |

**示例代码**

```typescript
import JuggleIM from 'juggleim-rnsdk';

// 被合并的消息所处的会话
const srcConversation = {
  type: 1,
  id: 'userId1'
};

const messageIdList = ['messageId1', 'messageId2', 'messageId3'];

const previewList = [
  {
    previewContent: 'previewContent0',
    sender: {
      userId: 'userId0',
      userName: 'userName0'
    }
  },
  {
    previewContent: 'previewContent1',
    sender: {
      userId: 'userId1',
      userName: 'userName1'
    }
  }
];

const mergeMessage = {
  title: 'title',
  conversation: srcConversation,
  messageIdList: messageIdList,
  previewList: previewList
};

// 将要转发的目标会话
const dstConversation = {
  type: 2,
  id: 'groupId1'
};

const callback = (message: any, errorCode: number) => {
  if (errorCode === 0) {
    console.log('sendMergeMessage success, messageId is ' + message.messageId);
  } else {
    console.log('sendMergeMessage error, errorCode is ' + errorCode.toString());
  }
};

JuggleIM.sendMergeMessage(mergeMessage, dstConversation, callback).then((message) => {
  console.log('after send, clientMsgNo is ' + message.clientMsgNo);
});
```

**获取被合并的消息列表**

```typescript
const mergedMessages = await JuggleIM.getMergedMessageList('messageId');
```

</TabItem>
<TabItem value="flutter">

**MergeMessage 结构**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| title                        | String  | 合并消息的标题                                           | 0.6.3    |
| conversation           | Conversation  | 会话标识，所有被合并的消息必须来自同一会话           | 0.6.3    |
| messageIdList         | List  | 所有被合并的消息 id 列表，不能超过 100 条 | 0.6.3    |
| previewList         |  List | 消息气泡上用来预览的被合并消息列表，不能超过 10 条 | 0.6.3    |


**示例代码**

```dart
// 将要合并消息的会话（原会话）
Conversation srcConversation = Conversation(ConversationType.group, 'groupId1');
// messages 是在原会话选择的消息列表
List<Message> messages = [];

List<MergeMessagePreviewUnit> previewList = [];
List<String> messageIdList = [];
String title = 'xxx 的聊天记录';
for (Message message in messages) {
  messageIdList.add(message.messageId);
  // 假设都是文本，如果是图片消息通常替换成 [图片]
  previewList.add(MergeMessagePreviewUnit(message.content.content, message.sender));
}
MergeMessage mergeMessage = MergeMessage.create(title, srcConversation, messageIdList, previewList);
// 将要转发的目标会话
Conversation dstConversation = Conversation(ConversationType.private, 'userId1');

DataCallback<Message> callback = (m, errorCode) {
  if (errorCode == 0) {
    print("sendMessage success, messageId is " + m.messageId);
  } else {
    print('sendMessage error, errorCode is ' + errorCode.toString() + ', clientMsgNo is ' + m.clientMsgNo!.toString());
  }
};

Message message = await JuggleIm.instance.sendMessage(mergeMessage, dstConversation, callback);
```

**获取被合并的消息列表**

```dart
Result<List<Message>> result = await JuggleIm.instance.getMergedMessageList('messageId');
```

</TabItem>
</Tabs>