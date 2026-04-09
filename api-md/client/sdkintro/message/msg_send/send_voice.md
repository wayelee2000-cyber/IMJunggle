---
title: 发送语音
hide_title: true
sidebar_position: 1
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| content                        | MessageContent  | 消息实体                                           | 1.0.0    |
| conversation                   | Conversation  | 会话标识                          | 1.0.0    |
| callback         | ISendMessageCallback  | 回调 | 1.0.0    |

**示例代码**

```java
VoiceMessage voice = new VoiceMessage();
voice.setLocalPath("xxx");
voice.setDuration(1024);
Conversation conversation = new Conversation(Conversation.ConversationType.PRIVATE, "userid1");
IMessageManager.ISendMediaMessageCallback callback = new IMessageManager.ISendMediaMessageCallback() {
    @Override
    public void onProgress(int progress, Message message) {
        Log.i("TAG", "onProgress");
    }

    @Override
    public void onSuccess(Message message) {
        Log.i("TAG", "send message success");
    }

    @Override
    public void onError(Message message, int errorCode) {
        Log.i("TAG", "send message error");
    }

    @Override
    public void onCancel(Message message) {
        Log.i("TAG", "onCancel");
    }
};
Message message = JIM.getInstance().getMessageManager().sendMediaMessage(voice, conversation, callback);
Log.i("TAG", "after send, clientMsgNo is " + message.getClientMsgNo());
```

</TabItem>
<TabItem value="ios">

**接口定义**

```objectivec
/// 发送媒体消息（先上传媒体，再发送消息）
/// - Parameters:
///   - content: 媒体消息实体
///   - conversation: 会话
///   - progressBlock: 上传进度回调
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
///   - cancelBlock: 用户取消上传回调
- (JMessage *)sendMediaMessage:(JMediaMessageContent *)content
                inConversation:(JConversation *)conversation
                      progress:(void (^)(int progress, JMessage *message))progressBlock
                       success:(void (^)(JMessage *message))successBlock
                         error:(void (^)(JErrorCode errorCode, JMessage *message))errorBlock
                        cancel:(void (^)(JMessage *message))cancelBlock;
```

**示例代码**
```objectivec
JConversation *conversation = [[JConversation alloc] initWithConversationType:JConversationTypePrivate conversationId:@"userid2"];
JVoiceMessage *voice = [[JVoiceMessage alloc] init];
voice.localPath = @"xxxxxxxxx";
voice.duration = 60;
JMessage *m = [JIM.shared.messageManager sendMediaMessage:voice
                                            inConversation:conversation
                                                  progress:^(int progress, JMessage *message) {
    
} success:^(JMessage *message) {
    
} error:^(JErrorCode errorCode, JMessage *message) {
    
} cancel:^(JMessage *message) {
    
}];
NSLog(@"after send, m.clientMsgNo is %lld", m.clientMsgNo);
```
</TabItem>
<TabItem value="js">

**参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| message                        | Object  | 是     |        | 消息对象                                                      | 1.0.0    |
| message.conversationType       | Number  | 是     |        | [会话类型](../../../enum/web#conversation)                            | 1.0.0    |
| message.conversationId         | String  | 是     |        | 会话 Id，会话类型是 `PRIVATE` 时，会话 Id 是接收方的 userId，会话类型是 `GROUP` 时是群组 Id | 1.0.0    |
| message.content                | Object  | 是     |        |                                                              | 1.0.0    |
| message.content.file           | File    | 是     |        | 音频对象               | 1.0.0    |
| message.content.duration       | String  | 否     |        | 音频时长，单位：秒    | 1.0.0    |
| message.content.type           | String  | 是     |        | 音频类型，透传给对端，用来自定义文件类型并展示 UI            | 1.0.0    |
| message.mentionInfo            | Object  | 否     |  无    | conversationType 为 `GROUP` 时有效，设置 mentionInfo 表示本条消息是 @ 消息 | 1.0.0    |
| mentionInfo.mentionType        | Number  | 否     |  无    | @ 类型，详细可查看 [@ 消息枚举](../../../enum/web#mention) 说明         | 1.0.0    |
| mentionInfo.targetIds          | Array   | 否     |  无    | @ 指定人列表，SDK 会优先根据 mentionType 判断消息的 @ 类型         | 1.0.0    |
| lifeTime                   | Number    | 否    |  0    |消息的销毁时间段，必须大于 `0`, 单位 `ms`, 例如 60s: `1 * 60 * 1000`   | 1.9.0    |
| lifeTimeAfterRead             | Number    | 否    |  0    |消息的阅后即焚的时间段，必须大于 0, 单位 `ms`, 例如 60s: `1 * 60 * 1000`  | 1.9.0    |

**callbacks 参数说明**

| 名称                           | 类型    | 必填   | 默认值  | 描述                                                         | 版本     |
|--------------------------------|---------|--------|--------|--------------------------------------------------------------|----------|
| callbacks                      | Object  | 否     |        | 回调对象                                                      | 1.0.0    |
| callbacks.onbefore             | Function| 否     |        | 消息发送前回调，此方法触发后会返回临时消息标识 `tid`，可向页面渲染消息，消息发送成功后台根据 `tid` 更新消息状态| 1.0.0    |
| callbacks.onprogress           | Function| 否     |        | 文件上传进度回调 | 1.0.0    |
| callbacks.onerror              | Function| 否     |        | 文件上传失败，会返回具体的异常说明，消息将会停止发送 | 1.0.0    |


**成功回调**

| 名称      | 类型    | 描述                                                                      | 版本   |
|-----------|---------|---------------------------------------------------------------------------|--------|
| message   | Object  | 发送成功后返回带 `messageId` 和 `sentTime` 消息对象，消息结构请查看 [Message](../../../msg/message) | 1.0.0  |

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| result | Object  | 发送失败后会返回对象中包含 `tid` 属性信息，同时包含 `error` 信息，可以直接查看 `error.msg`，或者查看 [状态码](../../../status_code/web) | 1.0.0  |

**示例代码**
```js
let { ConversationType } = JIM;

// 通过 <input type="file"> onchange 获取 file 对象
let file = e.target.files[0];

let message = {
  conversationType: ConversationType.PRIVATE,
  conversationId: 'userid02',
  content: {
    file: file,
    type: 'aac',
    duration: 40
  },
};

jim.sendVoiceMessage(message, {
  onbefore: (message) => {
    /* 
      message.tid  此时可将消息渲染至页面，可通过 message.tid 做唯一标识，onprogress 触发后通过 message.tid 更新进度条
    */
  },
  onprogress: ({ percent, message }) => {
    console.log(`${percent}%`, message);
  },
  onerror: (error) => {
    console.log('upload file error', error);
  }
}).then((msg) => {
  console.log('send voice message successfully', msg)
}, (result) => {
  let { error, tid } = result;
  // 可根据 tid 修改消息发送失败的状态, Web 端消息失败仅在 SDK 内存中保存，刷新后将无法获取到发送失败的消息
  console.log(tid, error);
});
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

由于发送消息是异步的，调用 `sendVoiceMessage` 会同步返回 `message` 对象，此时可优先向页面展示消息，

并用 `message.clientMsgNo` 做唯一标识，`callback` 触发后可根据 `clientMsgNo` 做消息状态更新，如上传进度。

SDK 内置文件上传功能，只需将本地文件路径赋值给 `VoiceMessage.localPath`，SDK 会自动上传文件并返回文件 URL。

> 注意：发送文件、图片、视频等消息时，需要先在私有开发者后台配置文件存储 `OSS`。

<p/>

**示例代码**

```typescript
import JuggleIM from 'juggleim-rnsdk';

const conversation = {
  type: 1,
  id: 'userId1'
};

const voiceMessage = {
  conversation: conversation,
  content: {
    contentType: 'jg:voice',
    localPath: '/path/to/voice.aac',
    duration: 10
  }
};

const callback = (message: any, errorCode: number, progress?: number) => {
  if (errorCode === 0) {
    console.log('sendVoiceMessage success, messageId is ' + message.messageId);
  } else if (errorCode === 100) {
    console.log('sendVoiceMessage onProgress, progress is ' + progress);
  } else {
    console.log('sendVoiceMessage error, errorCode is ' + errorCode.toString());
  }
};

JuggleIM.sendVoiceMessage(voiceMessage, callback).then((message) => {
  console.log('after send, clientMsgNo is ' + message.clientMsgNo);
});
```

</TabItem>
<TabItem value="flutter" label="Flutter">

由于发送消息是异步的，调用 `sendMessage` 会同步返回 `message` 对象，此时可优先向页面展示消息，

并用 `message.clientMsgNo` 做唯一标识，`callback` 触发后可根据 `clientMsgNo` 做消息状态更新，如上传进度。

SDK 内置文件上传功能，只需将本地文件路径赋值给 `ImageMessage.localPath`，SDK 会自动上传文件并返回文件 URL。

> 注意：发送文件、图片、视频等消息时，需要先在私有开发者后台配置文件存储 `OSS`。

<p/>

**示例代码**

```dart
Conversation conversation = Conversation(ConversationType.group, 'groupId1');

VoiceMessage voiceMessage = VoiceMessage();
voiceMessage.localPath = '/Applications/xxx/xxx/voice.aac';
voiceMessage.duration = 10;

DataCallback<Message> callback = (m, errorCode) {
  if (errorCode == 0) {
    print("sendMediaMessage success, messageId is " + m.messageId);
  } else {
    print('sendMediaMessage error, errorCode is ' + errorCode.toString() + ', clientMsgNo is ' + m.clientMsgNo!.toString());
  }
};

//progress 取值范围 0～100
SendMessageProgressCallback progressCallback = (message, progress) {
  print('sendMediaMessage onProgress, progress is $progress');
};

Message mediaMessage = await JuggleIm.instance.sendMediaMessage(voiceMessage, conversation, callback, progressCallback);
```

</TabItem>
</Tabs>