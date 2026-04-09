---
title: 设置已读
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
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

**设置已读**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid2");
List<String> messageIds = new ArrayList<>(2);
messageIds.add("messageId1");
messageIds.add("messageId2");
JIM.getInstance().getMessageManager().sendReadReceipt(conversation, messageIds, new IMessageManager.ISendReadReceiptCallback() {
	@Override
	public void onSuccess() {
		Log.d("TAG", "send read receipt success");
	}

	@Override
	public void onError(int errorCode) {
		Log.e("TAG", "send read receipt error, code is " + code);
	}
});
```

**获取群阅读状态**

```java
/**
 * 获取群消息阅读状态
 * @param conversation 消息所在会话
 * @param messageId 需要查询的群消息 id
 * @param callback 结果回调
 */
void getGroupMessageReadDetail(Conversation conversation,
                                String messageId,
                                IGetGroupMessageReadDetailCallback callback);
```

</TabItem>
<TabItem value="ios">

**设置已读**

```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
NSArray *messageIds = @[@"messageId1", @"messageId2"];
[JIM.shared.messageManager sendReadReceipt:messageIds
                            inConversation:c
								   success:^{
	NSLog(@"sendReadReceipt success");
} error:^(JErrorCode code) {
	NSLog(@"sendReadReceipt error, code is %d", code);
}];
```

**获取群阅读状态**

```objectivec
/// 获取群消息阅读状态
/// - Parameters:
///   - messageId: 需要查询的群消息 id
///   - conversation: 消息所在会话
///   - successBlock: 成功回调，readMemberIds 存放已读用户 id 列表，unreadMemberIds 存放未读用户 id 列表
///   - errorBlock: 失败回调
- (void)getGroupMessageReadDetail:(NSString *)messageId
                   inConversation:(JConversation *)conversation
                          success:(void (^)(NSArray<JUserInfo *> *readMembers, NSArray<JUserInfo *> *unreadMembers))successBlock
                            error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.messageId              | String   | 是    |         |消息 UId                                      | 1.0.0  |
| message.unreadIndex            | Number   | 是    |         |消息索引，可从 `message.messageIndex` 获取   | 1.0.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

// 方式一：单条消息设置已读
let message = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  unreadIndex: 1
};
jim.readMessage(message).then(() => {
  console.log('read message successfully.')
}, (error) => {
  console.log(error)
});

// 方式二：多条消息设置已读
let msgs = [
  {
    conversationType: ConversationType.GROUP,
    conversationId: 'groupid1',
    messageId: 'xxxdkadhdsa',
    unreadIndex: 2
  }
];
jim.readMessage(msgs).then(() => {
  console.log('read message successfully.')
}, (error) => {
  console.log(error)
});
```
</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conver                   | Conversation  | 消息所在会话                          | 1.0.0    |
| msgIds                        | string[]  | 需要发送阅读回执的消息  id 列表                           | 1.0.0    |
| callback         | CommonCallback  | 回调 | 1.0.0    |

**示例代码**

```java
 let conver = new Conversation("userid1",1)
JuggleIm.instance.getMessageManager().sendReadReceipt(conver,["message_id"],(code)=>{
    
})
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

**参数说明**

| 名称                           | 类型    | 描述          | 版本     |
|-------------------------------|---------|----------------|----------|
| conversation   | Conversation  | 会话标识     | 1.0.0    |
| messageIds | string[] | 需要发送阅读回执的消息  id 列表  | 1.0.0    |

**示例代码**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1,
  id: 'userId1'
};

const messageIds = ['messageId1', 'messageId2'];

JuggleIM.sendReadReceipt(conversation, messageIds).then((success) => {
  console.log('sendReadReceipt success:', success);
});
```
</TabItem>


</Tabs>