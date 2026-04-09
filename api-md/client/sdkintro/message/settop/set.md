---
title: 设置置顶
hide_title: true
sidebar_position: 1
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

设置消息置顶，支持将会话中的某条消息置于会话顶端用作提醒，`设置置顶` 和 `取消置顶` 通过 `isTop` 区分。

**接口定义**

```java
/**
 * 设置置顶
 * @param messageId 消息 id
 * @param conversation 消息所属会话标识
 * @param isTop 是否置顶
 * @param callback 结果回调
 */
void setTop(String messageId, Conversation conversation, boolean isTop, ISimpleCallback callback);
```

</TabItem>
<TabItem value="ios">

设置消息置顶，支持将会话中的某条消息置于会话顶端用作提醒，`设置置顶` 和 `取消置顶` 通过 `isTop` 区分。

**接口定义**

```objectivec
/// 设置置顶
/// - Parameters:
///   - isTop: YES 表示置顶，NO 表示不置顶
///   - messageId: 消息 id
///   - conversation: 会话标识
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)setTop:(BOOL)isTop
     messageId:(NSString *)messageId
  conversation:(JConversation *)conversation
       success:(void (^)(void))successBlock
         error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

设置消息置顶，支持将会话中的某条消息置于会话顶端用作提醒，`设置置顶` 和 `取消置顶` 通过 `isTop` 区分。

![](./top.png)

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.messageId              | String  | 是    |         | 被置顶的消息 Id                                | 1.0.0  |
| message.isTop                  | Boolean | 是    |         | 是否置顶  | 1.0.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

let msg = {
  conversationType: ConversationType.GROUP,
  conversationId: 'groupid1',
  messageId: 'xxxdkadhdsa',
  isTop: true
};

jim.setTopMessage(msg).then(() => {
  console.log('set message top successfully.')
}, (error) => {
  console.log(error)
});
```
</TabItem>

<TabItem value="reactnative" label="ReactNative">

设置消息置顶，支持将会话中的某条消息置于会话顶端用作提醒，`设置置顶` 和 `取消置顶` 通过 `isTop` 区分。

**参数说明**

| 名称                           | 类型    | 描述          | 版本     |
|-------------------------------|---------|----------------|----------|
| messageId   | String  | 消息 id     | 1.0.0    |
| conversation | Conversation | 会话标识 | 1.0.0    |
| isTop | boolean | 是否置顶  | 1.0.0    |

**示例代码**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const messageId = 'messageId1';
const conversation = {
  type: 1,
  id: 'userId1'
};
const isTop = true;

const success = await JuggleIM.setMessageTop(messageId, conversation, isTop);
console.log('setMessageTop success:', success);
```

</TabItem>
</Tabs>