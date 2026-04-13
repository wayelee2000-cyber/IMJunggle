---
title: Clear Historical Messages
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
{ label: 'Hongmeng', value: 'harmony', },
]
}>
<TabItem value="android">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| startTime | long | Messages sent before startTime will be cleared; passing 0 indicates the current time | 1.0.0 |
| callback | IMessageManager.ISimpleCallback | Result callback | 1.0.0 |

**Sample Code**

```java
Conversation conversation = new Conversation(Conversation.ConversationType.GROUP, "groupId1");
JIM.getInstance().getMessageManager().clearMessages(conversation, 0, new IMessageManager.ISimpleCallback() {
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

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | JConversation | Session identifier | 1.0.0 |
| startTime | long long | Messages sent before startTime will be cleared; passing 0 indicates the current time | 1.0.0 |
| successBlock | | Success callback | 1.0.0 |
| errorBlock | | Failure callback | 1.0.0 |

**Sample Code**

```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypeGroup conversationId:@"groupId1"];
[JIM.shared.messageManager clearMessagesIn:conversation
                                  startTime:0
                                   success:^{
    
} error:^(JErrorCode errorCode) {
    
}];
```

</TabItem>
<TabItem value="js">

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|--------------------------|---------|----------|--------|----------------------------------------------------------|--------|
| params | Object | Yes | - | Parameters for clearing historical messages | 1.0.0 |
| params.conversationType | Number | Yes | - | [Conversation Type](../../../enum/web#conversation) | 1.0.0 |
| params.conversationId | String | Yes | - | Session ID. For `PRIVATE` sessions, this is the userId of the receiver; for `GROUP` sessions, it is the group ID | 1.0.0 |
| params.time | Number | Yes | - | Clear historical messages sent before the specified time; typically the sentTime of the last message in the session | 1.0.0 |

**Success Callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure Callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code upon failure. You can view `error.msg` or refer to the [status code](../../../status_code/web) documentation | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2',
  time: 1702180128970
};

jim.clearMessage(params).then(() => {
  console.log('Messages cleared successfully');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="harmony">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | Conversation | Conversation identifier | 1.0.0 |
| startTime | long | Messages sent before startTime will be cleared | 1.0.0 |
| callback | CommonCallback | Result callback | 1.0.0 |

**Sample Code**

```java
let conver = new Conversation("userid1", 1);
JuggleIm.instance.getMessageManager().clearMessages(conver, new Date().getTime(), (code) => {

});
```

</TabItem>
<TabItem value="flutter">

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|----------|---------|------------------------------------------|--------|
| conversation | Conversation | Yes | - | Conversation object. For `private` conversations, the conversation ID is the userId of the other party. For `group` conversations, it is the group ID. | 0.6.3 |
| startTime | int | Yes | - | Timestamp; messages sent before this time will be cleared. 0 represents the current time by default | 0.6.3 |
| forAllUsers | bool | No | false | Scope of message clearing. `true` clears historical messages for all users; `false` clears only the current user's messages | 0.6.3 |

**forAllUsers Applicable Scenarios**

> Group scenario: Control the clear button based on permissions. For example, administrators can clear history messages for all members, while regular members can only clear their own history messages.

> Single chat scenario: Typically, only the historical messages of yourself and the other party are cleared.

**Sample Code**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');
int startTime = 0;
bool forAllUsers = false;

await JuggleIm.instance.clearMessages(conversation, startTime, forAllUsers);
```

</TabItem>
</Tabs>