---
title: 删除属性
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

删除聊天室属性，支持批量操作，删除指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**接口定义**

```java
/**
 * 删除聊天室属性
 *
 * @param chatroomId 聊天室 id
 * @param keys 待删除的属性 key 列表。非当前用户设置的 key 不能删除。
 * @param callback 完成回调。
 *                 code 返回 JErrorCode.NONE 时表示所有属性都删除成功。
 *                 其它 code 表示存在删除失败的 key，所有删除失败的 key 都会回调，并返回对应的错误码，可以从 JErrorCode 的定义中找到对应的错误码。
 */
void removeAttributes(String chatroomId, List<String> keys, IChatroomAttributesUpdateCallback callback);
```

**示例代码**

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

删除聊天室属性，支持批量操作，删除指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**接口定义**

```objectivec
/// 删除聊天室属性
/// - Parameters:
///   - keys: 待删除的属性 key 列表。非当前用户设置的 key 不能删除。
///   - chatroomId: 聊天室 id
///   - completeBlock: 完成回调。
///                    code 返回 JErrorCodeNone 时表示所有属性都删除成功。
///                    其它 code 表示存在删除失败的 key，所有删除失败的 key 都会回调，并返回对应的错误码，可以从 JErrorCode 的定义中找到对应的错误码。
- (void)removeAttributes:(NSArray <NSString *> *)keys
             forChatroom:(NSString *)chatroomId
                complete:(void (^)(JErrorCode code, NSDictionary<NSString *, NSNumber *> *failedKeys))completeBlock;
```

**示例代码**

```objectivec
NSArray <NSString *> *keys = @[@"key1"];
    
[JIM.shared.chatroomManager removeAttributes:keys
                                 forChatroom:@"chatroomId1"
                                    complete:^(JErrorCode code, NSDictionary<NSString *,NSNumber *> *failedKeys) {

}];
```

</TabItem>
<TabItem value="js">

删除聊天室属性，支持批量操作，删除指令会自动同步至聊天室全部成员，通过 [聊天室属性删除事件](../event) 返回

批量删除属性时可能会删除失败，例如 `key` 已经被其他成员设置，没有设置 `isForce` 为 `true` 会提示失败

**参数说明**

| 名称                    | 类型     | 必填   | 默认值  | 描述| 版本     |
|-------------------------|---------|-------|---|----------|----------|
| chatroom                | Object | 是     | 无 | 聊天室对象 | 1.6.0    |
| chatroom.id             | String | 是     | 无 | 聊天室 ID | 1.6.0    |
| chatroom.attributes     | Array  | 是     | 无 | 删除的属性列表 | 1.6.0    |

**_chatroom.attributes 每项对象说明_**

| 名称           | 类型     | 必填   | 默认值  | 描述| 版本     |
|---------------|---------|-------|---|----------|----------|
| key           | String | 是     | 无 | 聊天室对象 | 1.6.0    |
| value         | String | 是     | 无 | 聊天室 ID | 1.6.0    |
| isForce       | Boolean | 否    | false | 是否强制删除 | 1.6.0    |

**示例代码**

```js
let chatroom = {
  id: 'chatroom1001',
  attributes: [
    { key: 'name', isForce: true },
    { key: 'age' }
  ]
};

jim.removeChatroomAttributes(chatroom).then((result) => {
  console.log('remove chatroom attributes successfully');
  /* 
    result => { success: [{ key: 'name' }], fail:[{ key: 'age', code: 14006 }] }
  */
}, (error) => {
  console.log('error', error);
});
```

</TabItem>
<TabItem value="flutter">

删除聊天室属性，支持批量操作，删除指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**示例代码**

```dart
List<String> keys = ["key1"];
await JuggleIm.instance.getChatroomManager().removeAttributes("chatroomId1", keys);
```

</TabItem>
<TabItem value="reactnative">

删除聊天室属性，支持批量操作，删除指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**示例代码**

```ts
import JuggleIM from 'juggleim-rnsdk';

const keys = ["key1"];
await JuggleIM.removeChatroomAttributes("chatroomId1", keys);
```

</TabItem>
<TabItem value="harmony">

删除聊天室属性，支持批量操作，删除指令会自动同步至聊天室全部成员，通过 [聊天室属性变更事件](../event) 返回

**示例代码**

```js
let keys = ["key1"];
JuggleIm.instance.getChatroomManager().removeAttributes("chatroomId1", keys);
```

</TabItem>
</Tabs>