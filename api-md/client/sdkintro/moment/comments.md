---
title: 评论列表
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

获取朋友圈的评论列表，支持按指定时间前后分页获取。

**GetMomentCommentOption 结构**

| 名称          | 类型    | 描述                                           | 版本     |
|--------------|---------|------------------------------------------------|----------|
| momentId  | String  | 朋友圈 ID | 1.8.30   |
| count  | int  | 获取指定数量的评论，单次最多获取 20 条记录 | 1.8.30   |
| direction  | JIMConst.PullDirection  | 获取方向，支持按 `startTime` 获取更早的评论或者更（四声）新的评论| 1.8.30   | 
| startTime   | long  | 从指定时间点开始获取评论，可以配合 `direction` 使用，传 0 时表示使用当前时间 | 1.8.30   |

**接口说明**

```java
/**
 * 获取评论列表
 * @param option 获取参数
 * @param callback 结果回调
 */
void getCommentList(GetMomentCommentOption option, JIMConst.IResultListCallback<MomentComment> callback);
```

**示例代码**
```java
GetMomentCommentOption o = new GetMomentCommentOption();
o.setCount(20);
o.setDirection(JIMConst.PullDirection.OLDER);
o.setMomentId("momentId");
JIM.getInstance().getMomentManager().getCommentList(o, new JIMConst.IResultListCallback<MomentComment>() {
    @Override
    public void onSuccess(List<MomentComment> data, boolean isFinish) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">

获取朋友圈的评论列表，支持按指定时间前后分页获取。

**JGetMomentCommentOption 结构**

| 名称          | 类型    | 描述                                           | 版本     |
|--------------|---------|------------------------------------------------|----------|
| momentId  | NSString  | 朋友圈 ID | 1.8.30   |
| count  | int  | 获取指定数量的评论，单次最多获取 20 条记录 | 1.8.30   |
| direction  | JPullDirection  | 获取方向，支持按 `startTime` 获取更早的评论或者更（四声）新的评论| 1.8.30   | 
| startTime   | long long  | 从指定时间点开始获取评论，可以配合 `direction` 使用，传 0 时表示使用当前时间 | 1.8.30   |

**接口说明**

```objectivec
/// 获取评论列表
/// - Parameters:
///   - option: 获取参数
///   - completeBlock: 结果回调
- (void)getCommentList:(nonnull JGetMomentCommentOption *)option
              complete:(nullable void (^)(JErrorCode errorCode, NSArray <JMomentComment *> * _Nullable commentList, BOOL isFinish))completeBlock;
```

**示例代码**
```objectivec
JGetMomentCommentOption *o = [[JGetMomentCommentOption alloc] init];
o.momentId = @"momentId";
o.count = 10;
o.direction = JPullDirectionOlder;
[JIM.shared.momentManager getCommentList:o
                                complete:^(JErrorCode errorCode, NSArray<JMomentComment *> * _Nullable commentList, BOOL isFinish) {
}];
```



</TabItem>
<TabItem value="flutter">

获取朋友圈的评论列表，支持按指定时间前后分页获取。

**GetMomentCommentOption 结构**

| 名称          | 类型    | 默认值 | 描述                                           | 版本     |
|--------------|---------| ------| ------------------------------------------------|----------|
| momentId  | String  | '' | 朋友圈 ID | 0.0.66   |
| count  | int  | 10 | 获取指定数量的评论，单次最多获取 20 条记录 | 0.0.66   |
| direction  | int | 1 | 获取方向(0 获取更新的记录，1 获取更早的数据)，支持按 `startTime` 获取更早的朋友圈或者更（四声）新的评论| 0.0.66   | 
| startTime   | int  | 0 | 从指定时间点开始获取评论，可以配合 `direction` 使用，传 0 时表示使用当前时间 | 0.0.66   |

**接口说明**

```dart
/**
 * 获取评论列表
 * @param o 获取参数
 * return 评论列表
 */
Future<ResultHasMore<List<MomentComment>>> getMomentCommentList(GetMomentCommentOption o) async
```

**示例代码**
```dart
GetMomentCommentOption commentOption = GetMomentCommentOption();
commentOption.momentId = 'momentId';
ResultHasMore<List<MomentComment>> commentList = await JuggleIm.instance.getMomentCommentList(commentOption);
```

</TabItem>
<TabItem value="reactnative">

获取朋友圈的评论列表，支持按指定时间前后分页获取。

**GetMomentCommentOption 结构**

| 名称          | 类型    | 默认值 | 描述                                           | 版本     |
|--------------|---------| ------| ------------------------------------------------|----------|
| momentId  | string  | '' | 朋友圈 ID | -   |
| count  | number  | 10 | 获取指定数量的评论，单次最多获取 20 条记录 | -   |
| direction  | number | 1 | 获取方向(0 获取更新的记录，1 获取更早的数据)，支持按 `startTime` 获取更早的朋友圈或者更（四声）新的评论| -   |
| startTime   | number  | 0 | 从指定时间点开始获取评论，可以配合 `direction` 使用，传 0 时表示使用当前时间 | -   |

**接口说明**

```typescript
/**
 * 获取评论列表
 * @param option 获取参数
 * return Promise<{ list: MomentComment[], isFinished: boolean }>
 */
getCommentList(option: GetMomentCommentOption): Promise<{ list: MomentComment[], isFinished: boolean }>
```

**示例代码**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const commentOption = {
  momentId: 'momentId',
};
const commentList = await JuggleIMMoment.getCommentList(commentOption);
```

</TabItem>
<TabItem value="js">

获取朋友圈的评论列表，支持按指定时间前后分页获取。

**参数说明**

| 名称          | 类型    | 必填     | 默认值                               | 描述                                           | 版本     |
|--------------|---------|----------|--------------------------------------|------------------------------------------------|----------|
| option        | Object  | 否       |                                    |  | 1.9.6   |
| option.count  | Number  | 否       | 50                                   | 获取指定数量的评论，单次最多获取 20 条记录 | 1.9.6   |
| option.order  | Number  | 否       | [获取方向](../../enum/web#comment_order) | 获取方向，支持按 `time` 获取更早的评论或者更（四声）新的评论| 1.9.6   | 
| option.time   | Number  | 否       | 0                                    | 从指定时间点开始获取评论，可以配合 `order` 使用 | 1.9.6   |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.9.6   |
| result.comments | Array | 评论数组，单个评论对象结构请查看 [Comment](../moment_model) | 1.9.6   | 
| result.isFinished | Boolean | 标志会话是否获取完成 | 1.9.6   |

**示例代码**
```js
/* 
  假设当前用户有 79 个评论，每页获取 20 条，评论列表按时间倒序排列，实现评论列表分页逻辑如下：  
  1、加载第 1 页获取参数： { count: 20, time: 0 }
  2、加载第 2 页获取参数： { count: 20, time: '获取第 1 页评论数组中最小的 commentTime' }
  3、加载第 3 页获取参数： { count: 20, time: '获取第 2 页评论数组中最小的 commentTime' }  
  4、加载第 4 页获取参数： { count: 20, time: '获取第 3 页评论数组中最小的 commentTime' }
  5、结束：isFinished 返回 true，停止加载
*/
jim.getComments().then((result) => {
  let { comments, isFinished } = result;
  console.log(isFinished, comments);
})
```

</TabItem>
</Tabs>