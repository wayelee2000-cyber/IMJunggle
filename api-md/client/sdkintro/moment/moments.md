---
title: 朋友圈列表
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

获取所有好友的朋友圈列表，支持按指定时间前后分页获取。

**GetMomentOption 结构**

| 名称          | 类型    |  描述                                           | 版本     |
|--------------|---------|------------------------------------------------|----------|
| count  | int  | 获取指定数量的朋友圈，单次最多获取 20 条记录 | 1.8.30   |
| direction | JIMConst.PullDirection  | 获取方向，支持按 `startTime` 获取更早的朋友圈或者更（四声）新的朋友圈| 1.8.30   |
| startTime   | long  | 从指定时间点开始获取朋友圈，可以配合 `direction` 使用，传 0 时表示使用当前时间 | 1.8.30   |
| userId   | String  | 获取指定用户发布的朋友圈列表，为空表示获取所有好友的朋友圈列表。只支持 getMomentList 接口；getCachedMomentList 接口不支持该参数| 1.8.44   |

**接口说明**

```java
/**
 * 获取朋友圈列表
 * @param option 获取参数
 * @param callback 结果回调
 */
void getMomentList(GetMomentOption option, JIMConst.IResultListCallback<Moment> callback);
```

**示例代码**
```java
GetMomentOption o = new GetMomentOption();
o.setCount(10);
o.setStartTime(0);
o.setDirection(JIMConst.PullDirection.OLDER);
JIM.getInstance().getMomentManager().getMomentList(o, new JIMConst.IResultListCallback<Moment>() {
    @Override
    public void onSuccess(List<Moment> data, boolean isFinish) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

**获取本地缓存的朋友圈列表**

```java
/**
 * 获取缓存的朋友圈列表（缓存的数据不一定是最新版本，可用于第一时间渲染界面，优化用户体验）
 * @param option 获取参数
 * @return 缓存的朋友圈列表
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


获取所有好友的朋友圈列表，支持按指定时间前后分页获取。

**JGetMomentOption 结构**

| 名称          | 类型    |  描述                                           | 版本     |
|--------------|---------|------------------------------------------------|----------|
| count  | int  | 获取指定数量的朋友圈，单次最多获取 20 条记录 | 1.8.30   |
| direction | JPullDirection  | 获取方向，支持按 `startTime` 获取更早的朋友圈或者更（四声）新的朋友圈| 1.8.30   |
| startTime   | long long | 从指定时间点开始获取朋友圈，可以配合 `direction` 使用，传 0 时表示使用当前时间 | 1.8.30   |
| userId   | NSString  | 获取指定用户发布的朋友圈列表，为空表示获取所有好友的朋友圈列表。只支持 getMomentList 接口；getCachedMomentList 接口不支持该参数| 1.8.44   |

**接口说明**

```objectivec
/// 获取朋友圈列表
/// - Parameters:
///   - option: 获取参数
///   - completeBlock: 结果回调
- (void)getMomentList:(nonnull JGetMomentOption *)option
             complete:(nullable void (^)(JErrorCode errorCode, NSArray <JMoment *> * _Nullable momentList, BOOL isFinish))completeBlock;
```

**示例代码**
```objectivec
JGetMomentOption *o = [JGetMomentOption new];
o.startTime = 0;
o.count = 10;
o.direction = JPullDirectionOlder;
[JIM.shared.momentManager getMomentList:o complete:^(JErrorCode errorCode, NSArray<JMoment *> * _Nullable momentList, BOOL isFinish) {
}];
```

**获取本地缓存的朋友圈列表**

```objectivec
/// 获取缓存的朋友圈列表（缓存的数据不一定是最新版本，可用于第一时间渲染界面，优化用户体验）
/// - Parameter option: 获取参数
- (NSArray <JMoment *> *_Nonnull)getCachedMomentList:(nonnull JGetMomentOption *)option;
```

```objectivec
JGetMomentOption *o = [JGetMomentOption new];
o.startTime = 0;
o.count = 10;
o.direction = JPullDirectionOlder;
NSArray *r = [JIM.shared.momentManager getCachedMomentList:o];
```

</TabItem>
<TabItem value="flutter">

获取所有好友的朋友圈列表，支持按指定时间前后分页获取。

**GetMomentOption 结构**

| 名称          | 类型    | 默认值                               | 描述                                           | 版本     |
|--------------|---------|--------------------------------------|------------------------------------------------|----------|
| count  | int  | 10                                   | 获取指定数量的朋友圈，单次最多获取 20 条记录 | 0.0.66   |
| direction | int  | 1 | 获取方向(0 获取更新的记录，1 获取更早的数据)，支持按 `startTime` 获取更早的朋友圈或者更（四声）新的朋友圈| 0.0.66   |
| startTime   | int  | 0                                    | 从指定时间点开始获取朋友圈，可以配合 `direction` 使用，传 0 时表示使用当前时间 | 0.0.66   |

**接口说明**

```dart
/**
 * 获取朋友圈列表
 * @param o 获取参数
 * return 朋友圈列表
 */
Future<ResultHasMore<List<Moment>>> getMomentList(GetMomentOption o) async
```

**示例代码**
```dart
GetMomentOption o = GetMomentOption();
ResultHasMore<List<Moment>> momentList = await JuggleIm.instance.getMomentList(o);
```

**获取本地缓存的朋友圈列表**

```dart
/**
 * 获取缓存的朋友圈列表（缓存的数据不一定是最新版本，可用于第一时间渲染界面，优化用户体验）
 * @param o 获取参数
 * @return 缓存的朋友圈列表
 */
Future<List<Moment>> getCachedMomentList(GetMomentOption o) async
```

```dart
GetMomentOption o = GetMomentOption();
List<Moment> cachedMomentList = await JuggleIm.instance.getCachedMomentList(o);
```

</TabItem>
<TabItem value="reactnative">

获取所有好友的朋友圈列表，支持按指定时间前后分页获取。

**GetMomentOption 结构**

| 名称          | 类型    | 默认值                               | 描述                                           | 版本     |
|--------------|---------|--------------------------------------|------------------------------------------------|----------|
| count  | number  | 10                                   | 获取指定数量的朋友圈，单次最多获取 20 条记录 | -   |
| direction | number  | 1 | 获取方向(0 获取更新的记录，1 获取更早的数据)，支持按 `startTime` 获取更早的朋友圈或者更（四声）新的朋友圈| -   |
| startTime   | number  | 0                                    | 从指定时间点开始获取朋友圈，可以配合 `direction` 使用，传 0 时表示使用当前时间 | -   |
| userId   | string  |                                 | 获取指定用户发布的朋友圈列表，为空表示获取所有好友的朋友圈列表。只支持 getMomentList 接口；getCachedMomentList 接口不支持该参数 | 0.3.1  |

**接口说明**

```typescript
/**
 * 获取朋友圈列表
 * @param option 获取参数
 * return Promise<{ list: Moment[], isFinished: boolean }>
 */
getMomentList(option: GetMomentOption): Promise<{ list: Moment[], isFinished: boolean }>
```

**示例代码**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const o = {
  count: 10,
  startTime: 0,
  direction: 1,
};
const momentList = await JuggleIMMoment.getMomentList(o);
```

**获取本地缓存的朋友圈列表**

```typescript
/**
 * 获取缓存的朋友圈列表（缓存的数据不一定是最新版本，可用于第一时间渲染界面，优化用户体验）
 * @param option 获取参数
 * @return 缓存的朋友圈列表
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

获取所有好友的朋友圈列表，支持按指定时间前后分页获取。

**参数说明**

| 名称          | 类型    | 必填     | 默认值                               | 描述                                           | 版本     |
|--------------|---------|----------|--------------------------------------|------------------------------------------------|----------|
| option        | Object  | 否       |                                    |  | 1.9.6   |
| option.count  | Number  | 否       | 50                                   | 获取指定数量的朋友圈，单次最多获取 20 条记录 | 1.9.6   |
| option.order  | Number  | 否       | [获取方向](../../enum/web#moment_order) | 获取方向，支持按 `time` 获取更早的朋友圈或者更（四声）新的朋友圈| 1.9.6   |
| option.time   | Number  | 否       | 0                                    | 从指定时间点开始获取朋友圈，可以配合 `order` 使用 | 1.9.6   |
| option.userId   | String  | 否       | -                                    | 获取指定用户发布的朋友圈列表，为空表示获取所有好友的朋友圈列表。 | 1.9.8   |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.9.6   |
| result.moments | Array | 朋友圈数组，单个朋友圈对象结构请查看 [Moment](./moment.md) | 1.9.6   | 
| result.isFinished | Boolean | 标志会话是否获取完成 | 1.9.6   |

**示例代码**
```js
/* 
  假设当前用户有 79 个朋友圈，每页获取 20 条，朋友圈列表按时间倒序排列，实现朋友圈列表分页逻辑如下：
  1、加载第 1 页获取参数： { count: 20, time: 0 }
  2、加载第 2 页获取参数： { count: 20, time: '获取第 1 页朋友圈数组中最小的 momentTime' }
  3、加载第 3 页获取参数： { count: 20, time: '获取第 2 页朋友圈数组中最小的 momentTime' }  
  4、加载第 4 页获取参数： { count: 20, time: '获取第 3 页朋友圈数组中最小的 momentTime' }
  5、结束：isFinished 返回 true，停止加载
*/
jim.getMoments().then((result) => {
  let { moments, isFinished } = result;
  console.log(isFinished, moments); 
})
```

</TabItem>
</Tabs>