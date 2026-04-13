---
title: create label
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

> Not yet provided

</TabItem>
<TabItem value="ios">

> Not yet provided

</TabItem>
<TabItem value="js">

Add a session tag. The session tag is valid only for the current user. The `SDK` will automatically synchronize the tag value across multiple devices currently in use.

![](./tag.png)

**Parameter Description**

| Name     | Type   | Required | Default | Description                                                      | Version |
|----------|--------|----------|---------|------------------------------------------------------------------|---------|
| tag      | Object | Yes      |         | Tag object                                                      | 1.7.5   |
| tag.id   | String | Yes      |         | Tag ID, customizable by the developer, with a maximum length of 64 characters | 1.7.5   |
| tag.name | String | Yes      |         | Tag name, defined by the developer, with a maximum length of 64 characters | 1.7.5   |

**Success Callback**

No parameters are returned. The callback is triggered to indicate success.

**Failure Callback**

| Name  | Type   | Description                                                                                  | Version |
|-------|--------|----------------------------------------------------------------------------------------------|---------|
| error | Object | Contains a corresponding status code when the operation fails. You can check `error.msg` or refer to [Status Code](../../../../sdkintro/status_code/web) | 1.0.0   |

**Sample Code**
```js
let tag = {
  id: 'tag_01',
  name: 'My attention'
};

jim.createConversationTag(tag).then(() => {
  console.log('createConversationTag successfully');
}, (error) => {
  console.log(error);
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