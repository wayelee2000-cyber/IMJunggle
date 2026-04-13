---
title: group information
hide_title: true
sidebar_position: 2
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

**Group Information Structure**

GroupInfo is the group information object encapsulated by the SDK.

| Attribute name | Type | Description | Version |
| ------------- | ------------- | -------------------------- | ----- |
| groupId | String | Group ID | 1.0.0 |
| groupName | String | Group name | 1.0.0 |
| portrait | String | Group avatar URL | 1.0.0 |
| extra | Map<String, String> | Extension fields | 1.0.0 |
| updatedTime | long | Update timestamp | 1.0.0 |

**Get Group Information**

```java
// Interface definition

/**
 * Get group information
 * @param groupId Group ID
 * @return Group information
 */
GroupInfo getGroupInfo(String groupId);
```

```java
// Sample code
GroupInfo groupInfo = JIM.getInstance().getUserInfoManager().getGroupInfo("groupId");
```

**Get Group Information in Batches**

```java
// Interface definition

/**
 * Get group information in batches
 * @param groupIdList List of group IDs
 * @return List of group information
 */
List<GroupInfo> getGroupInfoList(List<String> groupIdList);
```

```java
// Sample code
List<String> groupIdList = new ArrayList<>();
groupIdList.add("groupId1");
groupIdList.add("groupId2");
List<GroupInfo> groupInfoList = JIM.getInstance().getUserInfoManager().getGroupInfoList(groupIdList);
```

**Fetch the Latest Group Information from the Server**

```java
// Interface definition
/**
 * Fetch the latest group information from the server
 * @param groupId Group ID
 * @param callback Result callback
 */
void fetchGroupInfo(String groupId, JIMConst.IResultCallback<GroupInfo> callback);
```

```java
// Sample code
JIM.getInstance().getUserInfoManager().fetchGroupInfo("groupId", new JIMConst.IResultCallback<GroupInfo>() {
    @Override
    public void onSuccess(GroupInfo groupInfo) {
        // Handle success
    }

    @Override
    public void onError(int errorCode) {
        // Handle error
    }
});
```

</TabItem>

<TabItem value="ios">

**Group Information Structure**

JGroupInfo is the group information object encapsulated by the SDK.

| Attribute name | Type | Description | Version |
| ------------- | ------------- | -------------------------- | ----- |
| groupId | NSString | Group ID | 1.0.0 |
| groupName | NSString | Group name | 1.0.0 |
| portrait | NSString | Group avatar URL | 1.0.0 |
| extraDic | NSDictionary<NSString *, NSString *> | Extension fields | 1.0.0 |
| updatedTime | long long | Update timestamp | 1.0.0 |

**Get Group Information**

```objectivec
// Interface definition

/// Get group information
/// - Parameter groupId: Group ID
- (JGroupInfo *)getGroupInfo:(NSString *)groupId;
```

```objectivec
// Sample code
JGroupInfo *groupInfo = [JIM.shared.userInfoManager getGroupInfo:@"groupId"];
```

**Get Group Information in Batches**

```objectivec
// Interface definition

/// Get group information in batches
/// - Parameter groupIdList: List of group IDs
- (NSArray<JGroupInfo *> *)getGroupInfoList:(NSArray<NSString *> *)groupIdList;
```

```objectivec
// Sample code
NSArray<JGroupInfo *> *groupInfoList = [JIM.shared.userInfoManager getGroupInfoList:@[@"groupId1", @"groupId2"]];
```

**Fetch the Latest Group Information from the Server**

```objectivec
// Interface definition

/// Fetch the latest group information from the server
/// - Parameters:
///   - groupId: Group ID
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)fetchGroupInfo:(NSString *)groupId
               success:(void (^)(JGroupInfo *groupInfo))successBlock
                 error:(void (^)(JErrorCode code))errorBlock;
```

```objectivec
// Sample code
[JIM.shared.userInfoManager fetchGroupInfo:@"groupId"
                                   success:^(JGroupInfo *groupInfo) {
    // Handle success
} error:^(JErrorCode code) {
    // Handle error
}];
```

</TabItem>
<TabItem value="js">



</TabItem>

<TabItem value="flutter">

**Group Information Structure**

GroupInfo is the group information object encapsulated by the SDK.

| Attribute name | Type | Description | Version |
| ------------- | ------------- | -------------------------- | ----- |
| groupId | String | Group ID | 1.0.0 |
| groupName | String | Group name | 1.0.0 |
| portrait | String | Group avatar URL | 1.0.0 |
| extraMap | Map<String, String>? | Extension fields | 1.0.0 |

**Get Group Information**

```dart
// Interface definition

/**
 * Get group information
 * @param groupId Group ID
 * @return Group information
 */
Future<GroupInfo?> getGroupInfo(String groupId) async
```

```dart
// Sample code
GroupInfo? groupInfo = await JuggleIm.instance.getGroupInfo("groupId");
```

</TabItem>

<TabItem value="reactnative">



</TabItem>

</Tabs>