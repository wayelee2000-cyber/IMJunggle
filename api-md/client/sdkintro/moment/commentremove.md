---
title: Delete comment
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

Delete a comment by its comment ID

**Interface description**

```java
/**
 * Delete comment
 * @param momentId Moment ID
 * @param commentId Comment ID
 * @param callback Result callback
 */
void removeComment(String momentId, String commentId, IMessageManager.ISimpleCallback callback);
```

**Code Example**

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

Delete a comment by its comment ID

**Interface description**

```objectivec
/// Delete comment
/// - Parameters:
///   - commentId: Comment ID
///   - momentId: Moment ID
///   - completeBlock: Result callback
- (void)removeComment:(nonnull NSString *)commentId
             momentId:(nonnull NSString *)momentId
             complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**Code Example**

```objectivec
[JIM.shared.momentManager removeComment:@"commentId" momentId:@"momentId" complete:^(JErrorCode errorCode) {
}];
```

</TabItem>
<TabItem value="flutter">

Delete a comment by its comment ID

**Interface description**

```dart
/**
 * Delete comment
 * @param momentId Moment ID
 * @param commentId Comment ID
 * @return Result code, 0 indicates success
 */
Future<int> removeMomentComment(String momentId, String commentId) async 
```

**Code Example**

```dart
int removeCommentResult = await JuggleIm.instance.removeMomentComment('momentId', 'commentId');
```

</TabItem>
<TabItem value="reactnative">

Delete a comment by its comment ID

**Interface description**

```typescript
/**
 * Delete comment
 * @param momentId Moment ID
 * @param commentId Comment ID
 * @returns Promise<void>
 */
removeComment(momentId: string, commentId: string): Promise<void>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.removeComment('momentId', 'commentId');
```

</TabItem>
<TabItem value="js">

Delete a comment by its comment ID

**Parameter description**

| Name           | Type   | Required | Default | Description           | Version |
|----------------|--------|----------|---------|-----------------------|---------|
| params         | Object | Yes      | -       | Parameters for removing a comment | 1.9.6   |
| params.momentId | String | Yes      | -       | Moment ID             | 1.9.6   |
| params.commentIds | Array  | Yes      | -       | Comment IDs           | 1.9.6   |

**Code Example**

```js
// Delete comments
let params = {
  momentId: 'momentId',
  commentIds: ['commentId1', 'commentId2']
};
jim.removeComment(params).then(() => {
  console.log('removeComment succeeded');
});
```

</TabItem>
</Tabs>