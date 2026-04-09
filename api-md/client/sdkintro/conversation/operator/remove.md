---
title: 删除指定会话
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

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |
| callback     | IConversationManager.ISimpleCallback | 结果回调 | 1.0.0    |

**示例代码**

```java

Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "user1");
JIM.getInstance().getConversationManager().deleteConversationInfo(conversation, new IConversationManager.ISimpleCallback() {
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

| 名称           | 类型     | 描述                                      | 版本     |
|----------------|---------|---------------------------------------------|----------|
| conversation   | JConversation | 会话标识 | 1.0.0    |
| successBlock |  | 成功回调 | 1.0.0    |
| errorBlock   |  | 失败回调 | 1.0.0    |

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"user1"];

[JIM.shared.conversationManager deleteConversationInfoBy:conversation
                                                success:^{
  
} error:^(JErrorCode code) {
  
}];
```

</TabItem>
<TabItem value="js">

删除会话多端同步，本地和云端会一起删除，会话删除成功后会触发 [会话删除监听](../../../watcher/conversation)

**参数说明**

| 名称           | 类型     | 必填   | 默认值  | 描述                                      | 版本     |
|----------------|---------|-------|---|---------------------------------------------|----------|
| conversation   | Object | 是     | 无 | 删除的会话，支持删除单个会话，或者传入一个会话数组 | 1.0.0    |


**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

// 删除单个会话
jim.removeConversation(conversation).then(() => {
  console.log('remove conversation successfully');
});

// 批量删除会话
let conversations = [conversation];
jim.removeConversation(conversation).then(() => {
  console.log('remove conversations successfully');
});
```
</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |
| CommonCallback     |  | 结果回调 | 1.0.0    |

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getConversationManager().delConversation(conver,(code)=>{
  
})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

删除会话多端同步，本地和云端会一起删除，会话删除成功后会触发 [会话删除监听](../../../watcher/conversation)。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation              | Conversation | 会话标识 | 0.6.3    |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.private, 'user1');
Result result = await JuggleIm.instance.deleteConversationInfo(conversation);
```

</TabItem>
<TabItem value="reactnative">

删除会话多端同步，本地和云端会一起删除，会话删除成功后会触发 [会话删除监听](../../../watcher/conversation)。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation              | Object | 会话标识 | 0.6.3    |
| conversationType              | Number | 会话类型 | 0.6.3    |
| conversationId              | String | 会话ID | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.deleteConversationInfo({
  conversationType: 1,
  conversationId: 'user1'
});
```

</TabItem>
</Tabs>