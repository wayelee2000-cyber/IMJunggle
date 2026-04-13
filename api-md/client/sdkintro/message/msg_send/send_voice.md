---
title: Send voice
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

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| content | MessageContent | Message entity | 1.0.0 |
| conversation | Conversation | Conversation identifier | 1.0.0 |
| callback | ISendMessageCallback | Callback | 1.0.0 |

**Sample Code**

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

**Interface definition**

```objectivec
/// Send media message (upload media first, then send message)
/// - Parameters:
///   - content: media message entity
///   - conversation: conversation
///   - progressBlock: upload progress callback
///   - successBlock: success callback
///   - errorBlock: failure callback
///   - cancelBlock: user cancels upload callback
- (JMessage *)sendMediaMessage:(JMediaMessageContent *)content
                inConversation:(JConversation *)conversation
                      progress:(void (^)(int progress, JMessage *message))progressBlock
                       success:(void (^)(JMessage *message))successBlock
                         error:(void (^)(JErrorCode errorCode, JMessage *message))errorBlock
                        cancel:(void (^)(JMessage *message))cancelBlock;
```

**Sample Code**
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

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| message | Object | Yes | | Message object | 1.0.0 |
| message.conversationType | Number | Yes | | [Conversation Type](../../../enum/web#conversation) | 1.0.0 |
| message.conversationId | String | Yes | | Session ID. When the session type is `PRIVATE`, the session ID is the userId of the receiver; when the session type is `GROUP`, it is the group ID | 1.0.0 |
| message.content | Object | Yes | | | 1.0.0 |
| message.content.file | File | Yes | | Audio file object | 1.0.0 |
| message.content.duration | String | No | | Audio duration in seconds | 1.0.0 |
| message.content.type | String | Yes | | Audio type, transparently transmitted to the peer, used to customize file types and display UI | 1.0.0 |
| message.mentionInfo | Object | No | None | Valid when conversationType is `GROUP`. Setting mentionInfo indicates this message is an @ message | 1.0.0 |
| mentionInfo.mentionType | Number | No | None | @ type, see [@ message enumeration](../../../enum/web#mention) for details | 1.0.0 |
| mentionInfo.targetIds | Array | No | None | List of specified @ recipients. The SDK prioritizes determining the @ type of the message based on mentionType | 1.0.0 |
| lifeTime | Number | No | 0 | Message destruction time period, must be greater than `0`, unit: `ms`. For example, 60s: `1 * 60 * 1000` | 1.9.0 |
| lifeTimeAfterRead | Number | No | 0 | Time period for the message to disappear after reading, must be greater than 0, unit: `ms`. For example, 60s: `1 * 60 * 1000` | 1.9.0 |

**Callbacks parameter description**

| Name | Type | Required | Default | Description | Version |
|--------------------------------|---------|--------|--------|----------------------------------------------------------------|----------|
| callbacks | Object | No | | Callback object | 1.0.0 |
| callbacks.onbefore | Function| No | | Callback before the message is sent. After this method is triggered, it returns the temporary message ID `tid`, which can be used to render the message on the page. If the message is sent successfully, the backend will update the message status based on `tid` | 1.0.0 |
| callbacks.onprogress | Function| No | | File upload progress callback | 1.0.0 |
| callbacks.onerror | Function| No | | If the file upload fails, a specific error description is returned and the message sending stops | 1.0.0 |

**Successful callback**

| Name | Type | Description | Version |
|-----------|----------|-------------------------------------------------------------------------------|--------|
| message | Object | After successful sending, returns a message object with `messageId` and `sentTime`. See the message structure [Message](../../../msg/message) | 1.0.0 |

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| result | Object | After failure to send, the returned object contains `tid` and `error` information. You can view `error.msg` directly or refer to [status code](../../../status_code/web) | 1.0.0 |

**Sample Code**
```js
let { ConversationType } = JIM;

// Get the file object through <input type="file"> onchange
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
message.tid can be used to render the message on the page. It uniquely identifies the message. After onprogress is triggered, the progress bar can be updated using message.tid.
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
  // You can update the message sending failure status based on tid. On the web, failed messages are only saved in SDK memory and cannot be retrieved after refreshing.
  console.log(tid, error);
});
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

Since sending messages is asynchronous, calling `sendVoiceMessage` returns the `message` object synchronously. At this point, the message can be displayed on the page immediately.

Use `message.clientMsgNo` as a unique identifier. After the `callback` is triggered, the message status can be updated based on `clientMsgNo`, such as upload progress.

The SDK includes a built-in file upload function. Simply assign the local file path to `VoiceMessage.localPath`, and the SDK will automatically upload the file and return the file URL.

> Note: When sending messages such as files, pictures, videos, etc., you must first configure file storage `OSS` in the private developer backend.

<p/>

**Sample Code**

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

Since sending messages is asynchronous, calling `sendMessage` returns the `message` object synchronously. At this point, the message can be displayed on the page immediately.

Use `message.clientMsgNo` as a unique identifier. After the `callback` is triggered, the message status can be updated based on `clientMsgNo`, such as upload progress.

The SDK includes a built-in file upload function. Simply assign the local file path to `ImageMessage.localPath`, and the SDK will automatically upload the file and return the file URL.

> Note: When sending messages such as files, pictures, videos, etc., you must first configure file storage `OSS` in the private developer backend.

<p/>

**Sample Code**

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

// Progress value range 0–100
SendMessageProgressCallback progressCallback = (message, progress) {
  print('sendMediaMessage onProgress, progress is $progress');
};

Message mediaMessage = await JuggleIm.instance.sendMediaMessage(voiceMessage, conversation, callback, progressCallback);
```

</TabItem>
</Tabs>