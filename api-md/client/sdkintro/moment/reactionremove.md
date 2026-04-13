---
title: delete likes
hide_title: true
sidebar_position: 31
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


Remove likes, including likes from a specific circle of friends or a custom interaction type.

**Interface description**

```java
/**
 * Cancel like
 * @param momentId Moment ID
 * @param key Like type
 * @param callback Result callback
 */
void removeReaction(String momentId, String key, IMessageManager.ISimpleCallback callback);
```

**Code Example**

```java
JIM.getInstance().getMomentManager().removeReaction("momentId", "like", new IMessageManager.ISimpleCallback() {
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


Remove likes, including likes from a specific circle of friends or a custom interaction type.

**Interface description**

```objectivec
/// Cancel like
/// - Parameters:
///   - momentId: Moment ID
///   - key: Like type
///   - completeBlock: Result callback
- (void)removeReaction:(nonnull NSString *)momentId
                   key:(nonnull NSString *)key
              complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**Code Example**

```objectivec
[JIM.shared.momentManager removeReaction:@"momentId" key:@"like" complete:^(JErrorCode errorCode) {
}];
```

</TabItem>
<TabItem value="flutter">

Remove likes, including likes from a specific circle of friends or a custom interaction type.

**Interface description**

```dart
/**
 * Cancel like
 * @param momentId Moment ID
 * @param key Like type
 * @return Result code, 0 indicates success
 */
Future<int> removeMomentReaction(String momentId, String key) async
```

**Code Example**

```dart
int removeReactionResult = await JuggleIm.instance.removeMomentReaction('momentId', 'like');
```

</TabItem>
<TabItem value="reactnative">

Remove likes, including likes from a specific circle of friends or a custom interaction type.

**Interface description**

```typescript
/**
 * Cancel like
 * @param momentId Moment ID
 * @param key Like type
 * @returns Promise<void>
 */
removeReaction(momentId: string, key: string): Promise<void>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.removeReaction('momentId', 'like');
```

</TabItem>
<TabItem value="js">

Remove likes, including likes from a specific circle of friends or a custom interaction type.

**Parameter description**

| Name             | Type   | Required | Default | Description                                | Version |
|------------------|--------|----------|---------|--------------------------------------------|---------|
| params           | Object | Yes      | -       | Parameters for removing a like             | 1.9.6   |
| params.momentId   | String | Yes      | -       | Moment ID                                  | 1.9.6   |
| params.reaction   | Object | Yes      | -       | Interaction type                           | 1.9.6   |
| params.reaction.key | String | Yes    | -       | Interaction type key; see code example for details | 1.9.6   |

**Code Example**

```js
jim.removeReaction({
  momentId: 'momentId',
  reaction: {
    key: 'like',
  },
}).then(() => {
  console.log('removeReaction succeeded');
});
```

</TabItem>
</Tabs>