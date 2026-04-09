---
title: 查询收藏
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

查询收藏列表，按时间倒序排列，支持 `count` 和 `offset` 分页查询。

**接口定义**

```java
/**
 * 获取收藏的消息
 * @param option 查询参数
 * @param callback 结果回调
 */
void getFavorite(GetFavoriteMessageOption option, IGetFavoriteMessageCallback callback);
```

</TabItem>
<TabItem value="ios">

查询收藏列表，按时间倒序排列，支持 `count` 和 `offset` 分页查询。

**接口定义**

```objectivec
/// 获取收藏的消息
/// - Parameters:
///   - option: 查询参数
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)getFavorite:(JGetFavoriteMessageOption *)option
            success:(void (^)(NSArray <JFavoriteMessage *> *messageList, NSString *offset))successBlock
              error:(void (^)(JErrorCode code))errorBlock;
```

</TabItem>
<TabItem value="js">

查询收藏列表，按时间倒序排列，支持 `limit` 和 `offset` 分页查询。

![](./list.png)

**参数说明**

| 名称                    | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|-------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| params                  | Object  | 是     |        | 参数对象                                                      | 1.0.0    |
| message.limit           | Number  | 否     |   20     | 每次查询的条数                           | 1.0.0    |
| message.offset          | String  | 否     |   空    | 默认为空，查询成功后会返回 `offset`，再次获取需传入返回的 `offset` | 1.0.0    |

**成功回调**

| 名称                 | 类型    | 描述                                    | 版本   |
|---------------------|---------|-----------------------------------------|--------|
| result              | Object  |                                        | 1.0.0  |
| result.offset       | String  | 获取更多标识，再次获取收藏消息时需要传入 `offset`| 1.0.0  |
| result.list         | Array  | 收藏列表，`list.lenght` 小于等于 `limit` 时表示数据已取完，`offset` 会返回空 `字符串`          | 1.0.0  |
| result.list[0]      | Array  | 收藏的 [Message](../../../msg/message) 对象          | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js

let params = {
  offset: '',
  limit: 20
};

jim.getFavoriteMessages(params).then((result) => {

  let { offset, list } = result;

  // offset => 分页标识
  
  // list => 收藏消息列表

}, (error) => {
  console.log(error)
});
```
</TabItem>
<TabItem value="flutter">

查询收藏列表，按时间倒序排列，支持 `count` 和 `offset` 分页查询。

**接口定义**

```objectivec
/// 获取收藏的消息
/// - Parameters:
///   - option: 查询参数
Future<Result<FavoriteMessageResult>> getFavoriteMessages(GetFavoriteMessageOption option) async
```

</TabItem>
</Tabs>