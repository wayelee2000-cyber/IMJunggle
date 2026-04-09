---
title: 获取指定属性
hide_title: true
sidebar_position: 8
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
{ label: '鸿蒙', value: 'harmony', }
]
}>
<TabItem value="android">

> 即将发布

</TabItem>
<TabItem value="ios">

> 即将发布

</TabItem>
<TabItem value="flutter">

> 即将发布

</TabItem>
<TabItem value="js">

获取聊天室指定属性的值，需要在加入聊天室成功后调用，未加入聊天室获取属性 SDK 会返回空数据。

**参数说明**

| 名称                    | 类型     | 必填   | 默认值  | 描述| 版本     |
|-------------------------|---------|-------|---|----------|----------|
| chatroom                | Object | 是     | 无 | 聊天室对象 | 1.6.0    |
| chatroom.id             | String | 是     | 无 | 聊天室 ID | 1.6.0    |
| chatroom.attributes     | Array  | 是     | 无 | 聊天室属性列表，数据结构请参考示例代码 | 1.6.0    |

**回调说明**

| 属性                 | 类型    | 描述                               | 版本  |
|---------------------|---------|-----------------------------------|----------|
| chatroom            | Object  | 会话对象                            | 1.6.0    |
| chatroom.id         | String  | 聊天室 ID                           | 1.6.0    |
| chatroom.attributes | Array   | 聊天室全部属性，数据结构请参考示例代码   | 1.6.0    |

**示例代码**

```js
let chatroom = {
  id: 'chatroom1001',
  attributes: [ { key: 'name' }, { key: 'age' }]
};

jim.getChatRoomAttributes(chatroom).then((chatroom) => {
  let { id, attributes } = chatroom;
  /* 
    attributes => 
      [
        { key: 'name', value: 'xiaoshan' },
        { key: 'age', value: 18 },
      ]
  */
}, (error) => {
  console.log('error', error)
});
```

</TabItem>
<TabItem value="reactnative">

> 即将发布

</TabItem>
<TabItem value="harmony">

> 即将发布

</TabItem>
</Tabs>