---
title: 数据结构
hide_title: true
sidebar_position: 0
---

<Tabs
groupId="sdks-language"
values={[
{ label: 'Android', value: 'android', },
{ label: 'iOS', value: 'ios', },
{ label: 'JavaScript', value: 'js', },
{ label: 'Flutter', value: 'flutter', },
{ label: 'ReactNative', value: 'reactnative', },
]
}>
<TabItem value="android">

**Moment 结构**

| 属性名                          | 类型         | 说明                                                | 版本   |
|---------------------------------|--------------|-----------------------------------------------------|--------|
| momentId                        | String       | 朋友圈 ID，全局唯一                                  | 1.8.30  |
| content                   | String       | 朋友圈的文字内容                                        | 1.8.30  |
| mediaList                  | `List<MomentMedia>`        | 朋友圈的媒体文件链接列表（图片/视频等），详细请参考下方 `MomentMedia` 结构                  | 1.8.30  |
| userInfo                        | UserInfo       | 发布朋友圈的用户                                     | 1.8.30  |
| commentList                    | `List<MomentComment>`        | 前 20 条评论列表，详细请参考下方 `MomentComment` 结构                  | 1.8.30  |  
| reactionList                       | `List<MomentReaction>`        | 朋友圈的点赞或其他自定义交互列表，详细请参考下方 `MomentReaction` 结构 | 1.8.30  |
| createTime                      | long       | 朋友圈创建时间, 单位: 毫秒                                       | 1.8.30  |  

**MomentMedia 结构**

| 属性名        | 类型         | 说明                                                | 版本   |
|---------------|--------------|-----------------------------------------------------|--------|
| type          | MomentMediaType       | 朋友圈媒体类型                | 1.8.30  |
| url           | String       | 图片朋友圈的原图链接或者视频链接                  | 1.8.30  |
| snapshotUrl   | String       | 图片朋友圈的缩略图，视频朋友圈首帧缩略图                  | 1.8.30  |
| height        | int       | 图片或者视频的高度                  | 1.8.30  |
| width         | int       | 图片或者视频的宽度                  | 1.8.30  |
| duration      | int       | 视频的时长，仅视频朋友圈时有效                  | 1.8.30  |

**MomentComment 结构**

| 属性名               | 类型         | 说明                                                | 版本   |
|----------------------|--------------|-----------------------------------------------------|--------|
| commentId            | String       | 评论唯一标识 Id                                      | 1.8.30  |
| momentId             | String       | 朋友圈 Id                                      | 1.8.30  |
| parentCommentId      | String       | 父评论 Id，回复评论时为回复的评论 Id，无父评论时为空字符串 | 1.8.30  |
| content        | String       | 评论文本内容                                        | 1.8.30  |
| userInfo           | UserInfo       | 评论用户信息               | 1.8.30  |
| parentUserInfo           | UserInfo       | 父评论用户信息（无父评论时为空对象）                | 1.8.30  |
| createTime          | long       | 评论发布时间, 单位: 毫秒                              | 1.8.30  |

**MomentReaction 结构**

| 属性名               | 类型         | 说明                                                | 版本   |
|----------------------|--------------|-----------------------------------------------------|--------|
| key                | String       | 点赞或自定义互动值，例如 `like`、`dislike`、`collect` 等 | 1.8.30  |
| userList            | `List<UserInfo>`       | 点赞操作的用户列表                             | 1.8.30  |

</TabItem>
<TabItem value="ios">

**JMoment 结构**

| 属性名                          | 类型         | 说明                                                | 版本   |
|---------------------------------|--------------|-----------------------------------------------------|--------|
| momentId                        | NSString       | 朋友圈 ID，全局唯一                                  | 1.8.30  |
| content                   | NSString       | 朋友圈的文字内容                                        | 1.8.30  |
| mediaArray                  | `NSArray <JMomentMedia *>`        | 朋友圈的媒体文件链接列表（图片/视频等），详细请参考下方 `JMomentMedia` 结构                  | 1.8.30  |
| userInfo                        | JUserInfo       | 发布朋友圈的用户                                     | 1.8.30  |
| commentArray                    | `NSArray <JMomentComment *>`        | 前 20 条评论列表，详细请参考下方 `JMomentComment` 结构                  | 1.8.30  |  
| reactionArray                       | `NSArray <JMomentReaction *>`        | 朋友圈的点赞或其他自定义交互列表，详细请参考下方 `JMomentReaction` 结构 | 1.8.30  |
| createTime                      | long long     | 朋友圈创建时间, 单位: 毫秒                                       | 1.8.30  |  

**JMomentMedia 结构**

| 属性名        | 类型         | 说明                                                | 版本   |
|---------------|--------------|-----------------------------------------------------|--------|
| type          | JMomentMediaType       | 朋友圈媒体类型                | 1.8.30  |
| url           | NSString       | 图片朋友圈的原图链接或者视频链接                  | 1.8.30  |
| snapshotUrl   | NSString       | 图片朋友圈的缩略图，视频朋友圈首帧缩略图                  | 1.8.30  |
| height        | int       | 图片或者视频的高度                  | 1.8.30  |
| width         | int       | 图片或者视频的宽度                  | 1.8.30  |
| duration      | int       | 视频的时长，仅视频朋友圈时有效                  | 1.8.30  |

**JMomentComment 结构**

| 属性名               | 类型         | 说明                                                | 版本   |
|----------------------|--------------|-----------------------------------------------------|--------|
| commentId            | NSString       | 评论唯一标识 Id                                      | 1.8.30  |
| momentId             | NSString       | 朋友圈 Id                                      | 1.8.30  |
| parentCommentId      | NSString       | 父评论 Id，回复评论时为回复的评论 Id，无父评论时为空字符串 | 1.8.30  |
| content        | NSString       | 评论文本内容                                        | 1.8.30  |
| userInfo           | JUserInfo       | 评论用户信息               | 1.8.30  |
| parentUserInfo           | JUserInfo       | 父评论用户信息（无父评论时为空对象）                | 1.8.30  |
| createTime          | long       | 评论发布时间, 单位: 毫秒                              | 1.8.30  |

**JMomentReaction 结构**

| 属性名               | 类型         | 说明                                                | 版本   |
|----------------------|--------------|-----------------------------------------------------|--------|
| key                | NSString       | 点赞或自定义互动值，例如 `like`、`dislike`、`collect` 等 | 1.8.30  |
| userArray            | `NSArray <JUserInfo *>`       | 点赞操作的用户列表                             | 1.8.30  |

</TabItem>
<TabItem value="flutter">

**Moment 结构**

| 属性名                          | 类型         | 默认值       | 说明                                                | 版本   |
|---------------------------------|--------------|--------------|-----------------------------------------------------|--------|
| momentId                        | String       | ''           | 朋友圈 ID，全局唯一                                  | 0.0.66  |
| content                    | String       | ''            | 朋友圈的文字内容                                        | 0.0.66  |
| mediaList                  | `List<MomentMedia>`        | []           | 朋友圈的媒体文件链接列表（图片/视频等），详细请参考下方 `MomentMedia` 结构                  | 0.0.66  |
| userInfo                         | UserInfo?       | -            | 发布朋友圈的用户                                   | 0.0.66  |
| commentList                     | `List<MomentComment>`        | []           | 前 20 条评论列表，详细请参考下方 `MomentComment` 结构                  | 0.0.66  |  
| reactionList                       | `List<MomentReaction>`        | []           | 朋友圈的点赞或其他自定义交互列表，详细请参考下方 `MomentReaction` 结构 | 0.0.66  |
| createTime                      | int       | 0            | 朋友圈创建时间, 单位: 毫秒                                       | 0.0.66  |  

**MomentMedia 结构**

| 属性名        | 类型         | 默认值       | 说明                                                | 版本   |
|---------------|--------------|--------------|-----------------------------------------------------|--------|
| type          | int       | 0            | 0: IMAGE; 1: VIDEO                  | 0.0.66  |
| url           | String       | ''            | 图片朋友圈的原图链接或者视频链接                  | 0.0.66  |
| snapshotUrl   | String       | ''            | 图片朋友圈的缩略图，视频朋友圈首帧缩略图                  | 0.0.66  |
| height        | int       | 0            | 图片或者视频的高度                  | 0.0.66  |
| width         | int       | 0            | 图片或者视频的宽度                  | 0.0.66  |
| duration      | int       | 0            | 视频的时长，仅视频朋友圈时有效                  | 0.0.66  |

**MomentComment 结构**

| 属性名               | 类型         | 默认值       | 说明                                                | 版本   |
|----------------------|--------------|--------------|-----------------------------------------------------|--------|
| commentId            | String       | ''            | 评论唯一标识 Id                                      | 0.0.66  |
| momentId             | String       | ''            | 朋友圈 Id                                      | 0.0.66  |
| parentCommentId      | String       | ''           | 父评论 Id，回复评论时为回复的评论 Id，无父评论时为空字符串 | 0.0.66  |
| content         | String       | ''            | 评论文本内容                                        | 0.0.66  |
| userInfo           | UserInfo?       | -           | 评论用户信息              | 0.0.66  |
| parentUserInfo           | UserInfo?       | -           | 父评论用户信息（无父评论时为空对象）                | 0.0.66  |
| createTime          | int       | 0           | 评论发布时间, 单位: 毫秒                              | 0.0.66  |

**MomentReaction 结构**

| 属性名               | 类型         | 默认值       | 说明                                                | 版本   |
|----------------------|--------------|--------------|-----------------------------------------------------|--------|
| key                | String       | ''           | 点赞或自定义互动值，例如 `like`、`dislike`、`collect` 等 | 0.0.66  |
| userList          | `List<UserInfo>`       | []           | 点赞操作的用户列表                                     | 0.0.66  |

</TabItem>
<TabItem value="reactnative">

**Moment 结构**

| 属性名                          | 类型         | 默认值       | 说明                                                | 版本   |
|---------------------------------|--------------|--------------|-----------------------------------------------------|--------|
| momentId                        | string       | ''           | 朋友圈 ID，全局唯一                                  | -   |
| content                    | string       | ''            | 朋友圈的文字内容                                        | -   |
| mediaList                  | `MomentMedia[]`        | []           | 朋友圈的媒体文件链接列表（图片/视频等），详细请参考下方 `MomentMedia` 结构                  | -   |
| userInfo                         | UserInfo?       | -            | 发布朋友圈的用户                                   | -   |
| commentList                     | `MomentComment[]`        | []           | 前 20 条评论列表，详细请参考下方 `MomentComment` 结构                  | -   |
| reactionList                       | `MomentReaction[]`        | []           | 朋友圈的点赞或其他自定义交互列表，详细请参考下方 `MomentReaction` 结构 | -   |
| createTime                      | number       | 0            | 朋友圈创建时间, 单位: 毫秒                                       | -   |

**MomentMedia 结构**

| 属性名        | 类型         | 默认值       | 说明                                                | 版本   |
|---------------|--------------|--------------|-----------------------------------------------------|--------|
| type          | number       | 0            | 0: IMAGE; 1: VIDEO                  | -   |
| url           | string       | ''            | 图片朋友圈的原图链接或者视频链接                  | -   |
| snapshotUrl   | string       | ''            | 图片朋友圈的缩略图，视频朋友圈首帧缩略图                  | -   |
| height        | number       | 0            | 图片或者视频的高度                  | -   |
| width         | number       | 0            | 图片或者视频的宽度                  | -   |
| duration      | number       | 0            | 视频的时长，仅视频朋友圈时有效                  | -   |

**MomentComment 结构**

| 属性名               | 类型         | 默认值       | 说明                                                | 版本   |
|----------------------|--------------|--------------|-----------------------------------------------------|--------|
| commentId            | string       | ''            | 评论唯一标识 Id                                      | -   |
| momentId             | string       | ''            | 朋友圈 Id                                      | -   |
| parentCommentId      | string       | ''           | 父评论 Id，回复评论时为回复的评论 Id，无父评论时为空字符串 | -   |
| content         | string       | ''            | 评论文本内容                                        | -   |
| userInfo           | UserInfo?       | -           | 评论用户信息              | -   |
| parentUserInfo           | UserInfo?       | -           | 父评论用户信息（无父评论时为空对象）                | -   |
| createTime          | number       | 0           | 评论发布时间, 单位: 毫秒                              | -   |

**MomentReaction 结构**

| 属性名               | 类型         | 默认值       | 说明                                                | 版本   |
|----------------------|--------------|--------------|-----------------------------------------------------|--------|
| key                | string       | ''           | 点赞或自定义互动值，例如 `like`、`dislike`、`collect` 等 | -   |
| userList          | `UserInfo[]`       | []           | 点赞操作的用户列表                                     | -   |

</TabItem>
<TabItem value="js">

**Moment 结构**

| 属性名                          | 类型         | 默认值       | 说明                                                | 版本   |
|---------------------------------|--------------|--------------|-----------------------------------------------------|--------|
| momentId                        | String       | -            | 朋友圈 ID，全局唯一                                  | 1.9.6  |
| content.text                    | String       | -            | 朋友圈的文字内容                                        | 1.9.6  |
| content.medias                  | Array        | []           | 朋友圈的媒体文件链接列表（图片/视频等），详细请参考下方 `Media` 结构                  | 1.9.6  |
| user.id                         | String       | -            | 发布朋友圈的用户 Id                                      | 1.9.6  |
| user.avatar                     | String       | -            | 发布朋友圈的用户头像                                         | 1.9.6  |
| user.name                       | String       | -            | 发布朋友圈的用户名                                         | 1.9.6  |
| topComments                     | Array        | []           | 前 20 条评论列表，详细请参考下方 `Comment` 结构                  | 1.9.6  |  
| reactions                       | Array        | []           | 朋友圈的点赞或其他自定义交互列表，详细请参考下方 `Reaction` 结构 | 1.9.6  |
| momentTime                      | Number       | -            | 朋友圈创建时间, 单位: 毫秒                                       | 1.9.6  |  

**Media 结构**

| 属性名        | 类型         | 默认值       | 说明                                                | 版本   |
|---------------|--------------|--------------|-----------------------------------------------------|--------|
| type          | String       | -            | [朋友圈媒体类型](../../enum/web#moment_type)                  | 1.9.6  |
| url           | String       | -            | 图片朋友圈的原图链接或者视频链接                  | 1.9.6  |
| snapshotUrl   | String       | -            | 图片朋友圈的缩略图，视频朋友圈首帧缩略图                  | 1.9.6  |
| height        | Number       | -            | 图片或者视频的高度                  | 1.9.6  |
| width         | Number       | -            | 图片或者视频的宽度                  | 1.9.6  |
| duration      | Number       | -            | 视频的时长，仅视频朋友圈时有效                  | 1.9.6  |

**Comment 结构**

| 属性名               | 类型         | 默认值       | 说明                                                | 版本   |
|----------------------|--------------|--------------|-----------------------------------------------------|--------|
| commentId            | String       | -            | 评论唯一标识 Id                                      | 1.9.6  |
| momentId             | String       | -            | 朋友圈 Id                                      | 1.9.6  |
| parentCommentId      | String       | ""           | 父评论 Id，回复评论时为回复的评论 Id，无父评论时为空字符串 | 1.9.6  |
| content.text         | String       | -            | 评论文本内容                                        | 1.9.6  |
| parentUser           | Object       | {}           | 父评论用户信息（无父评论时为空对象）                | 1.9.6  |
| user.avatar          | String       | -            | 评论用户头像 URL                                    | 1.9.6  |
| user.id              | String       | -            | 评论用户唯一标识 Id                                 | 1.9.6  |
| user.name            | String       | -            | 评论用户名                                          | 1.9.6  |
| commentTime          | Number       | -            | 评论发布时间, 单位: 毫秒                              | 1.9.6  |

**Reaction 结构**

| 属性名               | 类型         | 默认值       | 说明                                                | 版本   |
|----------------------|--------------|--------------|-----------------------------------------------------|--------|
| value                | String       | -            | 点赞或自定义互动值，例如 `like`、`dislike`、`collect` 等 | 1.9.6  |
| timestamp            | Number       | -            | 点赞操作时间戳, 单位: 毫秒                              | 1.9.6  |
| user.avatar          | String       | -            | 点赞用户头像 URL                                    | 1.9.6  |
| user.id              | String       | -            | 点赞用户 Id                                  | 1.9.6  |
| user.name            | String       | -            | 点赞用户名                                          | 1.9.6  |

</TabItem>
</Tabs>