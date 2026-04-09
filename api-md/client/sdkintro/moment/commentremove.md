---
title: 删除评论
hide_title: true
sidebar_position: 21
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

根据评论 Id 删除评论

**接口说明**

```java
/**
 * 删除评论
 * @param momentId 朋友圈 id
 * @param commentId 评论 id
 * @param callback 结果回调
 */
void removeComment(String momentId, String commentId, IMessageManager.ISimpleCallback callback);
```

**代码示例**

```java
JIM.getInstance().getMomentManager().removeComment("momentId", "commentId", new IMessageManager.ISimpleCallback() {
    @Override
    public void onSuccess() {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">

根据评论 Id 删除评论

**接口说明**

```objectivec
/// 删除评论
/// - Parameters:
///   - commentId: 评论 id
///   - momentId: 朋友圈 id
///   - completeBlock: 结果回调
- (void)removeComment:(nonnull NSString *)commentId
             momentId:(nonnull NSString *)momentId
             complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**代码示例**

```objectivec
[JIM.shared.momentManager removeComment:@"commentId" momentId:@"momentId" complete:^(JErrorCode errorCode) {
}];
```


</TabItem>
<TabItem value="flutter">

根据评论 Id 删除评论

**接口说明**

```dart
/**
 * 删除评论
 * @param momentId 朋友圈 id
 * @param commentId 评论 id
 * return 结果码，0 表示成功
 */
Future<int> removeMomentComment(String momentId, String commentId) async 
```

**代码示例**

```dart
int removeCommentResult = await JuggleIm.instance.removeMomentComment('momentId', 'commentId');
```


</TabItem>
<TabItem value="reactnative">

根据评论 Id 删除评论

**接口说明**

```typescript
/**
 * 删除评论
 * @param momentId 朋友圈 id
 * @param commentId 评论 id
 * return Promise<void>
 */
removeComment(momentId: string, commentId: string): Promise<void>
```

**代码示例**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.removeComment('momentId', 'commentId');
```


</TabItem>
<TabItem value="js">

根据评论 Id 删除评论

**参数说明**

| 名称          | 类型    | 必填                          | 默认值      | 描述                                           | 版本     |
|--------------|---------|-------------------------------|------------|------------------------------------------------|----------|
| params        | Object  | 是                            | -   | 删除评论参数  | 1.9.6   |
| params.momentId    | String  | 是                            |  -   | 朋友圈 Id  | 1.9.6   |
| params.commentIds    | Array  | 是                            |  -   | 评论 Id  | 1.9.6   |

**代码示例**

```js
// 删除评论
let params = {
  momentId: 'momentId',
  commentIds: ['commentId1', 'commentId2']
};
jim.removeComment(params).then(() => {
  console.log('removeComment successfully');
});
```

</TabItem>
</Tabs>