---
title: Message subscription
hide_title: true
sidebar_position: 6
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

> Stay tuned

</TabItem>
<TabItem value="ios">

> Stay tuned

</TabItem>
<TabItem value="js">

> Applicable scenarios: Users who are not members of a group can view real-time messages within that group. After a successful subscription, new messages in the specified conversation will be delivered through the message event listener.

> _To use this feature, you must first enable the private `IM background` in your account under `Function configuration` -> `Access historical messages without joining the group`._

<br/>

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| conversation | Object | Yes | | Conversation object | 1.7.18 |
| conversation.conversationType | Number | Yes | | [Conversation Type](../enum/web.md#conversation) | 1.7.18 |
| conversation.conversationId | String | Yes | | Conversation ID. For `PRIVATE` conversations, this is the userId of the receiver; for `GROUP` conversations, it is the group ID. | 1.7.18 |

**Success callback**

No parameters are returned. The callback is triggered to indicate a successful subscription.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code if the subscription fails. You can check `error.msg` directly or refer to the [status code documentation](../status_code/web.md). | 1.7.18 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.GROUP,
  conversationId: 'group02',
};
// Subscribe to messages. If the connection is disconnected, be sure to call unsubscribeMessage to cancel the subscription.
jim.subscribeMessage(conversation).then(() => {
  console.log('subscribeMsg successfully.');
}, (error) => {
  console.log(error);
});

// Unsubscribe
jim.unsubscribeMessage(conversation).then(() => {
  console.log('unsubscribeMsg successfully.');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="reactnative" label="ReactNative">

> Stay tuned

</TabItem>
</Tabs>
