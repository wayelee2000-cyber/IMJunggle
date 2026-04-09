---
title: 群组成员信息
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

**群组成员信息结构**

GroupMember 是 SDK 封装的群组成员信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| groupId  | String | 群组 id                | 1.0.0 |
| userId | String      | 用户名 id        | 1.0.0 |
| groupDisplayName   | String           | 用户在群里的昵称          | 1.0.0 |
| extra    | Map<String, String>   | 扩展字段 | 1.0.0 |
| updatedTime         | long       | 更新时间戳                | 1.0.0 |

**获取群组成员信息**

```java
//接口定义

/**
 * 获取群成员
 * @param groupId 群组 id
 * @param userId 用户 id
 * @return 群成员信息
 */
GroupMember getGroupMember(String groupId, String userId);
```

```java
//示例代码
GroupMember member = JIM.getInstance().getUserInfoManager().getGroupMember("groupId", "userId");
```

</TabItem>

<TabItem value="ios">

**群组成员信息结构**

JGroupMember 是 SDK 封装的群组成员信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| groupId  | NSString | 群组 id                | 1.0.0 |
| userId | NSString      | 用户名 id        | 1.0.0 |
| groupDisplayName   | NSString           | 用户在群里的昵称          | 1.0.0 |
| extraDic    | NSDictionary <NSString *, NSString *>   | 扩展字段 | 1.0.0 |
| updatedTime         | long long      | 更新时间戳                | 1.0.0 |

**获取群组成员信息**

```objectivec
//接口定义

/// 获取群成员信息
/// - Parameters:
///   - groupId: 群组 id
///   - userId: 用户 id
- (JGroupMember *)getGroupMember:(NSString *)groupId
                          userId:(NSString *)userId;
```

```objectivec
//示例代码
JGroupMember *member = [JIM.shared.userInfoManager getGroupMember:@"groupId" userId:@"userId"];
```


</TabItem>
<TabItem value="js">



</TabItem>

<TabItem value="flutter">

**群组成员信息结构**

GroupMember 是 SDK 封装的群组成员信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| groupId  | String | 群组 id                | 1.0.0 |
| userId | String      | 用户名 id        | 1.0.0 |
| groupDisplayName   | String           | 用户在群里的昵称          | 1.0.0 |
| extraMap    | Map<String, String>?   | 扩展字段 | 1.0.0 |
| updatedTime         | long       | 更新时间戳                | 1.0.0 |

**获取群组成员信息**

```dart
//接口定义

/**
 * 获取群成员
 * @param groupId 群组 id
 * @param userId 用户 id
 * @return 群成员信息
 */
Future<GroupMember?> getGroupMember(String groupId, String userId) async
```

```dart
//示例代码
GroupMember? member = await JuggleIm.instance.getGroupMember("groupId", "userId");
```


</TabItem>

<TabItem value="reactnative">



</TabItem>

</Tabs>