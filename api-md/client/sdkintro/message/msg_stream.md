---
title: 流式消息
hide_title: true
sidebar_position: 7
---

![](./msg_stream.png)

> 1、`App Server` 请求大模型生成内容: `App Server` 向大模型发起流式生成请求，携带 prompt 和上下文信息。大模型持续返回分段内容，每个片段包含实际内容以及是否结束的标识。

> 2、`App Server` 逐段发送: 根据大模型返回结果，`App Server` 调用 `IM Server` 的 [SendStream](../../../../server/message/streammsg/sendstreammsg) 接口，将每个分片发送给 `IM Server`，每次调用后返回分片发送结果。

> 3、IM 推送初始消息: `App Server` 调用 [SendStream](../../../../server/message/streammsg/sendstreammsg) 接口, `seq = 1` 且 `is_finished = false` 时 `IM Server` 向客户端推送 `jg:streamtext` 类型的消息。客户端在消息监听中会收到这条流式消息。

> 4、客户端接收片段并追加: `IM Server` 循环向客户端推送新内容片段。客户端每次收到片段时触发 `append` 事件，将内容追加到消息中，同时会返回 `jg:streamtext` 的 `messageId`。

> 5、推送完成通: 大模型生成完成后，`App Server` 需要将 `seq = 最后一段的序号` 且 `is_finished = true` ，调用 [SendStream](../../../../server/message/streammsg/sendstreammsg) 接口，`IM Server` 会向客户端推送生成完成通知。客户端触发 `complete` 事件。

<br/>


:::caution 以下特殊情况业务层无需特殊处理

**1、断网重连**: SDK 会自动将断网期间未收到的 `新增片段` 收取完整通知给业务层处理

**2、开始生成后杀进程或关闭浏览器**: 用户再上线后依然能收到完整的生成内容或者是 `正在生成的片段`

**3、用户生成内容多设备自动同步**: 例如用户 A 在 iOS 端生成的内容，在 Web 端登录依然可以看到，如果是生成中支持同步更新

**4、生成内容超时时间**: `App Server` 开始发送流消息后，默认超过 `10 分钟` 没有设置 `is_finished = true` 会自动完成，可能会出现内容完整的情况

**5、获取历史消息**: 用户生成完的消息，通过各端获取历史消息接口直接可以获取，并且是拼接完整的消息内容，业务层可按照消息类型直接展示

:::

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'ReactNative', value: 'reactnative', }
]
}>
<TabItem value="android">

```java
JIM.getInstance().getMessageManager().addListener("main", new IMessageManager.IMessageListener() {
    /// 接收消息的回调
    @Override
    public void onMessageReceive(Message message) {
        MessageContent content = message.getContent();
        if (content instanceof StreamTextMessage) {
            Log.d("TAG", "stream message did receive, content is " + ((StreamTextMessage) content).getContent());
        }
    }
}

JIM.getInstance().getMessageManager().addStreamMessageListener("main", new IMessageManager.IStreamMessageListener() {
    @Override
    public void onStreamTextMessageAppend(String messageId, String content) {
        // messageId: 对应的流式消息的消息 id
        // content: 分片追加的内容，开发者可以在界面上把 content 追加到 StreamTextMessage 的 content 尾部
    }

    @Override
    public void onStreamTextMessageComplete(Message message) {
        // message: 完整的流式消息对象
    }
});

```

</TabItem>
<TabItem value="ios">

```objectivec
// 接收消息代理
[JIM.shared.messageManager addDelegate:self];
//流式消息代理
[JIM.shared.messageManager addStreamMessageDelegate:self];

#pragma mark - JMessageDelegate
/// 接收消息的回调
- (void)messageDidReceive:(JMessage *)message {
    JMessageContent *content = message.content;
    if ([content isKindOfClass:[JStreamTextMessage class]]) {
        NSLog(@"stream message did receive, content is %@", ((JStreamTextMessage *)content).content);
    }
}

#pragma mark - JStreamMessageDelegate
- (void)streamTextMessageDidAppend:(NSString *)messageId content:(NSString *)content {
    // messageId: 对应的流式消息的消息 id
    // content: 分片追加的内容，开发者可以在界面上把 content 追加到 JStreamTextMessage 的 content 尾部
}

- (void)streamTextMessageDidComplete:(JMessage *)message {
    // message: 完整的流式消息对象
}

```

</TabItem>
<TabItem value="js">

```js
let { Event, MessageType } = JIM;

// 全局只需注册一次，与消息监听位置一致即可，放到此处方便阅读

jim.on(Event.MESSAGE_RECEIVED, (message) => {
  if(message.name == MessageType.STREAM_TEXT){
    console.log('收到一条流消息', message)
  }
  //... 其他消息类型
});

jim.on(Event.STREAM_APPENDED, (notify) => {
  // notify => { content: '新增内容片段', messageId: 'MessageType.STREAM_TEXT 的 messageId' }
  console.log('Event.STREAM_APPENDED', notify)
});

jim.on(Event.STREAM_COMPLETED, (notify) => {
  // notify => { content: '完整的生成内容', messageId: 'MessageType.STREAM_TEXT' }
  console.log('Event.STREAM_COMPLETED', notify)
});
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">


> 流式消息用于 AI 助手等场景，支持实时文本流式输出。
> 如果要做打字效果，可以将消息 StreamTextMessageContent 放在一个队列中，
> 入队列后并通过append不断追加，可以逐字出队列处理，实现打字效果

* 收到消息后如果是流消息 jg:streamtext，且未完成
* 之后的流消息通过 onStreamTextMessageAppend 追加通知
* 直到流消息完成 onStreamTextMessageComplete 通知

```javascript

// 接收消息监听
JuggleIM.addMessageListener('MessageListScreen', {
      onMessageReceive: (message: Message) => {
}})


/**
 * 流式消息监听器
 * 用于监听流式消息的追加和完成事件
 */
const unsubscribe = JuggleIM.addStreamMessageListener('stream_listener_key', {
  /**
   * 流式消息分片追加的回调
   * @param {string} messageId - 流式消息的消息 id
   * @param {string} content - 分片追加的内容，开发者可以在界面上把 content 追加到 StreamTextMessage 的 content 尾部
   */
  onStreamTextMessageAppend: (messageId, content) => {
    console.log('Stream message append:', messageId, content);
    // 在 UI 中追加内容，实现打字机效果
  },
  
  /**
   * 流式消息完成的回调
   * @param {Message} message - 追加完成的流式消息
   */
  onStreamTextMessageComplete: (message) => {
    console.log('Stream message complete:', message);
    // 更新 UI，显示完整消息
  }
});

// 取消监听
// unsubscribe();

/**
 * 流式文本消息内容: jg:streamtext
 * 流式消息用于AI助手等场景，消息内容会分片追加
 * @property {string} content - 消息内容
 * @property {boolean} isFinished - 是否完成
 * @property {number} seq - 流式消息序号
 */
export class StreamTextMessageContent extends MessageContent {
    contentType: string;
    content: string;
    isFinished: boolean;
    seq: number;
}


```

</TabItem>
</Tabs>