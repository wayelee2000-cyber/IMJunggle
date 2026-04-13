---
title: Chat room monitoring
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
{ label: 'ReactNative', value: 'reactnative', },
{ label: 'Hongmeng', value: 'harmony', }
]
}>
<TabItem value="android">

Chat room messages are delivered through the unified [Message Listener](../../watcher/message).  
You can configure monitoring for multiple chat rooms to join and leave.

```java
JIM.getInstance().getChatroomManager().addListener("main", this);

@Override
public void onChatroomJoin(String chatroomId) {
    Log.i("TAG", "onChatroomJoin, chatroomId is " + chatroomId);
}

@Override
public void onChatroomQuit(String chatroomId) {
    Log.i("TAG", "onChatroomQuit, chatroomId is " + chatroomId);
}

@Override
public void onChatroomJoinFail(String chatroomId, int errorCode) {
    Log.i("TAG", "onChatroomJoinFail, chatroomId is " + chatroomId + ", errorCode is " + errorCode);
}

@Override
public void onChatroomQuitFail(String chatroomId, int errorCode) {
    Log.i("TAG", "onChatroomQuitFail, chatroomId is " + chatroomId + ", errorCode is " + errorCode);
}

@Override
public void onChatroomKick(String chatroomId) {
    Log.i("TAG", "onChatroomKick, chatroomId is " + chatroomId);
}

@Override
public void onChatroomDestroy(String chatroomId) {
    Log.i("TAG", "onChatroomDestroy, chatroomId is " + chatroomId);
}
```

You can also monitor chat room attribute changes with multiple configurations.

```java
JIM.getInstance().getChatroomManager().addAttributesListener("main", this);

@Override
public void onAttributesUpdate(String chatroomId, Map<String, String> attributes) {
    Log.i("TAG", "onAttributesUpdate, chatroomId is " + chatroomId + ", attributes are " + attributes);
}

@Override
public void onAttributesDelete(String chatroomId, Map<String, String> attributes) {
    Log.i("TAG", "onAttributesDelete, chatroomId is " + chatroomId + ", attributes are " + attributes);
}
```

</TabItem>
<TabItem value="ios">

Chat room messages are delivered through the unified [Message Listener](../../watcher/message).  
You can configure monitoring for multiple chat rooms to join and leave.

```objectivec
[JIM.shared.chatroomManager addDelegate:self];

- (void)chatroomDidJoin:(NSString *)chatroomId {
    NSLog(@"chatroomDidJoin, chatroomId is %@", chatroomId);
}

- (void)chatroomDidQuit:(NSString *)chatroomId {
    NSLog(@"chatroomDidQuit, chatroomId is %@", chatroomId);
}

- (void)chatroomJoinFail:(NSString *)chatroomId errorCode:(JErrorCode)errorCode {
    NSLog(@"chatroomJoinFail, chatroomId is %@, errorCode is %ld", chatroomId, errorCode);
}

- (void)chatroomQuitFail:(NSString *)chatroomId errorCode:(JErrorCode)errorCode {
    NSLog(@"chatroomQuitFail, chatroomId is %@, errorCode is %ld", chatroomId, errorCode);
}

- (void)chatroomDidDestroy:(NSString *)chatroomId {
    NSLog(@"chatroomDidDestroy, chatroomId is %@", chatroomId);
}

- (void)chatroomDidKick:(NSString *)chatroomId { 
    NSLog(@"chatroomDidKick, chatroomId is %@", chatroomId);
}
```

You can also monitor chat room attribute changes with multiple configurations.

```objectivec
[JIM.shared.chatroomManager addAttributesDelegate:self];

- (void)attributesDidDelete:(NSDictionary<NSString *,NSString *> *)attributes forChatroom:(NSString *)chatroomId {
    NSLog(@"attributesDidDelete, count is %ld, chatroom is %@", attributes.count, chatroomId);
}

- (void)attributesDidUpdate:(NSDictionary<NSString *,NSString *> *)attributes forChatroom:(NSString *)chatroomId {
    NSLog(@"attributesDidUpdate, count is %ld, chatroom is %@", attributes.count, chatroomId);
}
```

</TabItem>
<TabItem value="flutter">

> Not yet provided

</TabItem>
<TabItem value="js">

Chat room monitoring includes two main types: `attribute changes` and `member changes`.  
Chat room messages are delivered through the unified [Message Monitoring](../../watcher/message).

```js
// The current user rejoins the chat room. After a network disconnection and reconnection, the SDK will automatically rejoin the chat room.
jim.on(Event.CHATROOM_USER_REJOINED, (user) => {
  // user => { id: '10002', name: 'xiaokele' }
});

// Current user joins the chat room
jim.on(Event.CHATROOM_USER_JOINED, (user) => {
  // user => { id: '10002', name: 'xiaokele' }
});

// Current user leaves the chat room
jim.on(Event.CHATROOM_USER_QUIT, (user) => {
  // user => { id: '10002', name: 'xiaokele' }
});

// Chat room member joined event
jim.on(Event.CHATROOM_MEMBER_JOINED, (member) => {
  // member => { id: '10001', name: 'xiaoshan' }
});

// Chat room member left event
jim.on(Event.CHATROOM_MEMBER_QUIT, (member) => {
  // member => { id: '10001', name: 'xiaoshan' }
});

// Chat room destruction event. The chat room can be destroyed via the Server API.
jim.on(Event.CHATROOM_DESTROYED, (chatroom) => {
  // chatroom => { id: 'chatroom1001' }
});

// Chat room attribute deletion notification
jim.on(Event.CHATROOM_ATTRIBUTE_DELETED, (chatroom) => {
  console.log('Chat room attributes deleted', chatroom);
  /* 
    chatroom => 
      {
        id: 'chatroom1001',
        attributes: [{ key: 'name' }]
      }
  */
});

// Chat room attribute update notification
jim.on(Event.CHATROOM_ATTRIBUTE_UPDATED, (chatroom) => {
  console.log('Chat room attributes updated', chatroom);
  /* 
    chatroom => 
      {
        id: 'chatroom1001',
        attributes: [{ key: 'name', value: 'xiaoshan', userId: 'User ID who updated the key' }]
      }
  */
});
```

</TabItem>
<TabItem value="reactnative">

Chat room messages are delivered through the unified [Message Listener](../../watcher/message).  
You can configure monitoring for multiple chat rooms to join and leave.

```ts
import JuggleIM from 'juggleim-rnsdk';

// Chat room joined successfully
JuggleIM.onChatroomJoin = (chatroomId: string) => {
  console.log('onChatroomJoin, chatroomId is', chatroomId);
};

// Chat room exited successfully
JuggleIM.onChatroomQuit = (chatroomId: string) => {
  console.log('onChatroomQuit, chatroomId is', chatroomId);
};

// Failed to join chat room
JuggleIM.onChatroomJoinFail = (chatroomId: string, errorCode: number) => {
  console.log('onChatroomJoinFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// Failed to exit chat room
JuggleIM.onChatroomQuitFail = (chatroomId: string, errorCode: number) => {
  console.log('onChatroomQuitFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// Kicked out of chat room
JuggleIM.onChatroomKick = (chatroomId: string) => {
  console.log('onChatroomKick, chatroomId is', chatroomId);
};

// Chat room destroyed
JuggleIM.onChatroomDestroy = (chatroomId: string) => {
  console.log('onChatroomDestroy, chatroomId is', chatroomId);
};
```

You can also monitor chat room attribute changes with multiple configurations.

```ts
// Chat room attributes updated
JuggleIM.onChatroomAttributesUpdate = (chatroomId: string, attributes: Record<string, string>) => {
  console.log('onAttributesUpdate, chatroomId is', chatroomId, ', attributes are', attributes);
};

// Chat room attributes deleted
JuggleIM.onChatroomAttributesDelete = (chatroomId: string, attributes: Record<string, string>) => {
  console.log('onAttributesDelete, chatroomId is', chatroomId, ', attributes are', attributes);
};
```

</TabItem>
<TabItem value="harmony">

Chat room messages are delivered through the unified [Message Listener](../../watcher/message).  
You can configure monitoring for multiple chat rooms to join and leave.

```js
// Chat room joined successfully
JuggleIm.instance.getChatroomManager().onChatroomJoin = (chatroomId) => {
  console.log('onChatroomJoin, chatroomId is', chatroomId);
};

// Chat room exited successfully
JuggleIm.instance.getChatroomManager().onChatroomQuit = (chatroomId) => {
  console.log('onChatroomQuit, chatroomId is', chatroomId);
};

// Failed to join chat room
JuggleIm.instance.getChatroomManager().onChatroomJoinFail = (chatroomId, errorCode) => {
  console.log('onChatroomJoinFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// Failed to exit chat room
JuggleIm.instance.getChatroomManager().onChatroomQuitFail = (chatroomId, errorCode) => {
  console.log('onChatroomQuitFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// Kicked out of chat room
JuggleIm.instance.getChatroomManager().onChatroomKick = (chatroomId) => {
  console.log('onChatroomKick, chatroomId is', chatroomId);
};

// Chat room destroyed
JuggleIm.instance.getChatroomManager().onChatroomDestroy = (chatroomId) => {
  console.log('onChatroomDestroy, chatroomId is', chatroomId);
};
```

You can also monitor chat room attribute changes with multiple configurations.

```js
// Chat room attributes updated
JuggleIm.instance.getChatroomManager().onAttributesUpdate = (chatroomId, attributes) => {
  console.log('onAttributesUpdate, chatroomId is', chatroomId, ', attributes are', attributes);
};

// Chat room attributes deleted
JuggleIm.instance.getChatroomManager().onAttributesDelete = (chatroomId, attributes) => {
  console.log('onAttributesDelete, chatroomId is', chatroomId, ', attributes are', attributes);
};
```

</TabItem>
</Tabs>