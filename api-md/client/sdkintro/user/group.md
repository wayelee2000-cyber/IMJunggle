---
title: 群组信息
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

**群组信息结构**

GroupInfo 是 SDK 封装的群组信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| groupId  | String | 群组 id                | 1.0.0 |
| groupName | String      | 群组名字         | 1.0.0 |
| portrait   | String           | 群组头像 URL           | 1.0.0 |
| extra    | Map<String, String>   | 扩展字段 | 1.0.0 |
| updatedTime         | long       | 更新时间戳                | 1.0.0 |

**获取群组信息**

```java
//接口定义

/**
 * 获取群组信息
 * @param groupId 群组 id
 * @return 群组信息
 */
GroupInfo getGroupInfo(String groupId);
```

```java
//示例代码
GroupInfo groupInfo = JIM.getInstance().getUserInfoManager().getGroupInfo("groupId");
```

**批量获取群组信息**

```java
//接口定义

/**
 * 批量获取群组信息
 * @param groupIdList 群组 id 列表
 * @return 群组信息列表
 */
List<GroupInfo> getGroupInfoList(List<String> groupIdList);
```

```java
//示例代码
GroupInfo groupInfo = JIM.getInstance().getUserInfoManager().getGroupInfo("groupId");
List<String> groupIdList = new ArrayList<>();
groupIdList.add("groupId1");
groupIdList.add("groupId2");
List<GroupInfo> groupInfoList = JIM.getInstance().getUserInfoManager().getGroupInfoList(groupIdList);
```

**从服务端获取最新的群组信息**

```java
//接口定义
/**
 * 从服务端获取最新的群组信息
 * @param groupId 群组 id
 * @param callback 结果回调
 */
void fetchGroupInfo(String groupId, JIMConst.IResultCallback<GroupInfo> callback);

```

```java
//示例代码
JIM.getInstance().getUserInfoManager().fetchGroupInfo("groupId", new JIMConst.IResultCallback<GroupInfo>() {
    @Override
    public void onSuccess(GroupInfo groupInfo) {
        
    }

    @Override
    public void onError(int errorCode) {

    }
});
```

</TabItem>

<TabItem value="ios">

**群组信息结构**

JGroupInfo 是 SDK 封装的群组信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| groupId  | NSString | 群组 id                | 1.0.0 |
| groupName | NSString      | 群组名字         | 1.0.0 |
| portrait   | NSString           | 群组头像 URL           | 1.0.0 |
| extraDic    | NSDictionary <NSString *, NSString *>  | 扩展字段 | 1.0.0 |
| updatedTime         | long long       | 更新时间戳                | 1.0.0 |

**获取群组信息**

```objectivec
//接口定义

/// 获取群组信息
/// - Parameter groupId: 群组 id
- (JGroupInfo *)getGroupInfo:(NSString *)groupId;
```

```objectivec
//示例代码
JGroupInfo *groupInfo = [JIM.shared.userInfoManager getGroupInfo:@"groupId"];
```

**批量获取群组信息**

```objectivec
//接口定义

/// 批量获取群组信息
/// - Parameter groupIdList: 群组 id 列表
- (NSArray <JGroupInfo *> *)getGroupInfoList:(NSArray <NSString *> *)groupIdList;
```

```objectivec
//示例代码
NSArray <JGroupInfo *> *groupInfoList = [JIM.shared.userInfoManager getGroupInfoList:@[@"groupId1", @"groupId2"]];
```

**从服务端获取最新的群组信息**

```objectivec
//接口定义

/// 从服务端获取最新的群组信息
/// - Parameters:
///   - groupId: 群组 id
///   - successBlock: 成功回调
///   - errorBlock: 失败回调
- (void)fetchGroupInfo:(NSString *)groupId
               success:(void (^)(JGroupInfo *groupInfo))successBlock
                 error:(void (^)(JErrorCode code))errorBlock;
```

```objectivec
//示例代码
[JIM.shared.userInfoManager fetchGroupInfo:@"groupId"
                                   success:^(JGroupInfo *groupInfo) {
    
} error:^(JErrorCode code) {
    
}];
```

</TabItem>
<TabItem value="js">



</TabItem>

<TabItem value="flutter">

**群组信息结构**

GroupInfo 是 SDK 封装的群组信息对象。

| 属性名        | 类型          | 说明                       | 版本  |
| ------------- | ------------- | -------------------------- | ----- |
| groupId  | String | 群组 id                | 1.0.0 |
| groupName | String      | 群组名字         | 1.0.0 |
| portrait   | String           | 群组头像 URL           | 1.0.0 |
| extraMap    | Map<String, String>?   | 扩展字段 | 1.0.0 |

**获取群组信息**

```dart
//接口定义

/**
 * 获取群组信息
 * @param groupId 群组 id
 * @return 群组信息
 */
Future<GroupInfo?> getGroupInfo(String groupId) async
```

```dart
//示例代码
GroupInfo? groupInfo = await JuggleIm.instance.getGroupInfo("groupId");
```

</TabItem>

<TabItem value="reactnative">



</TabItem>

</Tabs>