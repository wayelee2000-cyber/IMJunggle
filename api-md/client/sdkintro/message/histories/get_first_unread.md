---
title: 获取第一条未读消息
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

获取会话中的第一条未读消息。

**接口定义**

```java
/**
 * 获取会话中第一条未读消息。
 *
 * @param conversation 会话标识。
 * @param callback  下载文件的回调。参考 {@link IDownloadMediaMessageCallback}。
 */
void getFirstUnreadMessage(Conversation conversation, IGetMessagesCallback callback);
```


</TabItem>
<TabItem value="ios">

获取会话中的第一条未读消息。

**接口定义**

```objectivec
/// 获取会话中第一条未读消息
/// - Parameters:
///   - conversation: 会话标识
///   - successBlock: 成功回调，如果没有未读消息则回调 nil
///   - errorBlock: 失败回调
- (void)getFirstUnreadMessage:(JConversation *)conversation
                      success:(void (^)(JMessage *message))successBlock
                        error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js" label="JavaScript">

> 暂未提供

</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
<TabItem value="harmony" label="鸿蒙">

> 暂未提供

</TabItem>
</Tabs>