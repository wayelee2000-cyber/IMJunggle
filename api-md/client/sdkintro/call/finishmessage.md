---
title: call end message
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

When a 1v1 call ends, the IM system automatically sends this message to the corresponding single chat session to identify the call record.  
The contentType for the call end message (CallFinishNotifyMessage) is `"jg:callfinishntf"`.

| Attribute name   | Type                 | Description       | Version |
| ---------------- | -------------------- | ----------------- | ------- |
| finishNotifyType | CallFinishNotifyType  | Call end type     | 1.8.2   |
| duration        | long                 | Call duration in milliseconds | 1.8.2   |
| mediaType       | CallMediaType        | Call type         | 1.8.2   |


```java
public enum CallFinishNotifyType {
    /// Caller canceled
    CANCEL(0),
    /// Called party rejected
    REJECT(1),
    /// No answer from the called party
    NO_RESPONSE(2),
    /// Call completed
    COMPLETE(3);
}
```

</TabItem>
<TabItem value="ios">

When a 1v1 call ends, the IM system automatically sends this message to the corresponding single chat session to identify the call record.  
The contentType for the call end message (JCallFinishNotifyMessage) is `"jg:callfinishntf"`.

| Attribute name   | Type                 | Description       | Version |
| ---------------- | -------------------- | ----------------- | ------- |
| finishNotifyType | JCallFinishNotifyType | Call end type     | 1.8.2   |
| duration        | long long            | Call duration in milliseconds | 1.8.2   |
| mediaType       | JCallMediaType       | Call type         | 1.8.2   |

```objectivec
typedef NS_ENUM(NSUInteger, JCallFinishNotifyType) {
    // Caller canceled
    JCallFinishNotifyTypeCancel = 0,
    // Called party rejected
    JCallFinishNotifyTypeReject = 1,
    // Called party did not answer
    JCallFinishNotifyTypeNoResponse = 2,
    // Call completed
    JCallFinishNotifyTypeComplete = 3
};
```

</TabItem>
<TabItem value="js">

When a 1v1 call ends, the IM system automatically sends this message to the corresponding single chat session to identify the call record.  
The call end message event listener will receive `MessageType.COMMAND_RTC_1V1_FINISHED`.

**message.content**

```js
let content = message.content;

/*
duration: call duration in milliseconds
media_type: 0 means audio, 1 means video
reason: 0 caller canceled, 1 called party rejected, 2 called party did not answer, 3 call ended
*/ 
let { duration, media_type, reason } = content;
```
</TabItem>

<TabItem value="flutter">

When a 1v1 call ends, the IM system automatically sends this message to the corresponding single chat session to identify the call record.  
The contentType for the call end message (CallFinishNotifyMessage) is `"jg:callfinishntf"`.

| Attribute name   | Type | Description       | Version |
| ---------------- | ---- | ----------------- | ------- |
| finishNotifyType | int  | Call end type     | 1.8.2   |
| duration        | int  | Call duration in milliseconds | 1.8.2   |
| mediaType       | int  | Call type         | 1.8.2   |


```dart
// Call end types
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

When a 1v1 call ends, the IM system automatically sends this message to the corresponding single chat session to identify the call record.  
The contentType for the call end message is `"jg:callfinishntf"`.

| Attribute name   | Type   | Description       | Version |
| ---------------- | ------ | ----------------- | ------- |
| finishNotifyType | number | Call end type     | 1.0.0   |
| duration        | number | Call duration in milliseconds | 1.0.0   |
| mediaType       | number | Call type         | 1.0.0   |

```typescript
// Call end types
enum CallFinishNotifyType {
  CANCEL = 0,      // Caller canceled
  REJECT = 1,      // Called party rejected
  NO_RESPONSE = 2, // Called party did not answer
  COMPLETE = 3     // Call completed
}

enum CallMediaType {
  VOICE = 0,  // Voice call
  VIDEO = 1   // Video call
}
```

</TabItem>
</Tabs>
