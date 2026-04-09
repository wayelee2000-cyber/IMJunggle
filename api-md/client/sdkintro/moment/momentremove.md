---
title: 删除朋友圈
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

删除朋友圈。

**接口说明**

```java
/**
 * 删除朋友圈
 * @param momentId 朋友圈 id
 * @param callback 结果回调
 */
void removeMoment(String momentId, IMessageManager.ISimpleCallback callback);
```

**代码示例**

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

删除朋友圈。

**接口说明**

```objectivec
/// 删除朋友圈
/// - Parameters:
///   - momentId: 朋友圈 id
///   - completeBlock: 结果回调
- (void)removeMoment:(nonnull NSString *)momentId
            complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**代码示例**

```objectivec
[JIM.shared.momentManager removeMoment:@"momentId" complete:^(JErrorCode errorCode) {
}];
```


</TabItem>
<TabItem value="flutter">

删除朋友圈。

**接口说明**

```dart
/**
 * 删除朋友圈
 * @param momentId 朋友圈 id
 * return 错误码，0 表示成功
 */
Future<int> removeMoment(String momentId) async
```

**代码示例**

```dart
int removeResult = await JuggleIm.instance.removeMoment('momentId');
```

</TabItem>
<TabItem value="reactnative">

删除朋友圈。

**接口说明**

```typescript
/**
 * 删除朋友圈
 * @param momentId 朋友圈 id
 * return Promise<void>
 */
removeMoment(momentId: string): Promise<void>
```

**代码示例**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.removeMoment('momentId');
```

</TabItem>
<TabItem value="js">

删除朋友圈，支持批量删除。

**参数说明**

| 名称          | 类型    | 必填                          | 默认值                               | 描述                                           | 版本     |
|--------------|---------|-------------------------------|-------------------------------------|------------------------------------------------|----------|
| params        | Object  | 是                           | -   | 朋友圈信息  | 1.9.6   |
| params.momentIds    | Array  | 是                     |  -   | 要删除的朋友圈 ID 数组  | 1.9.6   | 

**代码示例**

```js
let params = {
  momentIds: ['momentId'],
};
jim.removeMoment(params).then(() => {
  console.log('removeMoment successfully')
});
```

</TabItem>
</Tabs>