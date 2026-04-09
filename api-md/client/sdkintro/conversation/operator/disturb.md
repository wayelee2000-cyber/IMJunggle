---
title: 设置单个会话免打扰
hide_title: true
sidebar_position: 6
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

设置会话免打扰，多端同步，设置免打扰后移动端将不再接收离线推送，设置成功后，SDK 会自动更新会话的 mute 属性。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation                    | Conversation | 会话标识 | 1.0.0    |
| isMute   | boolean | YES 表示静音，NO 表示解除静音 | 1.0.0    |
| callback     | ISimpleCallback | 结果回调 | 1.0.0    |

**示例代码**
```java
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userId1");
JIM.getInstance().getConversationManager().setMute(conversation, true, new IConversationManager.ISimpleCallback() {
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

设置会话免打扰，多端同步，设置免打扰后移动端将不再接收离线推送，设置成功后，SDK 会自动更新会话的 mute 属性。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| isMute   | BOOL | YES 表示静音，NO 表示解除静音 | 1.0.0    |
| conversation | JConversation | 会话标识 | 1.0.0    |
| successBlock     |  | 成功回调 | 1.0.0    |
| errorBlock     |  | 失败回调 | 1.0.0    |

**示例代码**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userId1"];
[JIM.shared.conversationManager setMute:YES
                            conversation:conversation
                                success:^{
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">

设置会话免打扰，多端同步，设置免打扰后移动端将不再接收离线推送，设置成功后，SDK 会自动更新会话的 undisturbType 属性。

**参数说明**

| 名称                             | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------------------------|---------|-------|--------|----------|----------|
| conversation                    | Object | 是     | 无 | 会话对象 | 1.0.0    |
| conversation.conversationType   | Number | 是     | 无 | 会话类型 | 1.0.0    |
| conversation.conversationId     | String | 是     | 无 | 会话 Id | 1.0.0    |
| conversation.undisturbType      | Number | 是     | 无 | [免打扰类型](../../../enum/web#disturb) | 1.0.0    |

**示例代码**
```js
let { ConversationType, UndisturbType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01',
  undisturbType: UndisturbType.UNDISTURB,
};

jim.disturbConversation(conversation).then(() => {
  console.log('set conversation disturb successfully');
});
```
</TabItem>

<TabItem value="harmony">

设置会话免打扰，多端同步，设置免打扰后移动端将不再接收离线推送，设置成功后，SDK 会自动更新会话的 undisturbType 属性。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation                    | Conversation | 会话标识 | 1.0.0    |
| isMute   | boolean | YES 表示静音，NO 表示解除静音 | 1.0.0    |
| callback     | CommonCallback | 结果回调 | 1.0.0    |

**示例代码**
```java
let conver = new Conversation("userid1",1)
JuggleIm.instance.getConversationManager().setMute(conver,true,(code)=>{
  
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

设置会话免打扰，免打扰状态支出同步到当前的用户其他设备，设置免打扰后移动端将不再接收离线推送，设置成功后，SDK 会自动更新会话的 `mute` 属性。

**参数��明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation                    | Conversation | 会话标识 | 0.6.3    |
| isMute                          | bool | `true` 表示静音，`false` 表示解除静音 | 0.6.3    |

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.private, 'userId1');
Result result = await JuggleIm.instance.setMute(conversation, true);
```

</TabItem>
<TabItem value="reactnative">

设置会话免打扰，多端同步，设置免打扰后移动端将不再接收离线推送，设置成功后，SDK 会自动更新会话的 `mute` 属性。

**参数说明**

| 名称                             | 类型     | 描述| 版本     |
|---------------------------------|---------|----------|----------|
| conversation                    | Object | 会话标识 | 0.6.3    |
| conversationType                | Number | 会话类型 | 0.6.3    |
| conversationId                  | String | 会话ID | 0.6.3    |
| isMute                          | Boolean | `true` 表示静音，`false` 表示解除静音 | 0.6.3    |

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.setMute({
  conversationType: 1,
  conversationId: 'userId1',
  isMute: true
});
```

</TabItem>
</Tabs>