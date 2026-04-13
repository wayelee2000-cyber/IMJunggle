---
title: Flutter
hide_title: true
sidebar_position: 4
---

#### Connection Status

```dart
class ConnectionStatus {
  static const int idle = 0;
  static const int connected = 1;
  static const int disconnected = 2;
  static const int connecting = 3;
  static const int failure = 4;
}
```

#### Conversation Type

```dart
class ConversationType {
  static const int unknown = 0;
  static const int private = 1;
  static const int group = 2;
  static const int chatroom = 3;
  static const int system = 4;
}
```

#### Pull Direction

```dart
class PullDirection {
  static const int newer = 0;
  static const int older = 1;
}
```

#### Message Direction

```dart
class MessageDirection {
  static int send = 1;
  static int receive = 2;
}
```

#### Message State

```dart
class MessageState {
  static int unknown = 0;
  static int sending = 1;
  static int sent = 2;
  static int fail = 3;
  static int uploading = 4;
}
```

#### Call Status

```dart
class CallStatus {
  static const int idle = 0;
  static const int incoming = 1;
  static const int outgoing = 2;
  static const int connecting = 3;
  static const int connected = 4;
}
```

#### Call Media Type

```dart
class CallMediaType {
  static const int voice = 0;
  static const int video = 1;
}
```

#### Call End Reason

```dart
class CallFinishReason {
  /// Unknown reason
  static const int unknown = 0;
  /// Current user hung up an answered call
  static const int hangup = 1;
  /// Current user declined the call
  static const int decline = 2;
  /// Current user is busy
  static const int busy = 3;
  /// Current user did not answer
  static const int noResponse = 4;
  /// Current user canceled the call
  static const int cancel = 5;
  /// Remote user hung up an answered call
  static const int otherSideHangup = 6;
  /// Remote user declined the call
  static const int otherSideDecline = 7;
  /// Remote user is busy
  static const int otherSideBusy = 8;
  /// Remote user did not answer
  static const int otherSideNoResponse = 9;
  /// Remote user canceled the call
  static const int otherSideCancel = 10;
  /// Room was destroyed
  static const int roomDestroy = 11;
  /// Network error
  static const int networkError = 12;
  /// Current user answered the call on another device
  static const int acceptOnOtherClient = 13;
  /// Current user hung up the call on another device
  static const int hangupOnOtherClient = 14;
}
```