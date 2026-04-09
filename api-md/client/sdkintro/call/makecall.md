---
title: 发起通话
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

请在 IM 连接成功的状态下，传入对方的 `userId` 进行呼叫。开发者需要提前向用户申请麦克风和摄像头权限。

```java
//发起单人视频呼叫
ICallSession callSession = JIM.getInstance().getCallManager().startSingleCall(userId, CallConst.CallMediaType.VIDEO, null);

//发起单人音频呼叫
ICallSession callSession = JIM.getInstance().getCallManager().startSingleCall(userId, CallConst.CallMediaType.VOICE, null);
```

可以同时传入多个的 `userId` 进行多人呼叫。同样需要提前向用户申请麦克风和摄像头权限。

```java
//发起多人视频呼叫
ICallSession callSession = JIM.getInstance().getCallManager().startMultiCall(userIdList, CallConst.CallMediaType.VIDEO, null);

//发起多人音频呼叫
ICallSession callSession = JIM.getInstance().getCallManager().startMultiCall(userIdList, CallConst.CallMediaType.VOICE, null);
```

</TabItem>
<TabItem value="ios">

请在 IM 连接成功的状态下，传入对方的 `userId` 进行单人呼叫。开发者需要提前向用户申请麦克风和摄像头权限。

```objectivec
//发起单人视频呼叫
id<JCallSession> session = [JIM.shared.callManager startSingleCall:@"userId1"
                                                         mediaType:JCallMediaTypeVideo
                                                          delegate:self];

//发起单人音频呼叫
id<JCallSession> session = [JIM.shared.callManager startSingleCall:@"userId1"
                                                         mediaType:JCallMediaTypeVoice
                                                          delegate:self];
```

可以同时传入多个的 `userId` 进行多人呼叫。同样需要提前向用户申请麦克风和摄像头权限。

```objectivec
//发起多人视频呼叫
id<JCallSession> session = [JIM.shared.callManager startMultiCall:@[@"userId1", @"userId2"]
                                                        mediaType:JCallMediaTypeVideo
                                                         delegate:self];

//发起多人音频呼叫
id<JCallSession> session = [JIM.shared.callManager startMultiCall:@[@"userId1", @"userId2"]
                                                        mediaType:JCallMediaTypeVoice
                                                         delegate:self];
```

</TabItem>
<TabItem value="js">

请在 IM 连接成功的状态下，传入对方的 `userId` 进行呼叫。开发者需要提前向用户申请麦克风和摄像头权限。

```javascript
// 发起二人通话
let callSession = juggleCall.create();
callSession.startSingleCall({ memberId: '1y0mce0MrHm' }).catch((error) => {
  console.log('startcall error', error)
});
```

可以同时传入多个的 `userId` 进行多人呼叫。同样需要提前向用户申请麦克风和摄像头权限。

```javascript
// 发起多人通话
let callSession = juggleCall.create();
callSession.startMultiCall({ memberIds: ['1y0mce0MrHm'] });
```
</TabItem>
<TabItem value="flutter">

请在 IM 连接成功的状态下，传入对方的 `userId` 进行呼叫。开发者需要提前向用户申请麦克风和摄像头权限。

```dart
//发起单人视频呼叫
CallSession callSession = await JuggleIm.instance.startSingleCall(
    'userId1',
    1
);

//发起单人音频呼叫
CallSession callSession = await JuggleIm.instance.startSingleCall(
    'userId1',
    0
);
```

可以同时传入多个的 `userId` 进行多人呼叫。同样需要提前向用户申请麦克风和摄像头权限。

```dart
//发起多人视频呼叫
CallSession callSession = await JuggleIm.instance.startMultiCall(
    ['userId1', 'userId2'],
    1
);

//发起多人音频呼叫
CallSession callSession = await JuggleIm.instance.startMultiCall(
    ['userId1', 'userId2'],
    0
);
```

</TabItem>

<TabItem value="reactnative">

请在 IM 连接成功的状态下，传入对方的 `userId` 进行单人呼叫。开发者需要提前向用户申请麦克风和摄像头权限。

```typescript
import JuggleIMCall, { CallMediaType } from 'juggleim-rnsdk';

//发起单人视频呼叫
const callSession = await JuggleIMCall.startSingleCall('userId1', CallMediaType.VIDEO);

//发起单人音频呼叫
const callSession = await JuggleIMCall.startSingleCall('userId1', CallMediaType.VOICE);
```

可以同时传入多个的 `userId` 进行多人呼叫。同样需要提前向用户申请麦克风和摄像头权限。

```typescript
//发起多人视频呼叫
const callSession = await JuggleIMCall.startMultiCall(['userId1', 'userId2'], CallMediaType.VIDEO);

//发起多人音频呼叫
const callSession = await JuggleIMCall.startMultiCall(['userId1', 'userId2'], CallMediaType.VOICE);
```

</TabItem>

</Tabs>