---
title: 本地消息搜索
hide_title: true
sidebar_position: 3
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

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| conversation | Conversation | 要查询的会话 | 1.0.0 |
| searchContent    | String  | 查询内容                        | 1.0.0    |
| count       | int  | 拉取数量，超过 100 条按 100 返回 | 1.0.0    |
| timestamp        | long  | 消息时间戳，如果传 0 为当前时间 | 1.0.0    |
| direction | JIMConst.PullDirection | 查询方向 | 1.0.0 |

**示例代码**

```java
List<Message> searchResults = JIM.getInstance().getMessageManager().searchMessageInConversation(conversation, "searchContent", 100, 0, JIMConst.PullDirection.OLDER);
```


</TabItem>
<TabItem value="ios">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| searchContent    | NSString  | 查询内容                        | 1.0.0    |
|conversation | JConversation | 要查询的会话 | 1.0.0 |
| count       | int  | 拉取数量，超过 100 条按 100 返回 | 1.0.0    |
| time        | long long  | 消息时间戳，如果传 0 为当前时间 | 1.0.0    |
| direction | JPullDirection | 查询方向 | 1.0.0 |
| contentTypes | `NSArray<NSString *>` | 内容类型，传空返回所有类型 | 1.0.0|

**示例代码**

```objectivec
NSArray <JMessage *> *searchResults = [JIM.shared.messageManager searchMessagesWithContent:@"searchContent"
                                                                            inConversation:nil
                                                                                      count:100
                                                                                      time:0
                                                                                  direction:JPullDirectionOlder
                                                                                contentTypes:nil];
```

</TabItem>
<TabItem value="js">

:::danger 仅 Electron 中支持 
:::

本地消息搜索支持通过 `conversationId` 来控制 _单个会话消息_ 搜索和 _全部会话消息_, 同时支持分页获取，开发者可灵活的应用在全局搜索和聊天内搜索

**参数说明**

| 名称                     | 类型    | 必填 |描述                                                                      | 版本   |
|-------------------------|---------|----|---------------------------------------------------------------------------|--------|
| params                  | Object  | 是 | 消息搜索参数                                                                | 1.0.0  |
| params.conversationType | Number | 否  | [会话类型](../../../enum/web#conversation)                                       | 1.0.0  |
| params.conversationId   | String | 否  | 会话 Id，传值表示搜索 “单个会话消息”，传空表示搜索 “全部会话消息” | 1.0.0  |
| params.keywords       | Array  | 是    | 消息搜索关键字，最多支持 5 个，多个关键字之间是 “或” 的关系                | 1.0.0  |
| params.senderIds      | Number  | 否   | 过滤指定消息发送者的消息           | 1.0.0  |
| params.messageNames   | Number  | 否   | 过滤指定消息类型的消息                         | 1.0.0  |
| params.startTime      | Number  | 否   | 过滤指定时间段的开始时间，时间戳，单位：ms    | 1.0.0  |
| params.endTime        | Number  | 否   | 过滤指定时间段的结束时间，时间戳，单位：ms     | 1.0.0  |
| params.page         | Number  | 否   | 默认值 1，支持分页的页码，默认第一页                         | 1.0.0  |
| params.pageSize          | Number  | 否   | 默认值 10，每页的数据条数                         | 1.0.0  |

**成功回调**

| 名称                 | 类型    | 描述                                    | 版本   |
|---------------------|---------|-----------------------------------------|--------|
| result              | Object  |                                        | 1.0.0  |
| result.isFinished   | Boolean | 是否还有更多的搜索结果            | 1.0.0  |
| result.total        | Number  | 全部会话搜索：表示全部会话中命中关键词的总条数 <br/> 单个会话搜索：表示该会话内命中关键词的条数 | 1.0.0  |
| result.list         | Array   | 全部会话搜索：表示全部会话中命中关键词的消息列表，支持分页获取 <br/> 单个会话搜索：表示该会话内命中关键词的消息列表，支持分页获取 | 1.0.0  |

**result.list 是搜索结果数组，数组每一项说明如下：**

| 名称                 | 类型  | 描述                                    | 版本   |
|---------------------|-------|-----------------------------------------|--------|
| conversationType   | Number| 会话类型      | 1.0.0  |
| conversationId     | String| 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是对方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0  |
| matchedCount       | Array | 当前会话中命中关键词的数量 | 1.0.0  |
| matchedList        | Array | 当前会话中命中关键词的消息明细，数据内部是 [Message](../../../msg/message) 对象 | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**全部会话搜索: 示例代码**
```js
let params = {
  keywords: ['HelloChat'],
};
jim.searchMessages(params).then(({ isFinished, total, list }) => {
  console.log(isFinished, total, list)
});

```

**单个会话搜索: 示例代码**
```js
let { ConversationType } = JIM;
let params = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid1',
  keywords: ['HelloChat'],
};
jim.searchMessages(params).then(({ isFinished, total, list }) => {
  console.log(isFinished, total, list)
});
```
</TabItem>

<TabItem value="harmony">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| params    | SearchParams  | 查询参数                        | 1.0.0    |
| callback | QryMessagesCallback | 内容类型，传空返回所有类型 | 1.0.0|

**示例代码**

```java
let conver = new Conversation("userid1",1)
let params = new SearchParams()
params.conver = conver
params.keywords = "keywords"
JuggleIm.instance.getMessageManager().searchMessages(params,(code,msgs)=>{

})
```


</TabItem>
<TabItem value="flutter" label="Flutter">

**示例代码**

```dart
GetMessageOption option = GetMessageOption();
option.count = 20;
option.startTime = 0; // 开始时间，0 默认当前时间

List<Message> messageList = await JuggleIm.instance.searchMessagesInConversation(
  'searchContent',
  conversation,
  1, // 拉取方向。0: 拉取开始时间之后的消息；1: 拉取开始时间之前的消息
  option
);
```

</TabItem>
</Tabs>