---
title: 清空单个会话未读数
hide_title: true
sidebar_position: 9
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

| 名称                             | 类型    | 描述       | 版本     |
|----------------------------------|--------|------------|----------|
| conversation                     | Conversation  |   会话标识         | 1.0.0    |
| callback | IConversationManager.ISimpleCallback |  结果回调 | 1.0.0    |

**示例代码**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupid1");
JIM.getInstance().getConversationManager().clearUnreadCount(conversation, new IConversationManager.ISimpleCallback() {
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

| 名称                             | 类型    | 描述       | 版本     |
|----------------------------------|--------|------------|----------|
| conversation                     | JConversation  |   会话标识         | 1.0.0    |

**示例代码**
```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupid1"];
[JIM.shared.conversationManager clearUnreadCountByConversation:conversation
                                                        success:^{
    
} error:^(JErrorCode code) {

}];
```

</TabItem>
<TabItem value="js">

**参数说明**

| 名称                             | 类型    | 必填   | 默认值  | 描述       | 版本     |
|----------------------------------|---------|--------|--------|------------|----------|
| conversation                     | Object  | 是     |        |            | 1.0.0    |
| conversation.conversationType     | Number  | 是     |        | 会话类型   | 1.0.0    |
| conversation.conversationId       | String  | 是     |        | 会话 Id    | 1.0.0    |
| conversation.unreadIndex         | Number  | 是     |        | 会话最后一条消息的索引, 可在 `conversation.latestUnreadIndex` 获取   | 1.0.0    |
| conversation.messageId            | String  | 是     |        | 会话最后的 messageId, 可在 `conversation.latestMessage` 获取   | 1.0.0    |
| conversation.messageSentTime      | Number  | 是     |        | 会话最后一条消息的发送时间 可在 `conversation.latestMessage` 获取   | 1.0.0    |

**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId02',
  messageSentTime: 1724675506002,
  messageId: 'djdjakdk394alkjda',
  unreadIndex: 9
};

jim.clearUnreadcount(conversation).then(() => {
  console.log('clear unreadCount successfully');
})
```
</TabItem>
<TabItem value="flutter">

**参数说明**

| 名称                             | 类型    | 描述       | 版本     |
|----------------------------------|--------|------------|----------|
| conversation                     | Conversation  |   会话标识         | 0.6.3    |

**示例代码**
```dart
Conversation conversation = Conversation(ConversationType.private, 'user1');
Result result = await JuggleIm.instance.clearUnreadCount(conversation);
```

</TabItem>
<TabItem value="reactnative">

**参数说明**

| 名称                             | 类型    | 描述       | 版本     |
|----------------------------------|--------|------------|----------|
| conversation                     | Object  |   会话标识         | 0.6.3    |
| conversationType                 | Number  |   会话类型         | 0.6.3    |
| conversationId                   | String  |   会话ID         | 0.6.3    |

**示例代码**
```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.clearUnreadCount({
  conversationType: 1,
  conversationId: 'user1'
});
```

</TabItem>
<TabItem value="harmony">

**参数说明**

| 名称                             | 类型    | 描述       | 版本     |
|----------------------------------|--------|------------|----------|
| conver                     | Conversation  |   会话标识         | 1.0.0    |
| callback | CommonCallback |  结果回调 | 1.0.0    |

**示例代码**
```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getConversationManager().clearUnreadCount(conver,(code)=>{
  
})
```

</TabItem>
</Tabs>