---
title: Get Moments
hide_title: true
sidebar_position: 4
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

Retrieve information about a single circle of friends

**Interface description**

```java
/**
 * Retrieve details of a Moment
 * @param momentId Moment ID
 * @param callback result callback
 */
void getMoment(String momentId, JIMConst.IResultCallback<Moment> callback);
```

**Code Example**

```java
JIM.getInstance().getMomentManager().getMoment("momentId", new JIMConst.IResultCallback<Moment>() {
    @Override
    public void onSuccess(Moment data) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">

Retrieve information about a single circle of friends

**Interface description**

```objectivec
/// Retrieve details of a Moment
/// - Parameters:
///   - momentId: Moment ID
///   - completeBlock: result callback
- (void)getMoment:(nonnull NSString *)momentId
         complete:(nullable void (^)(JErrorCode errorCode, JMoment * _Nullable moment))completeBlock;
```

**Code Example**

```objectivec
[JIM.shared.momentManager getMoment:@"momentId" complete:^(JErrorCode errorCode, JMoment * _Nullable moment) {
}];
```

</TabItem>
<TabItem value="flutter">

Retrieve information about a single circle of friends

**Interface description**

```dart
/**
 * Retrieve details of a Moment
 * @param momentId Moment ID
 * @return Moment object
 */
Future<Result<Moment>> getMoment(String momentId) async
```

**Code Example**

```dart
Result<Moment> moment = await JuggleIm.instance.getMoment('momentId');
```

</TabItem>
<TabItem value="reactnative">

Retrieve information about a single circle of friends

**Interface description**

```typescript
/**
 * Retrieve details of a Moment
 * @param momentId Moment ID
 * @return Promise<Moment> object
 */
getMoment(momentId: string): Promise<Moment>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const moment = await JuggleIMMoment.getMoment('momentId');
```

</TabItem>
<TabItem value="js">

Retrieve information about a single circle of friends

**Parameter description**

| Name           | Type   | Required | Default | Description           | Version |
|----------------|--------|----------|---------|-----------------------|---------|
| params         | Object | Yes      | -       | Moment information    | 1.9.6   |
| params.momentId | String | Yes      | -       | Moment ID             | 1.9.6   |

**Callback description**

| Properties     | Type   | Description                                              | Version |
|----------------|--------|----------------------------------------------------------|---------|
| result         | Object | Query result                                             | 1.9.6   |
| result.moment  | Object | Moment object; see the [Moment](../moment.md) structure | 1.9.6   |

**Code Example**

```js
// Retrieve information about a single circle of friends
let momentId = '';
jim.getMoment({ momentId }).then((result) => {
  console.log('getMoment succeeded', result);
});
```

</TabItem>
</Tabs>