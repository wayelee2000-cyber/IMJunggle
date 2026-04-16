---
title: Get historical messages by ID
hide_title: true
sidebar_position: 8
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

Retrieve the corresponding local messages based on an array of message IDs.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| messageIdList | List | List of message IDs | 1.0.0 |

**Sample Code**

```java
List<Message> messageList = JIM.getInstance().getMessageManager().getMessagesByMessageIds(messageIds);
```
</TabItem>
<TabItem value="ios">

Retrieve the corresponding local messages based on an array of message IDs.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| messageIds | NSArray | List of message IDs | 1.0.0 |

**Sample Code**

```objectivec
NSArray *messages = [JIM.shared.messageManager getMessagesByMessageIds:messageIds];
```

</TabItem>
<TabItem value="js">

Retrieve message content by message IDs, supporting querying multiple messages at once. Ensure that all messageIds belong to the same session.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------------------------------------------|--------|
| params | Object | Yes | | Parameters for retrieving historical messages | 1.0.0 |
| params.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| params.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, it is the group ID | 1.0.0 |
| params.messageIds | Array | Yes | | Array of message IDs to retrieve | 1.0.0 |

**Successful callback**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | Object | | 1.0.0 |
| result.messages | Object | Array of messages. For properties of each message, see [Message](../msg/message) structure | 1.0.0 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code if the request fails. You can check `error.msg` or refer to [status codes](../status_code/web) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2',
  messageIds: ['nnx3axfbglsgv6fp', 'nnx3aw5wglqgv6fp']
};

jim.getMessagesByIds(params).then((result) => {
  let { messages } = result;
  console.log(messages);
}, (error) => {
  console.log(error);
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Retrieve the corresponding local messages based on an array of message IDs.

**Parameter description**

| Name | Type | Description | Version |
|----------------------|---------|----------------------------------------|----------|
| messageIdList | `List<String>` | List of message IDs | 0.6.3 |

**Sample Code**

```dart
List<String> messageIds = ["msg_id_01", "msg_id_02"];
List<Message> messages = await JuggleIm.instance.getMessagesByMessageIdList(messageIds);
```

The `messages` variable contains an array of messages. For the properties of each message, see the [Message](../../../msg/message) structure.

</TabItem>
</Tabs>