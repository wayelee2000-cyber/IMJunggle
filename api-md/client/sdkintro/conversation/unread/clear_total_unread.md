---
title: Clear the total number of unread sessions
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

**Sample Code**

```java
JIM.getInstance().getConversationManager().clearTotalUnreadCount(new IConversationManager.ISimpleCallback() {
    @Override
    public void onSuccess() {
        // Successfully cleared total unread count
    }

    @Override
    public void onError(int errorCode) {
        // Handle error
    }
});
```

</TabItem>
<TabItem value="ios">

**Sample Code**

```objectivec
[JIM.shared.conversationManager clearTotalUnreadCount:^{
    // Successfully cleared total unread count
} error:^(JErrorCode code) {
    // Handle error
}];
```

</TabItem>
<TabItem value="js">

**Sample Code**
```js
jim.clearTotalUnreadCount().then(() => {
  console.log('Successfully cleared total unread count');
});
```
</TabItem>
<TabItem value="flutter">

**Sample Code**

```dart
Result result = await JuggleIm.instance.clearTotalUnreadCount();
```

</TabItem>
<TabItem value="reactnative">

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.clearTotalUnreadCount();
```

</TabItem>
<TabItem value="harmony">

**Sample Code**

```java
JuggleIm.instance.getConversationManager().clearTotalUnreadCount((code) -> {
    // Handle callback
});
```

</TabItem>
</Tabs>