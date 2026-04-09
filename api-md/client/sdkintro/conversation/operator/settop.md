---
title: 设置会话置顶
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

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |
| isTop     | boolean | 是否置顶 | 1.0.0    |
| callback | ISimpleCallback | 结果回调 | 1.0.0    |

**示例代码**

```java
JIM.getInstance().getConversationManager().setTop(conversation, true, new IConversationManager.ISimpleCallback() {
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

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| isTop | BOOL | 是否置顶 | 1.0.0    |
| conversation     | JConversation | 会话标识 | 1.0.0    |
| successBlock |  | 成功回调 | 1.0.0    |
| errorBlock |  | 失败回调 | 1.0.0    |

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
[JIM.shared.conversationManager setTop:YES
                          conversation:conversation
                                success:^{
    
} error:^(JErrorCode code) {
    
}];
```


</TabItem>
<TabItem value="js">

设置会话置顶，支持多端同步，设置会话置顶方法调用成功后会触发 [会话变更监听](../../../watcher/conversation)

**参数说明**

| 名称                             | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------------------------|---------|-------|--------|----------|----------|
| conversation                    | Object | 是     | 无 | 会话对象 | 1.0.0    |
| conversation.conversationType   | Number | 是     | 无 | 会话类型 | 1.0.0    |
| conversation.conversationId     | String | 是     | 无 | 会话 Id | 1.0.0    |
| conversation.isTop              | Boolean | 是     | 无 | 是否置顶 | 1.0.0    |

**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01',
  isTop: true
};

jim.setTopConversation(conversation).then(() => {
  console.log('set conversation top successfully');
});
```
</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conver | Conversation | 会话标识 | 1.0.0    |
| isTop     | boolean | 是否置顶 | 1.0.0    |
| callback | CommonCallback | 结果回调 | 1.0.0    |

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getConversationManager().setTop(conver,true,(code)=>{
  
})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

设置会话置顶，支持多端同步，设置会话置顶方法调用成功后会触发 [会话变更监听](../../../watcher/conversation)。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 	会话标识 | 0.6.3    |
| isTop         | bool | 是否置顶 | 0.6.3    |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.private, 'user1');
await JuggleIm.instance.setTop(conversation, true);
```

</TabItem>
<TabItem value="reactnative">

设置会话置顶，支持多端同步，设置会话置顶方法调用成功后会触发 [会话变更监听](../../../watcher/conversation)。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Object | 会话标识 | 0.6.3    |
| conversationType | Number | 会话类型 | 0.6.3    |
| conversationId | String | 会话ID | 0.6.3    |
| isTop         | Boolean | 是否置顶 | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.setTop({
  conversationType: 1,
  conversationId: 'user1',
  isTop: true
});
```

</TabItem>
</Tabs>