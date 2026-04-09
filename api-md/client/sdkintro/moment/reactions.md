---
title: 点赞列表
hide_title: true
sidebar_position: 32
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


获取点赞列表，获取某条朋友圈的点赞或者自定义的互动类型列表。

**接口说明**

```java
/**
 * 获取点赞列表
 * @param momentId 朋友圈 id
 * @param callback 结果回调
 */
void getReactionList(String momentId, JIMConst.IResultListCallback<MomentReaction> callback);
```

**代码示例**

```java
JIM.getInstance().getMomentManager().getReactionList("momentId", new JIMConst.IResultListCallback<MomentReaction>() {
    @Override
    public void onSuccess(List<MomentReaction> data, boolean isFinish) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">


获取点赞列表，获取某条朋友圈的点赞或者自定义的互动类型列表。

**接口说明**

```objectivec
/// 获取点赞列表
/// - Parameters:
///   - momentId: 朋友圈 id
///   - completeBlock: 结果回调
- (void)getReactionList:(nonnull NSString *)momentId
               complete:(nullable void (^)(JErrorCode errorCode, NSArray <JMomentReaction *> * _Nullable reactionList))completeBlock;
```

**代码示例**

```objectivec
[JIM.shared.momentManager getReactionList:@"momentId" complete:^(JErrorCode errorCode, NSArray<JMomentReaction *> * _Nullable reactionList) {
}];
```

</TabItem>
<TabItem value="flutter">

获取点赞列表，获取某条朋友圈的点赞或者自定义的互动类型列表。

**接口说明**

```dart
/**
 * 获取点赞列表
 * @param momentId 朋友圈 id
 * return 点赞列表
 */
Future<Result<List<MomentReaction>>> getMomentReactionList(String momentId) async
```

**代码示例**

```dart
Result<List<MomentReaction>> reactionList = await JuggleIm.instance.getMomentReactionList('momentId');
```


</TabItem>
<TabItem value="reactnative">

获取点赞列表，获取某条朋友圈的点赞或者自定义的互动类型列表。

**接口说明**

```typescript
/**
 * 获取点赞列表
 * @param momentId 朋友圈 id
 * return Promise<MomentReaction[]>
 */
getReactionList(momentId: string): Promise<MomentReaction[]>
```

**代码示例**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const reactionList = await JuggleIMMoment.getReactionList('momentId');
```

</TabItem>
<TabItem value="js">

获取点赞列表，获取某条朋友圈的点赞或者自定义的互动类型列表。

**参数说明**

| 名称          | 类型    | 必填                          | 默认值      | 描述                                           | 版本     |
|--------------|---------|-------------------------------|------------|------------------------------------------------|----------|
| params        | Object  | 是                            | -   | 获取点赞列表参数  | 1.9.6   |
| params.momentId    | String  | 是                            |  -   | 朋友圈 Id  | 1.9.6   |

**回调说明**

| 名称          | 类型    | 描述                                           | 版本     |
|--------------|---------|------------------------------------------------|----------|
| result        | Object  | 获取点赞列表结果  | 1.9.6   |
| result.reactions    | Array  | 互动类型列表，对象结构请查看 [Reaction](../moment_model) | 1.9.6   |

**代码示例**

```js
jim.getReactions({
  momentId: 'momentId',
}).then((result) => {
  console.log('getReactions', result)
})
```
</TabItem>
</Tabs>