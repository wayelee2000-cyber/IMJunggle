---
title: event listening
hide_title: true
sidebar_position: 5
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

You can register event listeners during a call using the call entity `ICallSession` object.

```java
mCallSession.addListener("SingleCallActivity", this);
```

The callback interface is defined as follows:

```java
interface ICallSessionListener {
    // The call has been connected
    void onCallConnect();

    // The call has ended
    void onCallFinish(CallConst.CallFinishReason finishReason);

    // Error callback during the call
    void onErrorOccur(CallConst.CallErrorCode errorCode);

    // User is invited (used in multi-person calls)
    void onUsersInvite(String inviterId, List<String> userIdList);

    // User joins the call (used in multi-person calls)
    void onUsersConnect(List<String> userIdList);

    // User leaves the call (used in multi-person calls)
    void onUsersLeave(List<String> userIdList);

    // User turns camera on/off
    void onUserCameraEnable(String userId, boolean enable);

    // User turns microphone on/off
    void onUserMicrophoneEnable(String userId, boolean enable);

    // Changes in user voice volume
    // userId is the key, sound level is the value
    void onSoundLevelUpdate(HashMap<String, Float> soundLevels);

    // Video rendering first frame callback
    void onVideoFirstFrameRender(String userId);
}
```

</TabItem>
<TabItem value="ios">

You can register event listeners during a call using the call entity `id<JCallSession>` object.

```objectivec
[callSession addDelegate:self];
```

The delegate methods are defined as follows:

```objectivec
@protocol JCallSessionDelegate <NSObject>

@optional

/// Call connected
- (void)callDidConnect;

/// Call ended
/// - Parameter finishReason: reason for call end
- (void)callDidFinish:(JCallFinishReason)finishReason;

/// User invited (used in multi-person calls)
/// - Parameter userId: invited user ID
- (void)userDidInvite:(NSString *)userId;

/// User joins the call (used in multi-person calls)
/// - Parameter userId: user ID
- (void)userDidConnect:(NSString *)userId;

/// User leaves the call (used in multi-person calls)
/// - Parameter userId: user ID
- (void)userDidLeave:(NSString *)userId;

/// User turns camera on/off
/// - Parameters:
///   - enable: whether camera is enabled
///   - userId: user ID
- (void)userCamaraDidChange:(BOOL)enable
                     userId:(NSString *)userId;

/// User turns microphone on/off
/// - Parameters:
///   - enable: whether microphone is enabled
///   - userId: user ID
- (void)userMicrophoneDidChange:(BOOL)enable
                         userId:(NSString *)userId;

/// User voice volume change callback
/// - Parameter soundLevels: dictionary with userId as key and sound level as value
- (void)soundLevelDidUpdate:(NSDictionary<NSString *,NSNumber *> *)soundLevels;

/// Video rendering first frame callback
/// - Parameter userId: user ID
- (void)videoFirstFrameDidRender:(NSString *)userId;

/// Error callback during the call
/// - Parameter errorCode: error code
- (void)errorDidOccur:(JCallErrorCode)errorCode;

@end
```

</TabItem>
<TabItem value="js">

```javascript
let { CallEvent } = JuggleCall;

// When a member joins the call, the video DOM node can be displayed.
juggleCall.on(CallEvent.MEMBER_JOINED, (event) => {
  let { target: { callId, member } } = event;
  let session = juggleCall.getSession({ callId });
  let userId = member.id;
  // createVideo creates a video element
  let el = createVideo(userId);
  session.setVideoView([{ userId, videoElement: el }]);
  console.log('CallEvent.MEMBER_JOINED', event);
});

// When a member leaves the call, the video DOM node can be removed.
juggleCall.on(CallEvent.MEMBER_QUIT, (event) => {
  let { target: { member } } = event;
  console.log('CallEvent.MEMBER_QUIT', event);
});

// Callback after the call ends
juggleCall.on(CallEvent.CALL_FINISHED, (event) => {
  console.log('CallEvent.CALL_FINISHED', event);
  let { callId, callStatus, isMultiCall, members } = event;
  // members contains the reason each user disconnected
  // members[0] => { id: '', reason: 1 }
});
```

**Enumeration of Disconnect Reasons per User**:

| Key name                      | Value | Description                                  |
| ----------------------------- | ----- | -------------------------------------------- |
| CallFinishedReason.HANGUP      | 1     | The current user hung up the connected call |
| CallFinishedReason.DECLINE     | 2     | The current user rejected the call           |
| CallFinishedReason.BUSY        | 3     | The current user is busy                      |
| CallFinishedReason.NO_RESPONSE | 4     | The current user did not answer               |
| CallFinishedReason.CANCEL      | 5     | The current user canceled the call            |
| CallFinishedReason.OTHER_SIDE_HANGUP      | 6     | The peer user hung up the connected call     |
| CallFinishedReason.OTHER_SIDE_DECLINE     | 7     | The peer user rejected the call               |
| CallFinishedReason.OTHER_SIDE_BUSY        | 8     | The peer user is busy                          |
| CallFinishedReason.OTHER_SIDE_NO_RESPONSE | 9     | The peer user did not answer                   |
| CallFinishedReason.OTHER_SIDE_CANCEL      | 10    | The peer user canceled the call                |
| CallFinishedReason.ROOM_DESTROY            | 11    | The room was destroyed                          |
| CallFinishedReason.NETWORK_ERROR            | 12    | Network error                                  |

</TabItem>

<TabItem value="flutter">

You can monitor events during a call using the call entity `CallSession` object.

The callback events are defined as follows:

```dart
// The call has been connected
Function()? onCallConnect;
// The call has ended
Function(int finishReason)? onCallFinish;
// User is invited (used in multi-person calls)
Function(List<String> userIdList, String inviterId)? onUsersInvite;
// User joins the call (used in multi-person calls)
Function(List<String> userIdList)? onUsersConnect;
// User leaves the call (used in multi-person calls)
Function(List<String> userIdList)? onUsersLeave;
// User turns camera on/off
Function(String userId, bool enable)? onUserCameraChange;
// User turns microphone on/off
Function(String userId, bool enable)? onUserMicrophoneChange;
// Error callback during the call
Function(int errorCode)? onErrorOccur;
// Changes in user voice volume
// userId is the key, sound level is the value
Function(Map<String, double>)? onSoundLevelUpdate;
// Video rendering first frame callback
Function(String userId)? onVideoFirstFrameRender;
```

</TabItem>

<TabItem value="reactnative">

You can monitor events during a call using the call entity `CallSession` object.

The callback events are defined as follows:

```typescript
interface CallSessionListener {
  // The call has been connected
  onCallConnect?: () => void;
  // The call has ended
  onCallFinish?: (finishReason: number) => void;
  // User is invited (used in multi-person calls)
  onUsersInvite?: (userIdList: string[], inviterId: string) => void;
  // User joins the call (used in multi-person calls)
  onUsersConnect?: (userIdList: string[]) => void;
  // User leaves the call (used in multi-person calls)
  onUsersLeave?: (userIdList: string[]) => void;
  // User turns camera on/off
  onUserCameraChange?: (userId: string, enable: boolean) => void;
  // User turns microphone on/off
  onUserMicrophoneChange?: (userId: string, enable: boolean) => void;
  // Error callback during the call
  onErrorOccur?: (errorCode: number) => void;
  // Changes in user voice volume
  // userId is the key, sound level is the value
  onSoundLevelUpdate?: (soundLevels: Map<string, number>) => void;
  // Video rendering first frame callback
  onVideoFirstFrameRender?: (userId: string) => void;
}
```

</TabItem>

</Tabs>