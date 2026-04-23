---
title: Image message
hide_title: true
sidebar_position: 4
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android' },
{ label: 'iOS', value: 'ios' },
{ label: 'JavaScript', value: 'js' },
{ label: 'Flutter', value: 'flutter' },
{ label: 'ReactNative', value: 'reactnative' }
]}
>
<TabItem value="android">

Image messages (`ImageMessage`) are a built-in SDK message type with the corresponding contentType `@"jg:img"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| localPath | String | Local path of the image | 1.0.0 |
| url | String | Remote URL of the image | 1.0.0 |
| thumbnailLocalPath | String | Local path of the thumbnail image | 1.0.0 |
| thumbnailUrl | String | Remote URL of the thumbnail image | 1.0.0 |
| height | int | Image height | 1.0.0 |
| width | int | Image width | 1.0.0 |
| size | long | Image size in `Byte` | 1.0.0 |
| extra | String | Extension field | 1.0.0 |

</TabItem>
<TabItem value="ios">

Image messages (`JImageMessage`) are a built-in SDK message type with the corresponding contentType `@"jg:img"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| localPath | NSString | Local path of the image | 1.0.0 |
| url | NSString | Remote URL of the image | 1.0.0 |
| thumbnailLocalPath | NSString | Local path of the thumbnail image | 1.0.0 |
| thumbnailUrl | NSString | Remote URL of the thumbnail image | 1.0.0 |
| height | int | Image height | 1.0.0 |
| width | int | Image width | 1.0.0 |
| size | long long | Image size in `Byte` | 1.0.0 |
| extra | NSString | Extension field | 1.0.0 |

</TabItem>
<TabItem value="js">

Image messages are a built-in SDK message type, corresponding to the enum _[MessageType.IMAGE](../enum/web.md#message)_.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| url | String | URL of the original image | 1.0.0 |
| thumbnail | String | URL of the thumbnail image. The UI can use the width and height fields to reserve space and load the thumbnail first to reduce layout shifts | 1.0.0 |
| height | Number | Image height | 1.0.0 |
| width | Number | Image width | 1.0.0 |
| size | Number | Original image size, used when previewing or downloading and showing progress. Unit: `KB` | 1.0.0 |
| extra | String | Additional message content. Supports a JSON string and cannot be modified after being set | 1.0.0 |

```js
let imageMsg = {
  url: 'https://example.com/avatar.png',
  thumbnail: 'https://example.com/avatar_th.png',
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

<TabItem value="flutter">

Image messages (`ImageMessage`) are a built-in SDK message type with the corresponding contentType `"jg:img"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| localPath | String | Local path of the image | 0.6.3 |
| url | String | Remote URL of the image | 0.6.3 |
| thumbnailLocalPath | String | Local path of the thumbnail image | 0.6.3 |
| thumbnailUrl | String | Remote URL of the thumbnail image | 0.6.3 |
| height | int | Image height | 0.6.3 |
| width | int | Image width | 0.6.3 |
| size | int | Image size in `Byte` | 0.6.3 |
| extra | String | Extension field | 0.6.3 |

</TabItem>

<TabItem value="reactnative">

Image messages (`ImageMessageContent`) are a built-in SDK message type with the corresponding contentType `"jg:img"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| localPath | string | Local path of the image | 1.0.0 |
| url | string | Remote URL of the image | 1.0.0 |
| thumbnailLocalPath | string | Local path of the thumbnail image | 1.0.0 |
| thumbnailUrl | string | Remote URL of the thumbnail image | 1.0.0 |
| height | number | Image height | 1.0.0 |
| width | number | Image width | 1.0.0 |
| size | number | Image size in `Byte` | 1.0.0 |
| extra | string | Extension field | 1.0.0 |

</TabItem>
</Tabs>
