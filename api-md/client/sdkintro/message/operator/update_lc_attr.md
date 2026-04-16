---
title: Modify local message extension
hide_title: true
sidebar_position: 7
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

The local message extension function only affects local messages and will not be synchronized to the remote end.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| clientMsgNo | long | The unique identifier of the local message | 1.0.0 |
| attribute | String | Local attributes (JSON format can be used to support complex business scenarios) | 1.0.0 |

**Sample Code**

```java
JIM.getInstance().getMessageManager().setLocalAttribute(123L, "attribute1");
```

</TabItem>
<TabItem value="ios">

The local message extension function only affects local messages and will not be synchronized to the remote end.

**Parameter description**

| Name | Type | Description | Version |
|----------------------------------|---------|------------------------------------------------------------------|----------|
| attribute | NSString | Local attributes (JSON format can be used to support complex business scenarios) | 1.0.0 |
| clientMsgNo | long long | The unique identifier of the local message | 1.0.0 |

**Sample Code**

```java
[JIM.shared.messageManager setLocalAttribute:@"attribute1" forClientMsgNo:123];
```

</TabItem>
<TabItem value="js">

<div style="margin: 1rem 0; padding: 1rem 1.25rem; border-left: 4px solid #e5484d; background: #fff1f2; border-radius: 0 16px 16px 0;">
<p style="margin: 0 0 0.75rem; font-size: 1rem; font-weight: 700; color: #b42318;">This feature is only supported in Electron</p>
</div>

To support local messages, special fields are added to implement different functions. For example, adding a local file path to a message in `Electron` can be achieved using this method. After the extension is set successfully, the extension of the corresponding message will be automatically returned when retrieving historical messages.

**Parameter description**

| Name | Type | Required | Description | Version |
|---------------------|---------|----|-------------------------------------------------------------------------------|--------|
| message | Object | Yes | Message search parameters | 1.0.0 |
| message.tid | String | Yes | The unique identifier of the message, which can be obtained in [Message](../../../msg/message) | 1.0.0 |
| message.attribute | String | Yes | Extension data as a JSON string, maximum length of 1000 characters | 1.0.0 |

**Success callback**

No parameters are returned; the callback is triggered to indicate success.

**Failure callback**

| Name | Type | Description | Version |
|--------|---------|--------------------------------------------------------------|--------|
| error | Object | Contains a status code indicating the failure reason. You can view `error.msg` directly or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.0.0 |

**Sample Code**
```js
let message = { 
  tid: 'nrde5kxxaacg7sb5', 
  attribute: '{"fileUrl": "/Users/xxx/avatar.jpg"}' 
};

jim.updateMessageAttr(message).then(() => {
  console.log('Local message updated successfully');
}, (error) => {
  console.log(error);
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

The local message extension function only affects local messages and will not be synchronized to the remote end.

**Sample Code**

```dart
await JuggleIm.instance.setMessageLocalAttribute(
  100, // clientMsgNo of the message
  'localAttribute'
);
```

</TabItem>
</Tabs>
