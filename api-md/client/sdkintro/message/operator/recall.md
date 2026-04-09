---
title: 撤回消息
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
{ label: '鸿蒙', value: 'harmony', },
]
}>
<TabItem value="android">

只允许撤回自己发送的消息。撤回成功后，对应会话中的其他用户会收到 onMessageRecall 回调（需要添加[消息监听](../../../watcher/message)）

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| messageId                   | String | 消息 id                        | 1.0.0    |
|extras | ```Map<String, String>``` | 扩展信息 | 1.0.0 |
| callback         | IRecallMessageCallback  | 回调 | 1.0.0    |

**示例代码**

```java
Map<String, String> extras = new HashMap<>();
extras.put("key1", "value1");
JIM.getInstance().getMessageManager().recallMessage("messageId1", extras, new IMessageManager.IRecallMessageCallback() {
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

只允许撤回自己发送的消息。撤回成功后，对应会话中的其他用户会收到 messageDidRecall: 回调（需要添加[消息监听](../../../watcher/message)）

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| messageId                        | NSString  | 消息 id                           | 1.0.0    |
|extras | ```NSDictionary <NSString *, NSString *>``` | 扩展信息，key 和 value 都必须为 NSString | 1.0.0 |
| successBlock         |   | 成功回调 | 1.0.0    |
| errorBlock                   |   | 失败回调 | 1.0.0    |

**示例代码**

```objectivec
NSMutableDictionary *extras = [NSMutableDictionary dictionary];
[extras setObject:@"value1" forKey:@"key1"];
[JIM.shared.messageManager recallMessage:@"messageId1" extras:extras success:^(JMessage *message) {
	
} error:^(JErrorCode errorCode) {
	
}];
```

</TabItem>
<TabItem value="js">

只允许撤回自己发送的消息，群组管理员可以撤群内所有消息，A 撤回发给 B 的消息，撤回成功后，A 的其他设备和 B 会收到 [通知消息](../../../watcher/message#recall) 


**参数说明**

| 名称                       | 类型     | 是否必需 | 描述                                                 | 版本   |
|----------------------------|----------|----------|------------------------------------------------------|--------|
| message                    | Object   | 是       | 消息对象，可在 [历史消息](../../histories/get_all) 获取消息| 1.0.0  |
| message.conversationType   | Number   | 是       | [会话类型](../../../../sdkintro/enum/web#conversation)                   | 1.0.0  |
| message.conversationId     | String   | 是       | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0  |
| message.messageId          | String   | 是       | 被撤回的消息 Id                                       | 1.0.0  |
| message.sentTime           | Number   | 是       | 被撤回的消息的发送时间                                | 1.0.0  |
| message.exts               | Object   | 否       | 撤回消息时的扩展信息                                | 1.7.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

// 实际项目中，可以直接把 SDK 返回 message 对象传入 recallMessage 方法
let message = { 
  conversationType: ConversationType.PRIVATE, 
  conversationId: 'userid01',
  messageId: 'xxxdkadhdsa',
  sentTime: 1702180128970,
  exts: {
    name: 'xiaoshan',
    custom1: 'HaHa',
    //... 更多自定义属性
  }
};

jim.recallMessage(message).then((result) => {
  console.log('recall message successfully');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="harmony">

只允许撤回自己发送的消息。撤回成功后，对应会话中的其他用户会收到 onMessageRecall 回调（需要添加[消息监听](../../../watcher/message)）

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conver     |  Conversation |  所属会话 | 1.0.0|
| msgId                   | string | 消息 id                        | 1.0.0    |
|extras | ```Map<string, string>``` | 扩展信息 | 1.0.0 |
| callback         | IRecallMessageCallback  | 回调 | 1.0.0    |

**示例代码**

```java
let conver = new Conversation("userid1",1)
let extras:HashMap<string,string> = new HashMap()
extras.set("key1","value1")
JuggleIm.instance.getMessageManager().recallMessage(conver,"messageid",extras,(code,msg)=>{

})
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

只允许撤回自己发送的消息，群组管理员可以撤群内所有消息，A 撤回发给 B 的消息，撤回成功后，A 的其他设备和 B 会收到通知消息

**参数说明**

| 名称      | 类型    | 描述          | 版本     |
|-----------|---------|----------------|----------|
| messageId | String  | 需要撤回的消息 Id  | 1.0.0    |
| extras | Object | 扩展信息 | 1.0.0    |

**示例代码**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const messageId = 'messageId1';
const extras = {
  key1: 'value1'
};

const success = await JuggleIM.recallMessage(messageId, extras);
console.log('recallMessage success:', success);
```

</TabItem>
</Tabs>