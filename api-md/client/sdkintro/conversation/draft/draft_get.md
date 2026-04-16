---
title: Get conversation draft
hide_title: true
sidebar_position: 1
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

Each session includes a `draft` attribute, which is returned when retrieving the session list. For more details, please refer to the [Session Object](../../../conversation).
</TabItem>
<TabItem value="ios">

Each session includes a `draft` attribute, which is returned when retrieving the session list. For more details, please refer to the [Session Object](../../../conversation).

</TabItem>
<TabItem value="js">

The session list displays the draft status, so calling this method is generally unnecessary. Each session includes a `draft` attribute, which is returned when retrieving the session list. For more details, please refer to the [Session Object](../../../conversation).

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------|----------|-------|---|----------|----------|
| conversation | Object | Yes | None | Conversation object | 1.0.0 |
| conversation.conversationType | Number | Yes | None | Conversation type | 1.0.0 |
| conversation.conversationId | String | Yes | None | Conversation ID | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let conversation = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId01'
};

jim.getDraft(conversation).then((draft) => {
  console.log('Successfully retrieved conversation draft', draft);
});
```
</TabItem>
<TabItem value="flutter">

Each session includes a `draft` attribute, which is returned when retrieving the session list. For more details, please refer to the [Session Object](../../../conversation).

</TabItem>
<TabItem value="reactnative">

Each session includes a `draft` attribute, which is returned when retrieving the session list. For more details, please refer to the [Session Object](../../../conversation).

</TabItem>
</Tabs>