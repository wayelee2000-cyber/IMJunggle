---
title: Add Moments
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

Adding a Moment supports sending text, mixed text and images, mixed text and videos, mixed images and videos, and more.

**Interface Description**

```java
/**
 * Post to Moments
 * @param content Text content of the Moment
 * @param mediaList List of media content (images or videos) in the Moment
 * @param callback Result callback
 */
void addMoment(String content, List<MomentMedia> mediaList, JIMConst.IResultCallback<Moment> callback);
```

**Code Example**

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

Adding a Moment supports sending text, mixed text and images, mixed text and videos, mixed images and videos, and more.

**Interface Description**

```objectivec
/// Publish to Moments
/// - Parameters:
///   - content: Text content of the Moment
///   - mediaList: List of media content (images or videos) in the Moment
///   - completeBlock: Result callback
- (void)addMoment:(nonnull NSString *)content
        mediaList:(nullable NSArray <JMomentMedia *> *)mediaList
         complete:(nullable void (^)(JErrorCode errorCode, JMoment * _Nullable moment))completeBlock;
```

**Code Example**

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

Adding a Moment supports sending text, mixed text and images, mixed text and videos, mixed images and videos, and more.

**Interface Description**

```dart
/**
 * Post to Moments
 * @param content Text content of the Moment
 * @param mediaList List of media content (images or videos) in the Moment
 * @return Moment object
 */
Future<Result<Moment>> addMoment(String content, List<MomentMedia>? mediaList) async
```

**Code Example**

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

Adding a Moment supports sending text, mixed text and images, mixed text and videos, mixed images and videos, and more.

**Interface Description**

```typescript
/**
 * Post to Moments
 * @param content Text content of the Moment
 * @param mediaList List of media content (images or videos) in the Moment
 * @return Promise<Moment> object
 */
addMoment(content: string, mediaList?: MomentMedia[]): Promise<Moment>
```

**Code Example**

```typescript
import { JuggleIMMoment } from 'juggleim-rnsdk';

const content = 'Today is a good day';
const mediaList = [
  {
    type: 'image',
    url: 'http://example.com/image.jpg',
    width: 100,
    height: 100
  }
];

const moment = await JuggleIMMoment.addMoment(content, mediaList);
console.log('Moment added successfully', moment);
```

</TabItem>
<TabItem value="js">

Adding a Moment supports sending text, mixed text and images, mixed text and videos, mixed images and videos, and more.

**Parameter Description**

| Name         | Type   | Required                                | Default | Description                                                      | Version |
|--------------|--------|---------------------------------------|---------|------------------------------------------------------------------|---------|
| params       | Object | Yes                                   | -       | Moment information                                               | 1.9.6   |
| params.text  | String | At least one of `medias` or `text` is required | -       | Text content of the Moment, limited to 500 characters           | 1.9.6   |
| params.medias| Array  | At least one of `medias` or `text` is required | []      | Media content of the Moment; each element follows the [Media](./moment_model.md) structure | 1.9.6   |

**Callback Description**

| Properties    | Type   | Description                                                                 | Version |
|---------------|--------|-----------------------------------------------------------------------------|---------|
| result        | Object | Query result                                                                | 1.9.6   |
| result.moment | Array  | Array of Moments; see [Moment](./moment_model.md) for the structure of a single Moment object | 1.9.6   |

**Code Example**

```js
// Post text to Moments
let content = {
  text: 'This is a text-only Moment'
};
jim.addMoment(content).then((result) => {
  console.log('addMoment succeeded', result);
});

// Post a combination of images and text to Moments
let content = {
  text: 'This is a Moment combining images and text',
  medias: [
    {
      type: 'image',
      url: 'https://example.com/image.jpg',
    },
  ],
};
jim.addMoment(content).then((result) => {
  console.log('addMoment succeeded', result);
});
```

</TabItem>
</Tabs>
