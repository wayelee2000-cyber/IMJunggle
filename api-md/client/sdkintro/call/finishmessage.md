---
title: 通话结束消息
hide_title: true
sidebar_position: 6
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

1v1 通话结束时 IM 系统会自动往对应的单聊会话中发送此类消息，用于标识通话记录。
通话结束消息 （CallFinishNotifyMessage）对应的 contentType 是 "jg:callfinishntf";

| 属性名  | 类型     | 说明                                             | 版本  |
| ------- | -------- | ------------------------------------------------ | ----- |
| finishNotifyType | CallFinishNotifyType | 通话结束类型 | 1.8.2 |
| duration | long | 通话时长，单位（ms） | 1.8.2 |
| mediaType | CallMediaType | 通话类型 | 1.8.2 |


```java
public enum CallFinishNotifyType {
    /// 主叫取消
    CANCEL(0),
    /// 被叫拒绝
    REJECT(1),
    /// 被叫无应答
    NO_RESPONSE(2),
    /// 通话结束
    COMPLETE(3);
}
```

</TabItem>
<TabItem value="ios">

1v1 通话结束时 IM 系统会自动往对应的单聊会话中发送此类消息，用于标识通话记录。
通话结束消息 （JCallFinishNotifyMessage）对应的 contentType 是 "jg:callfinishntf";

| 属性名  | 类型     | 说明                                             | 版本  |
| ------- | -------- | ------------------------------------------------ | ----- |
| finishNotifyType | JCallFinishNotifyType | 通话结束类型 | 1.8.2 |
| duration | long long | 通话时长，单位（ms） | 1.8.2 |
| mediaType | JCallMediaType | 通话类型 | 1.8.2 |

```objectivec
typedef NS_ENUM(NSUInteger, JCallFinishNotifyType) {
    // 主叫取消
    JCallFinishNotifyTypeCancel = 0,
    // 被叫拒绝
    JCallFinishNotifyTypeReject = 1,
    // 被叫无应答
    JCallFinishNotifyTypeNoResponse = 2,
    //通话结束
    JCallFinishNotifyTypeComplete = 3
};
```


</TabItem>
<TabItem value="js">

1v1 通话结束时 IM 系统会自动往对应的单聊会话中发送此类消息，用于标识通话记录。
通话结束消息消息监听会收到 `MessageType.COMMAND_RTC_1V1_FINISHED`;

**message.content**

```js
let content = message.content;

/*
  duration: 通话时长
  media_type: 0 表示音频，1 表示视频
  reason: 0 主叫取消，1 被叫拒绝，2 被叫无应答，3 通话结束
*/ 
let { duration, media_type, reason } = content;
```
</TabItem>

<TabItem value="flutter">

1v1 通话结束时 IM 系统会自动往对应的单聊会话中发送此类消息，用于标识通话记录。
通话结束消息 （CallFinishNotifyMessage）对应的 contentType 是 "jg:callfinishntf";

| 属性名  | 类型     | 说明                                             | 版本  |
| ------- | -------- | ------------------------------------------------ | ----- |
| finishNotifyType | int | 通话结束类型 | 1.8.2 |
| duration | int | 通话时长，单位（ms） | 1.8.2 |
| mediaType | int | 通话类型 | 1.8.2 |


```dart
// 通话结束类型
static const int typeCancel = 0;
static const int typeReject = 1;
static const int typeNoResponse = 2;
static const int typeComplete = 3;

class CallMediaType {
  static const int voice = 0;
  static const int video = 1;
}
```

</TabItem>

<TabItem value="reactnative">

1v1 通话结束时 IM 系统会自动往对应的单聊会话中发送此类消息，用于标识通话记录。
通话结束消息对应的 contentType 是 "jg:callfinishntf";

| 属性名  | 类型     | 说明                                             | 版本  |
| ------- | -------- | ------------------------------------------------ | ----- |
| finishNotifyType | number | 通话结束类型 | 1.0.0 |
| duration | number | 通话时长，单位（ms） | 1.0.0 |
| mediaType | number | 通话类型 | 1.0.0 |

```typescript
// 通话结束类型
enum CallFinishNotifyType {
  CANCEL = 0,      // 主叫取消
  REJECT = 1,      // 被叫拒绝
  NO_RESPONSE = 2, // 被叫无应答
  COMPLETE = 3     // 通话结束
}

enum CallMediaType {
  VOICE = 0,  // 语音
  VIDEO = 1   // 视频
}
```

</TabItem>
</Tabs>