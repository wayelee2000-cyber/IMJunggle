---
title: 获取朋友圈
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

获取单个朋友圈信息

**接口说明**

```java
/**
 * 获取朋友圈详情
 * @param momentId 朋友圈 id
 * @param callback 结果回调
 */
void getMoment(String momentId, JIMConst.IResultCallback<Moment> callback);
```

**代码示例**

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

获取单个朋友圈信息

**接口说明**

```objectivec
/// 获取朋友圈详情
/// - Parameters:
///   - momentId: 朋友圈 id
///   - completeBlock: 结果回调
- (void)getMoment:(nonnull NSString *)momentId
         complete:(nullable void (^)(JErrorCode errorCode, JMoment * _Nullable moment))completeBlock;
```

**代码示例**

```objectivec
[JIM.shared.momentManager getMoment:@"momentId" complete:^(JErrorCode errorCode, JMoment * _Nullable moment) {
}];
```

</TabItem>
<TabItem value="flutter">

获取单个朋友圈信息

**接口说明**

```dart
/**
 * 获取朋友圈详情
 * @param momentId 朋友圈 id
 * return Moment 对象
 */
Future<Result<Moment>> getMoment(String momentId) async
```

**代码示例**

```dart
Result<Moment> moment = await JuggleIm.instance.getMoment('momentId');
```

</TabItem>
<TabItem value="reactnative">

获取单个朋友圈信息

**接口说明**

```typescript
/**
 * 获取朋友圈详情
 * @param momentId 朋友圈 id
 * return Promise<Moment> 对象
 */
getMoment(momentId: string): Promise<Moment>
```

**代码示例**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const moment = await JuggleIMMoment.getMoment('momentId');
```

</TabItem>
<TabItem value="js">

获取单个朋友圈信息

**参数说明**

| 名称          | 类型    | 必填                          | 默认值                               | 描述                                           | 版本     |
|--------------|---------|-------------------------------|-------------------------------------|------------------------------------------------|----------|
| params        | Object  | 是                            | -   | 朋友圈信息  | 1.9.6   |
| params.momentId    | String  | 是                            |  -   | 朋友圈 ID  | 1.9.6   |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.9.6   |
| result.moment | Object | 朋友圈对象，结构请查看 [Moment](../moment.md) | 1.9.6   | 

**代码示例**

```js
// 获取单个朋友圈信息
let momentId = '';
jim.getMoment({ momentId }).then((result) => {
  console.log('getMoment successfully', result)
});
```

</TabItem>
</Tabs>