---
title: 清空会话未读总数
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

**示例代码**

```java
JIM.getInstance().getConversationManager().clearTotalUnreadCount(new IConversationManager.ISimpleCallback() {
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

**示例代码**

```objectivec
[JIM.shared.conversationManager clearTotalUnreadCount:^{
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">

**示例代码**
```js
jim.clearTotalUnreadcount().then(() => {
  console.log('clear total unreadcount successfully');
})
```
</TabItem>
<TabItem value="flutter">

**示例代码**

```dart
Result result = await JuggleIm.instance.clearTotalUnreadCount();
```

</TabItem>
<TabItem value="reactnative">

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

await JuggleIM.clearTotalUnreadCount();
```

</TabItem>
<TabItem value="harmony">

**示例代码**

```java
JuggleIm.instance.getConversationManager().clearTotalUnreadCount((code)=>{

})
```

</TabItem>
</Tabs>