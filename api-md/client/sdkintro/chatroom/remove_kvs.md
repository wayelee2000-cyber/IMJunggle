---
title: delete attribute
hide_title: true
sidebar_position: 6
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

Deleting chat room attributes supports batch operations. The deletion command is automatically synchronized to all members of the chat room and delivered through the [Chat Room Attribute Change Event](../event).

**Interface definition**

```java
/**
 * Delete chat room attributes
 *
 * @param chatroomId Chat room ID
 * @param keys List of attribute keys to be deleted. Keys set by users other than the current user cannot be deleted.
 * @param callback Completion callback.
 *                 When the code returns JErrorCode.NONE, it means all attributes were deleted successfully.
 *                 Other codes indicate that some keys failed to be deleted. All keys that failed deletion will be returned with their corresponding error codes. Refer to the definition of JErrorCode for details.
 */
void removeAttributes(String chatroomId, List<String> keys, IChatroomAttributesUpdateCallback callback);
```

**Sample Code**

```java
List<String> keys = new ArrayList<>();
keys.add("Key1");
JIM.getInstance().getChatroomManager().removeAttributes("chatroomId1", keys, new IChatroomManager.IChatroomAttributesUpdateCallback() {
    @Override
    public void onComplete(int errorCode, Map<String, Integer> failedKeys) {

    }
});
```

</TabItem>
<TabItem value="ios">

Deleting chat room attributes supports batch operations. The deletion command is automatically synchronized to all members of the chat room and delivered through the [Chat Room Attribute Change Event](../event).

**Interface definition**

```objectivec
/// Delete chat room attributes
/// - Parameters:
///   - keys: List of attribute keys to be deleted. Keys set by users other than the current user cannot be deleted.
///   - chatroomId: Chat room ID
///   - completeBlock: Completion callback.
///     Returns JErrorCodeNone to indicate all attributes were deleted successfully.
///     Other codes indicate some keys failed to be deleted. All failed keys will be returned with their corresponding error codes. Refer to the definition of JErrorCode for details.
- (void)removeAttributes:(NSArray <NSString *> *)keys
             forChatroom:(NSString *)chatroomId
                complete:(void (^)(JErrorCode code, NSDictionary<NSString *, NSNumber *> *failedKeys))completeBlock;
```

**Sample Code**

```objectivec
NSArray <NSString *> *keys = @[@"key1"];
    
[JIM.shared.chatroomManager removeAttributes:keys
                                 forChatroom:@"chatroomId1"
                                    complete:^(JErrorCode code, NSDictionary<NSString *,NSNumber *> *failedKeys) {

}];
```

</TabItem>
<TabItem value="js">

Deleting chat room attributes supports batch operations. The deletion command is automatically synchronized to all members of the chat room and delivered through the [Chat Room Attribute Deletion Event](../event).

Batch deletion may fail for some attributes. For example, if a `key` was set by another member and `isForce` is not set to `true`, the deletion will fail.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|-------------------------|---------|-------|---|----------|----------|
| chatroom | Object | Yes | None | Chatroom object | 1.6.0 |
| chatroom.id | String | Yes | None | Chatroom ID | 1.6.0 |
| chatroom.attributes | Array | Yes | None | List of attributes to remove | 1.6.0 |

**_Description of each object in chatroom.attributes_**

| Name | Type | Required | Default | Description | Version |
|---------------|----------|-------|---|----------|----------|
| key | String | Yes | None | Attribute key | 1.6.0 |
| value | String | Yes | None | Attribute value | 1.6.0 |
| isForce | Boolean | No | false | Whether to force deletion | 1.6.0 |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001',
  attributes: [
    { key: 'name', isForce: true },
    { key: 'age' }
  ]
};

jim.removeChatroomAttributes(chatroom).then((result) => {
  console.log('Chatroom attributes removed successfully');
  /* 
    result => { success: [{ key: 'name' }], fail:[{ key: 'age', code: 14006 }] }
  */
}, (error) => {
  console.log('Error', error);
});
```

</TabItem>
<TabItem value="flutter">

Deleting chat room attributes supports batch operations. The deletion command is automatically synchronized to all members of the chat room and delivered through the [Chat Room Attribute Change Event](../event).

**Sample Code**

```dart
List<String> keys = ["key1"];
await JuggleIm.instance.getChatroomManager().removeAttributes("chatroomId1", keys);
```

</TabItem>
<TabItem value="reactnative">

Deleting chat room attributes supports batch operations. The deletion command is automatically synchronized to all members of the chat room and delivered through the [Chat Room Attribute Change Event](../event).

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const keys = ["key1"];
await JuggleIM.removeChatroomAttributes("chatroomId1", keys);
```

</TabItem>
</Tabs>