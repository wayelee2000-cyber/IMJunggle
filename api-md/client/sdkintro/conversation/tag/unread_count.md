---
title: Get the number of unread messages of the label
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

Retrieve the total number of unread messages across all conversations under the specified label.

**Interface definition**

```java
/**
 * Get the total number of unread messages based on the tag ID.
 * @param tagId The tag ID.
 * @return The total number of unread messages.
 */
int getUnreadCountWithTag(String tagId);
```


</TabItem>
<TabItem value="ios">

Retrieve the total number of unread messages based on the tag ID.

**Interface definition**

```objectivec
/// Get the total number of unread messages based on the tag ID.
/// - Parameter tagId: The tag ID.
- (int)getUnreadCountWithTag:(NSString *)tagId;
```

</TabItem>
<TabItem value="js">

> Not yet provided

</TabItem>
<TabItem value="flutter" label="Flutter">

> Not yet provided

</TabItem>
<TabItem value="reactnative">

Retrieve the total number of unread messages across all conversations under the specified label.

**Interface definition**

```typescript
/**
 * Get the number of unread messages for a tag.
 * @param conversationTypes Optional list of conversation types.
 */
getUnreadCountWithTypes(conversationTypes?: number[]): Promise<number>;
```

**Sample Code**

```javascript
import JuggleIM from 'juggleim-rnsdk';

// Get the total number of unread messages for all sessions
const count = await JuggleIM.getUnreadCountWithTypes();

// Get the total number of unread messages for sessions of the specified type
const count = await JuggleIM.getUnreadCountWithTypes([1]);
```

</TabItem>
</Tabs>