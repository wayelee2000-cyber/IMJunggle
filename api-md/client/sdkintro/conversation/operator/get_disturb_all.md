---
title: 获取全局免打扰
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

获取全局免打扰配置信息。

**回调参数**

| 名称             | 类型     | 描述| 版本     |
|-----------------|---------|-------|--------|
| errorCode | int | 错误码，0 为成功 | 1.1.0 |
| isMute     | boolean | 是否免打扰 | 1.1.0    |
| timezone | String | 时区 | 1.1.0 |
| periods   | `List<TimePeriod>` | 免打扰的时间段，如果为空则视为全天免打扰 | 1.1.0    |

**示例代码**

```java
JIM.getInstance().getMessageManager().getMuteStatus(new IMessageManager.IGetMuteStatusCallback() {
    @Override
    public void onSuccess(boolean isMute, String timezone, List<TimePeriod> periods) {
    }

    @Override
    public void onError(int errorCode) {
    }
});
```

</TabItem>
<TabItem value="ios">

获取全局免打扰配置信息。

**回调参数**

| 名称             | 类型     | 描述| 版本     |
|-----------------|---------|-------|--------|
| errorCode | JErrorCode | 错误码，0 为成功 | 1.1.0|
| isMute     | BOOL | 是否免打扰 | 1.1.0    |
| timezone | NSString | 时区 | 1.1.0 |
| periods   | NSArray `<JTimePeriod *>` | 免打扰的时间段，如果为空则视为全天免打扰 | 1.1.0    |

**示例代码**

```objectivec
[JIM.shared.messageManager getMuteStatus:^(JErrorCode errorCode, BOOL isMute, NSString *timezone, NSArray<JTimePeriod *> *periods) {
}];
```

</TabItem>
<TabItem value="js">

获取全局免打扰配置信息。

**回调参数**

| 属性            | 类型    | 描述                                           | 版本  |
|-----------------|---------|------------------------------------------------|----------|
| disturbInfo     | Object  | 免打扰信息                                       | 1.3.0    |
| disturbInfo.type | Number | [免打扰类型](../../../enum/web#disturb) | 1.3.0    |
| disturbInfo.timezone | String | 免到扰时区，例如: `Asia/Shanghai` | 1.3.0    |
| disturbInfo.times | Array | 免打扰时间段 | 1.3.0    |


**示例代码**

```js
jim.getAllDisturb().then((disturbInfo) => {
  console.log('get disturb successfully', disturbInfo);
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