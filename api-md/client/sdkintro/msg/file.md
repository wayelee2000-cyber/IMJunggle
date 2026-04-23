---
title: File message
hide_title: true
sidebar_position: 5
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

File messages (`FileMessage`) are a built-in SDK message type with the corresponding contentType `@"jg:file"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| name | String | File name | 1.0.0 |
| localPath | String | Local path of the file | 1.0.0 |
| url | String | Remote URL of the file | 1.0.0 |
| size | long | File size in `Byte` | 1.0.0 |
| type | String | File type | 1.0.0 |
| extra | String | Extension field | 1.0.0 |

</TabItem>
<TabItem value="ios">

File messages (`JFileMessage`) are a built-in SDK message type with the corresponding contentType `@"jg:file"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| name | NSString | File name | 1.0.0 |
| localPath | NSString | Local path of the file | 1.0.0 |
| url | NSString | Remote URL of the file | 1.0.0 |
| size | long long | File size in `Byte` | 1.0.0 |
| type | NSString | File type | 1.0.0 |
| extra | NSString | Extension field | 1.0.0 |

</TabItem>
<TabItem value="js">

File messages are a built-in SDK message type, corresponding to the enum _[MessageType.FILE](../enum/web.md#message)_.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| name | String | File name | 1.0.0 |
| url | String | File URL | 1.0.0 |
| size | Number | File size, used when previewing or downloading and showing progress. Unit: `KB` | 1.0.0 |
| type | String | File type. Common values include `word`, `excel`, `ppt`, and `zip` | 1.0.0 |
| extra | String | Additional message content. Supports a JSON string and cannot be modified after being set | 1.0.0 |

```js
let fileMsg = {
  name: 'demo.pptx',
  url: 'https://example.com/demo.pptx',
  size: 1000,
  type: 'pptx',
  extra: '{"Priority":"P0"}'
}

let message = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId1',
  name: MessageType.FILE,
  content: fileMsg
};
```
</TabItem>

<TabItem value="flutter">

File messages (`FileMessage`) are a built-in SDK message type with the corresponding contentType `"jg:file"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| name | String | File name | 0.6.3 |
| localPath | String | Local path of the file | 0.6.3 |
| url | String | Remote URL of the file | 0.6.3 |
| size | int | File size in `Byte` | 0.6.3 |
| type | String | File type | 0.6.3 |
| extra | String | Extension field | 0.6.3 |

</TabItem>

<TabItem value="reactnative">

File messages (`FileMessageContent`) are a built-in SDK message type with the corresponding contentType `"jg:file"`.

| Property | Type | Description | Version |
| --- | --- | --- | --- |
| name | string | File name | 1.0.0 |
| localPath | string | Local path of the file | 1.0.0 |
| url | string | Remote URL of the file | 1.0.0 |
| size | number | File size in `Byte` | 1.0.0 |
| type | string | File type | 1.0.0 |
| extra | string | Extension field | 1.0.0 |

</TabItem>
</Tabs>
