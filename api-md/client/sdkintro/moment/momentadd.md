---
title: 添加朋友圈
hide_title: true
sidebar_position: 2
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

添加朋友圈，支持发送文本、文字图片混排、文字视频混排、图片视频混排等多种符合形式。

**接口说明**

```java
/**
 * 发布朋友圈
 * @param content 朋友圈的文本内容
 * @param mediaList 朋友圈的媒体内容列表（图片或者视频）
 * @param callback 结果回调
 */
void addMoment(String content, List<MomentMedia> mediaList, JIMConst.IResultCallback<Moment> callback);
```

**代码示例**

```java
MomentMedia media1 = new MomentMedia();
media1.setType(MomentMedia.MomentMediaType.IMAGE);
media1.setUrl("www.baidu.com");
MomentMedia media2 = new MomentMedia();
media2.setType(MomentMedia.MomentMediaType.VIDEO);
media2.setUrl("www.google.com");
List<MomentMedia> l = new ArrayList<>();
l.add(media1);
l.add(media2);
JIM.getInstance().getMomentManager().addMoment("Beautiful!", l, new JIMConst.IResultCallback<Moment>() {
    @Override
    public void onSuccess(Moment moment) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">

添加朋友圈，支持发送文本、文字图片混排、文字视频混排、图片视频混排等多种符合形式。

**接口说明**

```objectivec
/// 发布朋友圈
/// - Parameters:
///   - content: 朋友圈的文本内容
///   - mediaList: 朋友圈的媒体内容列表（图片或者视频）
///   - completeBlock: 结果回调
- (void)addMoment:(nonnull NSString *)content
        mediaList:(nullable NSArray <JMomentMedia *> *)mediaList
         complete:(nullable void (^)(JErrorCode errorCode, JMoment * _Nullable moment))completeBlock;
```

**代码示例**

```objectivec
NSMutableArray *mediaList = [NSMutableArray array];
JMomentMedia *media1 = [JMomentMedia new];
media1.type = JMomentMediaTypeImage;
media1.url = @"www.baidu.com";
JMomentMedia *media2 = [JMomentMedia new];
media2.type = JMomentMediaTypeVideo;
media2.url = @"www.google.com";
media2.snapshotUrl = @"www.google.com";
media2.width = 100;
media2.height = 100;
media2.duration = 100;
[mediaList addObject:media1];
[mediaList addObject:media2];
[JIM.shared.momentManager addMoment:@"Beautiful!" mediaList:mediaList complete:^(JErrorCode errorCode, JMoment * _Nullable moment) {
}];
```


</TabItem>
<TabItem value="flutter">

添加朋友圈，支持发送文本、文字图片混排、文字视频混排、图片视频混排等多种符合形式。

**接口说明**

```dart
/**
 * 发布朋友圈
 * @param content 朋友圈的文本内容
 * @param mediaList 朋友圈的媒体内容列表（图片或者视频）
 * return Moment 对象
 */
Future<Result<Moment>> addMoment(String content, List<MomentMedia>? mediaList) async
```

**代码示例**

```dart
String content = 'Beautiful!';
MomentMedia m1 = MomentMedia();
m1.url = 'www.baidu.com';
m1.type = 0;
m1.duration = 111;
m1.height = 300;
m1.width = 600;
MomentMedia m2 = MomentMedia();
m2.url = 'www.google.com';
m2.type = 1;
m2.duration = 222;
m2.height = 1080;
m2.width = 2000;
m2.snapshotUrl = 'snapshot.com';
List<MomentMedia> l = [m1, m2];
Result<Moment> result = await JuggleIm.instance.addMoment(content, l);
```

</TabItem>
<TabItem value="reactnative">

添加朋友圈，支持发送文本、文字图片混排、文字视频混排、图片视频混排等多种符合形式。

**接口说明**

```typescript
/**
 * 发布朋友圈
 * @param content 朋友圈的文本内容
 * @param mediaList 朋友圈的媒体内容列表（图片或者视频）
 * return Promise<Moment> 对象
 */
addMoment(content: string, mediaList?: MomentMedia[]): Promise<Moment>
```

**代码示例**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const content = '今天是个好日子';
const mediaList = [
  {
    type: 'image',
    url: 'http://example.com/image.jpg',
    width: 100,
    height: 100
  }
];

const moment = await JuggleIMMoment.addMoment(content, mediaList);
console.log('添加朋友圈成功', moment);
```

</TabItem>
<TabItem value="js">

添加朋友圈，支持发送文本、文字图片混排、文字视频混排、图片视频混排等多种符合形式。

**参数说明**

| 名称          | 类型    | 必填                          | 默认值                               | 描述                                           | 版本     |
|--------------|---------|-------------------------------|-------------------------------------|------------------------------------------------|----------|
| params        | Object  | 是                            | -   | 朋友圈信息  | 1.9.6   |
| params.text    | String  | `medias` 和 `text` 至少二选一 |  -   | 朋友圈文本内容，文本字数 500 字以内  | 1.9.6   |
| params.medias    | Array  | `medias` 和 `text` 至少二选一 |  [] | 朋友圈媒体内容，每个元素为 [Media](../moment_model) 结构  | 1.9.6   |

**回调说明**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| result          | Object  | 查询结果                                       | 1.9.6   |
| result.moment | Array | 朋友圈数组，单个朋友圈对象结构请查看 [Moment](../moment.md) | 1.9.6   | 

**代码示例**

```js
// 发布文本朋友圈
let content = {
  text: '这是一条文本朋友圈'
};
jim.addMoment(content).then((result) => {
  console.log('addMoment successfully', result)
});

// 发布图文组合朋友圈
let content = {
  text: '这是一条图文组合朋友圈',
  medias: [
    {
      type: 'image',
      url: 'https://example.com/image.jpg',
    },
  ],
};
jim.addMoment(content).then((result) => {
  console.log('addMoment successfully', result)
});
```

</TabItem>
</Tabs>