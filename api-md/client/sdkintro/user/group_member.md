---
title: Group member information
hide_title: true
sidebar_position: 3
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

**Group Member Information Structure**

`GroupMember` is an object representing group member information encapsulated by the SDK.

| Attribute name     | Type               | Description               | Version |
| ------------------ | ------------------ | ------------------------- | ------- |
| groupId            | String             | Group ID                  | 1.0.0   |
| userId             | String             | User ID                   | 1.0.0   |
| groupDisplayName   | String             | User's nickname in the group | 1.0.0   |
| extra              | Map<String, String> | Extension fields          | 1.0.0   |
| updatedTime        | long               | Update timestamp          | 1.0.0   |

**Get Group Member Information**

```java
// Interface definition

/**
 * Get group member information
 * @param groupId Group ID
 * @param userId User ID
 * @return Group member information
 */
GroupMember getGroupMember(String groupId, String userId);
```

```java
// Sample code
GroupMember member = JIM.getInstance().getUserInfoManager().getGroupMember("groupId", "userId");
```

</TabItem>

<TabItem value="ios">

**Group Member Information Structure**

`JGroupMember` is an object representing group member information encapsulated by the SDK.

| Attribute name     | Type                          | Description               | Version |
| ------------------ | -----------------------------| ------------------------- | ------- |
| groupId            | NSString                      | Group ID                  | 1.0.0   |
| userId             | NSString                      | User ID                   | 1.0.0   |
| groupDisplayName   | NSString                      | User's nickname in the group | 1.0.0   |
| extraDic           | NSDictionary<NSString *, NSString *> | Extension fields          | 1.0.0   |
| updatedTime        | long long                    | Update timestamp          | 1.0.0   |

**Get Group Member Information**

```objectivec
// Interface definition

/// Get group member information
/// - Parameters:
///   - groupId: Group ID
///   - userId: User ID
- (JGroupMember *)getGroupMember:(NSString *)groupId
                          userId:(NSString *)userId;
```

```objectivec
// Sample code
JGroupMember *member = [JIM.shared.userInfoManager getGroupMember:@"groupId" userId:@"userId"];
```

</TabItem>
<TabItem value="js">

</TabItem>

<TabItem value="flutter">

**Group Member Information Structure**

`GroupMember` is an object representing group member information encapsulated by the SDK.

| Attribute name     | Type                 | Description               | Version |
| ------------------ | -------------------- | ------------------------- | ------- |
| groupId            | String               | Group ID                  | 1.0.0   |
| userId             | String               | User ID                   | 1.0.0   |
| groupDisplayName   | String               | User's nickname in the group | 1.0.0   |
| extraMap           | Map<String, String>?  | Extension fields          | 1.0.0   |
| updatedTime        | long                 | Update timestamp          | 1.0.0   |

**Get Group Member Information**

```dart
// Interface definition

/**
 * Get group member information
 * @param groupId Group ID
 * @param userId User ID
 * @return Group member information
 */
Future<GroupMember?> getGroupMember(String groupId, String userId) async
```

```dart
// Sample code
GroupMember? member = await JuggleIm.instance.getGroupMember("groupId", "userId");
```

</TabItem>

<TabItem value="reactnative">

</TabItem>

</Tabs>