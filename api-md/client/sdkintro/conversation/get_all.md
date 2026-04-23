---
title: Get conversation list
hide_title: true
sidebar_position: 2
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

Retrieve the conversation list in pages.

**Interface definition**

```java
/**
 * Retrieves the conversation list in pages, with results sorted in reverse chronological order by conversation time (newest first, oldest last).
 * @param count Number of conversations to retrieve
 * @param timestamp Timestamp to pull from (pass 0 to represent the current time)
 * @param direction Pull direction
 * @return List of conversation information
 */
List<ConversationInfo> getConversationInfoList(int count,
                                                long timestamp,
                                                JIMConst.PullDirection direction);
```

**Sample Code**

```java
List<ConversationInfo> list = JIM.getInstance().getConversationManager().getConversationInfoList(20, 0, JIMConst.PullDirection.OLDER);
```

</TabItem>
<TabItem value="ios">

Retrieve the conversation list in pages.

**Interface definition**
```objectivec
/// Retrieves the conversation list in pages, with results sorted in reverse chronological order by conversation time (newest first, oldest last)
/// - Parameters:
///   - count: Number of conversations to retrieve
///   - ts: Timestamp to pull from (pass 0 to represent the current time)
///   - direction: Pull direction
- (NSArray<JConversationInfo *> *)getConversationInfoListByCount:(int)count
                                                       timestamp:(long long)ts
                                                       direction:(JPullDirection)direction;
```

**Sample Code**
```objectivec
NSArray *array = [JIM.shared.conversationManager getConversationInfoListByCount:20 timestamp:0 direction:JPullDirectionOlder];
```

</TabItem>
<TabItem value="js">

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|----------------------------------|------------------------------------------------|----------|
| option | Object | No | | | 1.0.0 |
| option.count | Number | No | 50 | Number of conversations to retrieve, up to 100 conversations per request | 1.0.0 |
| option.order | Number | No | [FORWARD](../enum/web.md#conversation) | Retrieval direction. Supports fetching earlier or newer conversations, used together with the `time` attribute | 1.0.0 |
| option.time | Number | No | 0 | Starting point timestamp for fetching conversations. Use with `order` to specify direction (newer or older conversations) | 1.0.0 |

**Callback description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.0.0 |
| result.conversations | Array | Array of conversations. See [Conversation](../conversation.md) for the structure of a single conversation object | 1.0.0 |
| result.isFinished | Boolean | Indicates whether all conversations have been retrieved | 1.0.0 |

**Sample Code**
```js
/* 
Assuming the current user has 199 conversations and each page retrieves 50 items, the conversation list is sorted in reverse chronological order. The paging logic is as follows:
1. Load page 1 with parameters: { count: 50, time: 0 }
2. Load page 2 with parameters: { count: 50, time: 'Smallest sortTime in the conversation array on page 1 (conversation with the highest array index)' }
3. Load page 3 with parameters: { count: 50, time: 'Smallest sortTime in the conversation array on page 2 (conversation with the highest array index)' }
4. Load page 4 with parameters: { count: 50, time: 'Smallest sortTime in the conversation array on page 3 (conversation with the highest array index)' }
5. End: Stop loading when isFinished returns true.
*/
jim.getConversations().then((result) => {
  let { conversations, isFinished } = result;
  console.log(isFinished, conversations);
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Retrieve the conversation list in pages. Assume the current user has 199 conversations and each page retrieves 50 items. The conversation list is sorted in reverse chronological order. The paging logic is as follows:

> 1. Load page 1 with parameters: { count: 50, timestamp: 0 }

> 2. Load page 2 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the conversation array on page 1 (conversation with the highest array index)' }

> 3. Load page 3 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the conversation array on page 2 (conversation with the highest array index)' }

> 4. Load page 4 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the conversation array on page 3 (conversation with the highest array index)' }

> 5. End: Stop loading when fewer than 50 conversations are returned.

**Parameter description**

`GetConversationInfoOption option = GetConversationInfoOption();`

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|------------|------------------------------------------------|----------|
| option.count | int | No | 50 | Number of conversations to retrieve, up to 100 conversations per request | 0.6.3 |
| option.timestamp | int | No | 0 | Starting timestamp for retrieval. Use with `direction` to specify newer or older conversations | 0.6.3 |
| option.direction | int | No | 0 | Retrieval direction: `0` for conversations after the timestamp, `1` for conversations before the timestamp | 0.6.3 |

**Sample Code**

```dart
GetConversationInfoOption option = GetConversationInfoOption();
option.count = 20;
option.timestamp = 0;
option.direction = 1; // 0: Pull conversations after the timestamp, 1: Pull conversations before the timestamp
List<ConversationInfo> conversations = await JuggleIm.instance.getConversationInfoListByOption(option);
```

</TabItem>
<TabItem value="reactnative">

Retrieve the conversation list in pages. Assume the current user has 199 conversations and each page retrieves 50 items. The conversation list is sorted in reverse chronological order. The paging logic is as follows:

> 1. Load page 1 with parameters: { count: 50, timestamp: 0 }

> 2. Load page 2 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the conversation array on page 1 (conversation with the highest array index)' }

> 3. Load page 3 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the conversation array on page 2 (conversation with the highest array index)' }

> 4. Load page 4 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the conversation array on page 3 (conversation with the highest array index)' }

> 5. End: Stop loading when fewer than 50 conversations are returned.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|------------|------------------------------------------------|----------|
| count | Number | No | 50 | Number of conversations to retrieve, up to 100 conversations per request | 1.0.0 |
| timestamp | Number | No | 0 | Starting timestamp for retrieval. Use with `direction` to specify newer or older conversations | 1.0.0 |
| direction | Number | No | 0 | Retrieval direction: supports fetching earlier or newer conversations, used with the `timestamp` attribute | 1.0.0 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversations = await JuggleIM.getConversationInfoList({
  count: 20,
  timestamp: 0,
  direction: 1 // 0: Pull conversations after the timestamp, 1: Pull conversations before the timestamp
});
```

</TabItem>
</Tabs>
