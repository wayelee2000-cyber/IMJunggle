---
title: Custom message upload
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

When developers send media messages using the `sendMediaMessage` method, they can customize the upload process for media messages (`MediaMessageContent`), take control of the upload logic, and upload files to their own file servers.

**Sample Code**

```java
JIM.getInstance().getMessageManager().setMessageUploadProvider(this);

// Developer implements the upload method
@Override
public void uploadMessage(Message message, UploadCallback uploadCallback) {
    Handler mH = new Handler(Looper.getMainLooper());
    mH.postDelayed(new Runnable() {
        @Override
        public void run() {
            // Simulate upload progress callback
            uploadCallback.onProgress(50);
        }
    }, 100);
    mH.postDelayed(new Runnable() {
        @Override
        public void run() {
            MediaMessageContent mediaMessageContent = (MediaMessageContent) message.getContent();
            String localPath = mediaMessageContent.getLocalPath();
            // Use localPath to access the file content and upload it
            if (true) {
                // Upload successful
                mediaMessageContent.setUrl("xxxxxx"); // Uploaded file URL
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

When developers send media messages using the `sendMediaMessage` method, they can customize the upload process for media messages (`JMediaMessageContent`), take control of the upload logic, and upload files to their own file servers.

**Sample Code**

```objectivec
[JIM.shared.messageManager setMessageUploadProvider:self];

// Developer implements the upload method
- (void)uploadMessage:(JMessage *)message
             progress:(void (^)(int))progressBlock
              success:(void (^)(JMessage * _Nonnull))successBlock
                error:(void (^)(void))errorBlock cancel:(void (^)(void))cancelBlock {
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        // Simulate upload progress callback
        progressBlock(50);
    });
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)), dispatch_get_global_queue(0, 0), ^{
        JMediaMessageContent *content = (JMediaMessageContent *)message.content;
        NSString *localPath = content.localPath;
        // Use localPath to access the file content and upload it
        if (YES) {
            // Upload successful
            content.url = @"xxx"; // Uploaded file URL
            successBlock(message);
        } else {
            // Upload failed
            errorBlock();
        }
    });
}
```

</TabItem>
<TabItem value="reactnative" label="ReactNative">

> Not yet provided

</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
</Tabs>