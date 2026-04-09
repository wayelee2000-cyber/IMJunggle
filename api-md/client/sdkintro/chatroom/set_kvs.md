---
title: 设置属性
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

设置聊天室属性，支持批量操作，设置指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**接口定义**

```java
/**
 * 设置聊天室属性
 *
 * @param chatroomId 聊天室 id
 * @param attributes 聊天室属性，key 和 value 都是字符串，最多支持设置 100 个不同的属性。
 *                   非当前用户设置的 key 在客户端不能进行操作（返回 JErrorCode.CHATROOM_KEY_UNAUTHORIZED）。
 * @param callback 完成回调
 *                 code 返回 JErrorCode.NONE 时表示所有属性都设置成功。
 *                 其它 code 表示存在设置失败的 key，所有设置失败的 key 都会回调，并返回对应的错误码，可以从 JErrorCode 的定义中找到对应的错误码。
 */
void setAttributes(String chatroomId, Map<String, String> attributes, IChatroomAttributesUpdateCallback callback);
```

**示例代码**

```java
Map<String, String> attributes = new HashMap<>();
attributes.put("key1", "value1");
attributes.put("key2", "value2");
JIM.getInstance().getChatroomManager().setAttributes("chatroomId1", attributes, new IChatroomManager.IChatroomAttributesUpdateCallback() {
    @Override
    public void onComplete(int errorCode, Map<String, Integer> failedKeys) {

    }
});
```

</TabItem>
<TabItem value="ios">

设置聊天室属性，支持批量操作，设置指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**接口定义**

```objectivec
/// 设置聊天室属性。
/// - Parameters:
///   - attributes: 聊天室属性，key 和 value 都是字符串，最多支持设置 100 个不同的属性。非当前用户设置的 key 在客户端不能进行操作（返回 JErrorCodeChatroomKeyUnauthorized）。
///   - chatroomId: 聊天室 id
///   - completeBlock: 完成回调。
///                    code 返回 JErrorCodeNone 时表示所有属性都设置成功。
///                    其它 code 表示存在设置失败的 key，所有设置失败的 key 都会回调，并返回对应的错误码，可以从 JErrorCode 的定义中找到对应的错误码。
- (void)setAttributes:(NSDictionary <NSString *, NSString *> *)attributes
          forChatroom:(NSString *)chatroomId
             complete:(void (^)(JErrorCode code, NSDictionary<NSString *, NSNumber *> *failedKeys))completeBlock;
```

**示例代码**

```objectivec
NSDictionary <NSString *, NSString *> *attr = @{@"key1":@"value1", @"key2":@"value2"};
[JIM.shared.chatroomManager setAttributes:attr
                              forChatroom:@"chatroomId1"
                                  complete:^(JErrorCode code, NSDictionary<NSString *,NSNumber *> *failedKeys) {
    
}];
```

</TabItem>
<TabItem value="js">


设置聊天室属性，支持批量操作，设置指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

批量设置属性时可能会设置失败，例如 `key` 已经被其他成员设置，没有设置 `isForce` 为 `true` 会提示失败，请查看对应 [错误码](../../status_code/web)

**参数说明**

| 名称                    | 类型     | 必填   | 默认值  | 描述| 版本     |
|-------------------------|---------|-------|---|----------|----------|
| chatroom                | Object | 是     | 无 | 聊天室对象 | 1.6.0    |
| chatroom.id             | String | 是     | 无 | 聊天室 ID | 1.6.0    |
| chatroom.attributes     | Array  | 是     | 无 | 属性列表 | 1.6.0    |

**_chatroom.attributes 每项对象说明_**

| 名称           | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------|---------|-------|---|----------|----------|
| key           | String | 是     | 无 | 聊天室对象 | 1.6.0    |
| value         | String | 是     | 无 | 聊天室 ID | 1.6.0    |
| isForce       | Boolean | 否    | false | 是否强制设置 | 1.6.0    |
| isAutoDel     | Boolean | 否    | false | 设置属性的用户退出聊天室后是否自动删除 | 1.6.0    |

**示例代码**

```js
let chatroom = {
  id: 'chatroom1001',
  attributes: [
    { key: 'name', value: 'xiaoshan', isForce: true, isAutoDel },
    { key: 'age',  value: 18 }
  ]
};

jim.setChatroomAttributes(chatroom).then((result) => {
  console.log('set chatroom attributes successfully');
  /* 
    result => { success: [{ key: 'name' }], fail:[{ key: 'age', code: 14006 }] }
  */
}, (error) => {
  console.log('error', error);
});
```

</TabItem>
<TabItem value="flutter">

设置聊天室属性，支持批量操作，设置指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**示例代码**

```dart
Map<String, String> attributes = {
  "key1": "value1",
  "key2": "value2"
};
await JuggleIm.instance.getChatroomManager().setAttributes("chatroomId1", attributes);
```

</TabItem>
<TabItem value="reactnative">

设置聊天室属性，支持批量操作，设置指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**示例代码**

```ts
import JuggleIM from 'juggleim-rnsdk';

const attributes: Record<string, string> = {
  "key1": "value1",
  "key2": "value2"
};
await JuggleIM.setChatroomAttributes("chatroomId1", attributes);
```

</TabItem>
<TabItem value="harmony">

设置聊天室属性，支持批量操作，设置指令会自动同步至聊天室全部成员���通过 [聊天室属性变更事件](../event) 返回

**示例代码**

```js
let attributes = {
  "key1": "value1",
  "key2": "value2"
};
JuggleIm.instance.getChatroomManager().setAttributes("chatroomId1", attributes);
```

</TabItem>
</Tabs>