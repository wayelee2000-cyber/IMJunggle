---
title: data structure
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

**Moment structure**

| Attribute name | Type | Description | Version |
|----------------------------------|-------------|--------------------------------------------------------|--------|
| momentId | String | Unique global identifier for the Moment | 1.8.30 |
| content | String | Text content of the circle of friends | 1.8.30 |
| mediaList | `List<MomentMedia>` | List of media file links (pictures/videos, etc.) in the circle of friends. See the `MomentMedia` structure below for details | 1.8.30 |
| userInfo | UserInfo | User who posted the circle of friends | 1.8.30 |
| commentList | `List<MomentComment>` | List of the first 20 comments. See the `MomentComment` structure below for details | 1.8.30 |
| reactionList | `List<MomentReaction>` | List of likes or other custom interactions in the circle of friends. See the `MomentReaction` structure below for details | 1.8.30 |
| createTime | long | Creation time of the Moment, in milliseconds | 1.8.30 |

**MomentMedia Structure**

| Attribute name | Type | Description | Version |
|---------------|--------------|-----------------------------------------------------|--------|
| type | MomentMediaType | Type of media in the Moment | 1.8.30 |
| url | String | Original image or video URL in the circle of friends | 1.8.30 |
| snapshotUrl | String | Thumbnail image of the circle of friends; for videos, the first frame thumbnail | 1.8.30 |
| height | int | Height of the image or video | 1.8.30 |
| width | int | Width of the image or video | 1.8.30 |
| duration | int | Duration of the video, valid only for video Moments | 1.8.30 |

**MomentComment structure**

| Attribute name | Type | Description | Version |
|------------------------|--------------|--------------------------------------------------------|--------|
| commentId | String | Unique identifier for the comment | 1.8.30 |
| momentId | String | Identifier of the Moment | 1.8.30 |
| parentCommentId | String | Parent comment ID; when replying to a comment, this is the ID of the comment being replied to. Empty string if no parent comment | 1.8.30 |
| content | String | Text content of the comment | 1.8.30 |
| userInfo | UserInfo | Information about the user who made the comment | 1.8.30 |
| parentUserInfo | UserInfo | Information about the parent comment's user (empty object if no parent comment) | 1.8.30 |
| createTime | long | Timestamp when the comment was posted, in milliseconds | 1.8.30 |

**MomentReaction structure**

| Attribute name | Type | Description | Version |
|------------------------|--------------|--------------------------------------------------------|--------|
| key | String | Like or custom interaction type, e.g., `like`, `dislike`, `collect` | 1.8.30 |
| userList | `List<UserInfo>` | List of users who performed the interaction | 1.8.30 |

</TabItem>
<TabItem value="ios">

**JMoment structure**

| Attribute name | Type | Description | Version |
|----------------------------------|-------------|--------------------------------------------------------|--------|
| momentId | NSString | Unique global identifier for the Moment | 1.8.30 |
| content | NSString | Text content of the circle of friends | 1.8.30 |
| mediaArray | `NSArray <JMomentMedia *>` | List of media file links (pictures/videos, etc.) in the circle of friends. See the `JMomentMedia` structure below for details | 1.8.30 |
| userInfo | JUserInfo | User who posted the Moment | 1.8.30 |
| commentArray | `NSArray <JMomentComment *>` | List of the first 20 comments. See the `JMomentComment` structure below for details | 1.8.30 |
| reactionArray | `NSArray <JMomentReaction *>` | List of likes or other custom interactions in the circle of friends. See the `JMomentReaction` structure below for details | 1.8.30 |
| createTime | long long | Creation time of the Moment, in milliseconds | 1.8.30 |

**JMomentMedia structure**

| Attribute name | Type | Description | Version |
|---------------|--------------|-----------------------------------------------------|--------|
| type | JMomentMediaType | Type of media in the Moment | 1.8.30 |
| url | NSString | Original image or video URL in the circle of friends | 1.8.30 |
| snapshotUrl | NSString | Thumbnail image of the circle of friends; for videos, the first frame thumbnail | 1.8.30 |
| height | int | Height of the image or video | 1.8.30 |
| width | int | Width of the image or video | 1.8.30 |
| duration | int | Duration of the video, valid only for video Moments | 1.8.30 |

**JMomentComment structure**

| Attribute name | Type | Description | Version |
|------------------------|--------------|--------------------------------------------------------|--------|
| commentId | NSString | Unique identifier for the comment | 1.8.30 |
| momentId | NSString | Identifier of the Moment | 1.8.30 |
| parentCommentId | NSString | Parent comment ID; when replying to a comment, this is the ID of the comment being replied to. Empty string if no parent comment | 1.8.30 |
| content | NSString | Text content of the comment | 1.8.30 |
| userInfo | JUserInfo | Information about the user who made the comment | 1.8.30 |
| parentUserInfo | JUserInfo | Information about the parent comment's user (empty object if no parent comment) | 1.8.30 |
| createTime | long | Timestamp when the comment was posted, in milliseconds | 1.8.30 |

**JMomentReaction structure**

| Attribute name | Type | Description | Version |
|------------------------|--------------|--------------------------------------------------------|--------|
| key | NSString | Like or custom interaction type, e.g., `like`, `dislike`, `collect` | 1.8.30 |
| userArray | `NSArray <JUserInfo *>` | List of users who performed the interaction | 1.8.30 |

</TabItem>
<TabItem value="flutter">

**Moment structure**

| Property name | Type | Default value | Description | Version |
|----------------------------------|-------------|--------------|--------------------------------------------------------|--------|
| momentId | String | '' | Unique global identifier for the Moment | 0.0.66 |
| content | String | '' | Text content of the circle of friends | 0.0.66 |
| mediaList | `List<MomentMedia>` | [] | List of media file links in the Moment (pictures/videos, etc.). See the `MomentMedia` structure below for details | 0.0.66 |
| userInfo | UserInfo? | - | User who posted the circle of friends | 0.0.66 |
| commentList | `List<MomentComment>` | [] | List of the first 20 comments. See the `MomentComment` structure below for details | 0.0.66 |
| reactionList | `List<MomentReaction>` | [] | List of likes or other custom interactions in the Moment. See the `MomentReaction` structure below for details | 0.0.66 |
| createTime | int | 0 | Creation time of the Moment, in milliseconds | 0.0.66 |

**MomentMedia Structure**

| Property name | Type | Default value | Description | Version |
|---------------|--------------|--------------|--------------------------------------------------------|--------|
| type | int | 0 | 0: IMAGE; 1: VIDEO | 0.0.66 |
| url | String | '' | Original image or video URL in the circle of friends | 0.0.66 |
| snapshotUrl | String | '' | Thumbnail image of the circle of friends; for videos, the first frame thumbnail | 0.0.66 |
| height | int | 0 | Height of the image or video | 0.0.66 |
| width | int | 0 | Width of the image or video | 0.0.66 |
| duration | int | 0 | Duration of the video, valid only for video Moments | 0.0.66 |

**MomentComment structure**

| Property name | Type | Default value | Description | Version |
|----------------------|--------------|--------------|-------------------------------------------------------------|--------|
| commentId | String | '' | Unique identifier for the comment | 0.0.66 |
| momentId | String | '' | Identifier of the Moment | 0.0.66 |
| parentCommentId | String | '' | Parent comment ID; when replying to a comment, this is the ID of the comment being replied to. Empty string if no parent comment | 0.0.66 |
| content | String | '' | Text content of the comment | 0.0.66 |
| userInfo | UserInfo? | - | Information about the user who made the comment | 0.0.66 |
| parentUserInfo | UserInfo? | - | Information about the parent comment's user (empty object if no parent comment) | 0.0.66 |
| createTime | int | 0 | Timestamp when the comment was posted, in milliseconds | 0.0.66 |

**MomentReaction structure**

| Property name | Type | Default value | Description | Version |
|----------------------|--------------|--------------|-------------------------------------------------------------|--------|
| key | String | '' | Like or custom interaction type, e.g., `like`, `dislike`, `collect` | 0.0.66 |
| userList | `List<UserInfo>` | [] | List of users who performed the interaction | 0.0.66 |

</TabItem>
<TabItem value="reactnative">

**Moment structure**

| Property name | Type | Default value | Description | Version |
|----------------------------------|-------------|--------------|--------------------------------------------------------|--------|
| momentId | string | '' | Unique global identifier for the Moment | - |
| content | string | '' | Text content of the circle of friends | - |
| mediaList | `MomentMedia[]` | [] | List of media file links in the Moment (pictures/videos, etc.). See the `MomentMedia` structure below for details | - |
| userInfo | UserInfo? | - | User who posted the circle of friends | - |
| commentList | `MomentComment[]` | [] | List of the first 20 comments. See the `MomentComment` structure below for details | - |
| reactionList | `MomentReaction[]` | [] | List of likes or other custom interactions in the Moment. See the `MomentReaction` structure below for details | - |
| createTime | number | 0 | Creation time of the Moment, in milliseconds | - |

**MomentMedia Structure**

| Property name | Type | Default value | Description | Version |
|---------------|--------------|--------------|--------------------------------------------------------|--------|
| type | number | 0 | 0: IMAGE; 1: VIDEO | - |
| url | string | '' | Original image or video URL in the circle of friends | - |
| snapshotUrl | string | '' | Thumbnail image of the circle of friends; for videos, the first frame thumbnail | - |
| height | number | 0 | Height of the image or video | - |
| width | number | 0 | Width of the image or video | - |
| duration | number | 0 | Duration of the video, valid only for video Moments | - |

**MomentComment structure**

| Property name | Type | Default value | Description | Version |
|----------------------|--------------|--------------|-------------------------------------------------------------|--------|
| commentId | string | '' | Unique identifier for the comment | - |
| momentId | string | '' | Identifier of the Moment | - |
| parentCommentId | string | '' | Parent comment ID; when replying to a comment, this is the ID of the comment being replied to. Empty string if no parent comment | - |
| content | string | '' | Text content of the comment | - |
| userInfo | UserInfo? | - | Information about the user who made the comment | - |
| parentUserInfo | UserInfo? | - | Information about the parent comment's user (empty object if no parent comment) | - |
| createTime | number | 0 | Timestamp when the comment was posted, in milliseconds | - |

**MomentReaction structure**

| Property name | Type | Default value | Description | Version |
|----------------------|--------------|--------------|-------------------------------------------------------------|--------|
| key | string | '' | Like or custom interaction type, e.g., `like`, `dislike`, `collect` | - |
| userList | `UserInfo[]` | [] | List of users who performed the interaction | - |

</TabItem>
<TabItem value="js">

**Moment structure**

| Property name | Type | Default value | Description | Version |
|----------------------------------|-------------|--------------|--------------------------------------------------------|--------|
| momentId | String | - | Unique global identifier for the Moment | 1.9.6 |
| content.text | String | - | Text content of the circle of friends | 1.9.6 |
| content.medias | Array | [] | List of media file links in the Moment (pictures/videos, etc.). See the `Media` structure below for details | 1.9.6 |
| user.id | String | - | User ID of the person who posted the circle of friends | 1.9.6 |
| user.avatar | String | - | Avatar of the user who posted the Moment | 1.9.6 |
| user.name | String | - | Name of the user who posted the Moment | 1.9.6 |
| topComments | Array | [] | List of the top 20 comments. See the `Comment` structure below for details | 1.9.6 |
| reactions | Array | [] | List of likes or other custom interactions in the Moment. See the `Reaction` structure below for details | 1.9.6 |
| momentTime | Number | - | Creation time of the Moment, in milliseconds | 1.9.6 |

**Media Structure**

| Property name | Type | Default value | Description | Version |
|---------------|--------------|--------------|--------------------------------------------------------|--------|
| type | String | - | [Moment media type](../../enum/web#moment_type) | 1.9.6 |
| url | String | - | Original image or video URL in the circle of friends | 1.9.6 |
| snapshotUrl | String | - | Thumbnail image of the circle of friends; for videos, the first frame thumbnail | 1.9.6 |
| height | Number | - | Height of the image or video | 1.9.6 |
| width | Number | - | Width of the image or video | 1.9.6 |
| duration | Number | - | Duration of the video, valid only for video Moments | 1.9.6 |

**Comment structure**

| Property name | Type | Default value | Description | Version |
|----------------------|--------------|--------------|-------------------------------------------------------------|--------|
| commentId | String | - | Unique identifier for the comment | 1.9.6 |
| momentId | String | - | Identifier of the Moment | 1.9.6 |
| parentCommentId | String | "" | Parent comment ID; when replying to a comment, this is the ID of the comment being replied to. Empty string if no parent comment | 1.9.6 |
| content.text | String | - | Text content of the comment | 1.9.6 |
| parentUser | Object | {} | Information about the parent comment's user (empty object if no parent comment) | 1.9.6 |
| user.avatar | String | - | Avatar URL of the comment user | 1.9.6 |
| user.id | String | - | Unique identifier of the comment user | 1.9.6 |
| user.name | String | - | Username of the comment user | 1.9.6 |
| commentTime | Number | - | Timestamp when the comment was posted, in milliseconds | 1.9.6 |

**Reaction structure**

| Property name | Type | Default value | Description | Version |
|----------------------|--------------|--------------|-------------------------------------------------------------|--------|
| value | String | - | Like or custom interaction type, e.g., `like`, `dislike`, `collect` | 1.9.6 |
| timestamp | Number | - | Timestamp of the like operation, in milliseconds | 1.9.6 |
| user.avatar | String | - | Avatar URL of the user who liked | 1.9.6 |
| user.id | String | - | ID of the user who liked | 1.9.6 |
| user.name | String | - | Username of the user who liked | 1.9.6 |

</TabItem>
</Tabs>