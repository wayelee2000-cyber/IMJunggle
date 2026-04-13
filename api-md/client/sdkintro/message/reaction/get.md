---
title: Get message response
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
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

The SDK provides two methods for retrieving message reactions: one fetches the latest data from the backend, and the other retrieves cached message reactions locally.

The locally cached data may not be the most up-to-date version but can be used to render the interface immediately, enhancing the user experience.

**Interface definition**

```java
/**
 * Retrieve message reactions in batches (messages must belong to the same conversation)
 * @param messageIdList List of message IDs
 * @param conversation The conversation to which the messages belong
 * @param callback Result callback
 */
void getMessagesReaction(List<String> messageIdList,
                            Conversation conversation,
                            IMessageReactionListCallback callback);

/**
 * Retrieve cached message reactions (the cached data may not be the latest version but can be used for immediate rendering to improve user experience)
 * @param messageIdList List of message IDs
 * @return List of message reactions
 */
List<MessageReaction> getCachedMessagesReaction(List<String> messageIdList);
```

</TabItem>
<TabItem value="ios">

The SDK provides two methods for retrieving message reactions: one fetches the latest data from the backend, and the other retrieves cached message reactions locally.

The locally cached data may not be the most up-to-date version but can be used to render the interface immediately, enhancing the user experience.

**Interface definition**

```objectivec
/// Retrieve message reactions in batches (messages must belong to the same conversation)
/// - Parameters:
///   - messageIdList: List of message IDs
///   - conversation: The conversation to which the messages belong
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)getMessagesReaction:(NSArray <NSString *> *)messageIdList
               conversation:(JConversation *)conversation
                    success:(void (^)(NSArray <JMessageReaction *> *reactionList))successBlock
                      error:(void (^)(JErrorCode code))errorBlock;

/// Retrieve cached message reactions (the cached data may not be the latest version but can be used for immediate rendering to improve user experience)
/// - Parameter messageIdList: List of message IDs
- (NSArray <JMessageReaction *> *)getCachedMessagesReaction:(NSArray <NSString *> *)messageIdList;
```

</TabItem>
<TabItem value="js">

Access the `reactions` property directly from the message.

</TabItem>

<TabItem value="flutter">

The SDK provides two methods for retrieving message reactions: one fetches the latest data from the backend, and the other retrieves cached message reactions locally.

The locally cached data may not be the most up-to-date version but can be used to render the interface immediately, enhancing the user experience.

**Interface definition**

```dart
/**
 * Retrieve message reactions in batches (messages must belong to the same conversation)
 * @param messageIdList List of message IDs
 * @param conversation The conversation to which the messages belong
 */
Future<Result<List<MessageReaction>>> getMessagesReaction(List<String> messageIdList, Conversation conversation) async

/**
 * Retrieve cached message reactions (the cached data may not be the latest version but can be used for immediate rendering to improve user experience)
 * @param messageIdList List of message IDs
 * @return List of message reactions
 */
Future<Result<List<MessageReaction>>> getCachedMessagesReaction(List<String> messageIdList) async
```

</TabItem>
</Tabs>