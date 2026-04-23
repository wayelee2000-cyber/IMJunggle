---
title: Get Global Do Not Disturb
hide_title: true
sidebar_position: 5
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

Retrieve the global Do Not Disturb configuration.

**Callback Parameters**

| Name | Type | Description | Version |
|------------------|---------|---------------------------------|--------|
| errorCode | int | Error code; 0 indicates success | 1.1.0 |
| isMute | boolean | Indicates whether Do Not Disturb is enabled | 1.1.0 |
| timezone | String | Time zone | 1.1.0 |
| periods | `List<TimePeriod>` | Do Not Disturb time periods; if empty, Do Not Disturb is active all day | 1.1.0 |

**Sample Code**

```java
JIM.getInstance().getMessageManager().getMuteStatus(new IMessageManager.IGetMuteStatusCallback() {
    @Override
    public void onSuccess(boolean isMute, String timezone, List<TimePeriod> periods) {
        // Handle success
    }

    @Override
    public void onError(int errorCode) {
        // Handle error
    }
});
```

</TabItem>
<TabItem value="ios">

Retrieve the global Do Not Disturb configuration.

**Callback Parameters**

| Name | Type | Description | Version |
|------------------|---------|---------------------------------|--------|
| errorCode | JErrorCode | Error code; 0 indicates success | 1.1.0 |
| isMute | BOOL | Indicates whether Do Not Disturb is enabled | 1.1.0 |
| timezone | NSString | Time zone | 1.1.0 |
| periods | NSArray `<JTimePeriod *>` | Do Not Disturb time periods; if empty, Do Not Disturb is active all day | 1.1.0 |

**Sample Code**

```objectivec
[JIM.shared.messageManager getMuteStatus:^(JErrorCode errorCode, BOOL isMute, NSString *timezone, NSArray<JTimePeriod *> *periods) {
    // Handle callback
}];
```

</TabItem>
<TabItem value="js">

Retrieve the global Do Not Disturb configuration.

**Callback Parameters**

| Properties | Type | Description | Version |
|------------------|----------|------------------------------------------------|----------|
| disturbInfo | Object | Do Not Disturb information | 1.3.0 |
| disturbInfo.type | Number | [Do Not Disturb type](../../enum/web.md#disturb) | 1.3.0 |
| disturbInfo.timezone | String | Time zone, e.g., `Asia/Shanghai` | 1.3.0 |
| disturbInfo.times | Array | Do Not Disturb time periods | 1.3.0 |

**Sample Code**

```js
jim.getAllDisturb().then((disturbInfo) => {
  console.log('Successfully retrieved Do Not Disturb settings', disturbInfo);
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
<TabItem value="reactnative">

> Not yet provided

</TabItem>
</Tabs>
