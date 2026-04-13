---
title: Remove favorites
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
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

Remove favorites, supporting various message types such as pictures, files, voice notes, videos, and more.

**Interface definition**

```java
/**
 * Remove messages from favorites
 * @param messageIdList List of message IDs to be removed
 * @param callback Result callback
 */
void removeFavorite(List<String> messageIdList, ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

Remove favorites, supporting various message types such as pictures, files, voice notes, videos, and more.

**Interface definition**

```objectivec
/// Remove messages from favorites
/// - Parameters:
///   - messageIdList: List of message IDs to be removed
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)removeFavorite:(NSArray <NSString *> *)messageIdList
               success:(void (^)(void))successBlock
                 error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

Remove favorites, supporting various message types such as pictures, files, voice notes, videos, and more.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|----------------------------------------|---------|--------|--------|---------------------------------------------------------|----------|
| params | Object | Yes | | Message object | 1.0.0 |
| params.messages | Array | Yes | | List of favorite messages | 1.0.0 |
| params.messages[0].conversationType | Number | Yes | | [Conversation Type](../../enum/web.md#conversation) | 1.0.0 |
| params.messages[0].conversationId | String | Yes | | Session ID. For `PRIVATE` sessions, this is the receiver's userId; for `GROUP` sessions, this is the group ID | 1.0.0 |
| params.messages[0].senderId | String | Yes | | Message sender ID, see [Message.sender.id](../../../msg/message) | 1.0.0 |
| params.messages[0].messageId | String | Yes | | Message ID, see [Message.messageId](../../../msg/message) | 1.0.0 |

**Success callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains the corresponding status code upon failure. You can check `error.msg` or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

let params = {
  messages: [{
    conversationType: ConversationType.GROUP,
    conversationId: 'groupz001',
    messageId: 'nwmz3nrps6yj3rk8',
    senderId: "675NdFjkx"
  }] 
};

jim.removeFavoriteMessages(params).then(() => {
  console.log('removeFavoriteMessages succeeded.');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

Remove favorites, supporting various message types such as pictures, files, voice notes, videos, and more.

**Interface definition**

```dart
/// Remove messages from favorites
/// - Parameters:
///   - messageIdList: List of message IDs to be removed
Future<int> removeFavoriteMessages(List<String> messageIdList) async
```

</TabItem>
</Tabs>