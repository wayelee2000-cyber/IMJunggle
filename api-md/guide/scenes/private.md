---
title: 单聊/私信
hide_title: true
sidebar_position: 1
---

### 场景介绍{#intro}

单聊通常指两个人之间进行互动沟通，相互之间通过文本、文件、图片、语音、好友添加通知等消息交流，单聊之间对消息的硬指标是不丢、不重、不乱序，换设备后消息备份能自动同步至新设备，消息已读状态、未读数量、消息操作等要求一个用户的多个设备严格一致，消息操作例如 `撤回撤回`、`消息修改`、`回复消息`。

### 适用场景{#match}

> **熟人间私信**：熟人社交通常包含好友关系，双方通过手机号或唯一标识搜索添加为好友，好友添加成功后进行线上互动。

> **陌生人私信**：陌生人交友通常有明确的用户画像和用户标签，通过兴趣、年龄等标签进行匹配，双方进行 `灵魂社交`。

> **买卖双方沟**：买家卖家线上文字或图片沟通，通常是以订单货商品为关系链进行线上售后、售前的咨询。

> **主播粉丝互动**：具有 `KOL` 直播社交产品，提供关注主播功能，关注后可以和主播私信，发送有条数限制的互动消息。

> **更多单聊场景**：`司机和乘客`、`1v1 教学`、`师生沟通`、`家校沟通`、`快递商家`、`...`

### 方案特点{#sp}

> **关系方向**: 单项或双向好友关系，粉丝单项关注主播，好友人数可调至无人数限制

> **在线状态**: 用户按需订阅好友或者关注人的在线状态，开发者应用层做更友好的提示或者业务匹配

> **黑白名单**: 双向黑白名单限制消息发送，加黑名单后发送消息提示说明，或加入白名单后才允许发送消息

> **信息变更**: 用户的信息变更后，具备优雅的同步机制，自动告知给与自己有关系的用户

> **消息绑定用户信息**: 消息中包含用户的信息，便于客户端展示，降低集成复杂度

### 相关文档{#doc}

>**基础文档**：[SDK 下载](../../../client/import)、[集成示例](../../../client/quickstart/ios)

>**用户管理**：[用户注册](../../../server/user/register)、[更新信息](../../../server/user/updateuser)、[用户封禁](../../../server/user/addbanuser)、[禁言用户](../../../server/user/addblockuser)

>**消息相关**：[消息结构](../../../client/sdkintro/msg/message)、[发送消息](../../../client/sdkintro/message/msg_send/send)、[接收消息](../../../client/sdkintro/watcher/message)、[获取历史消息](../../../client/sdkintro/message/histories/get_all)、[清空历史消息](../../../client/sdkintro/message/histories/clear)、[消息撤回](../../../client/sdkintro/message/operator/recall)、[消息已读](../../../client/sdkintro/message/operator/read)、[REST API 发送消息](../../../server/message/privatemsg)

>**会话相关**：[会话结构](../../../client/sdkintro/conversation)、[获取会话列表](../../../client/sdkintro/conversation/get_all)、[会话置顶](../../../client/sdkintro/conversation/settop)、[免打扰](../../../client/sdkintro/conversation/disturb)、[获取未读总数](../../../client/sdkintro/conversation/get_total_unread)、[服务端获取会话列表](../../../server/convers/qryconvers)

>**状 态 码**：[Android 相关](../../../client/sdkintro/status_code/android)、[iOS 相关](../../../client/sdkintro/status_code/ios)、[Web 相关](../../../client/sdkintro/status_code/web)、[REST API 相关](../../../server/status)
