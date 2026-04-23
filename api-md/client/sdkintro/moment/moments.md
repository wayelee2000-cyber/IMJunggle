---
title: Moments list
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

Retrieve the list of all friends' Moments, supporting pagination before and after a specified time.

**GetMomentOption structure**

| Name | Type | Description | Version |
|--------------|---------|------------------------------------------------|----------|
| count | int | Number of friend circles to retrieve, up to 20 records per request | 1.8.30 |
| direction | JIMConst.PullDirection | Direction for retrieval; supports fetching earlier Moments or updating with newer Moments based on `startTime` | 1.8.30 |
| startTime | long | Retrieve Moments starting from the specified time. Can be used with `direction`. Passing 0 uses the current time | 1.8.30 |
| userId | String | Retrieve Moments published by the specified user. If empty, retrieves Moments from all friends. Supported only by `getMomentList`; `getCachedMomentList` does not support this parameter | 1.8.44 |

**Interface description**

```java
/**
 * Retrieve the list of friends' Moments
 * @param option Retrieval parameters
 * @param callback Result callback
 */
void getMomentList(GetMomentOption option, JIMConst.IResultListCallback<Moment> callback);
```

**Sample Code**
```java
GetMomentOption o = new GetMomentOption();
o.setCount(10);
o.setStartTime(0);
o.setDirection(JIMConst.PullDirection.OLDER);
JIM.getInstance().getMomentManager().getMomentList(o, new JIMConst.IResultListCallback<Moment>() {
    @Override
    public void onSuccess(List<Moment> data, boolean isFinish) {
        // Handle success
    }

    @Override
    public void onError(int errorCode) {
        // Handle error
    }
});
```

**Retrieve the locally cached list of friends' Moments**

```java
/**
 * Retrieve the cached list of friends' Moments (cached data may not be the latest but can be used to render the interface immediately and improve user experience)
 * @param option Retrieval parameters
 * @return Cached list of friends' Moments
 */
List<Moment> getCachedMomentList(GetMomentOption option);
```

```java
GetMomentOption o = new GetMomentOption();
o.setCount(10);
o.setStartTime(0);
o.setDirection(JIMConst.PullDirection.OLDER);
List<Moment> momentList = JIM.getInstance().getMomentManager().getCachedMomentList(o);
```

</TabItem>
<TabItem value="ios">

Retrieve the list of all friends' Moments, supporting pagination before and after a specified time.

**JGetMomentOption structure**

| Name | Type | Description | Version |
|--------------|---------|------------------------------------------------|----------|
| count | int | Number of friend circles to retrieve, up to 20 records per request | 1.8.30 |
| direction | JPullDirection | Direction for retrieval; supports fetching earlier Moments or updating with newer Moments based on `startTime` | 1.8.30 |
| startTime | long long | Retrieve Moments starting from the specified time. Can be used with `direction`. Passing 0 uses the current time | 1.8.30 |
| userId | NSString | Retrieve Moments published by the specified user. If empty, retrieves Moments from all friends. Supported only by `getMomentList`; `getCachedMomentList` does not support this parameter | 1.8.44 |

**Interface description**

```objectivec
/// Retrieve the list of friends' Moments
/// - Parameters:
///   - option: Retrieval parameters
///   - completeBlock: Result callback
- (void)getMomentList:(nonnull JGetMomentOption *)option
             complete:(nullable void (^)(JErrorCode errorCode, NSArray <JMoment *> * _Nullable momentList, BOOL isFinish))completeBlock;
```

**Sample Code**
```objectivec
JGetMomentOption *o = [JGetMomentOption new];
o.startTime = 0;
o.count = 10;
o.direction = JPullDirectionOlder;
[JIM.shared.momentManager getMomentList:o complete:^(JErrorCode errorCode, NSArray<JMoment *> * _Nullable momentList, BOOL isFinish) {
    // Handle result
}];
```

**Retrieve the locally cached list of friends' Moments**

```objectivec
/// Retrieve the cached list of friends' Moments (cached data may not be the latest but can be used to render the interface immediately and improve user experience)
/// - Parameter option: Retrieval parameters
- (NSArray <JMoment *> *_Nonnull)getCachedMomentList:(nonnull JGetMomentOption *)option;
```

```objectivec
JGetMomentOption *o = [JGetMomentOption new];
o.startTime = 0;
o.count = 10;
o.direction = JPullDirectionOlder;
NSArray *cachedMoments = [JIM.shared.momentManager getCachedMomentList:o];
```

</TabItem>
<TabItem value="flutter">

Retrieve the list of all friends' Moments, supporting pagination before and after a specified time.

**GetMomentOption structure**

| name | type | default value | description | version |
|--------------|---------|---------------|------------------------------------------------|----------|
| count | int | 10 | Number of friend circles to retrieve, up to 20 records per request | 0.0.66 |
| direction | int | 1 | Retrieval direction (0 for newer records, 1 for earlier records); supports fetching earlier Moments or updating with newer Moments based on `startTime` | 0.0.66 |
| startTime | int | 0 | Retrieve Moments starting from the specified time. Can be used with `direction`. Passing 0 uses the current time | 0.0.66 |

**Interface description**

```dart
/**
 * Retrieve the list of friends' Moments
 * @param o Retrieval parameters
 * @return List of friends' Moments
 */
Future<ResultHasMore<List<Moment>>> getMomentList(GetMomentOption o) async
```

**Sample Code**
```dart
GetMomentOption o = GetMomentOption();
ResultHasMore<List<Moment>> momentList = await JuggleIm.instance.getMomentList(o);
```

**Retrieve the locally cached list of friends' Moments**

```dart
/**
 * Retrieve the cached list of friends' Moments (cached data may not be the latest but can be used to render the interface immediately and improve user experience)
 * @param o Retrieval parameters
 * @return Cached list of friends' Moments
 */
Future<List<Moment>> getCachedMomentList(GetMomentOption o) async
```

```dart
GetMomentOption o = GetMomentOption();
List<Moment> cachedMomentList = await JuggleIm.instance.getCachedMomentList(o);
```

</TabItem>
<TabItem value="reactnative">

Retrieve the list of all friends' Moments, supporting pagination before and after a specified time.

**GetMomentOption structure**

| name | type | default value | description | version |
|--------------|---------|---------------|------------------------------------------------|----------|
| count | number | 10 | Number of friend circles to retrieve, up to 20 records per request | - |
| direction | number | 1 | Retrieval direction (0 for newer records, 1 for earlier records); supports fetching earlier Moments or updating with newer Moments based on `startTime` | - |
| startTime | number | 0 | Retrieve Moments starting from the specified time. Can be used with `direction`. Passing 0 uses the current time | - |
| userId | string | | Retrieve Moments published by the specified user. If empty, retrieves Moments from all friends. Supported only by `getMomentList`; `getCachedMomentList` does not support this parameter | 0.3.1 |

**Interface description**

```typescript
/**
 * Retrieve the list of friends' Moments
 * @param option Retrieval parameters
 * @return Promise resolving to an object containing the list of Moments and a completion flag
 */
getMomentList(option: GetMomentOption): Promise<{ list: Moment[], isFinished: boolean }>
```

**Sample Code**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const o = {
  count: 10,
  startTime: 0,
  direction: 1,
};
const momentList = await JuggleIMMoment.getMomentList(o);
```

**Retrieve the locally cached list of friends' Moments**

```typescript
/**
 * Retrieve the cached list of friends' Moments (cached data may not be the latest but can be used to render the interface immediately and improve user experience)
 * @param option Retrieval parameters
 * @return Cached list of friends' Moments
 */
getCachedMomentList(option: GetMomentOption): Promise<Moment[]>
```

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const o = {
  count: 10,
  startTime: 0,
  direction: 1,
};
const cachedMomentList = await JuggleIMMoment.getCachedMomentList(o);
```

</TabItem>
<TabItem value="js">

Retrieve the list of all friends' Moments, supporting pagination before and after a specified time.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|---------|------------------------------------------------|----------|
| option | Object | No | | | 1.9.6 |
| option.count | Number | No | 50 | Number of friend circles to retrieve, up to 20 records per request | 1.9.6 |
| option.order | Number | No | [Get direction](../enum/web.md#moment_order) | Retrieval direction; supports fetching earlier Moments or updating with newer Moments based on `time` | 1.9.6 |
| option.time | Number | No | 0 | Retrieve Moments starting from the specified time. Can be used with `order` | 1.9.6 |
| option.userId | String | No | - | Retrieve Moments published by the specified user. If empty, retrieves Moments from all friends. | 1.9.8 |

**Callback description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.9.6 |
| result.moments | Array | Array of Moments. See [Moment](./moment_model.md) for the structure of a single Moment object | 1.9.6 |
| result.isFinished | Boolean | Indicates whether the retrieval is complete | 1.9.6 |

**Sample Code**
```js
/* 
Assuming the current user has 79 friend circles, and each page retrieves 20 items. The friend circle list is ordered in reverse chronological order. The pagination logic is as follows:
1. Load page 1 with parameters: { count: 20, time: 0 }
2. Load page 2 with parameters: { count: 20, time: 'Smallest momentTime from page 1's Moments array' }
3. Load page 3 with parameters: { count: 20, time: 'Smallest momentTime from page 2's Moments array' }
4. Load page 4 with parameters: { count: 20, time: 'Smallest momentTime from page 3's Moments array' }
5. End when isFinished returns true and stop loading.
*/
jim.getMoments().then((result) => {
  let { moments, isFinished } = result;
  console.log(isFinished, moments); 
});
```

</TabItem>
</Tabs>
