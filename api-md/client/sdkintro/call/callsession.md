---
title: call entity
hide_title: true
sidebar_position: 2
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

In the SDK, audio and video calls are managed through the call entity `ICallSession`. When making an outgoing call, developers obtain the call entity from the return value of the `startSingleCall` or `startMultiCall` method. When answering a call, developers receive the call entity via the `onCallReceive` callback. Developers can also retrieve the call entity corresponding to a specified callId using the following method:

```java
ICallSession callSession = JIM.getInstance().getCallManager().getCallSession(callId);
```

Once developers have the call entity, they can easily access call-related attributes and perform operations such as answering and hanging up.

```java
// Answer a call
void accept();
// Hang up the call
void hangup();
// Turn on camera
void enableCamera(boolean isEnable);
// Set the user's video view
void setVideoView(String userId, View view);
// Start preview
void startPreview(View view);
// Mute microphone
void muteMicrophone(boolean isMute);
// Mute the speakers
void muteSpeaker(boolean isMute);
// Set external sound
// true uses external speakers; false uses earpiece
void setSpeakerEnable(boolean isEnable);
// Switch camera, default true uses front camera
void useFrontCamera(boolean isEnable);
// Invite users to join the call (this feature is not supported when isMultiCall is false)
void inviteUsers(List<String> userIdList);

// Call ID
String getCallId();
// Whether the call is multi-party; false means one-to-one call
boolean isMultiCall();
// Media type (voice/video)
CallConst.CallMediaType getMediaType();
// Call status
CallConst.CallStatus getCallStatus();
// Call start time (the time when the current user is called in a multi-person session; not necessarily equal to the start time of the entire call)
long getStartTime();
// The time the current user joined the call
long getConnectTime();
// The time when the current user ended the call
long getFinishTime();
// Initiator ID of the call
String getOwner();
// User ID that invited the current user to join the call
String getInviter();
// Reason for ending the call
CallConst.CallFinishReason getFinishReason();
// Call participants (excluding the current user)
List<CallMember> getMembers();
// Current user
CallMember getCurrentCallMember();
// Extension fields
String getExtra();
```


</TabItem>
<TabItem value="ios">

In the SDK, audio and video calls are managed through the call entity `id<JCallSession>`. When making an outgoing call, developers obtain the call entity from the return value of the `startSingleCall:mediaType:delegate:` or `startMultiCall:mediaType:delegate:` method. When answering a call, the call entity is received via the `callDidReceive:` callback. Developers can also retrieve the call entity corresponding to a specified callId using the following method:

```objectivec
id<JCallSession> callSession = [JIM.shared.callManager getCallSession:@"callId1"];
```

Once developers have the call entity, they can easily access call-related attributes and perform operations such as answering and hanging up.

```objectivec
@protocol JCallSession <NSObject>
/// Call ID
@property (nonatomic, copy) NSString *callId;
/// Whether the call is multi-party; NO means one-to-one call
@property (nonatomic, assign) BOOL isMultiCall;
/// Media type (Voice/Video)
@property (nonatomic, assign) JCallMediaType mediaType;
/// Call status
@property (nonatomic, assign) JCallStatus callStatus;
/// Call start time (the time when the current user is called in a multi-person session; not necessarily equal to the start time of the entire call)
@property (nonatomic, assign) long long startTime;
/// The time when the current user joined the call
@property (nonatomic, assign) long long connectTime;
/// The time when the current user ended the call
@property (nonatomic, assign) long long finishTime;
/// Initiator ID of the call
@property (nonatomic, copy) NSString *owner;
/// The user ID that invited the current user to join the call
@property (nonatomic, copy) NSString *inviter;
/// Reason for ending the call
@property (nonatomic, assign) JCallFinishReason finishReason;
/// Call participants (excluding the current user)
@property (nonatomic, copy, readonly) NSArray <JCallMember *> *members;
/// Current user
@property (nonatomic, strong, readonly) JCallMember *currentCallMember;
/// Extension fields
@property (nonatomic, copy) NSString *extra;

- (void)addDelegate:(id<JCallSessionDelegate>)delegate;

/// Answer incoming call
- (void)accept;

/// Hang up the call
- (void)hangup;

/// Turn on camera
/// - Parameter isEnable: whether to enable
- (void)enableCamera:(BOOL)isEnable;

/// Set the user's video view
/// - Parameters:
///   - view: video view
///   - userId: user ID (current user or other user in the session)
- (void)setVideoView:(UIView *)view
           forUserId:(NSString *)userId;

/// Start preview
/// - Parameter view: preview video view
- (void)startPreview:(UIView *)view;

/// Mute microphone
/// - Parameter isMute: whether to mute
- (void)muteMicrophone:(BOOL)isMute;

/// Mute the speaker
/// - Parameter isMute: whether to mute
- (void)muteSpeaker:(BOOL)isMute;

/// Set external sound
/// - Parameter isEnable: YES uses external speakers; NO uses earpiece
- (void)setSpeakerEnable:(BOOL)isEnable;

/// Switch camera, default YES uses front camera
/// - Parameter isEnable: YES to use the front camera; NO to use the rear camera
- (void)useFrontCamera:(BOOL)isEnable;

/// Invite users to join the call (this function is not supported when isMultiCall is NO)
/// - Parameter userIdList: list of user IDs to invite
- (void)inviteUsers:(NSArray <NSString *> *)userIdList;
```


</TabItem>
<TabItem value="js">

In the SDK, audio and video calls are managed through the call entity `CallSession`. When making an outgoing call, developers obtain the call entity from the return value of the `startSingleCall` or `startMultiCall` method. When answering a call, developers receive the call entity via the `CallEvent.INVITED` callback. Developers can also retrieve the call entity corresponding to a specified callId using the following method:

```javascript
const callSession = juggleCall.getCallSession(callId);
```

Once developers have the call entity, they can easily access call-related attributes and perform operations such as answering and hanging up.

```javascript
// Initiate a one-to-one call
await callSession.startSingleCall({
  memberId: 'user_id',
  isEnableCamera: true,
  isMuteMicrophone: false,
  ext: ''
});

// Initiate a multi-person call
await callSession.startMultiCall({
  memberIds: ['user_id1', 'user_id2'],
  isEnableCamera: true,
  isMuteMicrophone: false,
  ext: ''
});

// Answer a call
await callSession.accept({
  isEnableCamera: true,
  isMuteMicrophone: false
});

// Hang up the call
await callSession.hangup();

// Mute microphone
await callSession.muteMicrophone(true);

// Mute the speakers
await callSession.muteSpeaker(true);

// Invite users to join the call
await callSession.inviteUsers({
  memberIds: ['user_id'],
  isEnableCamera: true
});

// Set the user's video view
await callSession.setVideoView({
  userId: 'user_id',
  videoElement: HTMLVideoElement
});

/// Call ID
callId: string;
/// Whether the call is multi-party; false means one-to-one call
isMultiCall: boolean;
/// Call status
callStatus: number;
/// Call start time (the time when the current user is called in a multi-person session; not necessarily equal to the start time of the entire call)
startTime: number;
/// The time when the current user joined the call
connectTime: number;
/// The time when the current user ended the call
finishTime: number;
/// User who invited the current user to join the call
inviter: object;
/// Call participants (excluding the current user)
members: Array;
/// Extension fields
ext: string;
```
</TabItem>

<TabItem value="flutter">

In the SDK, audio and video calls are managed through the call entity `CallSession`. When making an outgoing call, developers obtain the call entity from the return value of the `startSingleCall` or `startMultiCall` method. When answering a call, developers receive the call entity via the `onCallReceive` callback. Developers can also retrieve the call entity corresponding to a specified callId using the following method:

```dart
CallSession callSession = await JuggleIm.instance.getCallSession(callId);
```

Once developers have the call entity, they can easily access call-related attributes and perform operations such as answering and hanging up.

```dart
// Answer a call
Future<void> accept() async;
// Hang up the call
Future<void> hangup() async;
// Turn on camera
Future<void> enableCamera(bool isEnable) async;
// Set the user's video view
Future<void> setVideoView(String userId, VideoView view) async;
// Start preview
Future<void> startPreview(VideoView view) async;
// Mute microphone
Future<void> muteMicrophone(bool isMute) async;
// Mute the speakers
Future<void> muteSpeaker(bool isMute) async;
// Set external sound
// true uses external speakers; false uses earpiece
Future<void> setSpeakerEnable(bool isEnable) async;
// Switch camera, default true uses front camera
Future<void> useFrontCamera(bool isEnable) async;
// Invite users to join the call (this feature is not supported when isMultiCall is false)
Future<void> inviteUsers(List<String> userIdList) async;

/// Call ID
String callId = '';
/// Whether the call is multi-party; false means one-to-one call
bool isMultiCall = false;
/// Media type (Voice 0 / Video 1)
int mediaType = 0;
/// Call status (refer to CallStatus)
int callStatus = 0;
/// Call start time (the time when the current user is called in a multi-person session; not necessarily equal to the start time of the entire call)
int startTime = 0;
/// The time when the current user joined the call
int connectTime = 0;
/// The time when the current user ended the call
int finishTime = 0;
/// Initiator ID of the call
String owner = '';
/// The user ID that invited the current user to join the call
String inviterId = '';
/// Reason for call ending (refer to CallFinishReason)
int finishReason = 0;
/// Call participants (excluding the current user)
List<CallMember> members = [];
/// Extension fields
String extra = '';
```


</TabItem>

<TabItem value="reactnative">

In the SDK, audio and video calls are managed through the call entity `CallSession`. When making an outgoing call, developers obtain the call entity from the return value of the `startSingleCall` or `startMultiCall` method. When answering a call, developers receive the call entity via the `onCallReceive` callback. Developers can also retrieve the call entity corresponding to a specified callId using the following method:

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

const callSession = await JuggleIMCall.getCallSession(callId);
```

Once developers have the call entity, they can easily access call-related attributes and perform operations such as answering and hanging up.

```typescript
// Answer a call
await callSession.accept();
// Hang up the call
await callSession.hangup();
// Turn on camera
await callSession.enableCamera(boolean);
// Mute microphone
await callSession.muteMicrophone(boolean);
// Mute the speakers
await callSession.muteSpeaker(boolean);
// Set external sound
// true uses external speakers; false uses earpiece
await callSession.setSpeakerEnable(boolean);
// Switch camera, default true uses front camera
await callSession.useFrontCamera(boolean);
// Invite users to join the call (this feature is not supported when isMultiCall is false)
await callSession.inviteUsers(userIdList);

// Set the user's video view
await callSession.setVideoView(userId: string, view: Component | null);

// Start preview
await callSession.startPreview(view);

  /**
     * Stop preview
     * Used to stop the preview when the called party hangs up before answering.
     * If you answer the call, there is no need to stop the preview (it is automatically handled at the end of the call).
     *
     * Usage scenarios:
     * - As the called party, the preview is turned on after being called, then hangs up directly, so the preview needs to be stopped.
     * - If the call is answered, there is no need to call this method (it will automatically stop when the call ends).
     */
await callSession.stopPreview();

/// Call ID
callId: string;
/// Whether the call is multi-party; false means one-to-one call
isMultiCall: boolean;
/// Media type (Voice 0 / Video 1)
mediaType: number;
/// Call status (refer to CallStatus)
callStatus: number;
/// Call start time
startTime: number;
/// The time when the current user joined the call
connectTime: number;
/// The time when the current user ended the call
finishTime: number;
/// Initiator ID of the call
owner: string;
/// The user ID that invited the current user to join the call
inviterId: string;
/// Reason for call ending (refer to CallFinishReason)
finishReason: number;
/// Call participants (excluding the current user)
members: CallMember[];
/// Current user
currentCallMember: CallMember;
/// Extension fields
extra: string;
```

</TabItem>

</Tabs>