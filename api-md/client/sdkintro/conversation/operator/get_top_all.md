---
title: Get the pinned conversation
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
]
}>
<TabItem value="android">

**Parameter Description**

| Name      | Type                 | Description                          | Version |
|-----------|----------------------|------------------------------------|---------|
| count     | int                  | Number of items to pull             | 1.0.0   |
| timestamp | long                 | Timestamp in milliseconds; 0 means current time | 1.0.0   |
| direction | JIMConst.PullDirection | Direction of pull                   | 1.0.0   |

**Sample Code**

```java
List<ConversationInfo> list = JIM.getInstance().getConversationManager().getTopConversationInfoList(100, 0, JIMConst.PullDirection.OLDER);
```

</TabItem>
<TabItem value="ios">

**Parameter Description**

| Name      | Type                 | Description                          | Version |
|-----------|----------------------|------------------------------------|---------|
| count     | int                  | Number of items to pull             | 1.0.0   |
| timestamp | long long            | Timestamp in milliseconds; 0 means current time | 1.0.0   |
| direction | JPullDirection       | Direction of pull                   | 1.0.0   |

**Sample Code**

```objectivec
NSArray <JConversationInfo *> *conversationList = [JIM.shared.conversationManager getTopConversationInfoListByCount:100 timestamp:0 direction:JPullDirectionOlder];
```

</TabItem>
<TabItem value="js">

**Callback Description**

| Property           | Type    | Description                                                                 | Version |
|--------------------|---------|-----------------------------------------------------------------------------|---------|
| result             | Object  | Query result                                                                | 1.0.0   |
| result.conversations | Array   | Array of conversations. See [Conversation](../../conversation.mdx) for the structure of a single conversation object | 1.0.0   |
| result.isFinished  | Boolean | Indicates whether the session retrieval is complete                        | 1.0.0   |

**Sample Code**

```js
jim.getTopConversations().then((result) => {
  let { conversations, isFinished } = result;
  console.log(isFinished, conversations);
})
```

</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
<TabItem value="reactnative">

Retrieve the list of pinned conversations.

**Parameter Description**

| Name      | Type   | Required | Default | Description                                                                 | Version |
|-----------|--------|----------|---------|-----------------------------------------------------------------------------|---------|
| count     | Number | No       | 100     | Number of items to pull                                                      | 0.6.3   |
| timestamp | Number | No       | 0       | Timestamp in milliseconds; 0 means current time                             | 0.6.3   |
| direction | Number | No       | 1       | Pull direction: 0 pulls sessions after the timestamp; 1 pulls sessions before the timestamp | 0.6.3   |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversations = await JuggleIM.getTopConversationInfoList({
  count: 100,
  timestamp: 0,
  direction: 1
});
```

</TabItem>
</Tabs>