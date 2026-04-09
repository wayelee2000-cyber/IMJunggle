---
title: 用户信息
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

**用户信息结构**

UserInfo 是 SDK 封装的用户信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| userId  | String | 用户 id                | 1.0.0 |
| userName | String      | 用户名字         | 1.0.0 |
| portrait   | String           | 用户头像 URL           | 1.0.0 |
| extra    | Map<String, String>   | 扩展字段 | 1.0.0 |
| updatedTime         | long       | 更新时间戳                | 1.0.0 |

**获取用户信息**

```java
//接口定义

/**
 * 获取用户信息
 * @param userId 用户 id
 * @return 用户信息
 */
UserInfo getUserInfo(String userId);
```

```java
//示例代码
UserInfo userInfo = JIM.getInstance().getUserInfoManager().getUserInfo("userId");
```

**批量获取用户信息**

```java
//接口定义

/**
 * 批量获取用户信息
 * @param userIdList 用户 id 列表
 * @return 用户信息列表
 */
List<UserInfo> getUserInfoList(List<String> userIdList);
```

```java
//示例代码
List<String> userIdList = new ArrayList<>();
userIdList.add("userId1");
userIdList.add("userId2");
List<UserInfo> userInfoList = JIM.getInstance().getUserInfoManager().getUserInfoList(userIdList);
```

**从服务端获取最新的用户信息**

```java
//接口定义
/**
 * 从服务端获取最新的用户信息
 * @param userId 用户 id
 * @param callback 结果回调
 */
void fetchUserInfo(String userId, JIMConst.IResultCallback<UserInfo> callback);

```

```java
//示例代码
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

**用户信息结构**

JUserInfo 是 SDK 封装的用户信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| userId  | NSString | 用户 id                | 1.0.0 |
| userName | NSString      | 用户名字         | 1.0.0 |
| portrait   | NSString           | 用户头像 URL           | 1.0.0 |
| extraDic    | NSDictionary <NSString *, NSString *>   | 扩展字段 | 1.0.0 |
| updatedTime         | long long      | 更新时间戳                | 1.0.0 |

**获取用户信息**

```objectivec
//接口定义

/// 获取用户信息
/// - Parameter userId: 用户 id
- (JUserInfo *)getUserInfo:(NSString *)userId;
```

```objectivec
//示例代码
JUserInfo *userInfo = [JIM.shared.userInfoManager getUserInfo:@"userId1"];
```

**批量获取用户信息**

```objectivec
//接口定义

/// 批量获取用户信息
/// - Parameter userIdList: 用户 id 列表
- (NSArray <JUserInfo *> *)getUserInfoList:(NSArray <NSString *> *)userIdList;
```

```objectivec
//示例代码
NSArray <JUserInfo *> *userInfoList = [JIM.shared.userInfoManager getUserInfoList:@[@"userId1", @"userId2"]];
```

**从服务端获取最新的用户信息**

```objectivec
//接口定义

/// 从服务端获取最新的用户信息
/// - Parameters:
///   - userId: 用户 id
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)fetchUserInfo:(NSString *)userId
              success:(void (^)(JUserInfo *userInfo))successBlock
                error:(void (^)(JErrorCode code))errorBlock;
```

```objectivec
//示例代码
[JIM.shared.userInfoManager fetchUserInfo:@"userId"
                                  success:^(JUserInfo *userInfo) {
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">



</TabItem>

<TabItem value="flutter">

**用户信息结构**

UserInfo 是 SDK 封装的用户信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| userId  | String | 用户 id                | 1.0.0 |
| userName | String      | 用户名字         | 1.0.0 |
| portrait   | String           | 用户头像 URL           | 1.0.0 |
| extraMap    | Map<String, String>?   | 扩展字段 | 1.0.0 |

**获取用户信息**

```dart
//接口定义

/**
 * 获取用户信息
 * @param userId 用户 id
 * @return 用户信息
 */
Future<UserInfo?> getUserInfo(String userId) async
```

```dart
//示例代码
UserInfo? userInfo = await JuggleIm.instance.getUserInfo("userId");
```

</TabItem>

<TabItem value="reactnative">



</TabItem>

</Tabs>