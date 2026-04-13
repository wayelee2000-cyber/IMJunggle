---
title: Initiate a call
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

After the IM connection is established, enter the other party's `userId` to initiate a call. Developers must request microphone and camera permissions from users in advance.

```java
// Make a single-person video call
ICallSession callSession = JIM.getInstance().getCallManager().startSingleCall(userId, CallConst.CallMediaType.VIDEO, null);

// Make a single audio call
ICallSession callSession = JIM.getInstance().getCallManager().startSingleCall(userId, CallConst.CallMediaType.VOICE, null);
```

You can also pass multiple `userId`s simultaneously to initiate a multi-person call. Remember to request microphone and camera permissions from users beforehand.

```java
// Initiate a multi-person video call
ICallSession callSession = JIM.getInstance().getCallManager().startMultiCall(userIdList, CallConst.CallMediaType.VIDEO, null);

// Make a multi-person audio call
ICallSession callSession = JIM.getInstance().getCallManager().startMultiCall(userIdList, CallConst.CallMediaType.VOICE, null);
```

</TabItem>
<TabItem value="ios">

After the IM connection is established, pass the other party's `userId` to initiate a single call. Developers must request microphone and camera permissions from users in advance.

```objectivec
// Make a single-person video call
id<JCallSession> session = [JIM.shared.callManager startSingleCall:@"userId1"
                                                         mediaType:JCallMediaTypeVideo
                                                          delegate:self];

// Make a single audio call
id<JCallSession> session = [JIM.shared.callManager startSingleCall:@"userId1"
                                                         mediaType:JCallMediaTypeVoice
                                                          delegate:self];
```

You can also pass multiple `userId`s simultaneously to initiate a multi-person call. Be sure to request microphone and camera permissions from users beforehand.

```objectivec
// Initiate a multi-person video call
id<JCallSession> session = [JIM.shared.callManager startMultiCall:@[@"userId1", @"userId2"]
                                                        mediaType:JCallMediaTypeVideo
                                                         delegate:self];

// Make a multi-person audio call
id<JCallSession> session = [JIM.shared.callManager startMultiCall:@[@"userId1", @"userId2"]
                                                        mediaType:JCallMediaTypeVoice
                                                         delegate:self];
```

</TabItem>
<TabItem value="js">

After the IM connection is established, enter the other party's `userId` to initiate a call. Developers must request microphone and camera permissions from users in advance.

```javascript
// Initiate a two-person call
let callSession = juggleCall.create();
callSession.startSingleCall({ memberId: '1y0mce0MrHm' }).catch((error) => {
  console.log('startcall error', error)
});
```

You can also pass multiple `userId`s simultaneously to initiate a multi-person call. Remember to request microphone and camera permissions from users beforehand.

```javascript
// Initiate a multi-person call
let callSession = juggleCall.create();
callSession.startMultiCall({ memberIds: ['1y0mce0MrHm'] });
```
</TabItem>
<TabItem value="flutter">

After the IM connection is established, enter the other party's `userId` to initiate a call. Developers must request microphone and camera permissions from users in advance.

```dart
// Make a single-person video call
CallSession callSession = await JuggleIm.instance.startSingleCall(
    'userId1',
    1
);

// Make a single audio call
CallSession callSession = await JuggleIm.instance.startSingleCall(
    'userId1',
    0
);
```

You can also pass multiple `userId`s simultaneously to initiate a multi-person call. Be sure to request microphone and camera permissions from users beforehand.

```dart
// Initiate a multi-person video call
CallSession callSession = await JuggleIm.instance.startMultiCall(
    ['userId1', 'userId2'],
    1
);

// Make a multi-person audio call
CallSession callSession = await JuggleIm.instance.startMultiCall(
    ['userId1', 'userId2'],
    0
);
```

</TabItem>

<TabItem value="reactnative">

After the IM connection is established, pass the other party's `userId` to initiate a single call. Developers must request microphone and camera permissions from users in advance.

```typescript
import JuggleIMCall, { CallMediaType } from 'juggleim-rnsdk';

// Make a single-person video call
const callSession = await JuggleIMCall.startSingleCall('userId1', CallMediaType.VIDEO);

// Make a single audio call
const callSession = await JuggleIMCall.startSingleCall('userId1', CallMediaType.VOICE);
```

You can also pass multiple `userId`s simultaneously to initiate a multi-person call. Remember to request microphone and camera permissions from users beforehand.

```typescript
// Initiate a multi-person video call
const callSession = await JuggleIMCall.startMultiCall(['userId1', 'userId2'], CallMediaType.VIDEO);

// Make a multi-person audio call
const callSession = await JuggleIMCall.startMultiCall(['userId1', 'userId2'], CallMediaType.VOICE);
```

</TabItem>

</Tabs>