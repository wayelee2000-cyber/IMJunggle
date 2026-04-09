---
title: 来电监听
hide_title: true
sidebar_position: 3
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

开发者需要注册一个全局的监听以获得被呼叫的事件，并从中得到通话实体。开发者需要提前向用户申请麦克风和摄像头权限。

```java
JIM.getInstance().getCallManager().addReceiveListener("CallReceive", this);
```

回调方法定义如下。

```java
interface ICallReceiveListener {
    void onCallReceive(ICallSession callSession);
}
```

</TabItem>
<TabItem value="ios">

开发者需要注册一个全局的监听以获得被呼叫的事件，并从中得到通话实体。开发者需要提前向用户申请麦克风和摄像头权限。

```objcetivec
[JIM.shared.callManager addReceiveDelegate:self];
```

监听方法定义如下。

```objcetivec
@protocol JCallReceiveDelegate <NSObject>
/// 接听到通话
/// - Parameter callSession: 通话实例
- (void)callDidReceive:(id<JCallSession>)callSession;

@end
```

</TabItem>
<TabItem value="js">

开发者需要注册全局监听以获得被呼叫的事件，并从中得到通话实体。开发者需要提前向用户申请麦克风和摄像头权限。

```javascript
let { CallEvent } = JuggleCall;

// 收到通话邀请
juggleCall.on(CallEvent.INVITED, ({ target }) => {
  let { callId } = target;
  let session = juggleCall.getSession({ callId })
  console.log('CallEvent.INVITED', session)
});

```
</TabItem>
<TabItem value="flutter">

开发者需要一个全局的监听以获得被呼叫的事件，并从中得到通话实体。开发者需要提前向用户申请麦克风和摄像头权限。

```dart
JuggleIm.instance.onCallReceive = (callSession) {

}
```

</TabItem>

<TabItem value="reactnative">

开发者需要注册一个全局的监听以获得被呼叫的事件，并从中得到通话实体。开发者需要提前向用户申请麦克风和摄像头权限。

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

const removeListener = JuggleIMCall.addReceiveListener({
  onCallReceive: (callSession) => {
    // 处理来电
    console.log('收到通话请求', callSession);
  }
});

// 取消监听
// removeListener();
```

</TabItem>

</Tabs>