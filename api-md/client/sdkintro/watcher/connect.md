---
title: Connection events
hide_title: true
sidebar_position: 2
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android' },
{ label: 'iOS', value: 'ios' },
{ label: 'JavaScript', value: 'js' },
{ label: 'Flutter', value: 'flutter' },
{ label: 'ReactNative', value: 'reactnative' }
]}
>
<TabItem value="android">

You can register multiple connection listeners.

```java
JIM.getInstance().getConnectionManager().addConnectionStatusListener("main", new IConnectionManager.IConnectionStatusListener() {

    /// Callback for connection status changes
    /// - Parameters:
    ///   - status: the new connection status
    ///   - code: connection error code. This is only valid when the status is
    ///           JIMConst.ConnectionStatus.FAILURE. In all other states it is 0.
    ///   - extra: additional message
    @Override
    public void onStatusChange(JIMConst.ConnectionStatus status, int code, String extra) {
        if (status == JIMConst.ConnectionStatus.CONNECTED) {
            Log.i("TAG", "SDK connect success");
        }
    }

    /// Callback when the local database is opened. Even while the device is
    /// offline, you can still open the local database and view message history.
    @Override
    public void onDbOpen() {
        Log.i("TAG", "onDbOpen");
    }

    @Override
    public void onDbClose() {

    }
});
```

</TabItem>
<TabItem value="ios">

You can register multiple delegates.

```objectivec
[JIM.shared.connectionManager addDelegate:self];

/// Callback when the local database is opened. Even while the device is
/// offline, you can still open the local database and view message history.
- (void)dbDidOpen {
    NSLog(@"dbDidOpen");
}

/// Callback for connection status changes
/// - Parameters:
///   - status: the new connection status
///   - code: connection error code. This is only valid when the status is
///           JConnectionStatusFailure. In all other states it is 0.
///   - extra: additional message
- (void)connectionStatusDidChange:(JConnectionStatus)status
                        errorCode:(JErrorCode)code
                            extra:(NSString *)extra {
    if (JConnectionStatusConnected == status) {
        NSLog(@"SDK connect success");
    }
}
```
</TabItem>
<TabItem value="js">

You only need to register this listener once globally. If you register it again, the previous handler is overwritten. Except for `connect`, all other SDK APIs should be called only after the connection is established. For event details, see [Listener enums](../enum/web.md#listener).

```js
let { Event, ConnectionState } = JIM;

jim.on(Event.STATE_CHANGED, ({ state, user }) => {

  if (ConnectionState.CONNECTING == state) {
    console.log('IM is connecting');
  }
  
  if (ConnectionState.CONNECTED == state) {
    console.log('IM is connected', user);
  }
  
  // The SDK handles reconnection internally, so the application layer usually
  // does not need to reconnect manually. Reconnect failure or an active
  // disconnect will both trigger the DISCONNECTED state.
  if (ConnectionState.DISCONNECTED == state) {
    console.log('IM is disconnected');
  }

});
```
</TabItem>
<TabItem value="reactnative">

You can register multiple connection listeners. Each listener must use a unique key. The returned function can be used to unsubscribe.

**Example Code**

```typescript
import JuggleIM from 'juggleim-rnsdk';

// Add a connection status listener and keep the returned unsubscribe function.
const unsubscribeConnection = JuggleIM.addConnectionStatusListener('connection_key', (status, code, extra) => {
  // status: 'connected' | 'connecting' | 'disconnected' | 'failure'
  // code: status code. When the connection fails, this is the error code.
  // extra: additional message
  if (status === 'connected') {
    // Connected successfully
  }
  if (status === 'connecting') {
    // Connecting
  }
  if (status === 'disconnected') {
    // Disconnected
  }
  if (status === 'failure') {
    // Connection failed. `code` is the error code and `extra` is the error message.
  }
});

// Remove the listener
// unsubscribeConnection();
```

</TabItem>
<TabItem value="flutter">

The connection listener can only be assigned once. Setting it again will replace the previous listener. If you need multiple handlers, it is recommended to process all states in one listener and then redistribute events in your application layer.

**Example Code**

```dart
JuggleIM.instance.onConnectionStatusChange = (int connectionStatus, int code, String extra) {
  if (connectionStatus == SDKConnectionStatus.CONNECTED) {
    // Connected successfully
  }
  if (connectionStatus == SDKConnectionStatus.CONNECTING) {
    // Connecting
  }
  if (connectionStatus == SDKConnectionStatus.DISCONNECTED) {
    // Disconnected
  }
  if (connectionStatus == SDKConnectionStatus.FAILURE) {
    // Connection failed. `code` is the error code and `extra` is the error message.
  }
};

// Callback when the local database is opened. Even while the device is
// offline, you can still open the local database and view message history.
JuggleIM.instance.onDbOpen = () {

};
```

</TabItem>
</Tabs>
