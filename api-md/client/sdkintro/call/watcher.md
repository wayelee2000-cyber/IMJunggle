---
title: 事件监听
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

通话中的事件监听，可以使用通话实体 `ICallSession` 对象来进行注册。

```java
mCallSession.addListener("SingleCallActivity", this);
```

回调事件定义如下。

```java
interface ICallSessionListener {
    //通话已接通
    void onCallConnect();

    //通话已结束
    void onCallFinish(CallConst.CallFinishReason finishReason);

    //通话中的错误回调
    void onErrorOccur(CallConst.CallErrorCode errorCode);

    // 用户被邀请（多人通话中使用）
    void onUsersInvite(String inviterId, List<String> userIdList);

    // 用户加入通话（多人通话中使用）
    void onUsersConnect(List<String> userIdList);

    // 用户退出通话（多人通话中使用）
    void onUsersLeave(List<String> userIdList);

    // 用户开启/关闭摄像头
    void onUserCameraEnable(String userId, boolean enable);

    // 用户开启/关闭麦克风
    void onUserMicrophoneEnable(String userId, boolean enable);

    // 用户声音大小变化
    // userId 为 key，声音大小为 value
    void onSoundLevelUpdate(HashMap<String, Float> soundLevels);

    // 视频渲染第一祯回调
    void onVideoFirstFrameRender(String userId);
}
```

</TabItem>
<TabItem value="ios">

通话中的事件监听，可以使用通话实体 `id<JCallSession>` 对象来进行注册。

```objectivec
[callSession addDelegate:self];
```

事件定义如下。

```objectivec
@protocol JCallSessionDelegate <NSObject>

@optional

/// 通话已接通
- (void)callDidConnect;

/// 通话已结束
/// - Parameter finishReason: 结束原因
- (void)callDidFinish:(JCallFinishReason)finishReason;

/// 用户被邀请（多人通话中使用）
/// - Parameter userId: 被邀请的用户 id
- (void)userDidInvite:(NSString *)userId;

/// 用户加入通话（多人通话中使用）
/// - Parameter userId: 用户 id
- (void)userDidConnect:(NSString *)userId;

/// 用户退出通话（多人通话中使用）
/// - Parameter userId: 用户 id
- (void)userDidLeave:(NSString *)userId;

/// 用户开启/关闭摄像头
/// - Parameters:
///   - enable: 是否开启
///   - userId: 用户 id
- (void)userCamaraDidChange:(BOOL)enable
                     userId:(NSString *)userId;

/// 用户开启/关闭麦克风
/// - Parameters:
///   - enable: 是否开启
///   - userId: 用户 id
- (void)userMicrophoneDidChange:(BOOL)enable
                         userId:(NSString *)userId;

/// 用户声音大小变化回调
/// - Parameter soundLevels: 由 userId 为 key，声音大小为 value 的字典
- (void)soundLevelDidUpdate:(NSDictionary<NSString *,NSNumber *> *)soundLevels;

/// 视频渲染第一祯回调
/// - Parameter userId: 用户 id
- (void)videoFirstFrameDidRender:(NSString *)userId;

/// 通话中的错误回调
/// - Parameter errorCode: 错误码
- (void)errorDidOccur:(JCallErrorCode)errorCode;

@end
```



</TabItem>
<TabItem value="js">


```javascript
let { CallEvent } = JuggleCall;

// 成员加入通话，可以显示视频的 DOM 节点
juggleCall.on(CallEvent.MEMBER_JOINED, (event) => {
  let { target: { callId, member } } = event;
  let session = juggleCall.getSession({ callId });
  let userId = member.id;
  // createVideo 创建 video 节点
  let el = createVideo(userId);
  session.setVideoView([{ userId, videoElement: el }]);
  console.log('CallEvent.MEMBER_JOINED', event);
});

// 成员退出通话，可以移除显示视频的 DOM 节点
juggleCall.on(CallEvent.MEMBER_QUIT, (event) => {
  let { target: { member } } = event;
  console.log('CallEvent.MEMBER_QUIT', event);
});

// 通话结束后返回
juggleCall.on(CallEvent.CALL_FINISHED, (event) => {
  console.log('CallEvent.CALL_FINISHED', event);
  let { callId, callStatus, isMultiCall, members} = event;
  // members 中包含每个用户断开的原因
  // members[0] => { id: '', reason: 1 }
});
```

**每个用户断开的枚举说明**:

| 键名                     | 值   | 含义                               |
| ------------------------ | ---- | ---------------------------------- |
| CallFinishedReason.HANGUP                   | 1    | 当前用户挂断已接通的来电           |
| CallFinishedReason.DECLINE                  | 2    | 当前用户拒接来电                   |
| CallFinishedReason.BUSY                     | 3    | 当前用户忙线                       |
| CallFinishedReason.NO_RESPONSE              | 4    | 当前用户未接听                     |
| CallFinishedReason.CANCEL                   | 5    | 当前用户取消呼叫                   |
| CallFinishedReason.OTHER_SIDE_HANGUP        | 6    | 对端用户挂断已接通的来电           |
| CallFinishedReason.OTHER_SIDE_DECLINE       | 7    | 对端用户拒接来电                   |
| CallFinishedReason.OTHER_SIDE_BUSY          | 8    | 对端用户忙线                       |
| CallFinishedReason.OTHER_SIDE_NO_RESPONSE   | 9    | 对端用户未接听                     |
| CallFinishedReason.OTHER_SIDE_CANCEL        | 10   | 对端用户取消呼叫                   |
| CallFinishedReason.ROOM_DESTROY             | 11   | 房间被销毁                         |
| CallFinishedReason.NETWORK_ERROR            | 12   | 网络出错                           |

</TabItem>

<TabItem value="flutter">

通话中的事件，可以使用通话实体 `CallSession` 对象来进行监听。

回调事件定义如下。

```dart
//通话已接通
Function()? onCallConnect;
//通话已结束
Function(int finishReason)? onCallFinish;
// 用户被邀请（多人通话中使用）
Function(List<String> userIdList, String inviterId)? onUsersInvite;
// 用户加入通话（多人通话中使用）
Function(List<String> userIdList)? onUsersConnect;
// 用户退出通话（多人通话中使用）
Function(List<String> userIdList)? onUsersLeave;
// 用户开启/关闭摄像头
Function(String userId, bool enable)? onUserCameraChange;
// 用户开启/关闭麦克风
Function(String userId, bool enable)? onUserMicrophoneChange;
//通话中的错误回调
Function(int errorCode)? onErrorOccur;
// 用户声音大小变化
// userId 为 key，声音大小为 value
Function(Map<String, double>)? onSoundLevelUpdate;
// 视频渲染第一祯回调
Function(String userId)? onVideoFirstFrameRender;
```

</TabItem>

<TabItem value="reactnative">

通话中的事件，可以使用通话实体 `CallSession` 对象来进行监听。

回调事件定义如下：

```typescript
interface CallSessionListener {
  //通话已接通
  onCallConnect?: () => void;
  //通话已结束
  onCallFinish?: (finishReason: number) => void;
  // 用户被邀请（多人通话中使用）
  onUsersInvite?: (userIdList: string[], inviterId: string) => void;
  // 用户加入通话（多人通话中使用）
  onUsersConnect?: (userIdList: string[]) => void;
  // 用户退出通话（多人通话中使用）
  onUsersLeave?: (userIdList: string[]) => void;
  // 用户开启/关闭摄像头
  onUserCameraChange?: (userId: string, enable: boolean) => void;
  // 用户开启/关闭麦克风
  onUserMicrophoneChange?: (userId: string, enable: boolean) => void;
  //通话中的错误回调
  onErrorOccur?: (errorCode: number) => void;
  // 用户声音大小变化
  // userId 为 key，声音大小为 value
  onSoundLevelUpdate?: (soundLevels: Map<string, number>) => void;
  // 视频渲染第一祯回调
  onVideoFirstFrameRender?: (userId: string) => void;
}
```

</TabItem>

</Tabs>