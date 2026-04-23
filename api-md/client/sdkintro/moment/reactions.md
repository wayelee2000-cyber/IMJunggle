---
title: Like list
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

Retrieve the list of likes, including likes from a specific circle of friends or a customized interaction type list.

**Interface description**

```java
/**
 * Retrieve the like list
 * @param momentId Moment ID
 * @param callback Result callback
 */
void getReactionList(String momentId, JIMConst.IResultListCallback<MomentReaction> callback);
```

**Code Example**

```java
JIM.getInstance().getMomentManager().getReactionList("momentId", new JIMConst.IResultListCallback<MomentReaction>() {
    @Override
    public void onSuccess(List<MomentReaction> data, boolean isFinish) {
        // Handle success
    }

    @Override
    public void onError(int errorCode) {
        // Handle error
    }
});
```

</TabItem>
<TabItem value="ios">

Retrieve the list of likes, including likes from a specific circle of friends or a customized interaction type list.

**Interface description**

```objectivec
/// Retrieve the like list
/// - Parameters:
///   - momentId: Moment ID
///   - completeBlock: Result callback
- (void)getReactionList:(nonnull NSString *)momentId
               complete:(nullable void (^)(JErrorCode errorCode, NSArray <JMomentReaction *> * _Nullable reactionList))completeBlock;
```

**Code Example**

```objectivec
[JIM.shared.momentManager getReactionList:@"momentId" complete:^(JErrorCode errorCode, NSArray<JMomentReaction *> * _Nullable reactionList) {
    // Handle result
}];
```

</TabItem>
<TabItem value="flutter">

Retrieve the list of likes, including likes from a specific circle of friends or a customized interaction type list.

**Interface description**

```dart
/**
 * Retrieve the like list
 * @param momentId Moment ID
 * @return Like list
 */
Future<Result<List<MomentReaction>>> getMomentReactionList(String momentId) async
```

**Code Example**

```dart
Result<List<MomentReaction>> reactionList = await JuggleIm.instance.getMomentReactionList('momentId');
```

</TabItem>
<TabItem value="reactnative">

Retrieve the list of likes, including likes from a specific circle of friends or a customized interaction type list.

**Interface description**

```typescript
/**
 * Retrieve the like list
 * @param momentId Moment ID
 * @return Promise<MomentReaction[]>
 */
getReactionList(momentId: string): Promise<MomentReaction[]>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const reactionList = await JuggleIMMoment.getReactionList('momentId');
```

</TabItem>
<TabItem value="js">

Retrieve the list of likes, including likes from a specific circle of friends or a customized interaction type list.

**Parameter description**

| Name           | Type   | Required | Default | Description                  | Version |
|----------------|--------|----------|---------|------------------------------|---------|
| params         | Object | Yes      | -       | Parameters for retrieving the like list | 1.9.6   |
| params.momentId | String | Yes      | -       | Moment ID                    | 1.9.6   |

**Callback description**

| Name            | Type  | Description                                                                 | Version |
|-----------------|-------|-----------------------------------------------------------------------------|---------|
| result          | Object| Result of retrieving the like list                                          | 1.9.6   |
| result.reactions| Array | List of interaction types; see the object structure [Reaction](./moment_model.md) | 1.9.6   |

**Code Example**

```js
jim.getReactions({
  momentId: 'momentId',
}).then((result) => {
  console.log('getReactions', result);
});
```
</TabItem>
</Tabs>
