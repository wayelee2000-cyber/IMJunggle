---
title: 修改本地消息扩展
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
{ label: '鸿蒙', value: 'harmony', },
]
}>
<TabItem value="android">

消息本地扩展功能，只对本地的消息生效，不会同步到远端。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| clientMsgNo    | long  | 本端消息唯一编号   | 1.0.0    |
| attribute       | String  | 本地属性（可以使用 JSON 以满足复杂的业务场景） | 1.0.0    |

**示例代码**

```java
JIM.getInstance().getMessageManager().setLocalAttribute(123L, "attribute1");
```

</TabItem>
<TabItem value="ios">

消息本地扩展功能，只对本地的消息生效，不会同步到远端。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| attribute       | NSString  | 本地属性（可以使用 JSON 以满足复杂的业务场景） | 1.0.0    |
| clientMsgNo    | long long | 本端消息唯一编号   | 1.0.0    |

**示例代码**

```java
[JIM.shared.messageManager setLocalAttribute:@"attribute1" forClientMsgNo:123];
```

</TabItem>
<TabItem value="js">

:::danger 仅 Electron 中支持 
:::

为方便本地消息增加特殊字段用来实现不同功能，例如在 `Electron` 中为消息添加本地文件路径，可使用此方法实现，设置扩展成功后，获取历史消息时会自动返回对应消息的扩展

**参数说明**

| 名称                    | 类型    | 必填 |描述                                                                      | 版本   |
|------------------------|---------|----|---------------------------------------------------------------------------|--------|
| message                | Object  | 是 | 消息搜索参数                                                                | 1.0.0  |
| message.tid            | String  | 是  | 消息的唯一标识，可在 [Message](../../../msg/message) 中获取 | 1.0.0  |
| message.attribute      | String  | 是  | 可以设置 JSON 字符串用来扩展，长度 `1000` 个字符           | 1.0.0  |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let message = { 
  tid: 'nrde5kxxaacg7sb5', 
  attribute: '{"fileUrl": "/Users/xxx/avatar.jpg"}' 
};

jim.updateMessageAttr(message).then(() => {
  console.log('Update Local Message successfully')
}, (error) => {
  console.log(error)
});
```
</TabItem>
<TabItem value="harmony">

消息本地扩展功能，只对本地的消息生效，不会同步到远端。

**参数说明**

| 名称                           | 类型    | 描述                                                         | 版本     |
|-------------------------------|---------|--------------------------------------------------------------|----------|
| msgId    | string  | 消息id   | 1.0.0    |
| attribute       | string  | 本地属性（可以使用 JSON 以满足复杂的业务场景） | 1.0.0    |

**示例代码**

```java
JuggleIm.instance.getMessageManager().setLocalAttribue("msgid1","json content")
```

</TabItem>
<TabItem value="flutter" label="Flutter">


消息本地扩展功能，只对本地的消息生效，不会同步到远端。

**示例代码**

```dart
await JuggleIm.instance.setMessageLocalAttribute(
  100, // 消息的 clientMsgNo
  'localAttribute'
);
```

</TabItem>
</Tabs>