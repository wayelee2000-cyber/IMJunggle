---
title: Get the first unread message
hide_title: true
sidebar_position: 9
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

Retrieve the first unread message in the conversation.

**Interface definition**

```java
/**
 * Retrieve the first unread message in the conversation.
 *
 * @param conversation The session ID.
 * @param callback The callback for downloading files. See {@link IDownloadMediaMessageCallback}.
 */
void getFirstUnreadMessage(Conversation conversation, IGetMessagesCallback callback);
```

</TabItem>
<TabItem value="ios">

Retrieve the first unread message in the conversation.

**Interface definition**

```objectivec
/// Retrieve the first unread message in the session
/// - Parameters:
///   - conversation: The conversation identifier
///   - successBlock: Success callback; returns nil if there are no unread messages
///   - errorBlock: Failure callback
- (void)getFirstUnreadMessage:(JConversation *)conversation
                      success:(void (^)(JMessage *message))successBlock
                        error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js" label="JavaScript">

> Not yet provided

</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
<TabItem value="harmony" label="Hongmeng">

> Not yet provided

</TabItem>
</Tabs>