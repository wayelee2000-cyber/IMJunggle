---
title: 插入指定会话
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

插入会话，SDK 自动向本地和云端插入，支持多端同步。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |
| callback     | ICreateConversationInfoCallback | 结果回调 | 1.0.0    |


**示例代码**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
JIM.getInstance().getConversationManager().createConversationInfo(conversation, new IConversationManager.ICreateConversationInfoCallback() {
    @Override
    public void onSuccess(ConversationInfo conversationInfo) {

    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>
<TabItem value="ios">

插入会话，SDK 自动向本地和云端插入，支持多端同步。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | JConversation | 会话标识 | 1.0.0    |
| successBlock |  | 成功回调 | 1.0.0    |
| errorBlock   |  | 失败回调 | 1.0.0    |

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
[JIM.shared.conversationManager createConversationInfo:conversation success:^(JConversationInfo *) {
    
} error:^(JErrorCode code) {
    
}];

```

</TabItem>
<TabItem value="js">

插入会话，SDK 自动向本地和云端插入，支持多端同步，若插入会话已存在，原会话将会**被覆盖**

:::info 会话信息

> Web 中依赖用户注册获取 Token 时传入的用户信息或创建群组时指定的头像和群昵称，如果没有注册或创建群组并设置群组信息，则没有会话信息

> Electron 中遵循 Web 原则，但指定 `conversationTitle` 和 `conversationPortrait` 会保存在本地数据库，获取会话会列表会返回
:::


**参数说明**

| 名称                             | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------------------------|---------|-------|--------|----------|----------|
| conversation                    | Object | 是     | 无 | 会话对象 | 1.0.0    |
| conversation.conversationId     | String | 是     | 无 | 会话 Id | 1.0.0    |
| conversation.conversationType   | Number | 是     | 无 | 会话类型 | 1.0.0    |
| conversation.conversationTitle    | String| 否    |  无 | 会话名称 | 1.0.0    |
| conversation.conversationPortrait | String| 否    |  无 | 会话头像 | 1.0.0    |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.0.0    |
| result.conversation | Object | [会话对象](../../../conversation)，包含用户或群组信息 | 1.0.0    |

**示例代码**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.insertConversation(conversation).then((result) => {
  let { conversation } = result;
  console.log(conversation);
});
```
</TabItem>

<TabItem value="flutter" label="Flutter">

插入会话，自动向本地和云端插入，同时支持同步到当前用户的的其他设备，若插入会话已存在，不会覆盖原会话，插入成功后会触发会话监听事件。

**参数说明**

| 名称          | 类型     | 描述| 版本     |
|--------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 0.6.3 |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.private, 'userid1');
Result<ConversationInfo> result = await JuggleIm.instance.createConversationInfo(conversation);
```

</TabItem>
<TabItem value="reactnative">

插入会话，自动向本地和云端插入，同时支持同步到当前用户的的其他设备，若插入会话已存在，不会覆盖原会话，插入成功后会触发会话监听事件。

**参数说明**

| 名称          | 类型     | 描述| 版本     |
|--------------|---------|----------|----------|
| conversation | Object | 会话标识 | 0.6.3 |
| conversationType | Number | 会话类型 | 0.6.3 |
| conversationId | String | 会话ID | 0.6.3 |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const result = await JuggleIM.createConversationInfo({
  conversationType: 1,
  conversationId: 'userid1'
});
```

</TabItem>
<TabItem value="harmony">

插入会话，自动向本地和云端插入，同时支持同步到当前用户的的其他设备，若插入会话已存在，不会覆盖原会话。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation | Conversation | 会话标识 | 1.0.0    |
| callback     | ConversationInsertCallback | 结果回调 | 1.0.0    |

**接口定义**

```java
//callback 定义
export type ConversationInsertCallback = (code:number,conver:ConversationInfo)=>void

insertConversation(conver:Conversation,callback:ConversationInsertCallback)
```

**示例代码**

```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getConversationManager().insertConversation(conver,(converInfo)=>{
  
})
```

</TabItem>

</Tabs>