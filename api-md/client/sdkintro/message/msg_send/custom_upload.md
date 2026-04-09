---
title: 自定义消息上传
hide_title: true
sidebar_position: 5
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

开发者在发送媒体消息调用 `sendMediaMessage` 方法时，可以自定义媒体消息（MediaMessageContent）的上传，接管上传逻辑，将文件上传到自己的文件服务器。

**示例代码**

```java
JIM.getInstance().getMessageManager().setMessageUploadProvider(this);

// 开发者实现上传方法
@Override
public void uploadMessage(Message message, UploadCallback uploadCallback) {
    Handler mH = new Handler(Looper.getMainLooper());
    mH.postDelayed(new Runnable() {
        @Override
        public void run() {
            //模拟上传进度回调
            uploadCallback.onProgress(50);
        }
    }, 100);
    mH.postDelayed(new Runnable() {
        @Override
        public void run() {
            MediaMessageContent mediaMessageContent = (MediaMessageContent) message.getContent();
            String localPath = mediaMessageContent.getLocalPath();
            // 使用 localPath 获取文件内容并进行上传
            if (true) {
                //上传成功
                mediaMessageContent.setUrl("xxxxxx");//上传的文件 url
                uploadCallback.onSuccess(message);
            } else {
                uploadCallback.onError();
            }
        }
    }, 1000);
}

```

</TabItem>
<TabItem value="ios">

开发者在发送媒体消息调用 `sendMediaMessage` 方法时，可以自定义媒体消息（JMediaMessageContent）的上传，接管上传逻辑，将文件上传到自己的文件服务器。

**示例代码**

```objectivec
[JIM.shared.messageManager setMessageUploadProvider:self];

// 开发者实现上传方法
- (void)uploadMessage:(JMessage *)message
             progress:(void (^)(int))progressBlock
              success:(void (^)(JMessage * _Nonnull))successBlock
                error:(void (^)(void))errorBlock cancel:(void (^)(void))cancelBlock {
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        //模拟上传进度回调
        progressBlock(50);
    });
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)), dispatch_get_global_queue(0, 0), ^{
        JMediaMessageContent *content = (JMediaMessageContent *)message.content;
        NSString *localPath = content.localPath;
        // 使用 localPath 获取文件内容并进行上传
        if (YES) {
            //上传成功
            content.url = @"xxx";//上传的文件 url
            successBlock(message);
        } else {
            //上传失败
            errorBlock();
        }
    });
}
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

> 暂未提供

</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
</Tabs>