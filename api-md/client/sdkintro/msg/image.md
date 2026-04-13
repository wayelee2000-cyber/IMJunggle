---
title: 图片消息
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
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

图片消息（ImageMessage）是 SDK 内置的消息类型，对应的 contentType 为 @"jg:img"。

| 属性名             | 类型     | 说明                     | 版本  |
| ------------------ | -------- | ------------------------ | ----- |
| localPath          | String   | 图片的本地路径           | 1.0.0 |
| url                | String   | 图片的远端地址           | 1.0.0 |
| thumbnailLocalPath  | String   | 缩略图的本地路径         | 1.0.0 |
| thumbnailUrl       | String   | 缩略图的远端地址         | 1.0.0 |
| height             | int      | 图片高度                 | 1.0.0 |
| width              | int      | 图片宽度                 | 1.0.0 |
| size               | long     | 图片大小，单位为 `Byte`  | 1.0.0 |
| extra              | String   | 扩展字段                 | 1.0.0 |

</TabItem>
<TabItem value="ios">

图片消息（JImageMessage）是 SDK 内置的消息类型，对应的 contentType 为 @"jg:img"。

| 属性名             | 类型       | 说明                     | 版本  |
| ------------------ | ---------- | ------------------------ | ----- |
| localPath          | NSString   | 图片的本地路径           | 1.0.0 |
| url                | NSString   | 图片的远端地址           | 1.0.0 |
| thumbnailLocalPath  | NSString   | 缩略图的本地路径         | 1.0.0 |
| thumbnailUrl       | NSString   | 缩略图的远端地址         | 1.0.0 |
| height             | int        | 图片高度                 | 1.0.0 |
| width              | int        | 图片宽度                 | 1.0.0 |
| size               | long long  | 图片大小，单位为 `Byte`  | 1.0.0 |
| extra              | NSString   | 扩展字段                 | 1.0.0 |

</TabItem>
<TabItem value="js">

图片消息是 SDK 内置的消息类型，枚举对应 _[MessageType.IMAGE](../../enum/web#message)_。

| 属性名    | 类型    | 说明                                                                 | 版本  |
|-----------|---------|----------------------------------------------------------------------|-------|
| url       | String  | 图片消息的原图地址                                                   | 1.0.0 |
| thumbnail | String  | 图片消息的缩略图地址。UI 通过高宽属性展示占位图，优先加载缩略图，避免图片加载后跳动 | 1.0.0 |
| height    | Number  | 图片高度                                                           | 1.0.0 |
| width     | Number  | 图片宽度                                                           | 1.0.0 |
| size      | Number  | 图片消息原图大小，用于查看或下载时显示进度条，单位为 `KB`           | 1.0.0 |
| extra     | String  | 消息附加内容，支持 JSON 字符串，设置后不可修改                      | 1.0.0 |

```js
let imageMsg = {
  url: "https://example.com/avatar.png",
  thumbnail: "https://example.com/avatar_th.png",
  height: 640,
  width: 480,
  size: 100,
  extra: '{"Priority":"P0"}'
}

let message = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId1',
  name: MessageType.IMAGE,
  content: imageMsg
};
```
</TabItem>

<TabItem value="harmony">

图片消息（ImageMessage）是 SDK 内置的消息类型，对应的 contentType 为 @"jg:img"。

| 属性名    | 类型    | 说明                     | 版本  |
| --------- | ------- | ------------------------ | ----- |
| url       | string  | 图片的远端地址           | 1.0.0 |
| thumbnail | string  | 缩略图的远端地址         | 1.0.0 |
| height    | number  | 图片高度                 | 1.0.0 |
| width     | number  | 图片宽度                 | 1.0.0 |
| size      | number  | 图片大小，单位为 KB      | 1.0.0 |
| extra     | string  | 扩展字段                 | 1.0.0 |

</TabItem>

<TabItem value="flutter">

图片消息（ImageMessage）是 SDK 内置的消息类型，对应的 contentType 为 "jg:img"。

| 属性名             | 类型     | 说明                     | 版本  |
| ------------------ | -------- | ------------------------ | ----- |
| localPath          | String   | 图片的本地路径           | 0.6.3 |
| url                | String   | 图片的远端地址           | 0.6.3 |
| thumbnailLocalPath  | String   | 缩略图的本地路径         | 0.6.3 |
| thumbnailUrl       | String   | 缩略图的远端地址         | 0.6.3 |
| height             | int      | 图片高度                 | 0.6.3 |
| width              | int      | 图片宽度                 | 0.6.3 |
| size               | int      | 图片大小，单位为 `Byte`  | 0.6.3 |
| extra              | String   | 扩展字段                 | 0.6.3 |

</TabItem>

<TabItem value="reactnative">

图片消息（ImageMessageContent）是 SDK 内置的消息类型，对应的 contentType 为 "jg:img"。

| 属性名             | 类型     | 说明                     | 版本  |
| ------------------ | -------- | ------------------------ | ----- |
| localPath          | string   | 图片的本地路径           | 1.0.0 |
| url                | string   | 图片的远端地址           | 1.0.0 |
| thumbnailLocalPath  | string   | 缩略图的本地路径         | 1.0.0 |
| thumbnailUrl       | string   | 缩略图的远端地址         | 1.0.0 |
| height             | number   | 图片高度                 | 1.0.0 |
| width              | number   | 图片宽度                 | 1.0.0 |
| size               | number   | 图片大小，单位为 `Byte`  | 1.0.0 |
| extra              | string   | 扩展字段                 | 1.0.0 |

</TabItem>
</Tabs>