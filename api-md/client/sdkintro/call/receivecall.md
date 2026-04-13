---
title: Call monitoring
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

Developers must register a global listener to receive call events and obtain the call entity. Additionally, they need to request microphone and camera permissions from users in advance.

```java
JIM.getInstance().getCallManager().addReceiveListener("CallReceive", this);
```

The callback interface is defined as follows:

```java
interface ICallReceiveListener {
    void onCallReceive(ICallSession callSession);
}
```

</TabItem>
<TabItem value="ios">

Developers must register a global listener to receive call events and obtain the call entity. Additionally, they need to request microphone and camera permissions from users in advance.

```objcetivec
[JIM.shared.callManager addReceiveDelegate:self];
```

The delegate protocol is defined as follows:

```objcetivec
@protocol JCallReceiveDelegate <NSObject>
/// Received call
/// - Parameter callSession: call instance
- (void)callDidReceive:(id<JCallSession>)callSession;

@end
```

</TabItem>
<TabItem value="js">

Developers must register a global listener to receive call events and obtain the call entity. Additionally, they need to request microphone and camera permissions from users in advance.

```javascript
let { CallEvent } = JuggleCall;

// Receive call invitation
juggleCall.on(CallEvent.INVITED, ({ target }) => {
  let { callId } = target;
  let session = juggleCall.getSession({ callId });
  console.log('CallEvent.INVITED', session);
});
```

</TabItem>
<TabItem value="flutter">

Developers must register a global listener to receive call events and obtain the call entity. Additionally, they need to request microphone and camera permissions from users in advance.

```dart
JuggleIm.instance.onCallReceive = (callSession) {
  // Handle incoming call
};
```

</TabItem>

<TabItem value="reactnative">

Developers must register a global listener to receive call events and obtain the call entity. Additionally, they need to request microphone and camera permissions from users in advance.

```typescript
import JuggleIMCall from 'juggleim-rnsdk';

const removeListener = JuggleIMCall.addReceiveListener({
  onCallReceive: (callSession) => {
    // Handle incoming call
    console.log('Incoming call request', callSession);
  }
});

// To stop monitoring, call:
// removeListener();
```

</TabItem>

</Tabs>