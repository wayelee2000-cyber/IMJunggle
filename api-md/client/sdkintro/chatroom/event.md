---
title: 聊天室监听
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

聊天室消息通过统一的 [消息监听](../../watcher/message) 返回。
聊天室加入退出监听，可以设置多个。

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

聊天室属性变更监听，可以设置多个。

```java
JIM.getInstance().getChatroomManager().addAttributesListener("main", this);

@Override
public void onAttributesUpdate(String chatroomId, Map<String, String> attributes) {
    Log.i("TAG", "onAttributesUpdate, chatroomId is " + chatroomId + ", count is " + attributes);
}

@Override
public void onAttributesDelete(String chatroomId, Map<String, String> attributes) {
    Log.i("TAG", "onAttributesDelete, chatroomId is " + chatroomId + ", count is " + attributes);
}
```

</TabItem>
<TabItem value="ios">

聊天室消息通过统一的 [消息监听](../../watcher/message) 返回。
聊天室加入退出监听，可以设置多个。

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

聊天室属性变更监听，可以设置多个。

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

> 暂未提供

</TabItem>
<TabItem value="js">

聊天室监听包含 `属性变更` 和 `成员变更` 两大类监听，聊天室消息会通过统一 [消息监听](../../watcher/message) 返回

```js

// 当前用户重新加入事件，断网恢复后 SDK 会自动重新加入聊天室
jim.on(Event.CHATROOM_USER_REJOINED, (user) => {
 // user => { id: '10002', name: 'xiaokele' }
});

// 当前用户加入房间
jim.on(Event.CHATROOM_USER_JOINED, (user) => {
  // user => { id: '10002', name: 'xiaokele' }
});

// 当前用户退出房间
jim.on(Event.CHATROOM_USER_QUIT, (user) => {
  // user => { id: '10002', name: 'xiaokele' }
});

// 聊天室成员加入事件
jim.on(Event.CHATROOM_MEMBER_JOINED, (member) => {
  // member => { id: '10001', name: 'xiaoshan' }
});

// 聊天室成员退出事件
jim.on(Event.CHATROOM_MEMBER_QUIT, (member) => {
  // member => { id: '10001', name: 'xiaoshan' }
});

// 聊天室销毁事件，通过 Server API 可销毁聊天室
jim.on(Event.CHATROOM_DESTROYED, (chatroom) => {
  // chatroom => { id: 'chatroom1001' }
});

// 聊天室属性删除通知
jim.on(Event.CHATROOM_ATTRIBUTE_DELETED, (chatroom) => {
  console.log('chatroom attributes deleted', chatroom);
  /* 
    chatroom => 
      {
        id: 'chatroom1001',
        attributes:[{ key: 'name' }]
      }
  */
});

// 聊天室属性更新通知
jim.on(Event.CHATROOM_ATTRIBUTE_UPDATED, (chatroom) => {
  console.log('chatroom attributes updated', chatroom);
  /* 
    chatroom => 
      {
        id: 'chatroom1001',
        attributes:[{ key: 'name', value: 'xiaoshan', userId: '更新 Key 的用户 Id' }]
      }
  */
});

```

</TabItem>
<TabItem value="reactnative">

聊天室消息通过统一的 [消息监听](../../watcher/message) 返回。
聊天室加入退出监听，可以设置多个。

```ts
import JuggleIM from 'juggleim-rnsdk';

// 聊天室加入成功
JuggleIM.onChatroomJoin = (chatroomId: string) => {
  console.log('onChatroomJoin, chatroomId is', chatroomId);
};

// 聊天室退出成功
JuggleIM.onChatroomQuit = (chatroomId: string) => {
  console.log('onChatroomQuit, chatroomId is', chatroomId);
};

// 聊天室加入失败
JuggleIM.onChatroomJoinFail = (chatroomId: string, errorCode: number) => {
  console.log('onChatroomJoinFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// 聊天室退出失败
JuggleIM.onChatroomQuitFail = (chatroomId: string, errorCode: number) => {
  console.log('onChatroomQuitFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// 聊天室被踢出
JuggleIM.onChatroomKick = (chatroomId: string) => {
  console.log('onChatroomKick, chatroomId is', chatroomId);
};

// 聊天室销毁
JuggleIM.onChatroomDestroy = (chatroomId: string) => {
  console.log('onChatroomDestroy, chatroomId is', chatroomId);
};
```

聊天室属性变更监听，可以设置多个。

```ts
// 聊天室属性更新
JuggleIM.onChatroomAttributesUpdate = (chatroomId: string, attributes: Record<string, string>) => {
  console.log('onAttributesUpdate, chatroomId is', chatroomId, ', attributes is', attributes);
};

// 聊天室属性删除
JuggleIM.onChatroomAttributesDelete = (chatroomId: string, attributes: Record<string, string>) => {
  console.log('onAttributesDelete, chatroomId is', chatroomId, ', attributes is', attributes);
};
```

</TabItem>
<TabItem value="harmony">

聊天室消息通过统一的 [消息监听](../../watcher/message) 返回。
聊天室加入退出监听，可以设置多个。

```js
// 聊天室加入成功
JuggleIm.instance.getChatroomManager().onChatroomJoin = (chatroomId) => {
  console.log('onChatroomJoin, chatroomId is', chatroomId);
};

// 聊天室退出成功
JuggleIm.instance.getChatroomManager().onChatroomQuit = (chatroomId) => {
  console.log('onChatroomQuit, chatroomId is', chatroomId);
};

// 聊天室加入失败
JuggleIm.instance.getChatroomManager().onChatroomJoinFail = (chatroomId, errorCode) => {
  console.log('onChatroomJoinFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// 聊天室退出失败
JuggleIm.instance.getChatroomManager().onChatroomQuitFail = (chatroomId, errorCode) => {
  console.log('onChatroomQuitFail, chatroomId is', chatroomId, ', errorCode is', errorCode);
};

// 聊天室被踢出
JuggleIm.instance.getChatroomManager().onChatroomKick = (chatroomId) => {
  console.log('onChatroomKick, chatroomId is', chatroomId);
};

// 聊天室销毁
JuggleIm.instance.getChatroomManager().onChatroomDestroy = (chatroomId) => {
  console.log('onChatroomDestroy, chatroomId is', chatroomId);
};
```

聊天室属性变更监听，可以设置多个。

```js
// 聊天室属性更新
JuggleIm.instance.getChatroomManager().onAttributesUpdate = (chatroomId, attributes) => {
  console.log('onAttributesUpdate, chatroomId is', chatroomId, ', attributes is', attributes);
};

// 聊天室属性删除
JuggleIm.instance.getChatroomManager().onAttributesDelete = (chatroomId, attributes) => {
  console.log('onAttributesDelete, chatroomId is', chatroomId, ', attributes is', attributes);
};
```

</TabItem>
</Tabs>