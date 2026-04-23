---
title: Get message context
hide_title: true
sidebar_position: 7
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

> Not yet provided

</TabItem>
<TabItem value="ios">

> Not yet provided

</TabItem>
<TabItem value="js">

Retrieving the message context refers to obtaining the list of messages before and after a specified time, which facilitates displaying contextual messages in the business layer. This interface is suitable for use when entering a session for the first time. To load more historical messages in the `Down` or `Up` direction, please use the [Get Historical Messages](./get_all.md) interface.

:::simple usage scenarios

> When entering a conversation, locate the first unread message and display the messages before and after it.

> After searching for messages, click on a matched message to locate the corresponding conversation and display the context around that message.

:::


**Parameter description**

| Name | Type | Required | Default | Description | Version |
|---------------------|---------|------|------------------|------------------------------------------------------------------------------|--------|
| params | Object | Yes | | Parameters for retrieving historical messages | 1.8.3 |
| params.conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.8.3 |
| params.conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the userId of the other party; for `GROUP` sessions, it is the group ID | 1.8.3 |
| params.time | Number | No | `Time of the first unread message` | The starting time for retrieving context messages | 1.8.3 |
| params.count | Number | No | 10 | Number of context messages to retrieve. `count` messages will be fetched before and after the specified `time` and returned in `frontMessages` and `backMessages`. Valid range is 1 - 10 | 1.8.3 |

**Successful callback**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | Object | | 1.8.3 |
| result.frontMessages | Array | Array of messages before the specified time. See the [message object](../../msg/message.md) | 1.8.3 |
| result.isFrontFinished | Boolean | Indicates whether there are more historical messages available before the specified time | 1.8.3 |
| result.backMessages | Array | Array of messages after the specified time. See the [message object](../../msg/message.md) | 1.8.3 |
| result.isBackFinished | Boolean | Indicates whether there are more historical messages available after the specified time | 1.8.3 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the error status code and message. You can view `error.msg` directly or refer to [status code](../../status_code/web.md) | 1.8.3 |

**Sample Code**
```js
let { ConversationType } = JIM;

let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid2',
  count: 10
};

jim.getContextMessages(params).then((result) => {
  let { frontMessages, isFrontFinished, backMessages, isBackFinished } = result;
  console.log(result);
}, (error) => {
  console.log(error);
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
</Tabs>
