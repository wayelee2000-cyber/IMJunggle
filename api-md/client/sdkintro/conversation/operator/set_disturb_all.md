---
title: 设置全局免打扰
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

设置当前用户全局免打扰，设置成功后当前用户不再接收全部离线消息推送，支持分时段设置，一个用户的多个设备同时设置全局免打扰，以最后一次成功设置为准。

**参数说明**

| 名称             | 类型     | 描述| 版本     |
|-----------------|---------|-------|--------|
| isMute     | boolean | 是否免打扰 | 1.1.0    |
| periods   | `List<TimePeriod>` | 免打扰的时间段，如果为空则视为全天免打扰 | 1.1.0    |
| callback   | ISimpleCallback | 结果回调 | 1.1.0    |

**示例代码**

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

设置当前用户全局免打扰，设置成功后当前用户不再接收全部离线消息推送，支持分时段设置，一个用户的多个设备同时设置全局免打扰，以最后一次成功设置为准。

**参数说明**

| 名称             | 类型     | 描述| 版本     |
|-----------------|---------|-------|--------|
| isMute     | BOOL | 是否免打扰 | 1.1.0    |
| periods   | NSArray `<JTimePeriod *>` | 免打扰的时间段，如果为空则视为全天免打扰 | 1.1.0    |
|  completeBlock   |  | 结果回调 | 1.1.0    |

**示例代码**

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

设置当前用户全局免打扰，设置成功后当前用户不再接收全部离线消息推送，支持按时区分时段设置，一个用户的多个设备同时设置全局免打扰，以最后一次成功设置为准。

**参数说明**

| 名称             | 类型     | 必填   | 默认值  | 描述| 版本     |
|-----------------|---------|-------|--------|----------|----------|
| params          | Object | 是     | 无 |  | 1.0.0    |
| params.type     | Number | 是     | 无 | [免打扰类型](../../../enum/web#disturb) | 1.0.0    |
| params.timezone | String | [UndisturbType.DISTURB](../../../enum/web#disturb) 时必传     | 无 | 时区字符串，例如：`Asia/Shanghai` | 1.3.0    |
| params.times    | Array | [UndisturbType.DISTURB](../../../enum/web#disturb) 时必传     | 无 | 免打扰时间段，支持设置多个，请参考示例 | 1.3.0    |

**示例代码**

```js
let { UndisturbType } = JIM;

 let params = {
  type: UndisturbType.DISTURB,
  timezone: 'Asia/Shanghai',
  times: [
    // 上午 8 点 至上午 12 点免打扰
    { start: '08:00', end: '12:00' },
    
    // 下午 19 点 至下午 20 点免打扰
    { start: '19:00', end: '20:00' },
    
    // 晚上 23 点 至次日早 6 点免打扰
    { start: '23:00', end: '06:00' },
  ]
};

jim.setAllDisturb(params).then(() => {
  console.log('set all disturb successfully');
});
```
</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
<TabItem value="reactnative">

> 暂未提供

</TabItem>
</Tabs>