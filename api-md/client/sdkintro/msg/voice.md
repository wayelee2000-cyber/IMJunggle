---
title: 语音消息
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

Voice messages (VoiceMessage) are a built-in message type in the SDK, with the corresponding contentType @"jg:voice".

| Property  | Type   | Description                  | Version |
| --------- | ------ | ----------------------------|---------|
| localPath | String | Local path of the voice audio | 1.0.0  |
| url       | String | Remote URL of the voice audio | 1.0.0  |
| duration  | int    | Duration of the voice audio in seconds | 1.0.0 |
| extra     | String | Extension field              | 1.0.0  |

</TabItem>
<TabItem value="ios">

Voice messages (JVoiceMessage) are a built-in message type in the SDK, with the corresponding contentType @"jg:voice".

| Property  | Type     | Description                  | Version |
| --------- | -------- | ----------------------------|---------|
| localPath | NSString | Local path of the voice audio | 1.0.0  |
| url       | NSString | Remote URL of the voice audio | 1.0.0  |
| duration  | long     | Duration of the voice audio in seconds | 1.0.0 |
| extra     | NSString | Extension field              | 1.0.0  |
</TabItem>
<TabItem value="js">

Voice messages are a built-in message type in the SDK, corresponding to the enum _[MessageType.VOICE](../enum/web.md#message)_.

| Property  | Type    | Description                                                                 | Version |
|-----------|---------|-----------------------------------------------------------------------------|---------|
| url       | String  | URL of the voice audio. The storage location depends on the file storage setting used when sending the audio | 1.0.0   |
| type      | String  | Format of the voice audio. Default is `AAC`. Can be modified when sending voice. `AAC` is recommended for its high quality and small size | 1.0.0   |
| duration  | Number  | Duration of the voice audio in seconds                                      | 1.0.0   |
| extra     | String  | Additional message content, supports JSON string. Once set, it cannot be modified | 1.0.0   |

```js
let voiceMsg = {
  url: 'https://example.com/xxas.aac',
  type: 'aac',
  duration: 40,
  extra: '{"Priority":"P0"}'
}

let message = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userId1',
  name: MessageType.VOICE,
  content: voiceMsg
};
```

</TabItem>

<TabItem value="flutter">

Voice messages (VoiceMessage) are a built-in message type in the SDK, with the corresponding contentType @"jg:voice".

| Property  | Type   | Description                  | Version |
| --------- | ------ | ----------------------------|---------|
| localPath | String | Local path of the voice audio | 0.6.3  |
| url       | String | Remote URL of the voice audio | 0.6.3  |
| duration  | int    | Duration of the voice audio in seconds | 0.6.3 |
| extra     | String | Extension field              | 0.6.3  |

</TabItem>

<TabItem value="reactnative">

Voice messages (VoiceMessageContent) are a built-in message type in the SDK, with the corresponding contentType "jg:voice".

| Property  | Type   | Description                  | Version |
| --------- | ------ | ----------------------------|---------|
| localPath | string | Local path of the voice audio | 1.0.0  |
| url       | string | Remote URL of the voice audio | 1.0.0  |
| duration  | number | Duration of the voice audio in seconds | 1.0.0 |
| extra     | string | Extension field              | 1.0.0  |

</TabItem>

</Tabs>
