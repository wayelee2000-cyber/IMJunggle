---
title: Withdraw message
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
]
}>
<TabItem value="android">

Only messages sent by yourself can be withdrawn. After a successful withdrawal, other users in the corresponding session will receive the onMessageRecall callback (requires adding the [message event listener](../../watcher/message.md)).

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| messageId | String | Message ID | 1.0.0 |
| extras | ```Map<String, String>``` | Extended information | 1.0.0 |
| callback | IRecallMessageCallback | Callback | 1.0.0 |

**Sample Code**

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

Only messages sent by yourself can be withdrawn. After a successful withdrawal, other users in the corresponding session will receive the messageDidRecall: callback (requires adding the [message event listener](../../watcher/message.md)).

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| messageId | NSString | Message ID | 1.0.0 |
| extras | ```NSDictionary <NSString *, NSString *>``` | Extended information; both key and value must be NSString | 1.0.0 |
| successBlock |  | Success callback | 1.0.0 |
| errorBlock |  | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
NSMutableDictionary *extras = [NSMutableDictionary dictionary];
[extras setObject:@"value1" forKey:@"key1"];
[JIM.shared.messageManager recallMessage:@"messageId1" extras:extras success:^(JMessage *message) {
	
} error:^(JErrorCode errorCode) {
	
}];
```

</TabItem>
<TabItem value="js">

Only messages sent by yourself can be withdrawn. Group administrators can withdraw any message in the group. For example, user A withdraws a message sent to user B. After a successful withdrawal, A's other devices and B will receive a [notification message](../../watcher/message.md#recall).

**Parameter description**

| Name | Type | Required | Description | Version |
|----------------------------|----------|----------|--------------------------------------------------------|--------|
| message | Object | Yes | Message object; messages can be obtained from [Historical Messages](../histories/get_all.md) | 1.0.0 |
| message.conversationType | Number | Yes | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| message.conversationId | String | Yes | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, this is the group ID | 1.0.0 |
| message.messageId | String | Yes | ID of the message to be withdrawn | 1.0.0 |
| message.sentTime | Number | Yes | Timestamp when the message was sent | 1.0.0 |
| message.exts | Object | No | Extended information for recalling the message | 1.7.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code if the operation fails. You can check `error.msg` or refer to [Status Code](../../status_code/web.md) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

// In actual projects, you can directly pass the message object returned by the SDK into the recallMessage method
let message = { 
  conversationType: ConversationType.PRIVATE, 
  conversationId: 'userid01',
  messageId: 'xxxdkadhdsa',
  sentTime: 1702180128970,
  exts: {
    name: 'xiaoshan',
    custom1: 'HaHa',
    //...more custom properties
  }
};

jim.recallMessage(message).then(() => {
  console.log('Message recalled successfully');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

Only messages sent by yourself can be withdrawn. Group administrators can withdraw any message in the group. For example, user A withdraws a message sent to user B. After a successful withdrawal, A's other devices and B will receive notification messages.

**Parameter description**

| Name | Type | Description | Version |
|-----------|----------|----------------|----------|
| messageId | String | The ID of the message to be recalled | 1.0.0 |
| extras | Object | Extended information | 1.0.0 |

**Sample Code**

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
