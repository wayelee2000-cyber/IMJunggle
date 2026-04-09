---
title: 获取标签列表
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

获取当前用户创建的标签列表

![](./tag.png)

**成功回调**

无参数返回，回调触发表示成功

**失败回调**

| 名称   | 类型    | 描述                                                      | 版本   |
|--------|---------|-----------------------------------------------------------|--------|
| error  | Object  | 发送失败后会有对应的状态码，可以直接查看 `error.msg`，或者查看 [状态码](../../../../sdkintro/status_code/web) | 1.0.0  |

**示例代码**
```js
jim.getConversationTags().then(({ tags }) => {
  /* tags =>  [{ id: 'tag_01', name: '我的关注' }, ... ] */
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