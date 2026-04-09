---
title: 标记会话状态
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

标记指定会话未读状态，支持标记为 `未读` 状态，如需清理标记的未读状态，可调用 [清空单个会话未读数](../../unread/clear_unread) 接口，标记状态 SDK 自动同步至当前用户的多个设备。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.3.0    |
| callback     | ISimpleCallback | 结果回调 | 1.3.0    |

**示例代码**

```java
Conversation c = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
JIM.getInstance().getConversationManager().setUnread(c, new IConversationManager.ISimpleCallback() {
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

标记指定会话未读状态，支持标记为 `未读` 状态，如需清理标记的未读状态，可调用 [清空单个会话未读数](../../unread/clear_unread) 接口，标记状态 SDK 自动同步至当前用户的多个设备。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | JConversation | 会话标识 | 1.3.0    |
| successBlock     |  | 成功回调 | 1.3.0    |
| errorBlock     |  | 失败回调 | 1.3.0    |

**示例代码**

```objectivec
JConversation *c = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
[JIM.shared.conversationManager setUnread:c
                                  success:^{
    
} error:^(JErrorCode code) {
    
}];
```


</TabItem>
<TabItem value="js">

标记指定会话未读状态，支持标记为 `未读` 状态，如需清理标记的未读状态，可调用 [清空单个会话未读数](../../unread/clear_unread) 接口，标记状态 SDK 自动同步至当前用户的多个设备。


**参数说明**

| 名称           | 类型     | 必填   | 默认值  | 描述                                      | 版本     |
|----------------|---------|-------|---|---------------------------------------------|----------|
| conversation   | Object | 是     | 无 | 获取会话的对象 | 1.5.0    |
| conversation.conversationId   | String | 是     | 无 | 会话 Id | 1.5.0    |
| conversation.conversationType | Number | 是     | 无 | 会话类型 | 1.5.0    |
| conversation.unreadTag        | Number | 是     |  | [会话标记状态](../../../enum/web#unreadtag)| 1.5.0    |

**示例代码**

```js
jim.markUnread({
  conversationId: '7KeH8fjCO',
  conversationType: 2,
  unreadTag: UnreadTag.UNREAD,
}).then(() => {
  console.log('markunread successfully')
}, (error) => {
  console.log(error)
});

```
</TabItem>

<TabItem value="harmony">

标记指定会话未读状态，支持标记为 `未读` 状态，如需清理标记的未读状态，可调用 [清空单个会话未读数](../../unread/clear_unread) 接口，标记状态 SDK 自动同步至当前用户的多个设备。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.3.0    |
| callback     | ISimpleCallback | 结果回调 | 1.3.0    |

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getConversationManager().setUnread(conver,(code)=>{
  
})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

标记指定会话未读状态，支持标记为 `未读` 状态，如需清理标记的未读状态，可调用 [清空单个会话未读数](../../unread/clear_unread) 接口，标记状态 SDK 自动同步至当前用户的多个设备, 设置成功后会话变更事件会触发。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 0.6.3    |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
await JuggleIm.instance.setUnread(conversation);
```

</TabItem>
<TabItem value="reactnative">

标记指定会话未读状态，支持标记为 `未读` 状态，如需清理标记的未读状态，可调用 [清空单个会话未读数](../../unread/clear_unread) 接口，标记状态 SDK 自动同步至当前用户的多个设备，设置成功后会话变更事件会触发。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Object | 会话标识 | 0.6.3    |
| conversationType | Number | 会话类型 | 0.6.3    |
| conversationId | String | 会话ID | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.setUnread({
  conversationType: 2,
  conversationId: 'groupId1'
});
```

</TabItem>
</Tabs>