---
title: add likes
hide_title: true
sidebar_position: 30
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

Add likes, such as liking a specific circle of friends or customizing interaction types.

**Interface description**

```java
/**
 * Add likes
 * @param momentId Moment ID
 * @param key Like type
 * @param callback Result callback
 */
void addReaction(String momentId, String key, IMessageManager.ISimpleCallback callback);
```

**Code Example**

```java
JIM.getInstance().getMomentManager().addReaction("momentId", "like", new IMessageManager.ISimpleCallback() {
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

Add likes, such as liking a specific circle of friends or customizing interaction types.

**Interface description**

```objectivec
/// Add likes
/// - Parameters:
///   - momentId: Moment ID
///   - key: Like type
///   - completeBlock: Result callback
- (void)addReaction:(nonnull NSString *)momentId
                key:(nonnull NSString *)key
           complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**Code Example**

```objectivec
[JIM.shared.momentManager addReaction:@"momentId" key:@"like" complete:^(JErrorCode errorCode) {
}];
```

</TabItem>
<TabItem value="flutter">

Add likes, such as liking a specific circle of friends or customizing interaction types.

**Interface description**

```dart
/**
 * Add likes
 * @param momentId Moment ID
 * @param key Like type
 * @return Result code, 0 indicates success
 */
Future<int> addMomentReaction(String momentId, String key) async
```

**Code Example**

```dart
int addReactionResult = await JuggleIm.instance.addMomentReaction('momentId', 'like');
```

</TabItem>
<TabItem value="reactnative">

Add likes, such as liking a specific circle of friends or customizing interaction types.

**Interface description**

```typescript
/**
 * Add likes
 * @param momentId Moment ID
 * @param key Like type
 * @returns Promise<void>
 */
addReaction(momentId: string, key: string): Promise<void>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.addReaction('momentId', 'like');
```

</TabItem>
<TabItem value="js">

Add likes, such as liking a specific circle of friends or customizing interaction types.

**Parameter description**

| Name               | Type   | Required | Default | Description                                  | Version |
|--------------------|--------|----------|---------|----------------------------------------------|---------|
| params             | Object | Yes      | -       | Parameters for adding a like                  | 1.9.6   |
| params.momentId     | String | Yes      | -       | Moment ID                                     | 1.9.6   |
| params.reaction     | Object | Yes      | -       | Interaction type                              | 1.9.6   |
| params.reaction.key | String | Yes      | -       | Interaction type key (see code example)      | 1.9.6   |
| params.reaction.value | String | Yes    | -       | Interaction type value (see code example)    | 1.9.6   |

**Code Example**

```js
jim.addReaction({
  momentId: 'momentId',
  reaction: {
    key: 'like',
    value: 'like',
  },
}).then(() => {
  console.log('addReaction successfully');
});
```
</TabItem>
</Tabs>