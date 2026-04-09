---
title: 通话实体
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

SDK 中通过通话实体 `ICallSession` 对音视频通话进行操作。呼出通话时，开发者通过 `startSingleCall` 或者 `startMultiCall` 方法的返回值获取通话实体。接听通话时，开发者通过 `onCallReceive` 回调获取通话实体。开发者还可以使用下面方法获取指定 callId 对应的通话实体。

```java
ICallSession callSession = JIM.getInstance().getCallManager().getCallSession(callId);
```

开发者持有通话实体之后，可以方便的获取通话相关的属性，并对其进行接听、挂断等操作。

```java
// 接听来电
void accept();
// 挂断来电
void hangup();
// 开启摄像头
void enableCamera(boolean isEnable);
// 设置用户的视频 view
void setVideoView(String userId, View view);
// 开始预览
void startPreview(View view);
// 设置麦克风静音
void muteMicrophone(boolean isMute);
// 设置扬声器静音
void muteSpeaker(boolean isMute);
// 设置外放声音
// true 使用外放扬声器；false 使用听筒
void setSpeakerEnable(boolean isEnable);
// 切换摄像头，默认 true 使用前置摄像头
void useFrontCamera(boolean isEnable);
// 呼叫用户加入通话（isMultiCall 为 false 时不支持该功能）
void inviteUsers(List<String> userIdList);

// 通话 id
String getCallId();
// 是否多人通话，false 表示一对一通话
boolean isMultiCall();
// 媒体类型（语音/视频）
CallConst.CallMediaType getMediaType();
// 通话状态
CallConst.CallStatus getCallStatus();
// 呼叫开始时间（多人会话中当前用户被呼叫的时间，不一定等于整个通话开始的时间）
long getStartTime();
// 当前用户加入通话的时间
long getConnectTime();
// 当前用户结束通话的时间
long getFinishTime();
// 通话的发起人 id
String getOwner();
// 邀请当前用户加入通话的用户 id
String getInviter();
// 通话结束原因
CallConst.CallFinishReason getFinishReason();
// 通话参与者（除当前用户外的其他参与者）
List<CallMember> getMembers();
// 当前用户
CallMember getCurrentCallMember();
// 扩展字段
String getExtra();
```


</TabItem>
<TabItem value="ios">

SDK 中通过通话实体 `id<JCallSession>` 对音视频通话进行操作。呼出通话时，开发者通过 `startSingleCall:mediaType:delegate:` 或者 `startMultiCall:mediaType:delegate:` 方法的返回值获取通话实体。接听通话时，用户通过 `callDidReceive:` 回调获取通话实体。开发者还可以使用下面方法获取指定 callId 对应的通话实体。

```objectivec
id<JCallSession> callSession = [JIM.shared.callManager getCallSession:@"callId1"];
```

开发者持有通话实体之后，可以方便的获取通话相关的属性，并对其进行接听、挂断等操作。

```objectivec
@protocol JCallSession <NSObject>
/// 通话 id
@property (nonatomic, copy) NSString *callId;
/// 是否多人通话，NO 表示一对一通话
@property (nonatomic, assign) BOOL isMultiCall;
/// 媒体类型（语音/视频）
@property (nonatomic, assign) JCallMediaType mediaType;
/// 通话状态
@property (nonatomic, assign) JCallStatus callStatus;
/// 呼叫开始时间（多人会话中当前用户被呼叫的时间，不一定等于整个通话开始的时间）
@property (nonatomic, assign) long long startTime;
/// 当前用户加入通话的时间
@property (nonatomic, assign) long long connectTime;
/// 当前用户结束通话的时间
@property (nonatomic, assign) long long finishTime;
/// 通话的发起人 id
@property (nonatomic, copy) NSString *owner;
/// 邀请当前用户加入通话的用户 id
@property (nonatomic, copy) NSString *inviter;
/// 通话结束原因
@property (nonatomic, assign) JCallFinishReason finishReason;
/// 通话参与者（除当前用户外的其他参与者）
@property (nonatomic, copy, readonly) NSArray <JCallMember *> *members;
/// 当前用户
@property (nonatomic, strong, readonly) JCallMember *currentCallMember;
/// 扩展字段
@property (nonatomic, copy) NSString *extra;

- (void)addDelegate:(id<JCallSessionDelegate>)delegate;

/// 接听来电
- (void)accept;

/// 挂断电话
- (void)hangup;

/// 开启摄像头
/// - Parameter isEnable: 是否开启
- (void)enableCamera:(BOOL)isEnable;

/// 设置用户的视频 view
/// - Parameters:
///   - view: 视频 view
///   - userId: 用户 id（当前用户或者会话中的其他用户）
- (void)setVideoView:(UIView *)view
           forUserId:(NSString *)userId;

/// 开始预览
/// - Parameter view: 预览的视频 view
- (void)startPreview:(UIView *)view;

/// 设置麦克风静音
/// - Parameter isMute: 是否静音
- (void)muteMicrophone:(BOOL)isMute;

/// 设置扬声器静音
/// - Parameter isMute: 是否静音
- (void)muteSpeaker:(BOOL)isMute;

/// 设置外放声音
/// - Parameter isEnable: YES 使用外放扬声器；NO 使用听筒
- (void)setSpeakerEnable:(BOOL)isEnable;

/// 切换摄像头，默认 YES 使用前置摄像头
/// - Parameter isEnable: YES 使用前置摄像头；NO 使用后置摄像头
- (void)useFrontCamera:(BOOL)isEnable;

/// 呼叫用户加入通话（isMultiCall 为 NO 时不支持该功能）
/// - Parameter userIdList: 呼叫的用户 id 列表
- (void)inviteUsers:(NSArray <NSString *> *)userIdList;
```


</TabItem>
<TabItem value="js">

SDK 中通过通话实体 `CallSession` 对音视频通话进行操作。呼出通话时，开发者通过 `startSingleCall` 或者 `startMultiCall` 方法的返回值获取通话实体。接听通话时，开发者通过 `CallEvent.INVITED` 回调获取通话实体。开发者还可以使用下面方法获取指定 callId 对应的通话实体。

```javascript
const callSession = juggleCall.getCallSession(callId);
```

开发者持有通话实体之后，可以方便的获取通话相关的属性，并对其进行接听、挂断等操作。

```javascript
// 发起一对一通话
await callSession.startSingleCall({
  memberId: 'user_id',
  isEnableCamera: true,
  isMuteMicrophone: false,
  ext: ''
});

// 发起多人通话
await callSession.startMultiCall({
  memberIds: ['user_id1', 'user_id2'],
  isEnableCamera: true,
  isMuteMicrophone: false,
  ext: ''
});

// 接听来电
await callSession.accept({
  isEnableCamera: true,
  isMuteMicrophone: false
});

// 挂断来电
await callSession.hangup();

// 设置麦克风静音
await callSession.muteMicrophone(true);

// 设置扬声器静音
await callSession.muteSpeaker(true);

// 呼叫用户加入通话
await callSession.inviteUsers({
  memberIds: ['user_id'],
  isEnableCamera: true
});

// 设置用户的视频 view
await callSession.setVideoView({
  userId: 'user_id',
  videoElement: HTMLVideoElement
});

/// 通话 id
callId: string;
/// 是否多人通话，false 表示一对一通话
isMultiCall: boolean;
/// 通话状态
callStatus: number;
/// 呼叫开始时间（多人会话中当前用户被呼叫的时间，不一定等于整个通话开始的时间）
startTime: number;
/// 当前用户加入通话的时间
connectTime: number;
/// 当前用户结束通话的时间
finishTime: number;
/// 邀请当前用户加入通话的用户
inviter: object;
/// 通话参与者（除当前用户外的其他参与者）
members: Array;
/// 扩展字段
ext: string;
```
</TabItem>

<TabItem value="flutter">

SDK 中通过通话实体 `CallSession` 对音视频通话进行操作。呼出通话时，开发者通过 `startSingleCall` 或者 `startMultiCall` 方法的返回值获取通话实体。接听通话时，开发者通过 `onCallReceive` 回调获取通话实体。开发者还可以使用下面方法获取指定 callId 对应的通话实体。

```dart
CallSession callSession = await JuggleIm.instance.getCallSession(callId);
```

开发者持有通话实体之后，可以方便的获取通话相关的属性，并对其进行接听、挂断等操作。

```dart
// 接听来电
Future<void> accept() async;
// 挂断来电
Future<void> hangup() async;
// 开启摄像头
Future<void> enableCamera(bool isEnable) async;
// 设置用户的视频 view
Future<void> setVideoView(String userId, VideoView view) async;
// 开始预览
Future<void> startPreview(VideoView view) async;
// 设置麦克风静音
Future<void> muteMicrophone(bool isMute) async
// 设置扬声器静音
Future<void> muteSpeaker(bool isMute) async;
// 设置外放声音
// true 使用外放扬声器；false 使用听筒
Future<void> setSpeakerEnable(bool isEnable) async;
// 切换摄像头，默认 true 使用前置摄像头
Future<void> useFrontCamera(bool isEnable) async;
// 呼叫用户加入通话（isMultiCall 为 false 时不支持该功能）
Future<void> inviteUsers(List<String> userIdList) async;

/// 通话 id
String callId = '';
/// 是否多人通话，false 表示一对一通话
bool isMultiCall = false;
/// 媒体类型（语音 0 / 视频 1）
int mediaType = 0;
/// 通话状态（参考 CallStatus）
int callStatus = 0;
/// 呼叫开始时间（多人会话中当前用户被呼叫的时间，不一定等于整个通话开始的时间）
int startTime = 0;
/// 当前用户加入通话的时间
int connectTime = 0;
/// 当前用户结束通话的时间
int finishTime = 0;
/// 通话的发起人 id
String owner = '';
/// 邀请当前用户加入通话的用户 id
String inviterId = '';
/// 通话结束原因（参考 CallFinishReason）
int finishReason = 0;
/// 通话参与者（除当前用户外的其他参与者）
List<CallMember> members = [];
/// 扩展字段
String extra = '';
```


</TabItem>

<TabItem value="reactnative">

SDK 中通过通话实体 `CallSession` 对音视频通话进行操作。呼出通话时，开发者通过 `startSingleCall` 或者 `startMultiCall` 方法的返回值获取通话实体。接听通话时，开发者通过 `onCallReceive` 回调获取通话实体。开发者还可以使用下面方法获取指定 callId 对应的通话实体。

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

const callSession = await JuggleIMCall.getCallSession(callId);
```

开发者持有通话实体之后，可以方便的获取通话相关的属性，并对其进行接听、挂断等操作。

```typescript
// 接听来电
await callSession.accept();
// 挂断来电
await callSession.hangup();
// 开启摄像头
await callSession.enableCamera(boolean);
// 设置麦克风静音
await callSession.muteMicrophone(boolean);
// 设置扬声器静音
await callSession.muteSpeaker(boolean);
// 设置外放声音
// true 使用外放扬声器；false 使用听筒
await callSession.setSpeakerEnable(boolean);
// 切换摄像头，默认 true 使用前置摄像头
await callSession.useFrontCamera(boolean);
// 呼叫用户加入通话（isMultiCall 为 false 时不支持该功能）
await callSession.inviteUsers(userIdList);

// 设置用户的视频 view
await callSession.setVideoView(userId: string, view: Component | null);

// 开始预览
await callSession.startPreview(view);

  /**
     * 停止预览
     * 用于被叫方在接听前挂断时停止预览。
     * 如果接听后，则不需要停止预览（由通话结束自动处理）。
     *
     * 使用场景：
     * - 作为被叫方，被呼叫后开启了预览，之后直接挂断，需要停止预览
     * - 如果接听了通话，则不需要调用此方法（通话结束会自动停止）
     */
await callSession.stopPreview();

/// 通话 id
callId: string;
/// 是否多人通话，false 表示一对一通话
isMultiCall: boolean;
/// 媒体类型（语音 0 / 视频 1）
mediaType: number;
/// 通话状态（参考 CallStatus）
callStatus: number;
/// 呼叫开始时间
startTime: number;
/// 当前用户加入通话的时间
connectTime: number;
/// 当前用户结束通话的时间
finishTime: number;
/// 通话的发起人 id
owner: string;
/// 邀请当前用户加入通话的用户 id
inviterId: string;
/// 通话结束原因（参考 CallFinishReason）
finishReason: number;
/// 通话参与者（除当前用户外的其他参与者）
members: CallMember[];
/// 当前用户
currentCallMember: CallMember;
/// 扩展字段
extra: string;
```

</TabItem>

</Tabs>