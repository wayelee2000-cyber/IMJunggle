---
title: Get session list
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

Retrieve the session information list in pages.

**Interface definition**

```java
/**
 * Retrieves the session information list in pages, with results sorted in reverse chronological order by session time (newest first, oldest last).
 * @param count Number of sessions to retrieve
 * @param timestamp Timestamp to pull from (pass 0 to represent the current time)
 * @param direction Pull direction
 * @return List of session information
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

Retrieve the session information list in pages.

**Interface definition**
```objectivec
/// Retrieves the session information list in pages, with results sorted in reverse chronological order by session time (newest first, oldest last)
/// - Parameters:
///   - count: Number of sessions to retrieve
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
| option.count | Number | No | 50 | Number of sessions to retrieve, up to 100 sessions per request | 1.0.0 |
| option.order | Number | No | [FORWARD](../../enum/web#conversation) | Direction of retrieval; supports fetching earlier or newer sessions, used together with the `time` attribute | 1.0.0 |
| option.time | Number | No | 0 | Starting point timestamp for fetching sessions. Use with `order` to specify direction (newer or older sessions) | 1.0.0 |

**Callback description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.0.0 |
| result.conversations | Array | Array of conversations. See [Conversation](../conversation.mdx) for the structure of a single conversation object | 1.0.0 |
| result.isFinished | Boolean | Indicates whether all sessions have been retrieved | 1.0.0 |

**Sample Code**
```js
/* 
Assuming the current user has 199 sessions and each page retrieves 50 items, the session list is sorted in reverse chronological order. The paging logic is as follows:
1. Load page 1 with parameters: { count: 50, time: 0 }
2. Load page 2 with parameters: { count: 50, time: 'Smallest sortTime in the session array on page 1 (session with the highest array index)' }
3. Load page 3 with parameters: { count: 50, time: 'Smallest sortTime in the session array on page 2 (session with the highest array index)' }
4. Load page 4 with parameters: { count: 50, time: 'Smallest sortTime in the session array on page 3 (session with the highest array index)' }
5. End: Stop loading when isFinished returns true.
*/
jim.getConversations().then((result) => {
  let { conversations, isFinished } = result;
  console.log(isFinished, conversations);
})
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Retrieve the session information list in pages. Assume the current user has 199 sessions and each page retrieves 50 items. The session list is sorted in reverse chronological order. The paging logic is as follows:

> 1. Load page 1 with parameters: { count: 50, timestamp: 0 }

> 2. Load page 2 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the session array on page 1 (session with the highest array index)' }

> 3. Load page 3 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the session array on page 2 (session with the highest array index)' }

> 4. Load page 4 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the session array on page 3 (session with the highest array index)' }

> 5. End: Stop loading when fewer than 50 sessions are returned.

**Parameter description**

`GetConversationInfoOption option = GetConversationInfoOption();`

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|------------|------------------------------------------------|----------|
| option.count | int | No | 50 | Number of sessions to retrieve, up to 100 sessions per request | 0.6.3 |
| option.timestamp | int | No | 0 | Starting timestamp for retrieval. Use with `direction` to specify new or old sessions | 0.6.3 |
| option.direction | int | No | 0 | Direction of retrieval: 0 for sessions after timestamp, 1 for sessions before timestamp | 0.6.3 |

**Sample Code**

```dart
GetConversationInfoOption option = GetConversationInfoOption();
option.count = 20;
option.timestamp = 0;
option.direction = 1; // 0: Pull sessions after timestamp, 1: Pull sessions before timestamp
List<ConversationInfo> conversations = await JuggleIm.instance.getConversationInfoListByOption(option);
```

</TabItem>
<TabItem value="reactnative">

Retrieve the session information list in pages. Assume the current user has 199 sessions and each page retrieves 50 items. The session list is sorted in reverse chronological order. The paging logic is as follows:

> 1. Load page 1 with parameters: { count: 50, timestamp: 0 }

> 2. Load page 2 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the session array on page 1 (session with the highest array index)' }

> 3. Load page 3 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the session array on page 2 (session with the highest array index)' }

> 4. Load page 4 with parameters: { count: 50, timestamp: 'Smallest `sortTime` in the session array on page 3 (session with the highest array index)' }

> 5. End: Stop loading when fewer than 50 sessions are returned.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|------------|------------------------------------------------|----------|
| count | Number | No | 50 | Number of sessions to retrieve, up to 100 sessions per request | 1.0.0 |
| timestamp | Number | No | 0 | Starting timestamp for retrieval. Use with `direction` to specify new or old sessions | 1.0.0 |
| direction | Number | No | 0 | Direction of retrieval: supports fetching earlier or newer sessions, used with the `timestamp` attribute | 1.0.0 |

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

const conversations = await JuggleIM.getConversationInfoList({
  count: 20,
  timestamp: 0,
  direction: 1 // 0: Pull sessions after timestamp, 1: Pull sessions before timestamp
});
```

</TabItem>
</Tabs>