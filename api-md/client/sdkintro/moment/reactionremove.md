---
title: 删除点赞
hide_title: true
sidebar_position: 31
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


删除点赞，删除某条朋友圈的点赞或者自定义的互动类型。

**接口说明**

```java
/**
 * 取消点赞
 * @param momentId 朋友圈 id
 * @param key 点赞类型
 * @param callback 结果回调
 */
void removeReaction(String momentId, String key, IMessageManager.ISimpleCallback callback);
```

**代码示例**

```java
JIM.getInstance().getMomentManager().removeReaction("momentId", "like", new IMessageManager.ISimpleCallback() {
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


删除点赞，删除某条朋友圈的点赞或者自定义的互动类型。

**接口说明**

```objectivec
/// 取消点赞
/// - Parameters:
///   - momentId: 朋友圈 id
///   - key: 点赞类型
///   - completeBlock: 结果回调
- (void)removeReaction:(nonnull NSString *)momentId
                   key:(nonnull NSString *)key
              complete:(nullable void (^)(JErrorCode errorCode))completeBlock;
```

**代码示例**

```objectivec
[JIM.shared.momentManager removeReaction:@"momentId" key:@"like" complete:^(JErrorCode errorCode) {
}];
```

</TabItem>
<TabItem value="flutter">

删除点赞，删除某条朋友圈的点赞或者自定义的互动类型。

**接口说明**

```dart
/**
 * 取消点赞
 * @param momentId 朋友圈 id
 * @param key 点赞类型
 * return 结果码，0 表示成功
 */
Future<int> removeMomentReaction(String momentId, String key) async
```

**代码示例**

```dart
int removeReactionResult = await JuggleIm.instance.removeMomentReaction('momentId', 'like');
```

</TabItem>
<TabItem value="reactnative">

删除点赞，删除某条朋友圈的点赞或者自定义的互动类型。

**接口说明**

```typescript
/**
 * 取消点赞
 * @param momentId 朋友圈 id
 * @param key 点赞类型
 * return Promise<void>
 */
removeReaction(momentId: string, key: string): Promise<void>
```

**代码示例**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

await JuggleIMMoment.removeReaction('momentId', 'like');
```

</TabItem>
<TabItem value="js">

删除点赞，删除某条朋友圈的点赞或者自定义的互动类型。

**参数说明**

| 名称          | 类型    | 必填                          | 默认值      | 描述                                           | 版本     |
|--------------|---------|-------------------------------|------------|------------------------------------------------|----------|
| params        | Object  | 是                            | -   | 删除点赞参数  | 1.9.6   |
| params.momentId    | String  | 是                            |  -   | 朋友圈 Id  | 1.9.6   |
| params.reaction    | Object  | 是                            |  -   | 互动类型 | 1.9.6   |
| params.reaction.key    | String  | 是                            |  -   | 互动类型 key, 详见代码示例 | 1.9.6   |  

**代码示例**

```js
jim.removeReaction({
  momentId: 'momentId',
  reaction: {
    key: 'like',
  },
}).then(() => {
  console.log('removeReaction successfully');
})
```

</TabItem>
</Tabs>
