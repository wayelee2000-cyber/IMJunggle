---
title: Comment list
hide_title: true
sidebar_position: 22
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

Retrieve the comment list of Moments, supporting pagination before and after a specified time.

**GetMomentCommentOption structure**

| Name | Type | Description | Version |
|--------------|---------|------------------------------------------------|----------|
| momentId | String | Moment ID | 1.8.30 |
| count | int | Number of comments to retrieve, up to 20 records per request | 1.8.30 |
| direction | JIMConst.PullDirection | Direction for retrieval; supports using `startTime` to fetch earlier or newer comments | 1.8.30 |
| startTime | long | Starting point in time for fetching comments; can be used with `direction`. Passing 0 uses the current time | 1.8.30 |

**Interface description**

```java
/**
 * Retrieve the list of comments
 * @param option Retrieval parameters
 * @param callback Result callback
 */
void getCommentList(GetMomentCommentOption option, JIMConst.IResultListCallback<MomentComment> callback);
```

**Sample Code**
```java
GetMomentCommentOption o = new GetMomentCommentOption();
o.setCount(20);
o.setDirection(JIMConst.PullDirection.OLDER);
o.setMomentId("momentId");
JIM.getInstance().getMomentManager().getCommentList(o, new JIMConst.IResultListCallback<MomentComment>() {
    @Override
    public void onSuccess(List<MomentComment> data, boolean isFinish) {
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

Retrieve the comment list of Moments, supporting pagination before and after a specified time.

**JGetMomentCommentOption structure**

| Name | Type | Description | Version |
|--------------|---------|------------------------------------------------|----------|
| momentId | NSString | Moment ID | 1.8.30 |
| count | int | Number of comments to retrieve, up to 20 records per request | 1.8.30 |
| direction | JPullDirection | Direction for retrieval; supports using `startTime` to fetch earlier or newer comments | 1.8.30 |
| startTime | long long | Starting point in time for fetching comments; can be used with `direction`. Passing 0 uses the current time | 1.8.30 |

**Interface description**

```objectivec
/// Retrieve the list of comments
/// - Parameters:
///   - option: Retrieval parameters
///   - completeBlock: Result callback
- (void)getCommentList:(nonnull JGetMomentCommentOption *)option
              complete:(nullable void (^)(JErrorCode errorCode, NSArray <JMomentComment *> * _Nullable commentList, BOOL isFinish))completeBlock;
```

**Sample Code**
```objectivec
JGetMomentCommentOption *o = [[JGetMomentCommentOption alloc] init];
o.momentId = @"momentId";
o.count = 10;
o.direction = JPullDirectionOlder;
[JIM.shared.momentManager getCommentList:o
                                complete:^(JErrorCode errorCode, NSArray<JMomentComment *> * _Nullable commentList, BOOL isFinish) {
    // Handle result
}];
```

</TabItem>
<TabItem value="flutter">

Retrieve the comment list of Moments, supporting pagination before and after a specified time.

**GetMomentCommentOption structure**

| name | type | default value | description | version |
|--------------|---------| ------| --------------------------------------------------|----------|
| momentId | String | '' | Moment ID | 0.0.66 |
| count | int | 10 | Number of comments to retrieve, up to 20 records per request | 0.0.66 |
| direction | int | 1 | Direction for retrieval (0 for newer records, 1 for earlier records); supports using `startTime` to fetch earlier or newer comments | 0.0.66 |
| startTime | int | 0 | Starting point in time for fetching comments; can be used with `direction`. Passing 0 uses the current time | 0.0.66 |

**Interface description**

```dart
/**
 * Retrieve the list of comments
 * @param o Retrieval parameters
 * @return List of comments
 */
Future<ResultHasMore<List<MomentComment>>> getMomentCommentList(GetMomentCommentOption o) async
```

**Sample Code**
```dart
GetMomentCommentOption commentOption = GetMomentCommentOption();
commentOption.momentId = 'momentId';
ResultHasMore<List<MomentComment>> commentList = await JuggleIm.instance.getMomentCommentList(commentOption);
```

</TabItem>
<TabItem value="reactnative">

Retrieve the comment list of Moments, supporting pagination before and after a specified time.

**GetMomentCommentOption structure**

| name | type | default value | description | version |
|--------------|---------| ------| --------------------------------------------------|----------|
| momentId | string | '' | Moment ID | - |
| count | number | 10 | Number of comments to retrieve, up to 20 records per request | - |
| direction | number | 1 | Direction for retrieval (0 for newer records, 1 for earlier records); supports using `startTime` to fetch earlier or newer comments | - |
| startTime | number | 0 | Starting point in time for fetching comments; can be used with `direction`. Passing 0 uses the current time | - |

**Interface description**

```typescript
/**
 * Retrieve the list of comments
 * @param option Retrieval parameters
 * @return Promise<{ list: MomentComment[], isFinished: boolean }>
 */
getCommentList(option: GetMomentCommentOption): Promise<{ list: MomentComment[], isFinished: boolean }>
```

**Sample Code**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const commentOption = {
  momentId: 'momentId',
};
const commentList = await JuggleIMMoment.getCommentList(commentOption);
```

</TabItem>
<TabItem value="js">

Retrieve the comment list of Moments, supporting pagination before and after a specified time.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------|---------|----------|---------|------------------------------------------------|----------|
| option | Object | No | | Retrieval options | 1.9.6 |
| option.count | Number | No | 50 | Number of comments to retrieve, up to 20 records per request | 1.9.6 |
| option.order | Number | No | [Get direction](../enum/web.md#comment_order) | Direction for retrieval; supports using `time` to fetch earlier or newer comments | 1.9.6 |
| option.time | Number | No | 0 | Starting point in time for fetching comments; can be used with `order` | 1.9.6 |

**Callback description**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| result | Object | Query result | 1.9.6 |
| result.comments | Array | Array of comments; see [Comment](./moment_model.md) for the structure of a single comment object | 1.9.6 |
| result.isFinished | Boolean | Indicates whether all comments have been retrieved | 1.9.6 |

**Sample Code**
```js
/* 
Assuming the current user has 79 comments, with 20 comments retrieved per page. The comments are ordered in reverse chronological order. The pagination logic is as follows:
1. Load page 1 with parameters: { count: 20, time: 0 }
2. Load page 2 with parameters: { count: 20, time: 'Smallest commentTime from page 1 comments' }
3. Load page 3 with parameters: { count: 20, time: 'Smallest commentTime from page 2 comments' }
4. Load page 4 with parameters: { count: 20, time: 'Smallest commentTime from page 3 comments' }
5. End when isFinished returns true and stop loading.
*/
jim.getComments().then((result) => {
  let { comments, isFinished } = result;
  console.log(isFinished, comments);
});
```

</TabItem>
</Tabs>
