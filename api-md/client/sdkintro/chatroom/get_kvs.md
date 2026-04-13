---
title: Get the specified attribute
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
{ label: 'Hongmeng', value: 'harmony', }
]
}>
<TabItem value="android">

> Coming soon

</TabItem>
<TabItem value="ios">

> Coming soon

</TabItem>
<TabItem value="flutter">

> Coming soon

</TabItem>
<TabItem value="js">

Retrieve the value of a specified attribute from the chat room. This method must be called after successfully joining the chat room. If you attempt to get the attribute before joining, the SDK will return empty data.

**Parameter Description**

| Name | Type | Required | Default | Description | Version |
|-------------------------|---------|----------|---------|--------------------------------------------|----------|
| chatroom | Object | Yes | None | Chatroom object | 1.6.0 |
| chatroom.id | String | Yes | None | Chatroom ID | 1.6.0 |
| chatroom.attributes | Array | Yes | None | List of chat room attributes; see sample code for data structure | 1.6.0 |

**Callback Description**

| Properties | Type | Description | Version |
|---------------------|---------|--------------------------------------------|----------|
| chatroom | Object | Chatroom object | 1.6.0 |
| chatroom.id | String | Chatroom ID | 1.6.0 |
| chatroom.attributes | Array | All attributes of the chat room; see sample code for data structure | 1.6.0 |

**Sample Code**

```js
let chatroom = {
  id: 'chatroom1001',
  attributes: [ { key: 'name' }, { key: 'age' } ]
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
  console.log('error', error);
});
```

</TabItem>
<TabItem value="reactnative">

> Coming soon

</TabItem>
<TabItem value="harmony">

> Coming soon

</TabItem>
</Tabs>