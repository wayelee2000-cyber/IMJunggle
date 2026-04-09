---
title: 获取消息回应
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

SDK 提供了两个获取消息回应的接口，一个是从后端拉取最新数据，另一个是从本地获取缓存的消息回应。

本地缓存的数据不一定是最新版本，可以用于第一时间渲染界面，优化体验。

**接口定义**

```java
/**
 * 批量获取消息回应（消息必须属于同一个会话）
 * @param messageIdList 消息 id 列表
 * @param conversation 消息所属会话
 * @param callback 结果回调
 */
void getMessagesReaction(List<String> messageIdList,
                            Conversation conversation,
                            IMessageReactionListCallback callback);

/**
 * 获取缓存的消息回应（缓存的数据不一定是最新版本，可用于第一时间渲染，优化用户体验）
 * @param messageIdList 消息 id 列表
 * @return 消息回应列表
 */
List<MessageReaction> getCachedMessagesReaction(List<String> messageIdList);
```

</TabItem>
<TabItem value="ios">

SDK 提供了两个获取消息回应的接口，一个是从后端拉取最新数据，另一个是从本地获取缓存的消息回应。

本地缓存的数据不一定是最新版本，可以用于第一时间渲染界面，优化体验。

**接口定义** 

```objectivec
/// 批量获取消息回应（消息必须属于同一个会话）
/// - Parameters:
///   - messageIdList: 消息 id 列表
///   - conversation: 消息所属会话
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)getMessagesReaction:(NSArray <NSString *> *)messageIdList
               conversation:(JConversation *)conversation
                    success:(void (^)(NSArray <JMessageReaction *> *reactionList))successBlock
                      error:(void (^)(JErrorCode code))errorBlock;

/// 获取缓存的消息回应（缓存的数据不一定是最新版本，可用于第一时间渲染，优化用户体验）
/// - Parameter messageIdList: 消息 id 列表
- (NSArray <JMessageReaction *> *)getCachedMessagesReaction:(NSArray <NSString *> *)messageIdList;
```

</TabItem>
<TabItem value="js">

直接在消息中获取 `reactions` 属性。

</TabItem>

<TabItem value="flutter">

SDK 提供了两个获取消息回应的接口，一个是从后端拉取最新数据，另一个是从本地获取缓存的消息回应。

本地缓存的数据不一定是最新版本，可以用于第一时间渲染界面，优化体验。

**接口定义**

```dart
/**
 * 批量获取消息回应（消息必须属于同一个会话）
 * @param messageIdList 消息 id 列表
 * @param conversation 消息所属会话
 */
Future<Result<List<MessageReaction>>> getMessagesReaction(List<String> messageIdList, Conversation conversation) async

/**
 * 获取缓存的消息回应（缓存的数据不一定是最新版本，可用于第一时间渲染，优化用户体验）
 * @param messageIdList 消息 id 列表
 * @return 消息回应列表
 */
Future<Result<List<MessageReaction>>> getCachedMessagesReaction(List<String> messageIdList) async
```

</TabItem>
</Tabs>