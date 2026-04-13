---
title: Delete Moments
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
]
}>
<TabItem value="android">

Delete Moments.

**Interface Description**

```java
/**
 * Delete Moments
 * @param momentId Moment ID
 * @param callback Result callback
 */
void removeMoment(String momentId, IMessageManager.ISimpleCallback callback);
```

**Code Example**

```java
JIM.getInstance().getMomentManager().removeMoment("momentId", new IMessageManager.ISimpleCallback() {
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

Delete Moments.

**Interface Description**

```objectivec
/// Delete Moments
/// - Parameters:
///   - momentId: Moment ID
///   - completeBlock: Result callback
- (void)removeMoment:(nonnull NSString *)momentId
            complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**Code Example**

```objectivec
[JIM.shared.momentManager removeMoment:@"momentId" complete:^(JErrorCode errorCode) {
}];
```

</TabItem>
<TabItem value="flutter">

Delete Moments.

**Interface Description**

```dart
/**
 * Delete Moments
 * @param momentId Moment ID
 * @return Error code, 0 indicates success
 */
Future<int> removeMoment(String momentId) async
```

**Code Example**

```dart
int removeResult = await JuggleIm.instance.removeMoment('momentId');
```

</TabItem>
<TabItem value="reactnative">

Delete Moments.

**Interface Description**

```typescript
/**
 * Delete Moments
 * @param momentId Moment ID
 * @returns Promise<void>
 */
removeMoment(momentId: string): Promise<void>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.removeMoment('momentId');
```

</TabItem>
<TabItem value="js">

Delete Moments with support for batch deletion.

**Parameter Description**

| Name          | Type   | Required | Default | Description                         | Version |
|---------------|--------|----------|---------|-----------------------------------|---------|
| params        | Object | Yes      | -       | Moment information                | 1.9.6   |
| params.momentIds | Array  | Yes      | -       | Array of moment IDs to be deleted | 1.9.6   |

**Code Example**

```js
let params = {
  momentIds: ['momentId'],
};
jim.removeMoment(params).then(() => {
  console.log('removeMoment succeeded');
});
```

</TabItem>
</Tabs>