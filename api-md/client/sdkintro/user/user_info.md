---
title: user information
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

**User Information Structure**

UserInfo is the user information object encapsulated by the SDK.

| Attribute name | Type | Description | Version |
| ------------- | ------------- | -------------------------- | ----- |
| userId | String | User ID | 1.0.0 |
| userName | String | User name | 1.0.0 |
| portrait | String | User avatar URL | 1.0.0 |
| extra | Map<String, String> | Extension field | 1.0.0 |
| updatedTime | long | Update timestamp | 1.0.0 |

**Get User Information**

```java
// Interface definition

/**
 * Get user information
 * @param userId User ID
 * @return User information
 */
UserInfo getUserInfo(String userId);
```

```java
// Sample code
UserInfo userInfo = JIM.getInstance().getUserInfoManager().getUserInfo("userId");
```

**Get User Information in Batches**

```java
// Interface definition

/**
 * Obtain user information in batches
 * @param userIdList List of user IDs
 * @return List of user information
 */
List<UserInfo> getUserInfoList(List<String> userIdList);
```

```java
// Sample code
List<String> userIdList = new ArrayList<>();
userIdList.add("userId1");
userIdList.add("userId2");
List<UserInfo> userInfoList = JIM.getInstance().getUserInfoManager().getUserInfoList(userIdList);
```

**Get the Latest User Information from the Server**

```java
// Interface definition
/**
 * Get the latest user information from the server
 * @param userId User ID
 * @param callback Result callback
 */
void fetchUserInfo(String userId, JIMConst.IResultCallback<UserInfo> callback);
```

```java
// Sample code
JIM.getInstance().getUserInfoManager().fetchUserInfo("userId", new JIMConst.IResultCallback<UserInfo>() {
    @Override
    public void onSuccess(UserInfo userInfo) {
        
    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>

<TabItem value="ios">

**User Information Structure**

JUserInfo is the user information object encapsulated by the SDK.

| Attribute name | Type | Description | Version |
| ------------- | ------------- | -------------------------- | ----- |
| userId | NSString | User ID | 1.0.0 |
| userName | NSString | User name | 1.0.0 |
| portrait | NSString | User avatar URL | 1.0.0 |
| extraDic | NSDictionary <NSString *, NSString *> | Extension fields | 1.0.0 |
| updatedTime | long long | Update timestamp | 1.0.0 |

**Get User Information**

```objectivec
// Interface definition

/// Get user information
/// - Parameter userId: User ID
- (JUserInfo *)getUserInfo:(NSString *)userId;
```

```objectivec
// Sample code
JUserInfo *userInfo = [JIM.shared.userInfoManager getUserInfo:@"userId1"];
```

**Get User Information in Batches**

```objectivec
// Interface definition

/// Get user information in batches
/// - Parameter userIdList: List of user IDs
- (NSArray <JUserInfo *> *)getUserInfoList:(NSArray <NSString *> *)userIdList;
```

```objectivec
// Sample code
NSArray <JUserInfo *> *userInfoList = [JIM.shared.userInfoManager getUserInfoList:@[@"userId1", @"userId2"]];
```

**Get the Latest User Information from the Server**

```objectivec
// Interface definition

/// Get the latest user information from the server
/// - Parameters:
///   - userId: User ID
///   - successBlock: Success callback
///   - errorBlock: Failure callback
- (void)fetchUserInfo:(NSString *)userId
              success:(void (^)(JUserInfo *userInfo))successBlock
                error:(void (^)(JErrorCode code))errorBlock;
```

```objectivec
// Sample code
[JIM.shared.userInfoManager fetchUserInfo:@"userId"
                                  success:^(JUserInfo *userInfo) {
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">



</TabItem>

<TabItem value="flutter">

**User Information Structure**

UserInfo is the user information object encapsulated by the SDK.

| Attribute name | Type | Description | Version |
| ------------- | ------------- | -------------------------- | ----- |
| userId | String | User ID | 1.0.0 |
| userName | String | User name | 1.0.0 |
| portrait | String | User avatar URL | 1.0.0 |
| extraMap | Map<String, String>? | Extension fields | 1.0.0 |

**Get User Information**

```dart
// Interface definition

/**
 * Get user information
 * @param userId User ID
 * @return User information
 */
Future<UserInfo?> getUserInfo(String userId) async
```

```dart
// Sample code
UserInfo? userInfo = await JuggleIm.instance.getUserInfo("userId");
```

</TabItem>

<TabItem value="reactnative">



</TabItem>

</Tabs>