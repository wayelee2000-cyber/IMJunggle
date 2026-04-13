---
title: Get all attributes
hide_title: true
sidebar_position: 8
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

Retrieve all properties of a chat room

**Interface definition**

```java
/**
 * Retrieve all properties of a chat room
 *
 * @param chatroomId The chat room ID
 * @param callback Completion callback
 */
void getAllAttributes(String chatroomId, IChatroomAttributesCallback callback);

interface IChatroomAttributesCallback {
    /**
     * Completion callback
     *
     * @param errorCode Returns JErrorCode.NONE to indicate successful retrieval
     * @param attributes The list of attributes returned
     */
    void onComplete(int errorCode, Map<String, String> attributes);
}
```

**Sample Code**

```java
JIM.getInstance().getChatroomManager().getAllAttributes("chatroomId1", new IChatroomManager.IChatroomAttributesCallback() {
    @Override
    public void onComplete(int errorCode, Map<String, String> attributes) {
        // Handle the result here
    }
});
```

</TabItem>
<TabItem value="ios">

Retrieve all properties of a chat room

**Interface definition**

```objectivec
/// Retrieve all properties of the chat room
/// - Parameters:
///   - chatroomId: The chat room ID
///   - completeBlock: Completion callback; JErrorCodeNone indicates successful retrieval.
- (void)getAllAttributesFromChatroom:(NSString *)chatroomId
                            complete:(void (^)(JErrorCode code, NSDictionary<NSString *, NSString *> *attributes))completeBlock;
```

**Sample Code**

```objectivec
[JIM.shared.chatroomManager getAllAttributesFromChatroom:@"chatroomId1" complete:^(JErrorCode code, NSDictionary<NSString *,NSString *> * _Nonnull attributes) {
    // Handle the result here
}];
```

</TabItem>
<TabItem value="flutter">

> Not yet provided

</TabItem>
<TabItem value="js">

To retrieve all properties of a chat room, call this method after successfully joining the chat room. If you attempt to get the properties without joining, the SDK will return empty data.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|------------------|----------|-------|---|----------|----------|
| chatroom | Object | Yes | None | Chatroom object | 1.6.0 |
| chatroom.id | String | Yes | None | Chatroom ID | 1.6.0 |

**Callback description**

| Properties | Type | Description | Version |
|---------------------|---------|-----------------------------------|----------|
| chatroom | Object | Chatroom object | 1.6.0 |
| chatroom.id | String | Chatroom ID | 1.6.0 |
| chatroom.attributes | Array | All attributes of the chat room; see sample code for data structure | 1.6.0 |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001'
};

jim.getAllChatRoomAttributes(chatroom).then((chatroom) => {
  let { id, attributes } = chatroom;
  /* 
    attributes => 
      [
        { key: 'name', value: 'xiaoshan' },
        { key: 'age', value: 18 },
      ]
  */
}, (error) => {
  console.log('error', error);
});
```

</TabItem>
<TabItem value="reactnative">

Retrieve all properties of a chat room

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const attributes = await JuggleIM.getChatroomAttributes("chatroomId1");
```

</TabItem>
<TabItem value="harmony">

Retrieve all properties of a chat room

**Sample Code**

```js
const attributes = await JuggleIm.instance.getChatroomManager().getAllAttributes("chatroomId1");
```

</TabItem>
</Tabs>