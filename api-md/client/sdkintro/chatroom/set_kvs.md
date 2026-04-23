---
title: set attributes
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
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

Set chatroom properties with support for batch operations. The settings will be automatically synchronized to all members of the chatroom and returned through the [Chatroom Property Change Event](./event.md).

**Interface definition**

```java
/**
 * Set chatroom properties.
 *
 * @param chatroomId The chatroom ID.
 * @param attributes Chatroom attributes, where both keys and values are strings. Supports setting up to 100 different attributes.
 *                   Keys set by users other than the current user cannot be modified on the client (returns JErrorCode.CHATROOM_KEY_UNAUTHORIZED).
 * @param callback Completion callback.
 *                 When the code returns JErrorCode.NONE, all properties have been set successfully.
 *                 Other codes indicate that some keys failed to be set. All failed keys will be returned with their corresponding error codes, which can be found in the definition of JErrorCode.
 */
void setAttributes(String chatroomId, Map<String, String> attributes, IChatroomAttributesUpdateCallback callback);
```

**Sample Code**

```java
Map<String, String> attributes = new HashMap<>();
attributes.put("key1", "value1");
attributes.put("key2", "value2");
JIM.getInstance().getChatroomManager().setAttributes("chatroomId1", attributes, new IChatroomManager.IChatroomAttributesUpdateCallback() {
    @Override
    public void onComplete(int errorCode, Map<String, Integer> failedKeys) {
        // Handle completion
    }
});
```

</TabItem>
<TabItem value="ios">

Set chatroom properties with support for batch operations. The settings will be automatically synchronized to all members of the chatroom and returned through the [Chatroom Property Change Event](./event.md).

**Interface definition**

```objectivec
/// Set chatroom properties.
/// - Parameters:
///   - attributes: Chatroom attributes, where both keys and values are strings. Supports setting up to 100 different attributes. Keys set by users other than the current user cannot be modified on the client (returns JErrorCodeChatroomKeyUnauthorized).
///   - chatroomId: Chatroom ID.
///   - completeBlock: Completion callback.
///     Returns JErrorCodeNone when all properties are set successfully.
///     Other codes indicate that some keys failed to be set. All failed keys will be returned with their corresponding error codes, which can be found in the definition of JErrorCode.
- (void)setAttributes:(NSDictionary <NSString *, NSString *> *)attributes
          forChatroom:(NSString *)chatroomId
             complete:(void (^)(JErrorCode code, NSDictionary<NSString *, NSNumber *> *failedKeys))completeBlock;
```

**Sample Code**

```objectivec
NSDictionary <NSString *, NSString *> *attr = @{@"key1":@"value1", @"key2":@"value2"};
[JIM.shared.chatroomManager setAttributes:attr
                              forChatroom:@"chatroomId1"
                                  complete:^(JErrorCode code, NSDictionary<NSString *,NSNumber *> *failedKeys) {
    // Handle completion
}];
```

</TabItem>
<TabItem value="js">

Set chatroom properties with support for batch operations. The settings will be automatically synchronized to all members of the chatroom and returned through the [Chatroom Property Change Event](./event.md).

When setting attributes in batches, some settings may fail. For example, if a `key` has already been set by another member and `isForce` is not set to `true`, the operation will fail. Please refer to the corresponding [error codes](../status_code/web.md) for details.

**Parameter description**

| Name               | Type   | Required | Default | Description          | Version |
|--------------------|--------|----------|---------|----------------------|---------|
| chatroom           | Object | Yes      | None    | Chatroom object      | 1.6.0   |
| chatroom.id        | String | Yes      | None    | Chatroom ID          | 1.6.0   |
| chatroom.attributes | Array  | Yes      | None    | List of attributes   | 1.6.0   |

**_Description of each object in chatroom.attributes_**

| Name     | Type    | Required | Default | Description                                                                 | Version |
|----------|---------|----------|---------|-----------------------------------------------------------------------------|---------|
| key      | String  | Yes      | None    | Attribute key                                                               | 1.6.0   |
| value    | String  | Yes      | None    | Attribute value                                                             | 1.6.0   |
| isForce  | Boolean | No       | false   | Whether to force the setting                                                 | 1.6.0   |
| isAutoDel| Boolean | No       | false   | Whether the attribute set by the user will be automatically deleted on exit | 1.6.0   |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001',
  attributes: [
    { key: 'name', value: 'xiaoshan', isForce: true, isAutoDel: false },
    { key: 'age',  value: '18' }
  ]
};

jim.setChatroomAttributes(chatroom).then((result) => {
  console.log('Chatroom attributes set successfully');
  /* 
    result => { success: [{ key: 'name' }], fail: [{ key: 'age', code: 14006 }] }
  */
}, (error) => {
  console.log('Error:', error);
});
```

</TabItem>
<TabItem value="flutter">

Set chatroom properties with support for batch operations. The settings will be automatically synchronized to all members of the chatroom and returned through the [Chatroom Property Change Event](./event.md).

**Sample Code**

```dart
Map<String, String> attributes = {
  "key1": "value1",
  "key2": "value2"
};
await JuggleIm.instance.getChatroomManager().setAttributes("chatroomId1", attributes);
```

</TabItem>
<TabItem value="reactnative">

Set chatroom properties with support for batch operations. The settings will be automatically synchronized to all members of the chatroom and returned through the [Chatroom Property Change Event](./event.md).

**Sample Code**

```ts
import JuggleIM from 'juggleim-rnsdk';

const attributes: Record<string, string> = {
  "key1": "value1",
  "key2": "value2"
};
await JuggleIM.setChatroomAttributes("chatroomId1", attributes);
```

</TabItem>
</Tabs>