---
title: 获取全部属性
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

获取聊天室全部属性

**接口定义**

```java
/**
 * 获取聊天室所有属性
 *
 * @param chatroomId 聊天室 id
 * @param callback 完成回调
 */
void getAllAttributes(String chatroomId, IChatroomAttributesCallback callback);

interface IChatroomAttributesCallback {
    /**
     * 完成回调
     *
     * @param errorCode 返回 JErrorCode.NONE 时表示获取成功
     * @param attributes 获取回来的属性列表
     */
    void onComplete(int errorCode, Map<String, String> attributes);
}
```

**示例代码**

```java
JIM.getInstance().getChatroomManager().getAllAttributes("chatroomId1", new IChatroomManager.IChatroomAttributesCallback() {
    @Override
    public void onComplete(int errorCode, Map<String, String> attributes) {

    }
});
```

</TabItem>
<TabItem value="ios">

获取聊天室全部属性

**接口定义**

```objectivec
/// 获取聊天室所有属性
/// - Parameters:
///   - chatroomId: 聊天室 id
///   - completeBlock: 完成回调，JErrorCodeNone 表示获取成功。
- (void)getAllAttributesFromChatroom:(NSString *)chatroomId
                            complete:(void (^)(JErrorCode code, NSDictionary <NSString *, NSString *> *attributes))completeBlock;
```

**示例代码**

```objectivec
[JIM.shared.chatroomManager getAllAttributesFromChatroom:@"chatroomId1" complete:^(JErrorCode code, NSDictionary<NSString *,NSString *> * _Nonnull attributes) {
        
}];
```

</TabItem>
<TabItem value="flutter">

> 暂未提供

</TabItem>
<TabItem value="js">

获取聊天室全部属性，需要在加入聊天室成功后调用，未加入聊天室获取属性 SDK 会返回空数据。

**参数说明**

| 名称              | 类型     | 必填   | 默认值  | 描述| 版本     |
|------------------|---------|-------|---|----------|----------|
| chatroom         | Object | 是     | 无 | 聊天室对象 | 1.6.0    |
| chatroom.id      | String | 是     | 无 | 聊天室 ID | 1.6.0    |

**回调说明**

| 属性                 | 类型    | 描述                               | 版本  |
|---------------------|---------|-----------------------------------|----------|
| chatroom            | Object  | 会话对象                            | 1.6.0    |
| chatroom.id         | String  | 聊天室 ID                           | 1.6.0    |
| chatroom.attributes | Array   | 聊天室全部属性，数据结构请参考示例代码   | 1.6.0    |

**示例代码**

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
  console.log('error', error)
});
```


</TabItem>
<TabItem value="reactnative">

获取聊天室全部属性

**示例代码**

```ts
import JuggleIM from 'juggleim-rnsdk';

const attributes = await JuggleIM.getChatroomAttributes("chatroomId1");
```

</TabItem>
<TabItem value="harmony">

获取聊天室全部属性

**示例代码**

```js
const attributes = await JuggleIm.instance.getChatroomManager().getAllAttributes("chatroomId1");
```

</TabItem>
</Tabs>