---
title: add comment
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

Add a comment or reply to an existing comment.

**Interface description**

```java
/**
 * Post a comment
 * @param momentId The ID of the moment to comment on
 * @param parentCommentId The ID of the parent comment, can be empty
 * @param content The content of the comment
 * @param callback Result callback
 */
void addComment(String momentId, String parentCommentId, String content, JIMConst.IResultCallback<MomentComment> callback);
```

**Code Example**

```java
// "parentCommentId" can be empty
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

Add a comment or reply to an existing comment.

**Interface description**

```objectivec
/// Post a comment
/// - Parameters:
///   - momentId: The ID of the moment to comment on
///   - parentCommentId: The ID of the parent comment
///   - content: The content of the comment
///   - completeBlock: Result callback
- (void)addComment:(nonnull NSString *)momentId
   parentCommentId:(nullable NSString *)parentCommentId
           content:(nonnull NSString *)content
          complete:(nullable void (^)(JErrorCode errorCode, JMomentComment * _Nullable comment))completeBlock;
```

**Code Example**

```objectivec
// "parentCommentId" can be empty
[JIM.shared.momentManager addComment:@"momentId"
                     parentCommentId:@"parentCommentId"
                             content:@"Good picture!"
                            complete:^(JErrorCode errorCode, JMomentComment * _Nullable comment) {
}];
```

</TabItem>
<TabItem value="flutter">

Add a comment or reply to an existing comment.

**Interface description**

```dart
/**
 * Post a comment
 * @param momentId The ID of the moment to comment on
 * @param content The content of the comment
 * @param parentCommentId The ID of the parent comment, can be empty
 * @return MomentComment object
 */
Future<Result<MomentComment>> addMomentComment(String momentId, String content, [String? parentCommentId]) async
```

**Code Example**

```dart
// "parentCommentId" can be empty
Result<MomentComment> comment = await JuggleIm.instance.addMomentComment('momentId', 'Good picture!', 'parentCommentId');
```


</TabItem>
<TabItem value="reactnative">

Add a comment or reply to an existing comment.

**Interface description**

```typescript
/**
 * Post a comment
 * @param momentId The ID of the moment to comment on
 * @param content The content of the comment
 * @param parentCommentId The ID of the parent comment, can be empty
 * @return Promise<MomentComment> object
 */
addComment(momentId: string, content: string, parentCommentId?: string): Promise<MomentComment>
```

**Code Example**

```typescript
// "parentCommentId" can be empty
import { JuggleIMMoment } from 'juggleim-rnsdk';

const comment = await JuggleIMMoment.addComment('momentId', 'Good picture!', 'parentCommentId');
```


</TabItem>
<TabItem value="js">

Add a comment or reply to an existing comment.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|---------|------------------------------------------------|----------|
| params | Object | Yes | - | Comment information | 1.9.6 |
| params.momentId | String | Yes | - | Moment ID | 1.9.6 |
| params.parentCommentId | String | No | - | The ID of the comment being replied to; empty string when replying to the root comment | 1.9.6 |
| params.content | Object | Yes | - | Comment content | 1.9.6 |

**Callback description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.9.6 |
| result.comment | Object | Comment object; see [Comment](./moment_model.md) for structure | 1.9.6 |

**Code Example**

```js
// Reply to root comment
let comment = {
  momentId: 'momentId',
  parentCommentId: '',
  content: {
    text: 'This is a reply to the root comment'
  }
};
jim.addComment(comment).then((result) => {
  console.log('addComment succeeded', result);
});

// Reply to a sub-comment
let content = {
  text: 'This is a reply to a sub-comment'
};
jim.addComment({
  momentId: 'momentId',
  parentCommentId: 'parentCommentId',
  content
}).then((result) => {
  console.log('addComment succeeded', result);
});
```



</TabItem>
</Tabs>
