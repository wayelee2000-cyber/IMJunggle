---
title: 添加评论
hide_title: true
sidebar_position: 20
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

添加评论，同时支持回复某个人的评论。

**接口说明**

```java
/**
 * 发布评论
 * @param momentId 评论的朋友圈 id
 * @param parentCommentId 父级评论 id，可以为空
 * @param content 评论内容
 * @param callback 结果回调
 */
void addComment(String momentId, String parentCommentId, String content, JIMConst.IResultCallback<MomentComment> callback);
```

**代码示例**

```java
// "parentCommentId" 可以为空
JIM.getInstance().getMomentManager().addComment("momentId", "parentCommentId", "Good picture!", new JIMConst.IResultCallback<MomentComment>() {
    @Override
    public void onSuccess(MomentComment data) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```


</TabItem>
<TabItem value="ios">

添加评论，同时支持回复某个人的评论。

**接口说明**

```objectivec
/// 发布评论
/// - Parameters:
///   - momentId: 评论的朋友圈 id
///   - parentCommentId: 父级评论 id
///   - content: 评论内容
///   - completeBlock: 结果回调
- (void)addComment:(nonnull NSString *)momentId
   parentCommentId:(nullable NSString *)parentCommentId
           content:(nonnull NSString *)content
          complete:(nullable void (^)(JErrorCode errorCode, JMomentComment * _Nullable comment))completeBlock;
```

**代码示例**

```objectivec
// "parentCommentId" 可以为空
[JIM.shared.momentManager addComment:@"momentId"
                     parentCommentId:@"parentCommentId"
                             content:@"Good picture!"
                            complete:^(JErrorCode errorCode, JMomentComment * _Nullable comment) {
}];
```

</TabItem>
<TabItem value="flutter">

添加评论，同时支持回复某个人的评论。

**接口说明**

```dart
/**
 * 发布评论
 * @param momentId 评论的朋友圈 id
 * @param content 评论内容
 * @param parentCommentId 父级评论 id，可以为空
 * return MomentComment 对象
 */
Future<Result<MomentComment>> addMomentComment(String momentId, String content, [String? parentCommentId]) async
```

**代码示例**

```dart
// "parentCommentId" 可以为空
Result<MomentComment> comment = await JuggleIm.instance.addMomentComment('momentId', 'Good picture!', 'parentCommentId');
```


</TabItem>
<TabItem value="reactnative">

添加评论，同时支持回复某个人的评论。

**接口说明**

```typescript
/**
 * 发布评论
 * @param momentId 评论的朋友圈 id
 * @param content 评论内容
 * @param parentCommentId 父级评论 id，可以为空
 * return Promise<MomentComment> 对象
 */
addComment(momentId: string, content: string, parentCommentId?: string): Promise<MomentComment>
```

**代码示例**

```typescript
// "parentCommentId" 可以为空
import { JuggleIMMoment } from 'juggleim-rnsdk';

const comment = await JuggleIMMoment.addComment('momentId', 'Good picture!', 'parentCommentId');
```


</TabItem>
<TabItem value="js">

添加评论，同时支持回复某个人的评论。

**参数说明**

| 名称          | 类型    | 必填                          | 默认值                               | 描述                                           | 版本     |
|--------------|---------|-------------------------------|-------------------------------------|------------------------------------------------|----------|
| params        | Object  | 是                            | -   | 评论信息  | 1.9.6   |
| params.momentId    | String  | 是                            |  -   | 朋友圈 ID  | 1.9.6   |
| params.parentCommentId    | String  | 否                            |  -   | 回复的评论 ID，回复根评论时为空字符串  | 1.9.6   |
| params.content    | Object  | 是                            |  -   | 评论内容  | 1.9.6   |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.9.6   |
| result.comment | Object | 评论对象，结构请查看 [Comment](../moment_model) | 1.9.6   | 

**代码示例**

```js
// 回复评论
let comment = {
  momentId: 'momentId',
  parentCommentId: '',
  content: {
    text: '这是一条回复根评论'
  }
};
jim.addComment(comment).then((result) => {
  console.log('addComment successfully', result)
});

// 回复子评论
let content = {
  text: '这是一条回复子评论'
};
jim.addComment({
  momentId: 'momentId',
  parentCommentId: 'parentCommentId',
  content
}).then((result) => {
  console.log('addComment successfully', result)
});
```



</TabItem>
</Tabs>