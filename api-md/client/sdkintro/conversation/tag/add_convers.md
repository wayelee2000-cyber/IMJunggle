---
title: 向标签里添加会话
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
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

向存在的标签内添加会话，添加会话动作自动同步当前用户的多设备。

**接口定义**

```java
/**
 * 将会话添加到标签
 * @param conversations 会话列表
 * @param tagId 标签 id
 * @param callback 结果回调
 */
void addConversationsToTag(List<Conversation> conversations, String tagId, ISimpleCallback callback);
```


</TabItem>
<TabItem value="ios">

向存在的标签内添加会话，添加会话动作自动同步当前用户的多设备。

**接口定义**

```objectivec
/// 将会话添加到标签
/// - Parameters:
///   - conversationList: 会话列表
///   - tagId: 标签 id
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)addConversationList:(NSArray <JConversation *> *)conversationList
                      toTag:(NSString *)tagId
                    success:(void (^)(void))successBlock
                      error:(void (^)(JErrorCode code))errorBlock;
```


</TabItem>
<TabItem value="js">

向存在的标签内添加会话，添加会话动作自动同步当前用户的多设备。

**参数说明**

| 名称          | 类型    | 必填   | 默认值  | 描述                                       | 版本     |
|--------------|---------|--------|--------|--------------------------------------------|----------|
| tag          | Object  | 是     |        | Tag 对象                                   | 1.7.5    |
| tag.id       | String  | 是     |        | 标签 ID，开发者可自定义，最大长度 64 个字符     | 1.7.5    |
| tag.conversations       | Array  | 是     |        | 会话列表，详见代码示例     | 1.7.5    |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let tag = {
  id: 'tag_01',
  conversations: [
    { conversationType: ConversationType.PRIVATE, conversationId: 'userId01' }
  ]
};

jim.addConversationsToTag(tag).then(() => {
  console.log('addConversationsToTag successfully')
}, (error) => {
  console.log(error)
});
```

</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
<TabItem value="reactnative">

向存在的标签内添加会话，添加会话动作自动同步当前用户的多设备。

**接口定义**

```typescript
/**
 * 向标签里添加会话
 * @param tagId 标签ID
 * @param conversations 会话列表
 */
addConversationsToTag(tagId: string, conversations: Array<{
  conversationType: number;
  conversationId: string;
}>): Promise<void>;
```

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.addConversationsToTag('tag_01', [
  {
    conversationType: 1,
    conversationId: 'userId01'
  }
]);
```

</TabItem>
</Tabs>