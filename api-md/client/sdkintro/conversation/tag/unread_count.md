---
title: 获取标签未读消息数
hide_title: true
sidebar_position: 4
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

获取标签下所有会话的未读消息总数。

**接口定义**

```java
/**
 * 根据标签 id 获取消息未读总数
 * @param tagId 标签 id
 * @return 消息未读总数
 */
int getUnreadCountWithTag(String tagId);
```


</TabItem>
<TabItem value="ios">

获取标签下的会话列表，支持分页获取。

**接口定义**

```objectivec
/// 根据标签 id 获取消息未读总数
/// - Parameter tagId: 标签 id
- (int)getUnreadCountWithTag:(NSString *)tagId;
```

</TabItem>
<TabItem value="js">

> 暂未提供

</TabItem>
<TabItem value="flutter" label="Flutter">

> 暂未提供

</TabItem>
<TabItem value="reactnative">

获取标签下所有会话的未读消息总数。

**接口定义**

```typescript
/**
 * 获取标签未读消息数
 * @param conversationTypes 会话类型列表，可选
 */
getUnreadCountWithTypes(conversationTypes?: number[]): Promise<number>;
```

**示例代码**

```javascript
import JuggleIM from 'juggleim-rnsdk';

// 获取全部会话的未读总数
const count = await JuggleIM.getUnreadCountWithTypes();

// 获取指定类型会话的未读总数
const count = await JuggleIM.getUnreadCountWithTypes([1]);
```

</TabItem>
</Tabs>