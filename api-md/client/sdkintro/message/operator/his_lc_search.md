---
title: Local news search
hide_title: true
sidebar_position: 3
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

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| conversation | Conversation | The conversation to query | 1.0.0 |
| searchContent | String | Query content | 1.0.0 |
| count | int | Number of messages to retrieve; if more than 100 items are requested, only 100 will be returned | 1.0.0 |
| timestamp | long | Message timestamp; if 0 is passed, the current time is used | 1.0.0 |
| direction | JIMConst.PullDirection | Query direction | 1.0.0 |

**Sample Code**

```java
List<Message> searchResults = JIM.getInstance().getMessageManager().searchMessageInConversation(conversation, "searchContent", 100, 0, JIMConst.PullDirection.OLDER);
```

</TabItem>
<TabItem value="ios">

**Parameter Description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| searchContent | NSString | Query content | 1.0.0 |
| conversation | JConversation | The conversation to query | 1.0.0 |
| count | int | Number of messages to retrieve; if more than 100 items are requested, only 100 will be returned | 1.0.0 |
| time | long long | Message timestamp; if 0 is passed, the current time is used | 1.0.0 |
| direction | JPullDirection | Query direction | 1.0.0 |
| contentTypes | `NSArray<NSString *>` | Content types to filter; pass nil to return all types | 1.0.0 |

**Sample Code**

```objectivec
NSArray <JMessage *> *searchResults = [JIM.shared.messageManager searchMessagesWithContent:@"searchContent"
                                                                            inConversation:nil
                                                                                      count:100
                                                                                       time:0
                                                                                  direction:JPullDirectionOlder
                                                                              contentTypes:nil];
```

</TabItem>
<TabItem value="js">

<div style="margin: 1rem 0; padding: 1rem 1.25rem; border-left: 4px solid #e5484d; background: #fff1f2; border-radius: 0 16px 16px 0;">
<p style="margin: 0 0 0.75rem; font-size: 1rem; font-weight: 700; color: #b42318;">This feature is only supported in Electron</p>
</div>

Local message search supports using `conversationId` to control whether to search messages within a single conversation or across all conversations. It also supports paginated retrieval, allowing developers to flexibly implement both global search and chat-specific search.

**Parameter Description**

| Name | Type | Required | Description | Version |
|-------------------------|---------|----|-------------------------------------------------------------------------------|--------|
| params | Object | Yes | Message search parameters | 1.0.0 |
| params.conversationType | Number | No | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| params.conversationId | String | No | Session ID; passing a value searches messages within a single conversation, passing empty searches across all conversations | 1.0.0 |
| params.keywords | Array | Yes | Message search keywords; supports up to 5 keywords with an "OR" relationship between them | 1.0.0 |
| params.senderIds | Number | No | Filter messages by specified sender IDs | 1.0.0 |
| params.messageNames | Number | No | Filter messages by specified message types | 1.0.0 |
| params.startTime | Number | No | Filter start time of the specified period, timestamp in milliseconds | 1.0.0 |
| params.endTime | Number | No | Filter end time of the specified period, timestamp in milliseconds | 1.0.0 |
| params.page | Number | No | Page number for pagination; default is 1 (first page) | 1.0.0 |
| params.pageSize | Number | No | Number of items per page; default is 10 | 1.0.0 |

**Successful Callback**

| Name | Type | Description | Version |
|------------------------|---------|-----------------------------------------|--------|
| result | Object | | 1.0.0 |
| result.isFinished | Boolean | Indicates whether there are more search results | 1.0.0 |
| result.total | Number | For all sessions search: total number of keyword hits across all sessions <br/> For single session search: number of keyword hits in the session | 1.0.0 |
| result.list | Array | For all sessions search: list of messages matching keywords across all sessions, supports pagination <br/> For single session search: list of messages matching keywords in the session, supports pagination | 1.0.0 |

**Each item in `result.list` is described as follows:**

| Name | Type | Description | Version |
|---------------------|-------|------------------------------------------|--------|
| conversationType | Number | Conversation type | 1.0.0 |
| conversationId | String | Session ID; for `PRIVATE` conversations, this is the userId of the other party; for `GROUP` conversations, this is the group ID | 1.0.0 |
| matchedCount | Array | Number of matched keywords in the current session | 1.0.0 |
| matchedList | Array | Details of messages matching keywords in the current session; each item is a [message object](../../msg/message.md) | 1.0.0 |

**Failure Callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code if the request fails. You can check `error.msg` or refer to [Status Code](../../status_code/web.md) | 1.0.0 |

**All Sessions Search: Sample Code**

```js
let params = {
  keywords: ['HelloChat'],
};
jim.searchMessages(params).then(({ isFinished, total, list }) => {
  console.log(isFinished, total, list);
});
```

**Single Session Search: Sample Code**

```js
let { ConversationType } = JIM;
let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid1',
  keywords: ['HelloChat'],
};
jim.searchMessages(params).then(({ isFinished, total, list }) => {
  console.log(isFinished, total, list);
});
```

</TabItem>

<TabItem value="flutter" label="Flutter">

**Sample Code**

```dart
GetMessageOption option = GetMessageOption();
option.count = 20;
option.startTime = 0; // Start time; 0 defaults to current time

List<Message> messageList = await JuggleIm.instance.searchMessagesInConversation(
  'searchContent',
  conversation,
  1, // Pull direction: 0 fetches messages after the start time; 1 fetches messages before the start time
  option
);
```

</TabItem>
</Tabs>
