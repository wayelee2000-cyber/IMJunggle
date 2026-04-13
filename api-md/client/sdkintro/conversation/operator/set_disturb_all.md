---
title: Set global do not disturb
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
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

Set a global Do Not Disturb for the current user. Once set successfully, the user will no longer receive any offline push messages. Time-scheduled settings are supported. Multiple devices of the same user can set global Do Not Disturb simultaneously. The most recent successful setting takes precedence.

**Parameter description**

| Name | Type | Description | Version |
|------------------|---------|-------|--------|
| isMute | boolean | Whether to enable Do Not Disturb | 1.1.0 |
| periods | `List<TimePeriod>` | Do Not Disturb time periods; if empty, it is considered as Do Not Disturb all day | 1.1.0 |
| callback | ISimpleCallback | Result callback | 1.1.0 |

**Sample Code**

```java
List<TimePeriod> list = new ArrayList<>();
TimePeriod p1 = new TimePeriod();
p1.setStartTime("11:22");
p1.setEndTime("23:24");
list.add(p1);
JIM.getInstance().getMessageManager().setMute(true, list, new IMessageManager.ISimpleCallback() {
    @Override
    public void onSuccess() {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">

Set a global Do Not Disturb for the current user. Once set successfully, the user will no longer receive any offline push messages. Time-scheduled settings are supported. Multiple devices of the same user can set global Do Not Disturb simultaneously. The most recent successful setting takes precedence.

**Parameter description**

| Name | Type | Description | Version |
|------------------|---------|-------|--------|
| isMute | BOOL | Whether to enable Do Not Disturb | 1.1.0 |
| periods | NSArray `<JTimePeriod *>` | Do Not Disturb time periods; if empty, it is considered as Do Not Disturb all day | 1.1.0 |
| completeBlock | | Result callback | 1.1.0 |

**Sample Code**

```objectivec
NSMutableArray *a = [NSMutableArray array];
JTimePeriod *p1 = [[JTimePeriod alloc] init];
p1.startTime = @"11:23";
p1.endTime = @"20:40";
[a addObject:p1];

[JIM.shared.messageManager setMute:YES
                            periods:a
                          complete:^(JErrorCode errorCode) {
}];
```

</TabItem>
<TabItem value="js">

Set a global Do Not Disturb (DND) for the current user. After a successful setting, the user will no longer receive any offline message push notifications. Time-based settings and multiple time periods are supported. Multiple devices of the same user can set global DND simultaneously. The most recent successful setting takes precedence.

**Parameter description**

| Name | Type | Required | Default | Description | Version |
|------------------|----------|-------|--------|----------|----------|
| params | Object | Yes | None | | 1.0.0 |
| params.type | Number | Yes | None | [DND type](../../../enum/web#disturb) | 1.0.0 |
| params.timezone | String | Required for [UndisturbType.DISTURB](../../../enum/web#disturb) | None | Time zone string, e.g., `Asia/Shanghai` | 1.3.0 |
| params.times | Array | Must be provided every time for [UndisturbType.DISTURB](../../../enum/web#disturb) | None | Do Not Disturb time periods; multiple periods supported, see example | 1.3.0 |

**Sample Code**

```js
let { UndisturbType } = JIM;

let params = {
  type: UndisturbType.DISTURB,
  timezone: 'Asia/Shanghai',
  times: [
    // Do Not Disturb from 8:00 to 12:00
    { start: '08:00', end: '12:00' },
    
    // Do Not Disturb from 19:00 to 20:00
    { start: '19:00', end: '20:00' },
    
    // Do Not Disturb from 23:00 to 6:00 the next morning
    { start: '23:00', end: '06:00' },
  ]
};

jim.setAllDisturb(params).then(() => {
  console.log('Set all disturb successfully');
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