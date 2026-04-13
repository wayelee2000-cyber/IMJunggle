---
title: Set Do Not Disturb for a Single Session
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
{ label: 'Hongmeng', value: 'harmony', }
]
}>
<TabItem value="android">

Set the session to Do Not Disturb and synchronize this setting across multiple devices. After enabling Do Not Disturb for the session, the mobile device will no longer receive offline push notifications. Once the setting is successful, the SDK will automatically update the mute attribute of the session.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| isMute | boolean | `true` to mute, `false` to unmute | 1.0.0 |
| callback | ISimpleCallback | Result callback | 1.0.0 |

**Sample Code**
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

Set the session to Do Not Disturb and synchronize this setting across multiple devices. After enabling Do Not Disturb for the session, the mobile device will no longer receive offline push notifications. Once the setting is successful, the SDK will automatically update the mute attribute of the session.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| isMute | BOOL | `YES` to mute, `NO` to unmute | 1.0.0 |
| conversation | JConversation | Session identifier | 1.0.0 |
| successBlock | Block | Success callback | 1.0.0 |
| errorBlock | Block | Failure callback | 1.0.0 |

**Sample Code**

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

Set the session to Do Not Disturb and synchronize this setting across multiple devices. After enabling Do Not Disturb, the mobile device will no longer receive offline push notifications. Once the setting is successful, the SDK will automatically update the `undisturbType` attribute of the session.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|-------|--------|----------|----------|
| conversation | Object | Yes | None | Conversation object | 1.0.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.0.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.0.0 |
| conversation.undisturbType | Number | Yes | None | [DND Type](../../../enum/web#disturb) | 1.0.0 |

**Sample Code**
```js
let { ConversationType, UndisturbType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01',
  undisturbType: UndisturbType.UNDISTURB,
};

jim.disturbConversation(conversation).then(() => {
  console.log('Set conversation to Do Not Disturb successfully');
});
```
</TabItem>

<TabItem value="harmony">

Set the session to Do Not Disturb and synchronize this setting across multiple devices. After enabling Do Not Disturb, the mobile device will no longer receive offline push notifications. Once the setting is successful, the SDK will automatically update the `undisturbType` attribute of the session.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| isMute | boolean | `true` to mute, `false` to unmute | 1.0.0 |
| callback | CommonCallback | Result callback | 1.0.0 |

**Sample Code**
```java
let conver = new Conversation("userid1", 1);
JuggleIm.instance.getConversationManager().setMute(conver, true, (code) => {
  
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Set the session to Do Not Disturb, and synchronize the Do Not Disturb status across all devices of the current user. After enabling Do Not Disturb, the mobile device will no longer receive offline push notifications. Once the setting is successful, the SDK will automatically update the `mute` attribute of the session.

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Conversation | Conversation identifier | 0.6.3 |
| isMute | bool | `true` to mute, `false` to unmute | 0.6.3 |

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.private, 'userId1');
Result result = await JuggleIm.instance.setMute(conversation, true);
```

</TabItem>
<TabItem value="reactnative">

Set the session to Do Not Disturb and synchronize this setting across multiple devices. After enabling Do Not Disturb, the mobile device will no longer receive offline push notifications. Once the setting is successful, the SDK will automatically update the `mute` attribute of the session.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|----------|----------|
| conversation | Object | Conversation identifier | 0.6.3 |
| conversationType | Number | Conversation type | 0.6.3 |
| conversationId | String | Session ID | 0.6.3 |
| isMute | Boolean | `true` to mute, `false` to unmute | 0.6.3 |

**Sample Code**

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