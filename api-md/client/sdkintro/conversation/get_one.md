---
title: 获取单个会话
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

根据会话标识 `Conversation` 获取指定会话信息。返回空对象表示没有会话信息。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |

**示例代码**
```java
ConversationInfo info = JIM.getInstance().getConversationManager().getConversationInfo(conversation);
```

</TabItem>
<TabItem value="ios">

根据会话标识 `JConversation` 获取指定会话信息。返回空对象表示没有会话信息。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | JConversation | 会话标识 | 1.0.0    |

**示例代码**
```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
JConversationInfo *info = [JIM.shared.conversationManager getConversationInfo:conversation];
```

</TabItem>
<TabItem value="js">

根据 `conversationType` 和 `conversationId` 获取指定会话，如果本地没有会从云端获取，返回空对象表示没有会话信息

**参数说明**

| 名称           | 类型     | 必填   | 默认值  | 描述                                      | 版本     |
|----------------|---------|-------|---|---------------------------------------------|----------|
| conversation   | Object | 是     | 无 | 获取会话的对象 | 1.0.0    |
| conversation.conversationId   | String | 是     | 无 | 会话 Id | 1.0.0    |
| conversation.conversationType | Number | 是     | 无 | 会话类型 | 1.0.0    |

**回调参数**

| 名称                   | 类型    | 描述                                    | 版本   |
|------------------------|---------|-----------------------------------------|--------|
| result                | Object  | 返回值 | 1.0.0  |
| result.conversation   | Object  | 空对象表示会话不存在，属性可查看 [Conversation](../../conversation)| 1.0.0  |


**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.getConversation(conversation).then(({ conversation }) => {
  console.log(conversation);
});

```
</TabItem>

<TabItem value="harmony">

根据会话标识 `Conversation` 获取指定会话信息。返回空对象表示没有会话信息。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |

**接口定义**

```java
//callback 定义
export type ConversationCallback = (code:number,conver:ConversationInfo|null)=>void

/**
 * 获取单个会话的信息
 * @param conver 会话标识
 * @return 会话信息
 */
getConversation(conver:Conversation,callback:ConversationCallback)
```

**示例代码**
```java
JuggleIm.instance.getConversationManager().getConversation(new Conversation("userid2",1),(conver)=>{
    
})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

获取指定会话信息, 返回空对象表示没有会话信息，此方法仅从本地数据库获取会话信息，不会从云端获取。

**参数说明**

| 名称         | 类型         | 描述      | 版本     |
|------------------|--------------|----------|----------|
| conversationType | int | 会话类型 | 0.6.3    |
| conversationId | String | 会话标识 | 0.6.3    |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
ConversationInfo? conversationInfo = await JuggleIm.instance.getConversationInfo(conversation);
```

</TabItem>
<TabItem value="reactnative">

获取指定会话信息, 返回空对象表示没有会话信息，此方法仅从本地数据库获取会话信息，不会从云端获取。

**参数说明**

| 名称         | 类型         | 描述      | 版本     |
|------------------|--------------|----------|----------|
| conversationType | Number | 会话类型 | 0.6.3    |
| conversationId | String | 会话标识 | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversationInfo = await JuggleIM.getConversationInfo({
  conversationType: 2,
  conversationId: 'groupId1'
});
```

</TabItem>
</Tabs>