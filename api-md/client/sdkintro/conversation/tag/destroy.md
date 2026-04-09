---
title: 销毁标签
hide_title: true
sidebar_position: 1
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

> 暂未提供

</TabItem>
<TabItem value="ios">

> 暂未提供

</TabItem>
<TabItem value="js">

销毁会话标签，会话标签仅对当前用户有效，`SDK` 会自动将标签同步值当前用的多设备，标签删除后，标签里的会话会自动删除。

**参数说明**

| 名称          | 类型    | 必填   | 默认值  | 描述                                       | 版本     |
|--------------|---------|--------|--------|--------------------------------------------|----------|
| tag          | Object  | 是     |        | Tag 对象                                   | 1.7.5    |
| tag.id       | String  | 是     |        | 标签 ID，开发者可自定义，最大长度 64 个字符     | 1.7.5    |

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
let tag = {
  id: 'tag_01'
};

jim.destroyConversationTag(tag).then(() => {
  console.log('destroyConversationTag successfully')
}, (error) => {
  console.log(error)
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